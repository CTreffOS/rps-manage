#!/bin/env python
# -*- coding: utf-8 -*-

# Set default encoding to UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import sqlite3

def init():
	with sqlite3.connect('data.db') as con:
		cur = con.cursor()
		cur.execute('''CREATE TABLE IF NOT EXISTS user (
			user_id INTEGER PRIMARY KEY AUTOINCREMENT,
			name STRING NOT NULL,
			email STRING,
			code STRING NOT NULL,
			played BOOL NOT NULL DEFAULT FALSE,
			docker_image STRING NOT NULL,
			highscore INTEGER DEFAULT NULL)''')
		cur.execute('''CREATE TABLE IF NOT EXISTS games (
			game_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			p1 INT,
			p2 INT,
			result1 STRING,
			result2 STRING )''')
		con.commit()


if __name__ == "__main__":
	init()
