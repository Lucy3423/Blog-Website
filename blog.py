from user import User
class Blog:   
    def __init__(self, user, blog_name, topics):
        user:User = user
        blog_name = blog_name  
        self.topics:list = topics
