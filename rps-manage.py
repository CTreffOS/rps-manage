#!/bin/env python
# -*- coding: utf-8 -*-

# Set default encoding to UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import sqlite3
import json
import random
import time
from urllib2 import urlopen
import subprocess

def get_next():
	with sqlite3.connect('data.db') as con:
		cur = con.cursor()
		cur.execute('select * from user where not played limit 0,1')
		return cur.fetchone()


def play(p1, p2):

	error = False

	id1 = str(random.randint(1000000000,9999999999))
	id2 = str(random.randint(1000000000,9999999999))
	p = subprocess.Popen( ['docker', 'run', '-d', '--name', 'rps-server',
		'-p', '4441:4441', 'rockpaperscissors/server', '/rps/start.sh', id1, id2])
	p.communicate()
	if p.returncode:
		print('Failed to start rps-server docker container')
		exit()

	# Wait for server to start up
	result = None
	n = 0
	while not result:
		try:
			result = urlopen('http://localhost:4441').read()
		except:
			n += 1
			if n > 10000:
				print('Failed to connect to rps-server')
				error = True

	if not error:
		# Start Player 1
		p = subprocess.Popen( ['docker', 'run', '-d', '--name', 'rps-player-one',
			'--link', 'rps-server:rps-server ', p1, '/rps/start.sh', id1])
		p.communicate()
		if p.returncode:
			print('Failed to start player-one docker container')
			error = True

	if not error:
		# Start Player 1
		p = subprocess.Popen( ['docker', 'run', '-d', '--name', 'rps-player-two',
			'--link', 'rps-server:rps-server ', p2, '/rps/start.sh', id2])
		p.communicate()
		if p.returncode:
			print('Failed to start player-two docker container')
			error = True

	# Wait for server to start up
	result = 'playing'
	if not error:
		while result == 'playing':
			try:
				result = urlopen('http://localhost:4441').read()
				time.sleep(0.1)
			except:
				print('Failed to get result from rps-server')
				error = True
				break
		if not error:
			print(result)
			try:
				result = json.loads(result)
			except:
				error = True

	# Drop docker container
	subprocess.Popen( ['docker', 'stop', 'rps-server', 'rps-player-one',
		'rps-player-two']).communicate()
	subprocess.Popen( ['docker', 'rm', 'rps-server', 'rps-player-one',
		'rps-player-two']).communicate()

	if error:
		return None

	return result[id1], result[id2]


if __name__ == "__main__":
	nextplayer = get_next()
	print play('rockpaperscissors/player', 'rockpaperscissors/player')
