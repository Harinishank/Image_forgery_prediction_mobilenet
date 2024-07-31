from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)

def predict_image(imgname):
    test_image = image.load_img(imgname, target_size = (224, 224))

    test_image = np.asarray(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    model = load_model('static/mobilenet_project.h5')
    result = model.predict(test_image)

    final_labels = {0: 'Fake', 1: 'Real'}

    result_dict = dict()
    for key in list(final_labels.keys()):
        result_dict[final_labels[key]] = result[0][key]
    sorted_results = {k: v for k, v in sorted(result_dict.items(), key=lambda item: item[1], reverse=True)}

    final_result = []
    final_result.append(list(sorted_results.keys())[0])
    per = round(sorted_results[list(sorted_results.keys())[0]] * 100, 2)
    final_result.append(str(per)+'%')

    return final_result


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/_', methods=['POST'])
def process_image():
    # Get the image file from the request
    image_file = request.files['image']

    img_path = 'temp_img.jpg'
    image_file.save(img_path)

    prediction = predict_image(img_path)

    os.remove(img_path)

    result = {'result': 'The image is ' + prediction[0] + ' (Confidence Score: ' + prediction[1] + ')'}

    return jsonify(result)