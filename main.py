from flask import Flask, render_template, redirect, url_for, request, flash 

from blog_manager import Blog_manager
from blog import Blog
from topic import Topic
from user import User

from forms.build_blog_form import Build_blog_form

blog_manager = Blog_manager([])

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret" 

@app.route('/')
def home():
    return render_template("home_page.html") 
 

@app.route('/test')
def test():
    return render_template("test.html")



@app.route('/blog_form', methods=["GET", "POST"])
def blog_form():
    form = Build_blog_form()
    new_blog_id = blog_manager.creat_new_blog(form)

    if form.validate_on_submit():
        valid = blog_manager.check_image_format(form)
        print(valid)
        if valid == True:    
            return redirect(url_for("dashboard", blog_id=new_blog_id))
        # pass through the blog_id in route
        else: 
            flash("Incorret image format")
            return render_template("blog_form.html", form=form)
    return render_template("blog_form.html", form=form)



@app.route("/dashboard/<int:blog_id>", methods=["GET", "POST"])
def dashboard(blog_id):
    return render_template("blog_dashboard.html", blog_id=blog_id, blog_manager=blog_manager)

if __name__ == "__main__":
    app.run(debug=True)