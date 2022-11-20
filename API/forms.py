from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class PredictFromOneVal(FlaskForm):
    time_response=FloatField('time_response',
                        validators=[DataRequired()])
    ttl_hostname=IntegerField('ttl_hostname',
                     validators=[DataRequired()])
    asn_ip = IntegerField('asn_ip', validators=[DataRequired()])
    length_url = IntegerField('length_url',
                                    validators=[DataRequired()])
    domain_length = IntegerField('domain_length',
                                    validators=[DataRequired()])
    time_domain_activation = IntegerField('time_domain_activation',
                                    validators=[DataRequired()])
    time_domain_expiration = IntegerField('time_domain_expiration',
                                    validators=[DataRequired()])
    qty_vowels_domain = IntegerField('qty_vowels_domain',
                                    validators=[DataRequired()])
    directory_length = IntegerField('directory_length',
                                    validators=[DataRequired()])
    submit=SubmitField('Predict')
