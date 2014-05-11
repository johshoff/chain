#!/usr/bin/python

from collections import defaultdict
import json
import os
import sys

import git_events
import hg_events

out_filename = 'sources.json'
out_desc_filename = 'descriptions.json'

if len(sys.argv) < 3:
	print 'Usage: get_events.py <user> <repository_roots> [<additional repository roots> ...]'
	print
	print 'Repository roots will be scanned for hg and git repositories'
	print 'Events will be written to %s' % out_filename
	print 'Event descriptions will be written to %s' % out_desc_filename
	print
	print 'Only look at commits from <user>. This is just a substring match of the commit'
	print "author's name or email address. Note that in git this is case sensitive."
	sys.exit(0)

user        = sys.argv[1]
search_dirs = sys.argv[2:]

git_repos = []
hg_repos  = []

print 'Discovering repositories'

for directory in search_dirs:
	for root, dirs, files in os.walk(os.path.expanduser(directory)):
		for dirname in dirs:
			if dirname == '.hg':
				hg_repos.append(root)
			if dirname == '.git':
				git_repos.append(root)

event_dict = defaultdict(int)
event_desc = defaultdict(list)

def add_events(events):
	global event_dict
	for event in events:
		event_dict[str(event['timestamp'])] += 1

		if 'isodate' in event:
			event_desc[event['isodate']].append(event)

def repos_and_getters():
	for repo in git_repos:
		yield repo, git_events.get_events

	for repo in hg_repos:
		yield repo, hg_events.get_events

for repo, get_events in repos_and_getters():
	events = get_events(repo, user)
	print '%s: %d events' % (repo, len(events))
	add_events(events)

print 'Writing %d events to %s' % (len(event_dict), out_filename)

json.dump(event_dict, open(out_filename, 'w'))
json.dump(event_desc, open(out_desc_filename, 'w'))

