from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "change-me-in-production")
CSV_FILE = Path(__file__).parent / "cafe-data.csv"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()],
                       render_kw={"class": "form-control bg-white text-dark"})
    cafe_location=URLField("Cafe Location On Google Map(URL)",
        validators=[DataRequired(), URL(message="Please enter a valid URL starting with http:// or https://")],
                           render_kw={"class": "form-control bg-white text-dark"})

    opening_time=StringField("Opening Time e.g,8AM", validators=[DataRequired()],
                             render_kw={"class": "form-control bg-white text-dark"})

    closing_time=StringField("Closing Time e.g,5PM", validators=[DataRequired()],
                             render_kw={"class": "form-control bg-white text-dark"})

    coffee_rating=SelectField(
        label="coffee rating",
        choices=[
            ('☕️', '☕️'),
            ('☕️☕️', '☕️☕️'),
            ('☕️☕️☕️', '☕️☕️☕️'),
            ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
            ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')
        ],
        validators=[DataRequired()],
        render_kw={"class": "form-control bg-white text-dark"}

    )
    rating_wifi=SelectField(
        "Wifi Strength Rating",
        choices=[('✘', '✘'),
                ('💪', '💪'),
                ('💪💪', '💪💪'),
                ('💪💪💪', '💪💪💪')
        ],
        validators=[DataRequired()],
        render_kw={"class": "form-control bg-white text-dark"}
    )

    power=SelectField(
        "Power",
        choices=[
            ('🔌', '🔌'),
            ('🔌🔌', '🔌🔌'),
            ('🔌🔌🔌', '🔌🔌🔌')
        ],
        validators=[DataRequired()],
        render_kw={"class": "form-control bg-white text-dark"}
    )
    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = [
            form.cafe.data.strip(),
            form.cafe_location.data.strip(),
            form.opening_time.data.strip(),
            form.closing_time.data.strip(),
            form.coffee_rating.data,
            form.rating_wifi.data,
            form.power.data
        ]

        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_row)

        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open(CSV_FILE, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)
