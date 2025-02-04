import time
import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_facebook_page(username: str):
    url = f"https://www.facebook.com/{username}"
    
    # Automatically download and set up geckodriver
    geckodriver_autoinstaller.install()  # This downloads the appropriate version of geckodriver

    # Configure Firefox options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0")

    # Initialize WebDriver with Firefox and geckodriver
    service = Service()  # geckodriver_autoinstaller handles the geckodriver path
    driver = webdriver.Firefox(service=service, options=options)
    
    driver.get(url)
    
    try:
        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        time.sleep(5)  # Additional sleep time for content to load

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        # Save the soup object to a file
        with open("facebook.txt", "w", encoding="utf-8") as file:
            file.write(str(soup))  # Save the HTML content as text
        print("HTML content saved to facebook.txt")

    except Exception as e:
        print(f"Error while waiting for the page to load: {e}")
        driver.quit()
        return None

    driver.quit()

    # Extract profile picture from the first child of the <img> tag
    profile_pic = None
    profile_img_tag = soup.find("img", {"src": True})
    if profile_img_tag and profile_img_tag.findChildren():
        profile_pic = profile_img_tag.findChildren()[0].get("src")

    # Extract followers count by searching for the anchor link with the specific href
    followers = None
    followers_link = soup.find("a", href=lambda x: x and "followers" in x)
    if followers_link:
        followers = followers_link.get_text(strip=True)

    # In case the profile image and followers are still not found, we will try to inspect other elements
    if not profile_pic:
        profile_pic_tag = soup.find("div", {"class": "profilePicThumb"})
        if profile_pic_tag:
            profile_pic = profile_pic_tag.get("style", "").split("url(")[-1].split(")")[0]

    data = {
        "name": soup.find("title").text.strip() if soup.find("title") else None,
        "url": url,
        "profile_pic": profile_pic,
        "followers": followers,
    }
    
    return data

