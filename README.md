# 🏥 Hospital Management System

A full-stack hospital management system built with Django, PostgreSQL and Django REST Framework.

> Built from scratch as a learning project — first Django project, completed in one week.

## 🌐 Live Demo
**[https://hospital-django-dnk3.onrender.com](https://hospital-django-dnk3.onrender.com)**

## 📂 Source Code
**[github.com/Nick0099/hospital-django](https://github.com/Nick0099/hospital-django)**

---

## ✨ Features

- 👤 **Patients** — registration, blood group, emergency contacts
- 🩺 **Doctors** — specialties, qualifications, shifts, prescribable medications
- 🏥 **Staff** — non-medical staff with roles and departments
- 📅 **Appointments** — booking, cancellation, status tracking
- 💊 **Prescriptions** — dosage, frequency, instructions, active/inactive
- 📦 **Inventory** — medicines and supplies with low stock alerts
- 🔔 **Notifications** — automatic medication reminders and refill alerts
- 🔐 **Auth** — role-based login (doctor / patient / staff / admin dashboards)
- 🌐 **REST API** — full DRF API with JWT auth, filtering, search, pagination
- 📖 **Swagger** — interactive API docs at /api/docs/

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.14, Django 6.0 |
| API | Django REST Framework, JWT (simplejwt) |
| Database | PostgreSQL (prod), SQLite (dev) |
| Frontend | Bootstrap 5, Bootstrap Icons, Crispy Forms |
| Testing | pytest, pytest-django (28 tests) |
| DevOps | Docker, docker-compose, GitHub Actions CI/CD |
| Deployment | Render, WhiteNoise, gunicorn |

---

## 🚀 Quick Start

### Local development
```bash
git clone https://github.com/Nick0099/hospital-django.git
cd hospital-django
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Docker
```bash
docker-compose up --build
```

Visit `http://127.0.0.1:8000`

---

## 🔐 User Roles

Set up via `/admin/` under **Groups**:

| Group | Access |
|---|---|
| `Doctors` | Appointments, prescriptions |
| `Patients` | Own appointments, notifications |
| `Staff` | Full management access |
| Superuser | Everything + admin panel |

---

## 🔑 Demo Credentials

You can test the live application at [hospital-django-dnk3.onrender.com](https://hospital-django-dnk3.onrender.com) using the following demo accounts:

| Role          | Username       | Password    |
|---------------|----------------|-------------|
| Admin         | admin          | Django123   |
| Doctor        | doctor         | Django123   |
| Patient       | patient        | Django123   |
| Receptionist  | receptionist   | Django123   |

> ⚠️ These are demo accounts on a public demo instance — please don't store any real personal or sensitive data here.

---

## 🌐 API Endpoints

| Endpoint | Methods | Description |
|---|---|---|
| `/api/patients/` | GET, POST | List / create patients |
| `/api/doctors/` | GET, POST | List / create doctors |
| `/api/appointments/` | GET, POST | List / create appointments |
| `/api/prescriptions/` | GET, POST | List / create prescriptions |
| `/api/inventory/` | GET, POST | List / create inventory |
| `/api/inventory/low-stock/` | GET | Low stock alert |
| `/api/token/` | POST | Get JWT token |
| `/api/docs/` | GET | Swagger UI |

---

## 🧪 Tests

```bash
pytest
```

28 tests covering models, views and API endpoints.

---

## 📁 Project Structure

```
hospital/
├── hospital/          # Project config
├── patients/          # Patient management
├── doctors/           # Doctor profiles
├── staff/             # Non-medical staff
├── appointments/      # Appointment booking
├── prescriptions/     # Prescription management
├── inventory/         # Supply tracking
├── notifications/     # Reminders and alerts
├── api/               # REST API
├── templates/         # Shared templates
└── manage.py
```

---

## 👨‍💻 Author

**Nischal Neupane** — [@Nick0099](https://github.com/Nick0099)  
Self-taught developer, Kathmandu Nepal 🇳🇵
