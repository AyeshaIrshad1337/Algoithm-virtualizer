import re
import line1
import line2
import line3 
import bruteforce
import grahamscan
import jarvismarch
import quickelimination
import quickandgrahamcombine
from flask import Flask, send_file, request, render_template, redirect, url_for, session, flash
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/algebra', methods=['POST'])
def algebra():
    if request.method == 'POST':
        line1Point1X=request.form["line1Point1X"]
        line1Point1Y=request.form["line1Point1Y"]
        line1Point2X=request.form["line1Point2X"]
        line1Point2Y=request.form["line1Point2Y"]
        line2Point1X=request.form["line2Point1X"]
        line2Point1Y=request.form["line2Point1Y"]
        line2Point2X=request.form["line2Point2X"]
        line2Point2Y=request.form["line2Point2Y"]
        intersect_point=line1.find_intersection_point(line1Point1X, line1Point2X, line1Point1Y, line1Point2Y, line2Point1X, line2Point2X, line2Point1Y, line2Point2Y)
        i= line1.plot_lines_and_intersection(line1Point1X, line1Point2X, line1Point1Y, line1Point2Y, line2Point1X, line2Point2X, line2Point1Y, line2Point2Y, intersect_point)
        return send_file(i, mimetype='image/png')
if __name__ == '__main__':
    app.run(debug=True)