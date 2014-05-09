#!/usr/bin/python

from collections import defaultdict
import json

import git_events
import hg_events

git_repos = [
	# add sources
]

hg_repos = [
	# add sources
]

event_dict = defaultdict(int)

def add_events(events):
	global event_dict
	for event in events:
		event_dict[str(event['timestamp'])] += 1

user = 'Johannes'

for repo in git_repos:
	print repo
	add_events(git_events.get_events(repo, user))

for repo in hg_repos:
	print repo
	add_events(hg_events.get_events(repo, user))

print json.dumps(event_dict)

