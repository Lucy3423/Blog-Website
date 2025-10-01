from user import User
from topic import Topic

class Blog:   
    def __init__(self, blog_id, owner, description, blog_name, blog_cover, topics):
        self.blog_id = blog_id
        self.owner:User = owner
        self.description = description
        self.blog_name = blog_name  
        self.blog_cover = blog_cover
        self.topics:Topic = topics   
        
