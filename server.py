from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/index.html")
def my_webpage():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/submit_form", methods =['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        write_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "Form not submitted"

def write_to_csv(mydata):
    with open('database.csv', mode='a') as dbhandle:
        csv_writer = csv.writer(dbhandle, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        email = mydata['email']
        subject = mydata['subject']
        message = mydata['message']
        csv_writer.writerow([email, subject, message])


#     return render_template("works.html")
#
#
# @app.route("/about.html")
# def about():
#     return render_template("about.html")
#
# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")
#
#
# @app.route("/components.html")
# def components():
#     return render_template("components.html")
#

# @app.route("/blog/2020/dogs")
# def blog2():
#     return "This is my Dog"
