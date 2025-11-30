# Notes App — Flask + Jinja + Bootstrap

A simple and functional Notes Web Application built using:

- Flask (Python)
- Jinja2 Templates
- Bootstrap 5
- SQLite Database

Users can register, log in, create notes, edit notes, and view notes individually.

---

## Features

Authentication:
- User registration
- User login/logout
- Secure password hashing

Notes Management:
- Create new notes
- Edit existing notes
- View individual notes
- Notes list shows title and last updated date

UI:
- Clean Bootstrap design
- Mobile responsive
- Single shared base template

---

## Project Structure

notes-app/
│
├── app.py
├── database.db
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── note.html
│
└── static/
    └── style.css  (optional)

---

## Installation & Setup

1. Clone the repository:
   git clone https://github.com/your-username/notes-app.git
   cd notes-app

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate   (Linux/Mac)
   venv\Scripts\activate      (Windows)

3. Install dependencies:
   pip install flask flask_sqlalchemy flask_bcrypt

4. Run the application:
   python app.py

5. Open in browser:
   http://127.0.0.1:5000/

---

## Requirements

- Python 3.8+
- Flask
- Flask SQLAlchemy
- Flask Bcrypt

---

## Future Improvements

- Add search functionality
- Dark mode option
- Delete confirmation popup
- Rich text editor for notes
- Notes categories/tags

---

## Contributing

Pull requests are welcome.  
For major changes, please open an issue first.

---

## License

This project is licensed under the MIT License.
