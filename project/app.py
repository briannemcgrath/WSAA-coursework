from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#configure the database URI (SQLite for development)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#defining game model
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    platform = db.Column(db.String(50), nullable=False) # PS5, Switch, PC
    genre = db.Column(db.String(50))
    status = db.Column(db.String(50)) # Not Started, In Progress, Complete
    description = db.Column(db.Text)
    rating = db.Column(db.Float)

    def __repr__(self):
        return f'<Game {self.title}>'

@app.route('/')
def home():
    return render_template('base.html')

#test route to add sample game entry 
@app.route('/test-add-game')
def test_add_game():
    new_game = Game(
        title = 'Baulders Gate 3',
        platform = 'PS5',
        genre = 'RPG', 
        status = 'In Progress',
        description = 'Dungeons & Dragons influenced RPG',
        rating = 9.5
    )
    db.session.add(new_game)
    db.session.commit()
    return "Test game added! :)"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)