import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve social media tokens from environment variables
LINKEDIN_TOKEN = os.getenv("LINKEDIN_TOKEN")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
INSTAGRAM_TOKEN = os.getenv("INSTAGRAM_TOKEN")

def fetch_linkedin_info(name):
    headers = {"Authorization": f"Bearer {LINKEDIN_TOKEN}"}
    response = requests.get(f"https://api.linkedin.com/v2/people/(vanityName:{name})", headers=headers)
    return response.json() if response.ok else {"error": "LinkedIn data not available"}

def fetch_twitter_info(username):
    auth = OAuth1(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    response = requests.get(f"https://api.twitter.com/2/users/by/username/{username}", auth=auth)
    return response.json() if response.ok else {"error": "Twitter data not available"}

def fetch_instagram_info(user_id):
    response = requests.get(f"https://graph.instagram.com/{user_id}?fields=username&access_token={INSTAGRAM_TOKEN}")
    return response.json() if response.ok else {"error": "Instagram data not available"}

def fetch_all_social_media_info(name):
    linkedin_info = fetch_linkedin_info(name)
    twitter_info = fetch_twitter_info(name)
    instagram_info = fetch_instagram_info("placeholder_user_id")  # Placeholder for Instagram

    return {
        "LinkedIn": linkedin_info,
        "Twitter": twitter_info,
        "Instagram": instagram_info
    }
