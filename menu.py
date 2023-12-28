import re
import line1
import line2
import line3 
import bruteforce
import grahamscan
import jarvismarch
import quickelimination
import quickandgrahamcombine
from flask import Flask, request
app = Flask(__name__)

@app.route('/#algebra', methods=['POST'])
def algebra():
    # Extract values from form data
    line1Point1X = request.json.get('line1').get('point1').get('x')
    line1Point1Y = request.json.get('line1').get('point1').get('y')
    line1Point2X = request.json.get('line1').get('point2').get('x')
    line1Point2Y = request.json.get('line1').get('point2').get('y')
    line2Point1X = request.json.get('line2').get('point1').get('x')
    line2Point1Y = request.json.get('line2').get('point1').get('y')
    line2Point2X = request.json.get('line2').get('point2').get('x')
    line2Point2Y = request.json.get('line2').get('point2').get('y')

    # TODO: Add your algebra code here
    # For example, you can call a function from quickandgrahamcombine
    result = line1.find_intersection_point(line1Point1X, line1Point2X, line1Point1Y, line1Point2Y, line2Point1X, line2Point2X, line2Point1Y, line2Point2Y)
    line1.plot_lines_and_intersection(line1Point1X, line1Point2X, line1Point1Y, line1Point2Y, line2Point1X, line2Point2X, line2Point1Y, line2Point2Y, result)


if __name__ == '__main__':
    app.run(debug=True)