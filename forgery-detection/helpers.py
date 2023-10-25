import json
import cv2
import matplotlib.pyplot as plt
from datetime import datetime


def read_json(path, display=False):
    import pprint as pprint

    with open(path, "r") as f:
        data = json.load(f)

    if display:
        pprint(data)
    return data


def draw_bounding_boxes(image, data, display=False, write=False, retrieve_boxes=False):
    bounding_boxes = []
    for item in data[0]["words"]:
        x1, y1 = item["boundingBox"][0:2]
        x2, y2 = item["boundingBox"][-4:-2]
        image = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
        bounding_boxes.append([x1, y1, x2, y2])

    if write:
        output_str = datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + "_output.jpg"
        cv2.imwrite(output_str, image)

    if display:
        plt.imshow(image)
        plt.show()

    if retrieve_boxes:
        return bounding_boxes
