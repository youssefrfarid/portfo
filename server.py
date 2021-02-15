from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_html>')
def go_to_page(page_html='index.html'):
    return render_template(page_html)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'{email},{subject},{message}\n')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']

        fieldnames = ['email', 'subject', 'message']
        csv_writer = csv.DictWriter(database2, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)

        csv_writer.writerow(
            {'email': email, 'subject': subject, 'message': message})


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database!!'
    else:
        return 'Something went wrong try again'
