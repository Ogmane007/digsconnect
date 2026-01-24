DigsConnect

DigsConnect is a student accommodation marketplace that connects students looking for rental properties with landlords offering listings.
It supports role-based access, property listings with images, search & filtering, inquiries, and a landlord dashboard.

Built with Django 4.2, styled with Bootstrap 5, and designed to scale to production.

 Features
 Authentication & Roles

User registration & login

Role-based profiles:

Students

Landlords

Secure access control (landlords vs students)

 Property Listings

Landlords can:

Create properties

Upload multiple images per property

Edit and delete listings

Properties include:

Title

Description

Price

Address

Images

 Search & Browse

Search by keyword or location

Filter by price range

Sort by:

Newest

Price (low → high)

Price (high → low)

 Inquiries

Students can contact landlords about a property

Messages are private and stored securely

Landlords view inquiries in a dedicated dashboard

 Landlord Dashboard

View all owned listings

Manage images

View inquiries

Edit / delete properties

 UI & UX

Clean, responsive design

Bootstrap 5 + custom CSS

Mobile-friendly

Image preview cards

 Tech Stack

Backend: Django 4.2 (Python 3.12)

Frontend: Django Templates + Bootstrap 5

Database: SQLite (development), PostgreSQL (production)

Media Storage: Local (dev), cloud-ready

Auth: Django built-in authentication

Deployment: Render (Gunicorn + Whitenoise)

📁 Project Structure
digsconnect/
├── config/             # Project settings
├── properties/         # Main app (models, views, urls)
├── templates/          # HTML templates
│   ├── base.html
│   ├── registration/
│   └── properties/
├── static/             # CSS, static assets
│   └── css/main.css
├── media/              # Uploaded property images
├── manage.py
└── requirements.txt

 Installation (Local Development)
1️ Clone the repository
git clone https://github.com/YOUR_USERNAME/digsconnect.git
cd digsconnect

2️ Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️ Install dependencies
pip install -r requirements.txt

4️ Apply migrations
python manage.py migrate

5️ Create superuser
python manage.py createsuperuser

6️ Run the server
python manage.py runserver


Open:
 http://127.0.0.1:8000/

 Test Accounts
Landlord

Set user profile to landlord via admin

Access dashboard: /dashboard/

Add listings & images

Student

Default role

Browse listings

Submit inquiries

🗄 Admin Panel

Access Django admin:

/admin/


Manage:

Users

User profiles

Properties

Images

Inquiries

 Deployment

This project is production-ready and configured for Render deployment using:

gunicorn

whitenoise

dj-database-url

PostgreSQL

Key production files:

build.sh

Procfile

Environment variables:

SECRET_KEY

DATABASE_URL

DEBUG=False

 Security Notes

Role-based access enforced

Users cannot modify others’ listings

Media files protected by ownership logic

Production secrets loaded via environment variables

 Roadmap (Future Improvements)

Email notifications for inquiries

Cloud media storage (S3 / Cloudinary)

Favorites / saved listings

Reviews & ratings

Payments / premium listings

Map-based search

 License

This project is for educational and MVP purposes.
You may adapt or extend it as needed.

 Author

Built with  as a full-stack Django marketplace project.
