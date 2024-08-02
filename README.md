# Django Web Application Project

## Overview

This project is a Django web application designed to demonstrate my skills in developing a full-fledged web application with user authentication, profile management, and interaction with a MySQL database. The project includes user registration, login, and profile management features.

## Features

- User registration and login
- User profile creation and management
- Contact form with feedback messages
- Displaying motivational quotes on the homepage

## Project Structure

- `my_django_final_project/`
  - `settings.py`: Configuration settings for the Django project.
  - `urls.py`: URL routing for the project.
  - `wsgi.py`: Web Server Gateway Interface configuration.
  - `asgi.py`: Asynchronous Server Gateway Interface configuration.

- `my_django_app/`
  - `views.py`: Contains view functions for handling HTTP requests.
  - `models.py`: Database models for user information and profiles.
  - `templates/`: HTML templates for rendering web pages.
    - `home.html`: Homepage template.
    - `contact.html`: Contact form template.
    - `about.html`: About us page template.
    - `register.html`: User registration template.
    - `login.html`: User login template.
    - `profile.html`: User profile display template.
    - `profile_questions.html`: Profile questions template for additional user info.
    - `base.html`: Base template used for all the pages, such as the footer that is constant. 

## Setup and Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/my_django_final_project.git
   cd my_django_final_project
