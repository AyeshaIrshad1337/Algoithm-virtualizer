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
    image_path = os.path.join('static', 'orient_image.png')
    image=Image.open(BytesIO(i.getvalue()))
    image.save(image_path)
    image_url = image_path

    return jsonify({'image_url': image_url})
@app.route('/vector', methods=['POST'])
def vector():
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
    i=line3.Vectorisation(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y)
    image_path = os.path.join('static', 'vector_image.png')
    image=Image.open(BytesIO(i.getvalue()))
    image.save(image_path)
    image_url = image_path

    return jsonify({'image_url': image_url})
@app.route('/research', methods=['POST'])
def research():
    try:
        data = request.get_json()

        # Extract point data based on the structure of your form
        point_data = []
        for key, value in data.items():
            if key.startswith("point"):
                point_data.append(value)
                print(value)
        point_pairs = list(zip(point_data[::2], point_data[1::2]))

        xy = quickandgrahamcombine.proposedConvexHull(point_pairs)
        x=quickandgrahamcombine.plot_points(point_pairs, xy)
        # Save the image
        image_path = os.path.join('static', 'research-image.png')
        image = Image.open(BytesIO(x))
        image.save(image_path)
        image_url = image_path

        return jsonify({'image_url': image_url})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred during processing'}), 500
@app.route('/bruteforce', methods=['POST'])
def brute():
    try:
        data = request.get_json()

        # Extract point data based on the structure of your form
        point_data = []
        for key, value in data.items():
            if key.startswith("point"):
                point_data.append(value)
                print(value)
        point_pairs = list(zip(point_data[::2], point_data[1::2]))

        x=bruteforce.InputandStart(point_pairs)
        # Save the image
        image_path = os.path.join('static', 'brute-image.png')
        image = Image.open(BytesIO(x))
        image.save(image_path)
        image_url = image_path

        return jsonify({'image_url': image_url})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred during processing'}), 500

if __name__ == '__main__':
    app.run(debug=True)