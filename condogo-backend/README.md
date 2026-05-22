# CondoGo API

A REST API for CondoGo — a condominium access management system.
Built with FastAPI and PostgreSQL.

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL + SQLAlchemy
- **Auth:** JWT (python-jose + passlib)
- **Server:** Uvicorn
- **Language:** Python 3.11+

## Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL

### Installation

1. Clone the repository
   \```bash
   git clone https://github.com/yourname/condogo-backend.git
   cd condogo-backend
   \```

2. Create and activate virtual environment
   \```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   \```

3. Install dependencies
   \```bash
   pip install -r requirements.txt
   \```

4. Setup environment variables
   \```bash
   cp .env.example .env
   # Fill in your values
   \```

5. Run the server
   \```bash
   uvicorn app.main:app --reload
   \```

## Environment Variables

Create a `.env` file in the root directory:

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | JWT secret key |
| `ALGORITHM` | JWT algorithm (HS256) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry in minutes |

## API Endpoints

### Auth
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/auth/register` | Register new user | No |
| POST | `/auth/login` | Login | No |
| GET | `/auth/me` | Get current user | Yes |

### Users
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| GET | `/users` | Get all users | Admin |
| GET | `/users/{id}` | Get user by ID | Admin |
| DELETE | `/users/{id}` | Delete user | Admin |

## Project Structure

