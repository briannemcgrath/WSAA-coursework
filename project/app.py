from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random 

# ---------------------------------------
# Initial Games 
# ---------------------------------------

initial_games = [
    {
      "title": "Red Dead Redemption 2",
      "platform": "PS5",
      "genre": "Action",
      "status": "Complete",
      "description": "Action Adventure following Arthur Morgan and the Van Der Linde gang. Don't play past chapter five :)",
      "rating": 5.0
    },
    {
      "title": "Bear & Breakfast",
      "platform": "PC",
      "genre": "Simulation",
      "status": "Complete",
      "description": "Laid-back management adventure game where you build and run a B&B... but you're a bear ᵔᴥᵔ",
      "rating": 5.0
    },
    {
      "title": "Stardew Valley",
      "platform": "PC",
      "genre": "Simulation",
      "status": "Complete",
      "description": "Build your farm, befriend the townsfolk, and dig into the mines.",
      "rating": 5.0
    },
    {
      "title": "Hell Divers 2",
      "platform": "PS5",
      "genre": "Shooter",
      "status": "In Progress",
      "description": "Third person squad-based shooter that sees the elite forces of the Helldivers battling to win an intergalactic struggle to rid the galaxy of risen alien threats! For Liberty!!! ",
      "rating": 4.0
    },
    {
      "title": "The Sims 4",
      "platform": "PC",
      "genre": "Simulation",
      "status": "In Progress",
      "description": "Life Simulator - Susu!",
      "rating": 5.0
    },
    {
      "title": "Diablo IV",
      "platform": "PC",
      "genre": "Strategy",
      "status": "Complete",
      "description": "Dungeon crawling game slaying enemies! ",
      "rating": 3.0
    },
     {
      "title": "Fortnite",
      "platform": "PS5",
      "genre": "PVP",
      "status": "In Progress",
      "description": "Sabrina Carpenter was added so I'm back playing - no build mode always! ",
      "rating": 4.0
    },
      {
      "title": "Elder Scrolls IV: Oblivion (Remaster) ",
      "platform": "PS5",
      "genre": "RPG",
      "status": "Not Started",
      "description": "Bethesda shadow dropping Oblivion Remaster two weeks before all my assignments are due?? ",
      "rating": 5.0
    },
      {
      "title": "Ghost of Yōtei",
      "platform": "PS5",
      "genre": "Action",
      "status": "Not Started",
      "description": "Sequel to Ghost of Tsushima - releasing in October ",
      "rating": 4.0
    },
]

app = Flask(__name__)

# ---------------------------------------
# App Configuration
# ---------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #disable modification tracking for performance 


db = SQLAlchemy(app)

# ---------------------------------------
# Data Model
# --------------------------------------- 
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(150), nullable=False) 
    platform = db.Column(db.String(50), nullable=False) 
    genre = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50)) 
    description = db.Column(db.Text) 
    rating = db.Column(db.Float) 

    def to_dict(self):
        #convert model instance to dictionary for JSON response
        return {
            'id': self.id, 
            'title': self.title, 
            'platform': self.platform, 
            'genre': self.genre, 
            'status': self.status, 
            'description': self.description, 
            'rating': self.rating
        }

# ---------------------------------------
# Helper Data
# ---------------------------------------
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
    #render the homepage with a random tip and featured games
    games=Game.query.all()
    tip = random.choice(daily_tips)
    featured = games[:10]
    wishlist_gs = Game.query.filter_by(status="Not Started").all()
    wishlist_games = [g.to_dict() for g in wishlist_gs]
    return render_template('index.html', games=featured, tip=tip, wishlist=wishlist_games)

@app.route('/game/<int:game_id>')
def game_detail_view(game_id):
    #show details for a specific game
    game = Game.query.get_or_404(game_id)
    return render_template('game_detail.html', game=game)

@app.route('/game/new', methods=['GET'])
def new_game_form():
    #display form to add new game 
    return render_template('game_form.html', game=None) 

@app.route('/game/edit/<int:game_id>', methods=['GET'])
def edit_game_form(game_id):
    #display form to edit existing game 
    game = Game.query.get_or_404(game_id)
    return render_template('game_form.html', game=game)

