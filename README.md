# 🏥 Hospital Management System

A full-featured hospital management system built with Django. Manages patients, doctors, staff, appointments, prescriptions, inventory and notifications.

> Built as a learning project to master Django from scratch.

---

## 🚀 Features

- **Patients** — register patients with blood group, contact, emergency info
- **Doctors** — manage specialties, qualifications, shifts and prescribable medications
- **Staff** — non-medical staff with roles and departments
- **Appointments** — book, view and cancel appointments between patients and doctors
- **Prescriptions** — prescribe medications with dosage, frequency and instructions
- **Inventory** — track medicines and supplies with low stock alerts
- **Notifications** — automatic medication reminders and refill alerts for patients
- **Authentication** — role-based login for doctors, patients, staff and admins

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.14, Django 6.0 |
| Database | SQLite (dev), PostgreSQL (prod) |
| Frontend | Bootstrap 5, Bootstrap Icons |
| Auth | Django built-in authentication |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
hospital/
├── hospital/          # Project config (settings, urls)
├── patients/          # Patient management
├── doctors/           # Doctor profiles and specialties
├── staff/             # Non-medical staff
├── appointments/      # Appointment booking
├── prescriptions/     # Prescription management
├── inventory/         # Medicine and supply tracking
├── notifications/     # Med reminders and alerts
├── templates/         # Shared base template and dashboards
└── manage.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/Nick0099/hospital-django.git
cd hospital-django
```

### 2. Install dependencies
```bash
pip install django
```

### 3. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser
```bash
python manage.py createsuperuser
```

### 5. Run the server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/login/`

---

## 👤 User Roles

Set up roles via `/admin/` under **Groups**:

| Group | Access |
|---|---|
| `Doctors` | Doctor dashboard — view appointments, prescribe |
| `Patients` | Patient dashboard — view appointments, prescriptions, notifications |
| `Staff` | Staff dashboard — manage everything |
| Superuser | Full admin access |

---

## 🗺️ Roadmap

- [x] Patient management
- [x] Doctor management
- [x] Staff management
- [x] Appointment booking
- [x] Prescription system
- [x] Inventory with low stock alerts
- [x] Notification system
- [x] Role-based authentication
- [ ] REST API (Django REST Framework)
- [ ] Deploy to Railway/Render
- [ ] SMS notifications

---

## 👨‍💻 Author
Nischal Neupane

**Nischal** — [@Nick0099](https://github.com/Nick0099)

Built in May 2026 as part of a self-taught Django learning journey.
