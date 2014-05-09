#!/usr/bin/python

"Get events from a hg repository"

from subprocess import Popen, PIPE
import os


def get_events(cwd, user):
	cwd = os.path.expanduser(cwd)
	args = ['hg', 'log', '--user', user, '--template', '{date}\n']

	stdout, stderr = Popen(args, cwd=cwd, stdout=PIPE).communicate()

	if stdout.strip() == '':
		return []

	def fixup_line(line):
		return {'timestamp':int(line.split('.')[0])}

	return [fixup_line(line) for line in stdout.strip().split('\n')]

