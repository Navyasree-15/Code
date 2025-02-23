from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
    'locations' : util.get_location_names()

    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    #so here when we press button in html our data like price, bhk are taken by request object (which is imported) then they are taken as form
    #elements  then they are converted to normal variables to be sent to our python predict function
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print("starting python flask server for home price prediction")
    util.load_saved_artifacts()
    app.run()