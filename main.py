from flask import Flask, render_template, redirect, url_for, request 

app = Flask(__name__)
app.config["SECRET KEY"] = "mysecret" 

@app.route('/')
def home():
    image = "https://i.pinimg.com/1200x/33/cb/16/33cb16051f94c0205c96d088a93991e9.jpg"
    return render_template("home_page.html", image=image) 
 

@app.route('/blog-form')
def blog_form():
    return render_template("blog_form.html")



if __name__ == "__main__":
    app.run(debug=True)