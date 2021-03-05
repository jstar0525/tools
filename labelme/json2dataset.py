
# ref https://github.com/wkentaro/labelme/blob/master/labelme/cli/json_to_dataset.py

import json
import os
import os.path as osp

import imgviz
import PIL.Image
import numpy as np

from labelme import utils

JSON_DIR = './labelme/data/labeled/'
SAVE_DIR = './labelme/data/dataset/'

def main(JSON_DIR, SAVE_DIR):

    # read .json file list
    _, _, jsons = next(os.walk(JSON_DIR))
    jsons = [s for s in jsons if ".json" in s]
    
    # take the label_names.txt
    with open(osp.join(JSON_DIR, "label_names.txt"), "r") as f:
        cnt = 0
        label_name_to_value = {}
        for line in f:
            label_name_to_value[line.rstrip('\n')] = cnt
            cnt += 1
    
    for json_file in jsons:
        
        # read json
        data = json.load(open(JSON_DIR + json_file))
        
        # read image
        imageData = data.get("imageData")
        
        if not imageData:
            imagePath = os.path.join(JSON_DIR, data["imagePath"])
            img = np.asarray(PIL.Image.open(imagePath))
        else:
            img = utils.img_b64_to_arr(imageData)
        
        with open(osp.join(JSON_DIR, "label_names.txt"), "r") as f:
            cnt = 0
            label_name_to_value = {}
            for line in f:
                label_name_to_value[line.rstrip('\n')] = cnt
                cnt += 1
        
        # make a label data
        lbl, _ = utils.shapes_to_label(
            img.shape, data["shapes"], label_name_to_value
        )
        
        # make a viz data
        label_names = [None] * (max(label_name_to_value.values()) + 1)
        for name, value in label_name_to_value.items():
            label_names[value] = name
        
        lbl_viz = imgviz.label2rgb(
            label=lbl, img=imgviz.asgray(img), label_names=label_names, loc="rb"
        )
        
        # save dataset
        _, name, _ = json_file.replace('.', '_').split('_')
        
        PIL.Image.fromarray(img).save(osp.join(SAVE_DIR, "img_" + name + ".png"))
        utils.lblsave(osp.join(SAVE_DIR, "label_" + name + ".png"), lbl)
        PIL.Image.fromarray(lbl_viz).save(osp.join(SAVE_DIR, "viz_" + name + ".png"))
        
        with open(osp.join(SAVE_DIR, "label_names.txt"), "w") as f:
            for lbl_name in label_names:
                f.write(lbl_name + "\n")
    
if __name__ == "__main__":
	main(JSON_DIR, SAVE_DIR)
