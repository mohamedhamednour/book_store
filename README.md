Book Review System
Description
This is a Django-based web application for managing books and user reviews. Users can register, log in, and submit reviews for books, including ratings and comments. The project includes a custom user model, book management, review functionality, and unit tests using pytest.
Features

User Authentication: Users can register and log in using their email addresses.
Book Management: Store and retrieve book details (title, author, published date, description).
Review System: Authenticated users can submit reviews for books with ratings (1-5) and optional comments.
Custom Queries: A custom QuerySet (BookQuerySet) for advanced book filtering and querying.
Unit Tests: Comprehensive tests implemented with pytest to ensure functionality and reliability.

Technologies

Backend: Django
Database: postgresql
Testing: pytest

Installation

Clone the repository:
git clone  https://github.com/mohamedhamednour/book_store


Create a virtual environment:
python -m venv venv
source venv/bin/activate 


Install dependencies:
pip install -r requirements.txt


Apply database migrations:
python manage.py makemigrations
python manage.py migrate


Create a superuser (optional):
python manage.py createsuperuser



Usage

python manage.py runserver



Navigate to the registration page to create an account using an email and password.
Log in using the email-based authentication system.


Add books and reviews:

Use the admin panel (/admin) to add books (requires superuser access).
Authenticated users can submit reviews with ratings and comments for books.


Run tests:
pytest



Project Structure

Models:
User: Custom user model with email-based authentication, first name, last name, and phone number.
Book: Stores book details with a custom manager (BookQuerySet) for querying.
Review: Links users and books, with rating validation (1-5) and unique user-book constraint.


Authentication: Custom user model extending AbstractUser for email-based login.
Testing: Unit tests implemented with pytest to cover models, views, and authentication logic.



