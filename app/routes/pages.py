from fastapi import APIRouter
from app.database import db
from app.scraping import scrape_facebook_page
from app.services.cache import get_from_cache, set_to_cache

router = APIRouter()

@router.get("/page/{username}")
async def get_page(username: str):
   cached_data = get_from_cache(username)
    if cached_data:
       return cached_data
    data=scrape_facebook_page(username)
    print(data)
   page = await db["pages"].find_one({"username": username})
    if not page:
       data = scrape_facebook_page(username)
       if data:
           await db["pages"].insert_one(data)
          set_to_cache(username, data)
           return data
       return {"error": "Page not found"}
    return page
