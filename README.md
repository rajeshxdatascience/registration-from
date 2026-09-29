# Registration Form

A simple registration form built using React, FastAPI, and PostgreSQL. Users can enter their name and email, and the data is saved in the database.

## Tech Stack

* React
* FastAPI
* PostgreSQL
* SQLAlchemy

## Features

* Simple registration form
* Submit name and email
* Save user details in PostgreSQL
* Basic error handling

## Run Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Create a `.env` file in the backend folder:

```env
DB_PASSWORD=your_postgres_password
```

### Frontend

```bash
npm install
npm run dev
```

Open the local URL shown in the terminal.

## Database

Create a PostgreSQL database named `registration_db`. The `users` table is created automatically when the backend starts.

## How It Works

1. User enters their name and email in the React form.
2. React sends the data to the FastAPI backend.
3. FastAPI saves the data in PostgreSQL using SQLAlchemy.
4. A success message is shown after registration.
