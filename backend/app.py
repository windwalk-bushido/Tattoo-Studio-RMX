# LIBRARIES
from flask import Flask, json, jsonify, send_from_directory
from flask_cors import CORS
import gunicorn, os


# CONFIG
app = Flask(__name__, static_url_path='')
CORS(app)


# GLOBAL
url = "/gallery/"
links = {
  "landscape": {},
  "portrait": {},
  "square": {},
}

def CollectImages(type_of_image):
  type_of_image = type_of_image
  files = os.listdir("./static/" + url + type_of_image + "/")
  temp_dictionary = links[type_of_image]
  y = 0
  for file in files:
    image_url = { "url": url + type_of_image + "/" + file }
    temp_dictionary[y] = image_url
    y += 1
  links[type_of_image] = temp_dictionary


# Serve JSON file with URL's to images
@app.route("/")
def index():
  for i in range(3):
    if i == 0:
      CollectImages("landscape")
    if i == 1:
      CollectImages("square")
    if i == 2:
      CollectImages("portrait")
  jsonify(links)
  return links, 200

# Serve images directly via requested link
@app.route("/<path:path>")
def send_image():
  return send_from_directory('gallery', path)


# 404
@app.errorhandler(404)
def page_not_found(error):
  return jsonify(error = 404), 404


# INIT
if __name__ == "__main__": app.run()
