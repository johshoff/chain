#!/usr/bin/python

"Get events from a git repository"

from subprocess import Popen, PIPE
import os


def get_events(cwd, user):
	cwd = os.path.expanduser(cwd)
	args = ['git', 'log', '--author='+user, '--pretty=format:%at']

	stdout, stderr = Popen(args, cwd=cwd, stdout=PIPE).communicate()

	if stdout.strip() == '':
		return []

	def fixup_line(line):
		return {'timestamp':int(line)}

	return [fixup_line(line) for line in stdout.strip().split('\n')]

