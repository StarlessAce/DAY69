from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Your email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    name = StringField("Type your name", validators=[DataRequired()])
    submit = SubmitField("Create")


class LoginForm(FlaskForm):
    email = StringField("Your email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Let me in")


class CommentForm(FlaskForm):
    comment_text = CKEditorField('Type your comment here', validators=[DataRequired()])
    submit_button = SubmitField('Submit comment')