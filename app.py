from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret-to-a-random-value'  # change for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'notes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# Ensure DB exists
with app.app_context():
    db.create_all()


# Helper: login_required decorator
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            flash("Please log in to continue.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


# Routes
@app.route('/')
def index():
    if session.get('user_id'):
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        if not email or not password:
            flash("Email and password are required.", "danger")
            return render_template('register.html')

        if User.query.filter_by(email=email).first():
            flash("Email already registered. Try logging in.", "warning")
            return redirect(url_for('login'))

        user = User(email=email, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

        # Auto-login after register
        session['user_id'] = user.id
        session['user_email'] = user.email
        flash("Registered and logged in.", "success")
        return redirect(url_for('home'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_email'] = user.email
            flash("Logged in successfully.", "success")
            return redirect(url_for('home'))
        flash("Invalid email or password.", "danger")
        return render_template('login.html')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    user_id = session['user_id']
    # show only title + date for each note
    notes = Note.query.filter_by(user_id=user_id).order_by(Note.updated_at.desc()).all()
    # Format date for display
    notes_display = []
    for n in notes:
        notes_display.append({
            'id': n.id,
            'title': n.title,
            'date': n.updated_at.strftime('%d %b %Y %I:%M %p') if n.updated_at else n.created_at.strftime('%d %b %Y %I:%M %p')
        })
    return render_template('home.html', notes=notes_display)


@app.route('/note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def note(note_id):
    user_id = session['user_id']
    note_obj = None
    if note_id != 0:
        note_obj = Note.query.filter_by(id=note_id, user_id=user_id).first()
        if not note_obj:
            flash("Note not found or you don't have permission.", "danger")
            return redirect(url_for('home'))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        if not title:
            flash("Title is required.", "danger")
            return render_template('note.html', note=note_obj)

        if note_obj:
            # update
            note_obj.title = title
            note_obj.content = content
            db.session.commit()
            flash("Note updated.", "success")
            return redirect(url_for('home'))
        else:
            # create new
            new_note = Note(user_id=user_id, title=title, content=content)
            db.session.add(new_note)
            db.session.commit()
            flash("Note created.", "success")
            return redirect(url_for('home'))

    # GET request: render form (pass note if editing)
    return render_template('note.html', note=note_obj)


@app.route('/note/<int:note_id>/delete', methods=['POST'])
@login_required
def delete_note(note_id):
    user_id = session['user_id']
    note_obj = Note.query.filter_by(id=note_id, user_id=user_id).first()
    if not note_obj:
        flash("Note not found or you don't have permission.", "danger")
        return redirect(url_for('home'))

    db.session.delete(note_obj)
    db.session.commit()
    flash("Note deleted.", "success")
    return redirect(url_for('home'))


# Run
if __name__ == '__main__':
    app.run(debug=True)
