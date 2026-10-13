<div align="center">

# FastAPI Tutorial

**A structured learning repository for building scalable, production-ready APIs with FastAPI and MongoDB.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)

</div>

---

## Overview

FastAPI Tutorial is a hands-on project for learning how to structure a real-world FastAPI application. It follows a layered architecture with versioned routers, Pydantic schemas, a service layer, async MongoDB access, JWT authentication, custom exception handling, and logging middleware.

## Features

- **Versioned API** (`/api/v1`) with auth, user, and product endpoints.
- **JWT authentication** with password hashing (passlib and bcrypt).
- **Async MongoDB** access with Motor.
- **Layered architecture:** routers → services → database, with Pydantic schemas.
- **Custom exception classes and handlers.**
- **Request logging middleware.**
- **Settings management** with pydantic-settings and `.env`.
- **Code quality** with Ruff and Black.

## Tech Stack

| Area | Technology |
| --- | --- |
| Framework | FastAPI, Uvicorn |
| Language | Python |
| Database | MongoDB (Motor, PyMongo) |
| Validation | Pydantic v2, pydantic-settings |
| Authentication | PyJWT, passlib, bcrypt |
| Tooling | Ruff, Black |

## Getting Started

### Prerequisites

- Python 3.8 or newer
- A MongoDB instance

### Installation

```bash
git clone https://github.com/RithyBondeth/Fast-API-Tutorial.git
cd Fast-API-Tutorial
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./run.sh
```

Interactive docs are served at [http://localhost:8000/docs](http://localhost:8000/docs).

### Environment Variables

| Variable | Purpose |
| --- | --- |
| `MONGO_URL` | MongoDB connection string |
| `SECRET_KEY` | JWT signing secret |
| `ALGORITHM` | JWT algorithm (for example `HS256`) |

## Project Structure

```text
Fast-API-Tutorial/
├── app/
│   ├── api/v1/endpoints/   # auth, users, products
│   ├── core/               # config, security, dependencies, exceptions, middleware
│   ├── db/                 # MongoDB connection
│   ├── schemas/            # Pydantic models
│   ├── services/           # Business logic
│   └── main.py
├── requirements.txt
└── run.sh
```

## Author

**Rithy Bondeth** — Full Stack Developer & AI Engineer

[![Portfolio](https://img.shields.io/badge/Portfolio-0A0A0A?style=for-the-badge&logo=vercel&logoColor=white)](https://bondeth.dev)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RithyBondeth)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rithy-bondeth-484073282/)
