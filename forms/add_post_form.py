from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired 

class Add_post_form(FlaskForm):
    title = StringField("Title: ", validators=[DataRequired()])
    date = DateField("Date Published: ", validators=[DataRequired()])
    bio = TextAreaField("Give a summary for the post: ", validators=[DataRequired()])
    content = TextAreaField("Add the content for your blog here: ", validators=[DataRequired()])
    submit = SubmitField("Add Post")