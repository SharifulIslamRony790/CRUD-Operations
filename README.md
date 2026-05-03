# Django Blog CRUD Application

A professional, production-ready Django application demonstrating core CRUD (Create, Read, Update, Delete) operations using **Function-Based Views (FBVs)**. This project serves as a clean boilerplate for building blog-like systems with a focus on simplicity and traditional Django patterns.

## Description

This project is a blog management system where users can manage posts. It showcases the use of Django's ORM, template inheritance, and URL routing. Built with a clean separation of concerns, it uses the "blog" app to handle business logic and a centralized "templates" directory for the UI.

## Features

- **Read Operations**: List all blog posts with sorting and date formatting.
- **Data Management**: Tracks post creation and update timestamps.
- **Status Tracking**: Ability to mark posts as active or inactive.
- **Responsive UI**: Integrated with Bootstrap via a base template for mobile-friendly viewing.
- **Template Inheritance**: Efficient UI management using a base layout.
- **Admin Interface**: Full integration with Django Admin for backend management.

## Tech Stack

- **Backend**: Python 3.x, Django 4.2+
- **Database**: SQLite (Development) / PostgreSQL (Production ready)
- **Frontend**: HTML5, CSS3, Bootstrap 5 (via CDN in base.html)
- **Architecture**: MVT (Model-View-Template)

## Installation Guide

Follow these steps to set up the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/SharifulIslamRony790/CRUD-Operations.git
   cd CRUD-Operations
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   # Add other dependencies if applicable
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (to access the admin panel)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Usage Instructions

- Access the main list of posts: `http://127.0.0.1:8000/posts/list/`
- Management backend: `http://127.0.0.1:8000/admin/`
- To add a new post, log into the admin panel and navigate to the "Posts" section.

## Project Structure

```text
├── blog/                   # Core application folder
│   ├── migrations/         # Database migration history
│   ├── models.py           # Post database schema
│   ├── views.py            # Logic for list, create, edit, delete
│   ├── urls.py             # App-specific URL routing
│   └── admin.py            # Admin panel configuration
├── Crud_Operation/         # Project configuration
│   ├── settings.py         # Global settings
│   └── urls.py             # Root URL configuration
├── templates/              # HTML templates
│   ├── base.html           # Master layout
│   └── list.html           # Post list view
├── db.sqlite3              # Local development database
└── manage.py               # Django management script
```

## API / URL Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/posts/list/` | GET | View all blog posts |
| `/admin/` | GET/POST | Management interface |

## Contributing Guidelines

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Author Information

**Project Developer**
- GitHub: [@SharifulIslamRony790](https://github.com/SharifulIslamRony790)
- Email: mdsharifulislamrony790@gmail.com
