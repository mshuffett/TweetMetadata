import json
from datetime import datetime

class Collection(object):
    def __init__(self):
        self.start_date = datetime.max
        self.end_date = datetime.min

    def add_tweet(self, tweet):
        created_at = datetime.strptime(tweet.created_at, '%Y-%m-%d %H:%M:%S')
        self.start_date = min(self.start_date, created_at)
        self.end_date = max(self.start_date, created_at)

    def __str__(self):
        return json.dumps({'start_date': self.start_date, 'end_date': self.end_date})
