from blog import Blog
from user import User
from forms.build_blog_form import Build_blog_form

from flask import flash

class Blog_manager:
    def __init__(self, blogs):
        self.blogs:Blog = []
        self.current_id = 0
    
    def create_new_blog(self, form:Build_blog_form):
        new_user = User(form.owner_name.data, form.birthday.data)
        new_topics = [form.topic1.data, form.topic2.data, form.topic3.data]
        self.blogs.append(Blog(self.current_id, new_user, form.description.data, form.blog_name.data, form.blog_cover.data, new_topics))
        
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
        



