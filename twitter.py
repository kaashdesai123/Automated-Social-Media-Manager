import tweepy
from flask import Blueprint, render_template, request, redirect, url_for

twitter_bp = Blueprint('twitter', __name__)

CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

@twitter_bp.route('/post_tweet', methods=['POST'])
def post_tweet():
    tweet_content = request.form.get('tweet')
    api.update_status(tweet_content)
    return redirect(url_for('dashboard'))
