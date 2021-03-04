import base64
import json
import os
import os.path as osp

import imgviz
import PIL.Image

import utils

DATASET_PATH = './data/'
JSON_FOLDER = 'json/'
SAVE_DIR = DATASET_PATH + 'dataset/'        
_, _, jsons = next(os.walk(os.path.join(DATASET_PATH, JSON_FOLDER)))

for json_file in jsons:

    data = json.load(open(DATASET_PATH + JSON_FOLDER + json_file))
    imageData = data.get("imageData")
    
    if not imageData:
        imagePath = os.path.join(os.path.dirname(json_file), data["imagePath"])
        with open(imagePath, "rb") as f:
            imageData = f.read()
            imageData = base64.b64encode(imageData).decode("utf-8")
    img = utils.img_b64_to_arr(imageData)
    
    label_name_to_value = {"_background_": 0, "joint": 1, "stem": 2, "growth_point": 3}
    # label_name_to_value = {"_background_": 0}
    # for shape in sorted(data["shapes"], key=lambda x: x["label"]):
    #     label_name = shape["label"]
    #     if label_name in label_name_to_value:
    #         label_value = label_name_to_value[label_name]
    #     else:
    #         label_value = len(label_name_to_value)
    #         label_name_to_value[label_name] = label_value
    lbl, _ = utils.shapes_to_label(
        img.shape, data["shapes"], label_name_to_value
    )
    
    label_names = [None] * (max(label_name_to_value.values()) + 1)
    for name, value in label_name_to_value.items():
        label_names[value] = name
    
    lbl_viz = imgviz.label2rgb(
        label=lbl, img=imgviz.asgray(img), label_names=label_names, loc="rb"
    )
    
    _, name, _ = json_file.replace('.', '_').split('_')
    
    PIL.Image.fromarray(img).save(osp.join(SAVE_DIR, "img_" + name + ".png"))
    utils.lblsave(osp.join(SAVE_DIR, "label_" + name + ".png"), lbl)
    PIL.Image.fromarray(lbl_viz).save(osp.join(SAVE_DIR, "viz_" + name + ".png"))
    
    with open(osp.join(SAVE_DIR, "label_names.txt"), "w") as f:
        for lbl_name in label_names:
            f.write(lbl_name + "\n")
    

