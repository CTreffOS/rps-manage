rps-data-server
===============

This is a small server application deliver the information stored in the sqlite
database data.db in json format via http.

There are two REST points:

- /lastgame returns dictionary in json format with the following entries with
  informations about the last game:
	- "code_1" is the unique code of the first player of the game
	- "code_2" is the unique code of the second player of the game
	- "name_1" is the name of the first player
	- "name_2" is the name of the second player
	- "paper_1" is the number of the choice paper of the first player
	- "paper_2" is the number of the choice paper of the second player
	- "rock_1" is the number of the choice rock of the first player
	- "rock_2" is the number of the choice rock of the second player
	- "scissors_1" is the number of the choice scissors of the first player
	- "scissors_2" is the number of the choice scissors of the second player
	- "won_1"  is the number of the games the first player won.
	- "won_2"  is the number of the games the second player won.

	Here is an example output:
		{
			"code_1": "fhtl4",
			"code_2": "ajg7a",
			"name_1": "Frank",
			"name_2": "Johnny",
			"paper_1": 333,
			"paper_2": 333,
			"rock_1": 333,
			"rock_2": 333,
			"scissors_1": 333,
			"scissors_2": 333,
			"won_1": 333,
			"won_2": 333
		}
- /highscore returns a dictionary in json format with entries from "1" to "10"
  corrensponding to the ranking. Each of the entries points to a dictionary
  with the following informations about one player:
	- "code" is the unique code of the player
	- "name" is the name of the player
	- "won": is the number of sets the player won (not single games, but bunches of 1000)

	Here is an example output:
	{
		"1": {
	   	"code": "player1",
			"name": "player1",
			"won": 10
		},
		"2": {
	   	"code": "player2",
			"name": "player2",
			"won": 9
		},
		"3": {
	   	"code": "player3",
			"name": "player3",
			"won": 8
		},
		"4": {
	   	"code": "player4",
			"name": "player4",
			"won": 7
		},
		"5": {
	   	"code": "player5",
			"name": "player5",
			"won": 6
		},
		"6": {
	   	"code": "player6",
			"name": "player6",
			"won": 5
		},
		"7": {
	   	"code": "player7",
			"name": "player7",
			"won": 4
		},
		"8": {
	   	"code": "player8",
			"name": "player8",
			"won": 3
		},
		"9": {
	   	"code": "player9",
			"name": "player9",
			"won": 2
		},
		"10": {
	   	"code": "player10",
			"name": "player10",
			"won": 1
		}
	}

Requirements
------------

 - python
 - python flask
