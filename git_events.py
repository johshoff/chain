#!/usr/bin/python

"Get events from a git repository"

from subprocess import Popen, PIPE
import os


def get_events(cwd, user):
	cwd = os.path.expanduser(cwd)
	args = ['git', 'log', '--author='+user, '--pretty=format:%at\t%ai\t%s']

	stdout, stderr = Popen(args, cwd=cwd, stdout=PIPE).communicate()

	if stdout.strip() == '':
		return []

	def fixup_line(line):
		items = line.split('\t')
		return {
				'timestamp': int(items[0]),
				'isodate'  : items[1].split(' ')[0],
				'desc'     : items[2],
				'repo'     : os.path.split(cwd)[-1],
			}

	return [fixup_line(line) for line in stdout.strip().split('\n')]

