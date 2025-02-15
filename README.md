# ICE-wale_website
---
#### Databases on Render are available for a limited time only, so they may not return images or might show errors. However, everything works seamlessly in a local setup. local setup is given below.
[![🍦 Ice Wale](https://img.shields.io/badge/🍦-Visit%20Ice%20Wale-pink)](https://ice-wale.onrender.com/)

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
   
   `pip install requirements.txt`

4. **.env file**
   ```
   DATABASE_URL="postgresql://your link"

   SECRET_KEY="your key"

   DEBUG=False

   ALLOWED_HOSTS=127.0.0.1,localhost

   RENDER=True //it's refering to if you are running locally or on render

   RENDER_EXTERNAL_HOSTNAME=your-project.onrender.com
   
5. **setup database**

   `python manage.py makemigrations`
   
   `python manage.py migrate`

6. **Add admin to login**
   
   `python manage.py createsuperuser` and provide necessary details.

7. **Run server**

   `python manage.py runserver`

8. Open your browser and go to `http://127.0.0.1:8000/`

9. **To add images**: go to `http://127.0.0.1:8000/admin` and add url of images and you are good to go...


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
    |--- .env
    ├── static/ | staticfile/
    │   ├── media file
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


