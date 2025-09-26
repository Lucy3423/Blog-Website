from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

class Build_blog_form(FlaskForm): 
    owner_name = StringField('My name is... ', validators=[DataRequired()])
    blog_name = StringField('My blog is called... ', validators=[DataRequired()])
    birthday = StringField('My birthday is (dd/mm/yr)... ', validators=[DataRequired()])
    blog_cover = StringField("My blog background image is (.jpg or .img)...")
    fav_singer = StringField('My favourite singer/band is... ', validators=[DataRequired()])
    image_fav_singer = StringField("Here's a picture of them (.jpg or .img)... ", validators=[DataRequired()])
    fun_fact = StringField("A fun fact about me is...", validators=[DataRequired()])
    # enter topics that they want to feature in their blog
    topic1 = StringField("Topic 1 is about... ", validators=[DataRequired()])
    topic2 = StringField("Topic 2 is about... ", validators=[DataRequired()])
    topic3 = StringField("Topic 3 is about... ", validators=[DataRequired()])

    submit = SubmitField("SUBMIT")