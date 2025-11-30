# 📝 Notes App — Flask + Jinja + Bootstrap

A simple and clean Notes Web Application built using:

- **Flask (Python)**
- **Jinja2 Templates**
- **Bootstrap 5**
- **SQLite**

Users can register, log in, create notes, edit notes, and view notes—all inside a clean and responsive UI.

---

## 🚀 Features

### 🔐 Authentication
- User **Register**
- User **Login / Logout**
- Password hashing (secure)

### 📝 Notes Management
- Create notes  
- Edit notes  
- View a note  
- Home page displays:
  - Title  
  - Last updated date  

### 🎨 UI / UX
- Bootstrap 5 layout
- Clean base template
- Mobile responsive

---

## 📂 Project Structure

```
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
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/notes-app.git
cd notes-app
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install flask flask_sqlalchemy flask_bcrypt
```

### 4️⃣ Run App
```bash
python app.py
```

### 5️⃣ Open Browser
```
http://127.0.0.1:5000/
```

---

## 📦 Requirements

- Python 3.8+
- Flask
- Flask SQLAlchemy
- Flask Bcrypt

---

## 🔮 Future Enhancements

- Search notes
- Dark mode
- Tags/categories
- Delete confirmation popup
- Rich text editor for notes

---

## 🤝 Contributing

Pull requests are welcome.  
For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the **MIT License**.

