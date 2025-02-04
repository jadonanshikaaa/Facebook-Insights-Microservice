# Facebook-Insights-Microservice

## Overview
This project is a Facebook Insights Microservice that allows users to fetch and store insights of a given Facebook Page username. The service scrapes relevant details, stores them in a database, and exposes RESTful APIs to retrieve the stored insights with filtering options.

## Features
### Mandatory Features:
- **Scraper Service**
  - Extracts basic page details (Name, URL, ID, Profile Picture, Email, Website, Category, Followers, Likes, Creation Date, etc.)
  - Fetches recent posts (top 25-40 posts)
  - Retrieves comments on posts
  - Collects followers and following details (if available)
- **Database Storage**
  - Stores scraped data with relationships between entities
- **API Endpoints**
  - Get details of a given Facebook Page username
  - Filter pages by follower count range, name, category, etc.
  - Retrieve a list of followers and following
  - Fetch recent 10-15 posts
  - Pagination support for GET requests
- **Postman Collection**
  - A Postman Collection JSON for API testing

### Bonus Features:
- **AI-powered Page Summary** using ChatGPT API or other LLMs
- **Asynchronous Processing** for scraping, database operations, and API calls
- **Cloud Storage Integration** (S3, GCS, etc.) to store profile pictures and posts
- **Caching** with a TTL (Time-To-Live) of 5 minutes

## Tech Stack
- **Backend:** Python (FastAPI/Django/Flask)
- **Database:** MySQL/MongoDB
- **Scraping:** BeautifulSoup/Selenium/Scrapy
- **Asynchronous Handling:** Celery/Aiohttp
- **Caching:** Redis
- **Cloud Storage:** AWS S3/Google Cloud Storage

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/facebook-insights-microservice.git
   cd facebook-insights-microservice
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and configure database and API keys.
4. Run the database migrations (if applicable):
   ```sh
   python manage.py migrate  # For Django
   ```
5. Start the application:
   ```sh
   python app.py  # For Flask
   ```

## API Endpoints
### 1. Get Page Details
```http
GET /api/page/{username}
```
**Query Params:**
- `followers_min` (optional): Minimum number of followers
- `followers_max` (optional): Maximum number of followers
- `category` (optional): Filter by page category
- `name` (optional): Partial match for page name

### 2. Get Followers List
```http
GET /api/page/{username}/followers
```

### 3. Get Recent Posts
```http
GET /api/page/{username}/posts?limit=10
```

### 4. AI Summary of a Page
```http
GET /api/page/{username}/summary
```

## Deliverables
- [x] Public GitHub Repository
- [x] README Documentation
- [ ] Postman Collection (Optional)
- [ ] Deployed Server Link (Optional)
- [ ] Demo Video (Optional)

## Contribution
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

