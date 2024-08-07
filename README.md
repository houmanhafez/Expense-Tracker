# Expense Tracker

## Description

Expense Tracker is a web application built with Django and Tailwind CSS. It allows users to track their expenses, categorize them by month, and perform CRUD operations on expenses, add categories etc.

## Project Setup

### Prerequisites

- Python 3.10 or later
- pip 22 or later
- npm 8 or later

### Installation

1. **Create and activate a virtual environment:**

   ```
   python -m venv venv

   ```
   On MacOs/Linux:
   ```
   source venv/bin/activate
   ```
   On Windows:
   ```
   venv\Scripts\activate
   ```
3. **Install dependencies to the virtual environment:**
   ```
   pip install -r requirements.txt
   npm install
   ```
- Make and apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
- Make and apply the expenses migrations:
  ```
   python manage.py makemigrations expenses
   python manage.py migrate expenses  
  ```
- Create a superuser for the admin interface(optional):
   ```
   python manage.py createsuperuser
   ```
- Run the development server:
   ```
   python manage.py runserver
   ```
## Usage

- Open your browser and go to http://127.0.0.1:8000/
- Access the admin interface at http://127.0.0.1:8000/admin/ using the superuser email and password.

## License
This project is licensed under the MIT License.
