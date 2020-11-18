from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(page_name + '.html')
    except:
        return 'Page Not Found'


def write_to_file(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database,
                                delimiter=",",
                                quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('thankyou')
        except:
            return 'Form didn\'t submitted'
    else:
        return 'Something Went Wrong'