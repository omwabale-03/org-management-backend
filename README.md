# Organization Management Backend

A **FastAPI + MongoDB** based backend service that supports **multi-tenant organization management**.
Each organization has its **own dynamic MongoDB collection**, while a **master database** stores global metadata and admin credentials.

This project was built as part of a **Backend Developer Intern Assignment**.

---

## 🚀 Features

* Create and manage organizations (multi-tenant architecture)
* Dynamic MongoDB collection creation per organization
* Master database for global metadata
* Secure admin authentication using JWT
* Password hashing with bcrypt
* RESTful APIs with FastAPI
* Swagger UI for easy testing

---

## 🛠 Tech Stack

* **Backend Framework:** FastAPI (Python)
* **Database:** MongoDB (Community Edition)
* **Authentication:** JWT (JSON Web Tokens)
* **Password Security:** bcrypt
* **ORM / Driver:** PyMongo
* **API Documentation:** Swagger UI

---

## 📁 Project Structure

```
org-management-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── org_routes.py
│   │   └── auth_routes.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── org_model.py
│   │   └── admin_model.py
│   └── utils/
│       ├── __init__.py
│       ├── auth.py
│       └── hash.py
├── venv/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/org-management-backend.git
cd org-management-backend
```

---

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install & Start MongoDB

* Install MongoDB Community Server
* Ensure MongoDB service is running
* Default connection URL:

```
mongodb://localhost:27017/
```

---

### 5️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 API Endpoints

### 🔹 Create Organization

**POST** `/org/create`

```json
{
  "organization_name": "Google",
  "email": "admin@google.com",
  "password": "admin123"
}
```

---

### 🔹 Admin Login

**POST** `/admin/login`

```json
{
  "email": "admin@google.com",
  "password": "admin123"
}
```

Returns JWT token.

---

### 🔹 Get Organization

**GET** `/org/get?name=Google`

---

### 🔹 Update Organization

**PUT** `/org/update`

```json
{
  "old_name": "Google",
  "new_name": "Alphabet",
  "new_email": "admin@alphabet.com",
  "new_password": "newpass123"
}
```

---

### 🔹 Delete Organization

**DELETE** `/org/delete?name=Google`

Requires valid JWT token.

---

## 🧠 Architecture Overview

* **Master Database (`master_db`)**

  * `organizations` collection
  * `admins` collection

* **Dynamic Organization Databases**

  * `org_<organization_name>`

Each organization operates independently while sharing authentication logic.

---
