# IPO Backend – Django + DRF

This folder contains the complete backend code for the **IPO Web Application**, developed as part of the Bluestock Fintech internship program.

---

## 🔧 Tech Stack

- Python 3.12  
- Django 5.0.6  
- Django REST Framework 3.15.1  
- PostgreSQL  
- Bootstrap 5 (for welcome screen UI)

---

## 📁 Project Structure

```
rahul/
├── manage.py
├── ipo/                   # Django app with models, views, serializers
├── templates/             # Contains welcome page (home.html)
├── media/                 # For DRHP/RHP uploads
├── README.md              # This file
└── ... other project files
```

---

## 🚀 Features Implemented

- Full CRUD API for Companies, IPOs, and Documents
- File upload support for DRHP & RHP PDFs
- DRF filtering and search (e.g., `?status=Listed`, `?search=tata`)
- Admin panel customization
- Media/static setup
- Welcome page using Django templates

---

## 📦 Requirements

Before running the project, install dependencies:

```bash
pip install -r requirements.txt
```

> Or manually install:
```bash
pip install django djangorestframework django-filter
```

---

## ▶️ How to Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit:
- API Root: `http://127.0.0.1:8000/api/v1/`
- Admin Panel: `http://127.0.0.1:8000/admin/`
- Welcome Page: `http://127.0.0.1:8000/`

---



---
