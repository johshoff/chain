#!/usr/bin/python

"Get events from a hg repository"

from subprocess import Popen, PIPE
import os


def get_events(cwd, user):
	cwd = os.path.expanduser(cwd)
	args = ['hg', 'log', '--user', user, '--template', '{date|hgdate}\t{date|shortdate}\t{desc}\n']

	stdout, stderr = Popen(args, cwd=cwd, stdout=PIPE).communicate()

	if stdout.strip() == '':
		return []

	def fixup_line(line):
		items = line.split('\t')
		return {
				'timestamp': int(items[0].split(' ')[0]),
				'isodate'  : items[1],
				'desc'     : items[2],
				'repo'     : os.path.split(cwd)[-1],
			}

	return [fixup_line(line) for line in stdout.strip().split('\n')]