@app.route('/catalogue')
def catalogue():
    #list and filter games; display summary stats
    query = Game.query 
    title = request.args.get('title', None)
    platform = request.args.get('platform', None)
    genre = request.args.get('genre', None)
    status = request.args.get('status', None)

    if title: 
        query = query.filter(Game.title.ilike(f"%{title}%"))
    if platform: 
        query = query.filter(Game.platform.ilike(f"%{platform}%"))
    if genre: 
        query = query.filter(Game.genre.ilike(f"%{genre}%"))
    if status: 
        query = query.filter(Game.status.ilike(f"%{status}%"))
    
    games = query.all()
    total = len(games)
    completed = sum(1 for g in games if g.status == "Complete")
    wishlist  = sum(1 for g in games if g.status == "Not Started")
    playing = sum(1 for g in games if g.status == "In Progress")
    pct_done  = int((completed/total)*100) if total else 0
    stats={
            'total':total, 
            'playing': playing,
            'completed_pct': pct_done,
            'wishlist':wishlist
    }
    
    return render_template('catalogue.html', games=games, stats=stats)

@app.route('/by-genre')
def by_genre():
    #display games grouped by genre with jump links
    genres = sorted({g.genre for g in Game.query.all() if g.genre})
    genre_map = {
        g: Game.query.filter_by(genre=g).all()
        for g in genres
    }
    return render_template('by_genre.html', genre_map=genre_map) 

@app.route('/wishlist')
def wishlist():
    #display games not started yet 
    games = Game.query.filter_by(status='Not Started').all()
    return render_template('wishlist.html', games=games) 

@app.route('/analytics')
def analytics():
    #status breakdown
    statuses = ['Not Started', 'In Progress', 'Complete']
    status_counts = [Game.query.filter_by(status=s).count() for s in statuses]
    #genre breakdown
    genres = [ g[0] for g in db.session.query(Game.genre).distinct().filter(Game.genre != None) ]
    genre_counts = { g: Game.query.filter_by(genre=g).count() for g in genres }
    if genre_counts:
        popular_genre, popular_count = max(genre_counts.items(), key=lambda item: item[1])
    else:
        popular_genre, popular_count = None, 0

    #list and filter games; display summary stats
    query = Game.query 
    title = request.args.get('title', None)
    platform = request.args.get('platform', None)
    genre = request.args.get('genre', None)
    status = request.args.get('status', None)

    if title: 
        query = query.filter(Game.title.ilike(f"%{title}%"))
    if platform: 
        query = query.filter(Game.platform.ilike(f"%{platform}%"))
    if genre: 
        query = query.filter(Game.genre.ilike(f"%{genre}%"))
    if status: 
        query = query.filter(Game.status.ilike(f"%{status}%"))
    
    games = query.all()
    total = len(games)
    completed = sum(1 for g in games if g.status == "Complete")
    wishlist  = sum(1 for g in games if g.status == "Not Started")
    playing = sum(1 for g in games if g.status == "In Progress")
    pct_done  = int((completed/total)*100) if total else 0
    stats={
            'total':total, 
            'playing': playing,
            'completed_pct': pct_done,
            'wishlist':wishlist
    }
    return render_template('analytics.html', labels=statuses, counts=status_counts, genre_counts=genre_counts, popular_genre=popular_genre, popular_count=popular_count, games=games, stats=stats)

# --------------------------------
# RESTFUL API Endpoints for Game
# --------------------------------

@app.route('/games', methods=['GET'])
def get_games():
    #return JSON list of all games 
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games])

@app.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    #return JSON details for one game 
    game = Game.query.get_or_404(game_id)
    return jsonify(game.to_dict())

@app.route('/games', methods=['POST'])
def create_game():
    #create a new game from form data and redirect to catalogue 
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

@app.route('/games/<int:game_id>', methods=['POST'])
def update_game(game_id):
    #update fields of an existing game and redirect home 
    game = Game.query.get_or_404(game_id)
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
    return redirect(url_for('catalogue'))

@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    #delete a game and return JSON status message 
    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'Game deleted successfully!'})

#create tables as soon as module is imported & adding starter games 
with app.app_context():
    db.create_all()

    if Game.query.count() == 0:
        for g in initial_games:
            game = Game(
                title=g["title"],
                platform=g["platform"],
                genre=g["genre"],
                status=g["status"],
                description=g["description"],
                rating=g["rating"]
            )
            db.session.add(game)
        db.session.commit()

# ---------------------------------------
# Friendly Error Pages
# ---------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
        title="Opps! Page Not Found!", 
        message ="We couldn't find that page!"), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html', 
        title="Uh-oh, Internal Server Error",
        message="Our dungeon got a little too dark. We're on it!🔧"), 500

# --------------------------------------
# Run Server
# --------------------------------------- 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)