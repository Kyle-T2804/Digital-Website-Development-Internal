from flask import Blueprint, render_template, url_for, request, flash, redirect, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Note
from . import db
import json

# set blueprint
views = Blueprint("views", __name__)


# default/home route
@views.route("/")
@views.route("/home")
@views.route("/index")
def home():
    return render_template("home.html", user=current_user)

# Gallery route
@views.route("/gallery")
def gallery():
    return render_template("gallery.html", user=current_user)


# contant route
@views.route("/contact", methods=['POST', 'GET'])
@login_required
def contact():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Comment field cannot be empty!')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Comment Added!', category='success')
            
        
        
    return render_template("contact.html", user=current_user)



#delete note route
@views.route("/delete-note", methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})
