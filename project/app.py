from flask import Flask, render_template, request, jsonify 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#configure the app to use a SQLite database named games.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #disable modification tracking for performance 

#initialising the SQLAlchemy ORM 
db = SQLAlchemy(app)

#defining game model for storing game information 
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True) #unique ID for each game
    title = db.Column(db.String(150), nullable=False) #game title
    platform = db.Column(db.String(50), nullable=False) #game platform (e.g., PS5, Switch, PC)
    genre = db.Column(db.String(50)) #game genre
    status = db.Column(db.String(50)) #game progress (e.g., Not Started, In Progress, Complete)
    description = db.Column(db.Text) #game description
    rating = db.Column(db.Float) #game rating

    #converting game instance to a dictionary for JSON responses
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,  
            'platform': self.platform, 
            'genre': self.genre, 
            'status': self.status, 
            'description': self.description, 
            'rating': self.rating
        }

#---------------------------------------
#Template-rendering Routes (HTML Pages)
#---------------------------------------
@app.route('/')
def home():
    games = Game.query.all()
    return render_template('index.html', games=games)

@app.route('/game/<int:game_id>')
def game_detail_view(game_id):
    #get game from database; 404 if not found
    game = Game.query.get_or_404(game_id)
    #render the game_detail.html template, passing the game data
    return render_template('game_detail.html', game=game)

@app.route('/game/new', methods=['GET'])
def new_game_form():
    return render_template('game_form.html')

@app.route('/game/edit/<int:game_id>', methods=['GET'])
def edit_game_form(game_id):
    game = Game.query.get_or_404(game_id)
    return render_template('game_form.html', game=game)

# --------------------------------
# RESTFUL API Endpoints for Game
# --------------------------------

#GET /games: list all games 
@app.route('/games', methods=['GET'])
def get_games():
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games])

#GET /games/<id>: get details for a specific game 
@app.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = Game.query.get_or_400(game_id)
    return jsonify(game.to_dict())

#POST /games: create new game entry 
@app.route('/games', methods=['POST'])
def create_game():
    new_game = Game(
        title=request.form.get('title'), 
        platform=request.form.get('platform'), 
        genre=request.form.get('genre'), 
        status=request.form.get('status'), 
        description=request.form.get('description'),
        rating=request.form.get('rating')
    )
    db.session.add(new_game)
    db.session.commit()
    return jsonify(new_game.to_dict()), 201

#PUT /games/<id>: update an existing game
@app.route('/games/<int:game_id>', methods=['POST'])
def update_game(game_id):
    game = Game.query.get_or_404(game_id)
    data = request.get_json()

    #update only the fields provided in request
    if 'title' in data: 
        game.title = data['title']
    if 'platform' in data:
        game.platform = data['platform']
    if 'genre' in data: 
        game.genre = data['genre']
    if 'status' in data: 
        game.status = data['status']
    if 'description' in data: 
        game.description = data['description']
    if 'rating' in data: 
        game.rating = data['rating']
    
    db.session.commit()
    return jsonify(game.to_dict())

#DELETE /games/<id>: remove a game from catalogue
@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    game = Game.query.get_or_400(game_id)
    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'Game deleted successfully!'})

#run the app and create databse tables if they don't exist 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)