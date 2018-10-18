from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class EditForm(FlaskForm):
    title = StringField('title',
        validators=[DataRequired()],
        render_kw={'placeholder' : 'enter title...'}
    )

    description = TextAreaField('description',
        validators=[DataRequired()],
        render_kw={'placeholder' : 'enter description...'}
    )
