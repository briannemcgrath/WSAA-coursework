from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random 

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

daily_tips = [
    "Always save before exploring that dungeon!🗡️",
    "Sprinting is faster than walking!💭", 
    "Aim down sights to be more accurate!🎮", 
    "If you're having trouble winning in combat, try getting better at the game🤫", 
    "Take a break every hour or you'll cramp that thumb!🎮",
    "Achievement Unlocked: Spent more time customising your character than actually playing the game 💅🏻",
    "When in doubt, mash all the buttons simultaneously. True mastery comes from chaos🤯", 
    "Always reload your weapon after every shot - just to keep things interesting🔫",
    "If you're low on health trying using a healing potion? Just a thought💭"    
]

#---------------------------------------
#Template-rendering Routes (HTML Pages)
#---------------------------------------
@app.route('/')
def home():
    games=Game.query.all()
    #pick a random tip 
    tip = random.choice(daily_tips)
    featured = games[:10]   
    return render_template('index.html', games=featured, tip=tip)

@app.route('/game/<int:game_id>')
def game_detail_view(game_id):
    #get game from database; 404 if not found
    game = Game.query.get_or_404(game_id)
    return render_template('game_detail.html', game=game)

@app.route('/game/new', methods=['GET'])
def new_game_form():
    return render_template('game_form.html', game=None) 

@app.route('/game/edit/<int:game_id>', methods=['GET'])
def edit_game_form(game_id):
    game = Game.query.get_or_404(game_id)
    return render_template('game_form.html', game=game)

@app.route('/catalogue')
def catalogue():
    query = Game.query
    #get query parameters for filtering
    title = request.args.get('title', None)
    platform = request.args.get('platform', None)
    genre = request.args.get('genre', None)
    status = request.args.get('status', None)

    #filtering
    if title: 
        query = query.filter(Game.title.ilike(f"%{title}%"))
    if platform: 
        query = query.filter(Game.platform.ilike(f"%{platform}%"))
    if genre: 
        query = query.filter(Game.genre.ilike(f"%{genre}%"))
    if status: 
        query = query.filter(Game.status.ilike(f"%{status}%"))
    
    #filtered list
    games = query.all()

    #stats
    total = len(games)
    completed = sum(1 for g in games if g.status == "Complete")
    wishlist  = sum(1 for g in games if g.status == "Not Started")
    playing = sum(1 for g in games if g.status == "In Progress")
    pct_done  = int((completed/total)*100) if total else 0

    
    return render_template('catalogue.html', games=games,
        stats={
            'total':total, 
            'playing': playing,
            'completed_pct': pct_done,
            'wishlist':wishlist
        }
    )

@app.route('/by-genre')
def by_genre():
    genres = sorted({g.genre for g in Game.query.all() if g.genre})
    #mapping of genre - list of games
    genre_map = {
        g: Game.query.filter_by(genre=g).all()
        for g in genres
    }
    return render_template('by_genre.html', genre_map=genre_map) 

@app.route('/wishlist')
def wishlist():
    games = Game.query.filter_by(status='Not Started').all()
    return render_template('wishlist.html', games=games) 

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
    game = Game.query.get_or_404(game_id)
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
    return redirect(url_for('catalogue'))

#POST /games/<id>: update an existing game
@app.route('/games/<int:game_id>', methods=['POST'])
def update_game(game_id):
    game = Game.query.get_or_404(game_id)
    
    #update only the fields provided in the form
    if request.form.get('title'):
        game.title = request.form.get('title')
    if request.form.get('platform'):
        game.platform = request.form.get('platform')
    if request.form.get('genre'):
        game.genre = request.form.get('genre')
    if request.form.get('status'):
        game.status = request.form.get('status')
    if request.form.get('description'):
        game.description = request.form.get('description')
    if request.form.get('rating'):
        game.rating = request.form.get('rating')
    
    db.session.commit()
    return redirect(url_for('home'))

#DELETE /games/<id>: remove a game from catalogue
@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'Game deleted successfully!'})

#run the app and create databse tables if they don't exist 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)