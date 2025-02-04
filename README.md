# Facebook Insights Microservice

## Overview
This project is a Python-based web application that interacts with Facebook data. It includes functionalities for data scraping, API routes for handling posts and pages, and database management.

## Features
- Facebook data scraping
- API routes for managing posts and pages
- Database integration
- Docker support for containerization
- Modular and scalable architecture

## Installation

### Prerequisites
- Python 3.x
- Docker (optional)
- Virtual environment (recommended)

### Steps
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd facebook_project
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure environment variables in `config.py`.
5. Run database migrations (if applicable):
   ```sh
   python database.py migrate
   ```
6. Run the application:
   ```sh
   python main.py
   ```

## Usage
- The application exposes API routes to manage Facebook-related data.
- Use `scraping.py` to fetch data from Facebook.
- Modify `config.py` to adjust database and API settings.
- The API routes are available at `http://localhost:8000/api/`.

### API Endpoints
| Method | Endpoint          | Description          |
|--------|------------------|----------------------|
| GET    | `/api/pages`     | Fetch all pages     |
| GET    | `/api/posts`     | Fetch all posts     |
| POST   | `/api/pages`     | Create a new page   |
| POST   | `/api/posts`     | Create a new post   |

Example usage with `curl`:
```sh
curl -X GET http://localhost:8000/api/pages
```

## Docker Support
To run the project in Docker:
```sh
docker build -t facebook_project .
docker run -p 8000:8000 facebook_project
```

## Directory Structure
```
facebook_project/
│── app/
│   ├── config.py
│   ├── database.py
│   ├── dockerfile
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── scraping.py
│   ├── routes/
│   │   ├── pages.py
│   │   ├── posts.py
│
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License
This project is licensed under [Your License Here].

