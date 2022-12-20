from model import Model
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from db_utils import run_query, get_range_for_charge

app = Flask(__name__)
model = Model()
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/query', methods=["GET"])
@cross_origin()
def query():
    query = request.args.get('query')
    results = run_query(query)
    return jsonify(result=results)

@app.route('/survey', methods=["GET"])
@cross_origin()
def survey():
    age = int(request.args.get('age'))
    sex = request.args.get('sex')
    bmi = float(request.args.get('bmi'))
    children = int(request.args.get('children'))
    smoke = request.args.get('smoke')
    region = request.args.get('region')
    sex = 1 if sex == 'female' else 0
    smoke = 1 if smoke == 'yes' else 0
    region_northeast = 0
    region_northwest = 0
    region_southeast = 0
    region_southwest = 0
    if region == 'northeast':
        region_northeast = 1
    elif region == 'northwest':
        region_northwest = 1
    elif region == 'region_southeast':
        region_southeast = 1
    elif region == 'region_southwest':
        region_southwest = 1
    result = model.lg.predict([[age, sex, bmi, children, smoke, region_northeast, region_northwest, region_southeast, region_southwest]])
    range = get_range_for_charge()
    value = result[0] * range
    print(value)
    return jsonify(result=value)

@app.route('/')
def hello():
    return "Hello world"

if __name__ == "__main__":
	app.run(debug=True)