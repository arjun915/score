from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Event, Score

@app.route("/")
def index():
    events = Event.query.all()
    return render_template("index.html", events=events)

@app.route("/event/<int:event_id>", methods=["GET", "POST"])
def event(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == "POST":
        team_name = request.form["team_name"]
        score = request.form["score"]
        new_score = Score(event_id=event.id, team_name=team_name, score=int(score))
        db.session.add(new_score)
        db.session.commit()
        return redirect(url_for("event", event_id=event.id))
    return render_template("event.html", event=event)

@app.route("/create_event", methods=["GET", "POST"])
def create_event():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        new_event = Event(name=name, description=description)
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create_event.html")
