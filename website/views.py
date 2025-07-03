# store standard routes for website users (not related to authentication)
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# define this file is a blueprint of the application
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): # this funtion will run when we go to '/' route
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) # load data taken in by post request as a json obj 
    noteId = note['noteId'] # access noteId att
    note = Note.query.get(noteId) 
    if note:
        if note.user_id == current_user.id: # if signed in user owns note
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})