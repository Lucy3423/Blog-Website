from flask import Flask, render_template, redirect, url_for, request, flash 

from blog_manager import Blog_manager
from blog import Blog
from topic import Topic
from user import User
from post import Post

from forms.build_blog_form import Build_blog_form
from forms.add_post_form import Add_post_form

blog_manager = Blog_manager([])

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret" 

@app.route('/')
def home():
    return render_template("home_page.html") 
 


@app.route('/blog_form', methods=["GET", "POST"])
def blog_form():
    form = Build_blog_form()

    if form.validate_on_submit():
        valid = blog_manager.check_image_format(form)
        print(valid)
        if valid == True:  
            # create a new blog
            new_blog_id = blog_manager.create_new_blog(form)
            # identify the user's star sign
            sign = blog_manager.identify_star_sign(form)
            # update the user class with their sign
            blog_manager.blogs[new_blog_id].owner.sign = sign  

            return redirect(url_for("dashboard", blog_id=new_blog_id))
        # pass through the blog_id in route
        else: 
            flash("Incorret image format")
            return render_template("blog_form.html", form=form)
        
    return render_template("blog_form.html", form=form)


@app.route("/dashboard/<int:blog_id>", methods=["GET", "POST"])
def dashboard(blog_id):
    return render_template("blog_dashboard.html", blog_id=blog_id, blog_manager=blog_manager, sign = blog_manager.blogs[blog_id].owner.sign)


@app.route("/topic/<int:blog_id>/<int:topic_id>")
def topic(blog_id, topic_id):
    blog=blog_manager.blogs[blog_id]
    topic = blog.topics[topic_id]
    return render_template("topic.html", blog_id=blog_id, topic_id=topic_id, blog_manager=blog_manager, blog=blog, topic=topic)



# change the structure of topics. each topic is a different instance of the Topic class
# create a different instance of each topic to add to the the blog. 
# ensure the route can still work.

@app.route('/add_blog_entry/<int:blog_id>/<int:topic_id>', methods=["get", "post"])
def add_blog_post(blog_id, topic_id):
    form = Add_post_form() 
    blog = blog_manager.blogs[blog_id]
    if form.validate_on_submit():
        blog_manager.add_blog_post(form, blog, topic_id, blog_id)
        return redirect(url_for('topic', blog_id=blog_id, topic_id=topic_id))
    return render_template("add_blog_post.html", blog_id=blog_id, topic_id=topic_id, form=form)


@app.route('/blog_post/<int:blog_id>/<int:topic_id>/<int:post_id>')
def blog_post(blog_id, topic_id, post_id):
    blog = blog_manager.blogs[blog_id]
    posts = blog.topics[topic_id].posts
    return render_template('blog_post.html', posts=posts, blog_id=blog_id, topic_id=topic_id, post_id=post_id)




if __name__ == "__main__":
    app.run(debug=True)