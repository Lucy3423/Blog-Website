from post import Post

class Topic:
    def __init__(self, topic_id, topic_name, posts):  
        self.topic_id = topic_id
        self.topic_name = topic_name
        self.posts:Post = posts