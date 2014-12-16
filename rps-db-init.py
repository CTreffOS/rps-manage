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
			code STRING NOT NULL UNIQUE,
			played BOOL NOT NULL DEFAULT FALSE,
			docker_image STRING NOT NULL,
			highscore INTEGER DEFAULT NULL)''')
		cur.execute('''CREATE TABLE IF NOT EXISTS game (
			game_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         user_id_1         INTEGER,
         user_id_2         INTEGER,
         win_player_1      INTEGER,
         win_player_2      INTEGER,
         rock_player_1     INTEGER,
         paper_player_1    INTEGER,
         scissors_player_1 INTEGER,
         rock_player_2     INTEGER,
         paper_player_2    INTEGER,
         scissors_player_2 INTEGER)''')
		con.commit()


if __name__ == "__main__":
	init()
