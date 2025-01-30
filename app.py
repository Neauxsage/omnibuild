from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    print("Rendering index page.")
    return render_template('test.html')



    

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.json

    # Extract data
    packages = data['packages']
    timeline_options = data['timeline']
    website_links = data['websiteLinks']
    additional_info = data['additionalInfo']
    total_cost = data['totalCost']

    # Format package information
    package_details = "\n".join([f"{pkg['name']}: ${pkg['price']}" for pkg in packages])

    # Email content
    email_body = f"""
    Packages Selected:
    {package_details}

    Timeline Options:
    {timeline_options}

    Website Links:
    {', '.join(website_links)}

    Additional Information:
    {additional_info}

    Total Cost:
    ${total_cost}
    """

    # Email setup (Replace with your details)
    sender_email = "test1@gmail.com"
    receiver_email = "test@gmail.com"
    password = "asdfasdfasdfasdf"

    # Create and send email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Handyman Website Features Information"
    message.attach(MIMEText(email_body, "plain"))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

    return jsonify({"success": True})



if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)


