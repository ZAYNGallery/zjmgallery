import os
import random
import tweepy
import json

# Set up Twitter API client
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Directory containing photos
# Update this path based on where your photos are located in the branch
photos_dir = 'photos'

# File to track tweeted photos
tweeted_photos_file = 'tweeted_photos.json'

# Load tweeted photos
if os.path.exists(tweeted_photos_file):
    with open(tweeted_photos_file, 'r') as f:
        tweeted_photos = json.load(f)
else:
    tweeted_photos = []

# Get list of all photos
all_photos = [f for f in os.listdir(photos_dir) if os.path.isfile(os.path.join(photos_dir, f))]

# Get list of photos that have not been tweeted yet
untweeted_photos = list(set(all_photos) - set(tweeted_photos))

# Check if there are untweeted photos available
if untweeted_photos:
    # Choose a random photo
    random_photo = random.choice(untweeted_photos)
    
    # Tweet the photo with caption 'Zayn Malik'
    photo_path = os.path.join(photos_dir, random_photo)
    api.update_status_with_media(status='Zayn Malik', filename=photo_path)
    
    # Update the list of tweeted photos
    tweeted_photos.append(random_photo)
    with open(tweeted_photos_file, 'w') as f:
        json.dump(tweeted_photos, f)
else:
    print("All photos have been tweeted.")
