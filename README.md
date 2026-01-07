# Expense Tracker 🧾💸

A Django-based web application that helps users track, manage, and analyze their daily expenses efficiently.  
This project demonstrates a complete CRUD application with authentication, clean UI, and structured backend design.

---

## 🚀 Features

- 🔐 User Authentication (Sign Up, Login, Logout)
- ➕ Add Expenses with title, amount, category, date, and description
- ✏️ Update existing expenses
- 🗑️ Delete expenses
- 📂 Category-based filtering
- 📅 Expenses sorted date-wise
- 📊 Dashboard summary:
  - Today's spending
  - Monthly total
  - Overall total
- ⚙️ Account Settings:
  - Update email
  - Change password (with old password verification)
- 🔒 Secure session handling with CSRF protection
- 🎨 Clean UI using Bootstrap

---

## 🛠️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite3
- Authentication: Django built-in User model
- Version Control: Git & GitHub

---

## 📂 Project Structure

```
expensetracker/
│
├── expenses/                  # Main app
│   ├── templates/             # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── add_expense.html
│   │   ├── update_expense.html
│   │   ├── login.html
│   │   └── signup.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── expensetracker/            # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

1. Clone the repository
     git clone https://github.com/Rishikesh0117/expensetracker.git
     cd expensetracker
2. Create & activate virtual environment
     python -m venv venv
     venv\Scripts\activate
3. Install dependencies
     pip install -r requirements.txt
4. Run migrations
     python manage.py makemigrations
     python manage.py migrate
5. Start the server
     python manage.py runserver
6. Open browser
     http://127.0.0.1:8000/

---

## Security

```yaml
  authentication:
    - Uses Django built-in User model
    - Passwords are securely hashed (PBKDF2)
    - Plain-text passwords are never stored

  session_management:
    - Login-protected views using @login_required
    - Sessions cleared on logout
    - Browser caching disabled for sensitive pages

  csrf_protection:
    - CSRF tokens enabled for all POST forms
    - Prevents cross-site request forgery attacks

  data_isolation:
    - Expenses linked to users via foreign key
    - Users can access only their own data

  repository_safety:
    - Database file excluded using .gitignore
    - Virtual environment not tracked
    - No credentials committed to GitHub
```
---

## Future Scope

```yaml
  analytics:
    - Monthly and yearly expense analysis
    - Category-wise spending insights
    - Interactive charts and dashboards

  machine_learning:
    - Expense trend prediction
    - Budget forecasting models
    - Anomaly detection for unusual spending

  personalization:
    - Spending habit analysis
    - Smart recommendations to reduce expenses
    - User-specific financial insights

  data_export:
    - Export expenses as CSV
    - Export reports as PDF

  api_layer:
    - REST APIs using Django REST Framework
    - Support for mobile or frontend frameworks

  scalability:
    - Migration to PostgreSQL or MySQL
    - Cloud deployment support
```
