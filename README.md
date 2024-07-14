# Expense Tracker

## Description

Expense Tracker is a web application built with Django and Tailwind CSS. It allows users to track their expenses, categorize them by month, and perform CRUD operations on expenses, add categories etc.

## Project Setup

### Prerequisites

- Python 3.10 or later
- pip
- npm (Node Package Manager)

### Installation

1. **Clone the repository and cd into expense_tracker folder:**
   ```
   cd expense-tracker
   ```
2. **Create and activate a virtual environment:**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   npm install
   ```

4. **Set up Tailwind CSS:**
   ```
   python manage.py tailwind init
   Update Tailwind configuration:
   ```

- In tailwind.config.js, add paths to your Django templates:

   ```
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
   ```

- Make and apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

- Create a superuser:
   ```
   python manage.py createsuperuser
   ```
- Run the development server:
   ```
   python manage.py runserver
   ```
## Usage

- Access the application: Open your browser and go to http://127.0.0.1:8000/.
- Admin Interface: Access the admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials.

## File Structure

- expenses/: Contains the Django app for managing expenses.
- expenses/templates/: Contains the HTML templates.
- static/: Contains static files including Tailwind CSS.
- tailwind.config.js: Tailwind CSS configuration file.

## License
This project is licensed under the MIT License.
