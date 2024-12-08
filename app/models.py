from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    team_name = db.Column(db.String(150), nullable=False)
    score = db.Column(db.Integer, default=0)

    event = db.relationship('Event', backref=db.backref('scores', lazy=True))
