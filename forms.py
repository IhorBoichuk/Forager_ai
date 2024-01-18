"""
forms.py.

This module contains FlaskForm classes for capturing user input.

It includes the EmailForm class for capturing email input and the DomainForm
class for capturing domain input.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from config import MAX_DOMAIN_LENGTH


class EmailForm(FlaskForm):
    """EmailForm class represents a FlaskForm for capturing email input."""

    email: StringField = StringField(
        'Email',
        validators=[DataRequired(), Length(max=MAX_DOMAIN_LENGTH)],
    )
    submit: SubmitField = SubmitField('Submit')


class DomainForm(FlaskForm):
    """DomainForm class represents a FlaskForm for capturing domain input."""

    email: StringField = StringField(
        'Domain',
        validators=[DataRequired(), Length(max=MAX_DOMAIN_LENGTH)],
    )
    submit: SubmitField = SubmitField('Submit')
