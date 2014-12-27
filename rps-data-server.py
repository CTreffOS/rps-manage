from flask import Flask, jsonify, g
import json
import sqlite3

# Create aplication
app = Flask(__name__)


DATABASE = 'data.db'


@app.before_request
def before_request():
	g.db = sqlite3.connect(DATABASE)


@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()


@app.route('/lastgame')
def show_last_game():
	ga = g.db.execute('select user_id_1, user_id_2, win_player_1, win_player_2, '
			'rock_player_1, paper_player_1, scissors_player_1, rock_player_2, '
			'paper_player_2, scissors_player_2 ' 'from game order by game_id desc '
			'limit 0,1').fetchone()
	if not ga:
		return 'Last game not found', 404
	player1 = g.db.execute('select name, code from user where user_id = ?',
			(ga[0],)).fetchone()
	player2 = g.db.execute('select name, code from user where user_id = ?',
			(ga[1],)).fetchone()
	if not (player1 or player2):
		return 'Player not found', 500
	result = {'name_1' : player1[0], 'name_2' : player2[0], 'code_1' :
		player1[1], 'code_2' : player2[1], 'won_1' : ga[2], 'won_2' : ga[3],
			'rock_1' : ga[4], 'paper_1' : ga[5],'scissors_1' : ga[6], 'rock_2' :
			ga[7], 'paper_2' : ga[8],'scissors_2' : ga[9]}
	return 'lastgame(' + json.dumps(result) + ')\n', 200
	#return jsonify(result), 200


@app.route('/highscore')
def show_highscore():
	user = g.db.execute('select user_id, name, highscore, code from user where '
			'highscore not null order by highscore asc').fetchall()
	result = []
	for u in user:
		won = g.db.execute('select count() from game where (user_id_1 = ? and '
				'win_player_1 > win_player_2) or (user_id_2 = ? and win_player_2 > '
				'win_player_1)', (u[0],u[0])).fetchone()[0]
		result.append({'score': u[2], 'code' : u[3], 'name' : u[1], 'won' : won})
	return 'highscore(' + json.dumps(result) + ');\n', 200
	#return jsonify(result), 200


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, threaded=True, port=5001)
