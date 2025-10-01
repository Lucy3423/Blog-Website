from blog import Blog
from user import User
from forms.build_blog_form import Build_blog_form

from flask import flash

class Blog_manager:
    def __init__(self, blogs):
        self.blogs:Blog = []
        self.current_id = 0
    
    def creat_new_blog(self, form:Build_blog_form):
        new_user = User(form.owner_name.data, form.fav_singer.data, form.image_fav_singer.data, form.fun_fact.data)
        new_topics = [form.topic1.data, form.topic2.data, form.topic3.data]
        self.blogs.append(Blog(self.current_id, new_user, form.description.data, form.blog_name.data, form.blog_cover.data, new_topics))
        current_id = self.current_id
        self.current_id += 1
        return current_id

    def check_image_format(self, form:Build_blog_form):
        # check that the value of fav_singer_image at self.blogs[blog_index] is correct
        if (form.image_fav_singer.data[-4:] == ".img" or form.image_fav_singer.data[-4:] == ".jpg") or (form.blog_cover.data[-4:] == ".img" or form.blog_cover.data[-4:] == ".jpg"):
            valid = True
        else:
            valid = False

        return valid   
