from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

"""
Form for creating a new task. This form has 2 fields: title and description.
Both of which require data otherwise the form will not pass validation.
"""
class EditForm(FlaskForm):
    title = StringField('title',
        validators=[DataRequired()],
        render_kw={'placeholder' : 'enter title...'}
    )

    description = TextAreaField('description',
        validators=[DataRequired()],
        render_kw={'placeholder' : 'enter description...'}
    )

    submit = SubmitField('Submit')
