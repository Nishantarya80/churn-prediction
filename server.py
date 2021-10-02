from flask import Flask, request,json
from flask import jsonify
from predictionmodel import loadmodel


app = Flask(__name__)

@app.route('/predict', methods =['POST'])
def pridict():
    dic = request.json
    li= list(dic.values())
    li = list(map(float, li))
    result = 1.0-loadmodel.run_example(li)
    if result >= 0.85:
        risk = "Alert"
    elif result >= 0.66:
        risk = "High"
    elif result >= 0.33:
        risk ="Medium"
    else:
        risk = "Low"
    result = "{:.2f}".format(result*100)
    return jsonify({"churn_possibility": result+"%" ,
                    "Risk":risk})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)