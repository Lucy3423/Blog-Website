from blog import Blog
from user import User
from topic import Topic
from post import Post
from forms.build_blog_form import Build_blog_form
from forms.add_post_form import Add_post_form


from flask import flash

class Blog_manager:
    def __init__(self, blogs):
        self.blogs:Blog = []
        self.current_id = 0
    
    def create_new_blog(self, form:Build_blog_form):
        new_user = User(form.owner_name.data, form.birthday.data)
        topic1 = Topic(0, form.topic1.data, [])
        topic2 = Topic(1, form.topic2.data, [])
        topic3 = Topic(2, form.topic3.data, [])
        topics = [topic1, topic2, topic3]
        blog_id = len(self.blogs) - 1
        self.blogs.append(Blog(blog_id, new_user, form.description.data, form.blog_name.data, form.blog_cover.data, topics))
        
        current_id = self.current_id
        self.current_id += 1
        return current_id

    def check_image_format(self, form:Build_blog_form):
        # check that the value of fav_singer_image at self.blogs[blog_index] is correct
        if (form.blog_cover.data[-4:] == ".img" or form.blog_cover.data[-4:] == ".jpg"):
            valid = True
        else:
            valid = False

        return valid  


    def identify_star_sign(self, form:Build_blog_form):
        month = form.birthday.data.month
        day = form.birthday.data.day
        print(month)
        
        sign = 'Capricorn'
        # check against each month
        if month == 1:
            if day >= 1 and day <= 19:
                sign = "Capricorn"
            # for the rest of the month 
            else:
                sign = "Aquarius"
        if month == 2:
            if day >= 1 and day <=18:
                sign = "Aquarius"
            else:
                sign = "Pisces"
        if month == 3:
            if day >= 1 and day <=20:
                sign = "Pisces"
            else:
                sign = "Aries"
        if month == 4:
            if day >= 1 and day <=19:
                sign = "Aries"
            else:
                sign = "Tuarus"
        if month == 5:
            if day >=1 and day <=20:
                sign = "Tuarus"
            else:
                sign = "Gemini"
        if month == 6:
            if day >=1 and day <=21:
                sign = "Gemini"
            else:
                sign = "Cancer"
        if month == 7:
            if day >=1 and day <=22:
                sign = "Cancer"
            else:
                sign = "Leo"
        if month == 8:
            if day >=1 and day <=22:
                sign = "Leo"
            else:
                sign = "Virgo"
        if month == 9:
            if day >=1 and day <=22:
                sign = "Virgo"
            else:
                sign = "Libra"
        if month == 10:
            if day >=1 and day <=23:
                sign = "Libra"
            else:
                sign = "Scorpio"
        if month == 11:
            if day >=1 and day <=21:
                sign = "Scorpio"
            else:
                sign = "Saggittarius"
        if month == 12:
            if day >=1 and day <=21:
                sign = "Saggittarius"
            else:
                sign = "Capricorn"
        return sign
        
    def add_blog_post(self, form:Add_post_form, blog:Blog, topic_id, blog_id):
        new_post = Post(form.title.data, form.date.data, form.bio.data, form.content.data)
        topic = blog.topics[topic_id]
        topic.posts.append(new_post)
        return self.blogs


