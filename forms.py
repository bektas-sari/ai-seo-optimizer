from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    content = TextAreaField("Enter your blog content", validators=[DataRequired()])
    submit = SubmitField("Analyze SEO")
