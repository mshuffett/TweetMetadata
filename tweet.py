class Tweet(object):
    def __init__(self, id_str, text, created_at, screen_name, latitude, longitude, url_mentions=None, *args):
        self.id_str = id_str
        self.text = text
        self.created_at = created_at
        self.screen_name = screen_name
        self.latitude = latitude
        self.longitude = longitude
        self.url_mentions = url_mentions