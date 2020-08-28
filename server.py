from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_form(data)
        save_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


def save_form(data):
    with open('db.txt', 'a') as db:
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        db.write(f'\n{email},{subject},{message}')
    print('done writing!')


def save_csv(data):
    with open('db.csv', 'a',  newline='') as db:
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        csv_writer = csv.writer(
            db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
    print('done writing!')
