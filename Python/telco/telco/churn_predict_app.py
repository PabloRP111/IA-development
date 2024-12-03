import pickle

from flask import Flask, jsonify, request

from churn_predict_service import predict_single

app = Flask('churn-predict')

with open('models/churn-model.pck', 'rb') as f:
    dv, model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    churn, prediction = predict_single(customer, dv, model)

    result = {
        'churn': bool(churn),
        'churn_probability': float(prediction),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
