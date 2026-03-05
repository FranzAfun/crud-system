# Django CRUD System

A simple **CRUD (Create, Read, Update, Delete) web application** built with **Django** for an internship assignment.

## Project Overview

This project demonstrates how to build a basic CRUD system using Django.
The application allows users to:

* Create records
* View records
* Update records
* Delete records
* Upload files with preview and update support

The goal is to practice Django fundamentals including models, views, templates, URL routing, and file handling.

---

## Tech Stack

* Python 3.14
* Django 6.0.3
* SQLite (default Django database)
* HTML / Django Templates

---

## Project Structure

```
crud-system/
│
├── crudproject/        # Main Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── records/            # App responsible for CRUD operations
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── migrations/
│   └── tests.py
│
├── manage.py           # Django management commands
├── db.sqlite3          # SQLite database
├── requirements.txt
└── venv/
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone <your-repository-url>
cd crud-system
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate virtual environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Run migrations

```
python manage.py migrate
```

### 6. Start development server

```
python manage.py runserver
```

Then open:

```
http://127.0.0.1:8000
```

---

## Features (Planned)

* Record creation
* Record listing
* Record update
* Record deletion
* File upload with preview
* Basic UI for record management

---

## Author

Internship Django CRUD Assignment
