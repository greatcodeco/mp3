from wtforms import Form, StringField, validators

class inputForm(Form):
    youtube_url = StringField('Youtube Url', [validators.DataRequired(), validators.Length(min=5, max=1000)])