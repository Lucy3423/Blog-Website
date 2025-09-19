from user import User
from topic import Topic

class Blog:   
    def __init__(self, owner, blog_name, blog_cover, topics):
        self.owner:User = owner
        self.blog_name = blog_name  
        self.blog_cover = blog_cover
        self.topics:Topic = topics   
