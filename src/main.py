import csv
import os

from XgBoostModel import run_model, predict_model
from datetime import datetime
from flask import Flask, request, jsonify

# Press the green button in the gutter to run the script.
from XgClassifier import XGBoostClassifier

# creating a Flask app
app = Flask(__name__)


@app.route('/api-get-prediction', methods=['POST'])
def home():
    end_response = list()
    data = request.json
    with open(os.getcwd() + "/data/predictions.csv", 'r') as f:
        csvFile = csv.reader(f)
        # displaying the contents of the CSV file
        next(csvFile, None)
        for line in csvFile:
            if int(line[0]) in data['id']:
                end_response.append(line)
        return jsonify(end_response)


@app.route('/api-train-model', methods=['GET'])
def train_model():
    try:
        print("Running Model stated at=", datetime.now())
        train_X, train_y, test_X, cust_dict = run_model()

        xgB = XGBoostClassifier()
        xgB.main(train_X, train_y, test_X)
        out_df = predict_model(train_X, train_y, test_X, cust_dict)
        out_df.to_csv(os.getcwd() + "/data/predictions.csv", index=False)
        print("Model Completed = ", datetime.now())
        return "out_df.to_json"
    except Exception as e:
        return jsonify(e)


if __name__ == '__main__':
    # print("Running Model stated at=", datetime.now())
    # train_X, train_y, test_X, cust_dict = run_model()

    # xgB = XGBoostClassifier()
    # xgB.main(train_X, train_y, test_X)
    # out_df = predict_model(train_X, train_y, test_X, cust_dict)
    # out_df.to_csv(os.getcwd() + "/data/predictions.csv", index=False)
    # print("Model Completed = ", datetime.now())
    app.run(host='0.0.0.0')
