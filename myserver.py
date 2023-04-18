from flask import Flask, render_template ,url_for ,request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def flow():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file (data) :
    with open ('database.txt', mode = 'a') as database :
        First_Name = data["First Name"]
        Last_Name = data["Last Name"]
        email = data["email"]
        Phone_Number = data["Phone Number"]
        file =database.write(f'\n{First_Name},{Last_Name}, {email},{Phone_Number}')

def write_to_csv(data) :
    with open ('database.csv',newline= '', mode = 'a',) as database2:
        First_Name = data["First Name"]
        Last_Name = data["Last Name"]
        email = data["email"]
        Phone_Number = data["Phone Number"]
        csv_writer =csv.writer(database2, delimiter=',', quotechar = '"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([First_Name,Last_Name, email,Phone_Number])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try :
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect ('thankyou.html')
        except :
            return "Did not save to database"
    else :
        return 'Something Went Wrong'
