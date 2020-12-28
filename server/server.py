from flask import Flask, request, jsonify, render_template
import server.util as util  #replace this by import util for running locally

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")


@app.route('/predict_loan_acceptance', methods=['POST'])
def predict_loan_acceptance():

    applicantincome = float(request.form['ApplicantIncome'])
    coapplicantincome = float(request.form['CoapplicantIncome'])
    loanamount = int(request.form['LoanAmount'])
    loan_amount_term = int(request.form['Loan_Amount_Term'])
    married_yes = int(request.form['married_yes'])
    property_area = int(request.form['location'])


    response = jsonify({
        'estimated_price': util.get_estimated_price(applicantincome, coapplicantincome, loanamount, loan_amount_term, married_yes, property_area)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()
