# backend-assessment-cart

# Cart API Assessment

This repository contains a Flask-based microservice for a simple e-commerce cart. It demonstrates:

- Flask application structure
- SQLAlchemy models & relationships
- Alembic database migrations (schema + seed data)
- Dockerized development environment
- Health-check, cart, and product API endpoints

## Prerequisites

- Git
- Docker & Docker Compose (for dev environment)
- (Optional) Python 3.9+ and a local Postgres if running without Docker

## Getting Started

### 1. Clone the repository

```bash
git clone https://your.git.host/your-org/cart-api.git
cd cart-api
```

### 2. Development with Docker

1. **Build and start services**

   ```bash
   docker-compose up --build -d
   ```

This launches:

- **db**: PostgreSQL container (creates `cartdb` with seeded data)
- **api**: Flask service on port 3003

2. **Verify migrations**
   Migrations run automatically in the container. To check:

   ```bash
   docker-compose exec api alembic current
   ```

3. **Health-check**

   ```bash
   curl [http://localhost:3003/health](http://localhost:3003/health)
   curl [http://localhost:3003/health/db](http://localhost:3003/health/db)
   ```

4. **Browse in DataGrip or psql**
   Connect to `localhost:5432` with user `username` / `password`, database `cartdb`.

5. **Stop services**

   ```bash
   docker-compose down
   ```

### 3. Local Python Setup (without Docker)

1. **Create virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure environment**
   Create a `.env` file in the root:

   ```ini
   FLASK_APP=run.py
   FLASK_ENV=development
   DATABASE_URL=postgresql://username:password@localhost:5432/cartdb
   ```

3. **Initialize Postgres**
   Make sure a Postgres server is running and you’ve created:

   - Role: `username` with password `password`
   - Database: `cartdb` owned by `username`

4. **Run migrations**

   ```bash
   alembic upgrade head
   ```

5. **Start the server**

   ```bash
   python run.py
   ```

6. **Test endpoints**

   ```bash
   curl [http://localhost:5000/health](http://localhost:5000/health)
   curl [http://localhost:5000/health/db](http://localhost:5000/health/db)
   curl [http://localhost:5000/api/products](http://localhost:5000/api/products)
   ```

## Assessment Tasks

Candidates should implement the following endpoints (stubs are provided in `app/routes`):

- **Cart Resource** (`app/routes/cart.py`)
- `GET /api/cart/`
- `POST /api/cart/`
- `POST /api/cart/submit`

- **Products List** (`app/routes/products.py`)
- `GET /api/products` (completed, uses `Product.get_all()`)

The goal is to demonstrate:

- SQLAlchemy CRUD and transactions
- Alembic migrations & seeding
- Flask-RESTX for API organization

Good luck!
