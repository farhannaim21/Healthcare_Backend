# 🏥 Django Healthcare Backend API

This is a RESTful backend API for managing **patients**, **doctors**, and **patient-doctor assignments** for a healthcare system. Built using **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT authentication**, the system supports secure registration, login, and CRUD operations.

---

## 🔧 Tech Stack

- Python 3.10+
- Django 4+
- Django REST Framework
- PostgreSQL
- JWT Authentication (via `djangorestframework-simplejwt`)
- Environment Configuration via `python-decouple`

---

## 🚀 Features

- 🔐 User Registration & JWT Login
- 🩺 Patient Management (Add, Update, Delete, View)
- 👨‍⚕️ Doctor Management (Add, Update, Delete, View)
- 🔄 Patient–Doctor Assignment APIs
- ⚙️ PostgreSQL Database Integration
- 🧪 Tested with Postman
- 📦 Organized code with serializers, views, and URL routing
- 🌐 `.env` support for secure config management

---

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/farhannaim21/Healthcare_Backend.git
cd Healthcare_Backend
```
### Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # On Windows
```
### 3. Install Dependencies
```bash
pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt python-decouple
```
### 4. Configure .env
Create a .env file in the root directory:
```bash

SECRET_KEY=your_django_secret_key
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```
### 5. Apply Migrations
```bash

python manage.py makemigrations
python manage.py migrate
```
### 6. Create Superuser (Optional)
```bash

python manage.py createsuperuser
```
### 7. Run the Server
```bash

python manage.py runserver
```

