from flask import Flask, jsonify, g
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


@app.route('/user')
def show_user():
	user = g.db.execute('select user_id, name, email, played, highscore from '
			'user').fetchall()
	result = []
	for u in user:
		result.append({'user_id' : u[0], 'name' : u[1], 'email' : u[2],
				'played' : u[3], 'highscore' : u[4]})
	return jsonify({'player' : result}), 200


@app.route('/user/code/<code>')
def show_user_by_code(code):
	user = g.db.execute('select user_id, name, email, played, highscore from '
			'user where code=?', (code,)).fetchone()
	if not user:
		return 'User not found', 404
	result = {'user_id' : user[0], 'name' : user[1], 'email' : user[2], 'played'
			: user[3], 'highscore' : user[4]}
	return jsonify(result), 200


@app.route('/user/id/<int:id>')
def show_user_by_id(id):
	user = g.db.execute('select user_id, name, email, played, highscore from '
			'user where user_id=?', (id,)).fetchone()
	if not user:
		return 'User not found', 404
	result = {'user_id' : user[0], 'name' : user[1], 'email' : user[2], 'played'
			: user[3], 'highscore' : user[4]}
	return jsonify(result), 200


@app.route('/games')
def show_games():
	games = g.db.execute('select game_id, p1, p2, result1, result2 from '
			'games').fetchall()
	result = []
	for ga in games:
		result.append({'game_id' : ga[0], 'p1' : ga[1], 'p2' : ga[2], 'result1' :
			ga[3], 'result2' : ga[4]})
	return jsonify({'games' : result}), 200


@app.route('/lastgame')
def show_last_game():
	game = g.db.execute('select max(game_id), p1, p2, result1, result2 from '
			'games').fetchone()
	if not game:
		return 'Last game not found', 404
	result = {'game_id' : game[0], 'p1' : game[1], 'p2' : game[2], 'result1' :
			game[3], 'result2' : game[4]}
	return jsonify(result), 200


@app.route('/highscore')
def show_highscore():
	user = g.db.execute('select user_id, name, email, played, highscore from '
			'user where highscore not null').fetchall()
	result = {}
	for u in user:
		result[u[4]] = {'user_id' : u[0], 'name' : u[1], 'email' : u[2],
				'played' : u[3]}
	return jsonify(result), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, threaded=True)
