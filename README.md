# ICE-wale_website
---
## Project Overview
This is a **Django-based web application** designed to showcase templates, static files, and basic project structure and usage of database. It includes features like custom templates and reusable app components.

---

## Features
- Modular Django app structure.
- Static files setup.
- Templates for various pages:
  - `home.html`
  - `list.html`
  - `sundae.html`, and more.
- Easy-to-use configuration.
- database connectivity

---

## Prerequisites
Before running the project, make sure you have the following installed:
- Python (3.x)
- Django (latest version compatible with Python)
- Git (to clone the repository)
- A virtual environment manager (optional, but recommended)

---

## Installation
Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/therealdope/ICE-wale_website
   cd ICE-wale_website

2. **set environment**
   `python -m venv env`
   
   `source env/bin/activate`   #On Windows:`env\Scripts\activate`
   
3. **requirnment**
   `pip install django`

4. **setup database**
   `python manage.py makemigrations`
   
   `python manage.py migrate`

5. **Run server**
   `python manage.py runserver`

6. Open your browser and go to `http://127.0.0.1:8000/`


---

## Directory Structure
```
Directory structure:
└── therealdope-ICE-wale_website/
    ├── README.md
    ├── manage.py
    ├── base/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   └── migrations/
    │       ├── 0001_initial.py
    │       └── __init__.py
    ├── myapp/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── static/
    │   ├── d.jpg.avif
    │   └── logo3.avif
    └── tampletes/
        ├── bar.html
        ├── base.html
        ├── cake.html
        ├── cone.html
        ├── home.html
        ├── list.html
        └── sundae.html
```
---

## Contributions are welcome! To contribute:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Submit a pull request with a detailed description.

---

## License

This project is licensed under the MIT License.


