from post import Post

class Topic:
    def __init__(self, topic_id, topic_name, topic_image, posts):  
        self.topic_id = topic_id
        self.topic_name = topic_name
        self.topic_image = topic_image
        self.posts:list = posts