from flask import Flask, render_template, redirect, url_for, request, flash 

from user import User
from blog import Blog
from blog_manager import Blog_manager

from forms.build_blog_form import Build_blog_form

blog_manager = Blog_manager([])


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret" 

@app.route('/')
def home():
    return render_template("home_page.html") 
 

@app.route('/blog_form', methods=["GET", "POST"])
def blog_form():
    form = Build_blog_form()
    new_user = User(form.owner_name.data, form.birthday.data, form.fav_singer.data, form.image_fav_singer.data, form.fun_fact.data)
    new_topics = [form.topic1.data, form.topic2.data, form.topic3.data]
    blog_manager.blogs.append(Blog(new_user, form.blog_name.data, form.blog_cover.data, new_topics))

    if request.method == "post":
        redirect(url_for("blog_dashboard.html"))
    return render_template("blog_form.html", form=form)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("blog_dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)