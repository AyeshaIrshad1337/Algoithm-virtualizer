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
import os
from io import BytesIO
from flask import jsonify
from PIL import Image
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/algebra', methods=['POST'])
def algebra():
    data = request.get_json()
    print(data, 'json data')
    print()
    line1Point1X = int(data["line1Point1X"])
    line1Point1Y = int(data["line1Point1Y"])
    line1Point2X = int(data["line1Point2X"])
    line1Point2Y = int(data["line1Point2Y"])
    line2Point1X = int(data["line2Point1X"])
    line2Point1Y = int(data["line2Point1Y"])
    line2Point2X = int(data["line2Point2X"])
    line2Point2Y = int(data["line2Point2Y"])
    intersect_point = line1.find_intersection_point(line1Point1X, line1Point2X, line1Point1Y, line1Point2Y, line2Point1X, line2Point2X, line2Point1Y, line2Point2Y)
    i = line1.plot_lines_and_intersection(line1Point1X, line1Point2X, line1Point1Y, line1Point2Y, line2Point1X, line2Point2X, line2Point1Y, line2Point2Y, intersect_point)
    image_path = os.path.join('static', 'image.png')
    # i.save(image_path)
    image=Image.open(BytesIO(i.getvalue()))
    image.save(image_path)
    # Return the URL of the saved image
    image_url = image_path

    return jsonify({'image_url': image_url})
@app.route('/orient', methods=['POST'])
def orient():
    data = request.get_json()
    print(data, 'json data')
    print()
    line1Point1X = int(data["line1Point1X"])
    line1Point1Y = int(data["line1Point1Y"])
    line1Point2X = int(data["line1Point2X"])
    line1Point2Y = int(data["line1Point2Y"])
    line2Point1X = int(data["line2Point1X"])
    line2Point1Y = int(data["line2Point1Y"])
    line2Point2X = int(data["line2Point2X"])
    line2Point2Y = int(data["line2Point2Y"])
    i=line2.IntersectbyOrient(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y)
    image_path = os.path.join('static', 'image.png')
    image=Image.open(BytesIO(i.getvalue()))
    image.save(image_path)
    image_url = image_path

    return jsonify({'image_url': image_url})
if __name__ == '__main__':
    app.run(debug=True)