from flask import Flask, jsonify
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)


url = "/gallery/"
links = {
  "landscape": {},
  "portrait": {},
  "square": {},
}

def CollectImages(type_of_image):
  type_of_image = type_of_image
  files = os.listdir("." + url + type_of_image + "/")
  temp_dictionary = links[type_of_image]
  y = 0
  for file in files:
    image_url = { "url": url + type_of_image + "/" + file }
    temp_dictionary[y] = image_url
    y += 1
  links[type_of_image] = temp_dictionary


class ServeLinks(Resource):
  def get(self):
    for i in range(3):
      if i == 0:
        CollectImages("landscape")
      if i == 1:
        CollectImages("portrait")
      if i == 2:
        CollectImages("square")
    jsonify(links)
    return links, 200

api.add_resource(ServeLinks, '/')

if __name__ == '__main__': app.run(debug=True)
