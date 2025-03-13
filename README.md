# FastAPI-ToDo-App

This project is a To-Do application developed using FastAPI. Users can register, log in, and create their To-Do lists. It includes OAuth2 authentication and a secure login system using JWT. To-Do descriptions are generated using Google Gemini AI.

## Features
- User Registration and Login System (JWT Authentication)
- User-based To-Do list management
- Database support for SQLite
- Password hashing with `passlib` and authentication using `OAuth2PasswordBearer`
- HTML template support (using `Jinja2Templates`)
- Google Generative AI integration
- Environment variable support (using `dotenv`)

## Technologies Used
- **FastAPI** - Fast and modern API development
- **SQLAlchemy** - ORM and database management
- **JWT (JSON Web Token)** - Secure authentication
- **Jinja2** - HTML templating
- **Bcrypt** - Password hashing

## Installation
1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
2. **Create the database:**
    ```sh
    python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
    ```
3. **Start the server:**
    ```sh
    uvicorn main:app --reload
    ```
4. **Open the application:**
    - API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - Homepage redirection: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

| Endpoint            | Method | Description |
|---------------------|--------|-------------|
| `/auth/register`    | POST   | Creates a new user |
| `/auth/token`       | POST   | Logs in a user and returns a JWT token |
| `/todo/`           | GET    | Retrieves all tasks for the user |
| `/todo/{todo_id}`  | GET    | Retrieves a specific task by ID |
| `/todo/`           | POST   | Creates a new task |
| `/todo/{todo_id}`  | DELETE | Deletes a specified task |

