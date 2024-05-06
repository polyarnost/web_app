from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class GradeForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    score = FloatField('Score', validators=[DataRequired()])
    submit = SubmitField('Submit')
