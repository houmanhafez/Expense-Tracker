# Expense Tracker

## Description

Expense Tracker is a web application built with Django and Tailwind CSS. It allows users to track their expenses, categorize them by month, and perform CRUD operations on expenses.

## Project Setup

### Prerequisites

- Python 3.x
- pip
- npm (Node Package Manager)

### Installation

1. **Clone the repository:**
   ``
   git clone <repository-url>
   cd expense-tracker``
2. **Create and activate a virtual environment:**

``python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
``
3. **Install dependencies:**
``
pip install -r requirements.txt
npm install
``

4. **Set up Tailwind CSS:**
``
python manage.py tailwind init
Update Tailwind configuration:
``

- In tailwind.config.js, add paths to your Django templates:

``
module.exports = {
  content: [
    './templates/**/*.html',
    './expenses/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
``

- Make and apply migrations:
``
python manage.py makemigrations
python manage.py migrate
``

- Create a superuser:
``
python manage.py createsuperuser
``
- Run the development server:
``
python manage.py runserver
``
## Usage

- Access the application: Open your browser and go to http://127.0.0.1:8000/.
- Admin Interface: Access the admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials.

## Features

- Add, view, and edit expenses.
- Categorize expenses by month.
- View total expenses for each month.

## File Structure

- expenses/: Contains the Django app for managing expenses.
- templates/: Contains the HTML templates.
- static/: Contains static files including Tailwind CSS.
- tailwind.config.js: Tailwind CSS configuration file.

## Dependencies

- Django
- django-browser-reload (optional, for development)
- Tailwind CSS

## License
This project is licensed under the MIT License.
