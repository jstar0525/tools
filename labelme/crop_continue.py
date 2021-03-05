"""
# ref
https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
https://opencv-python.readthedocs.io/en/latest/doc/04.drawWithMouse/drawWithMouse.html
"""
import os
import numpy as np
from PIL import Image
import cv2

# Desired image size
w, h = 640, 480

# continue crop to y interval
y_interval = 100

# Dataset path
Dataset_DIR = "./data/dataset/"
# IMAGE_DIR = "./data/dataset/imgs/"
# LABEL_DIR = "./data/dataset/lbls/"
# VIZ_DIR = "./data/dataset/vizs/"
SAVE_DIR = './data/continue_croped'

# show resized image
show_resized = 1/3

cv2.namedWindow("image")

def lblsave(filename, lbl):
    import imgviz

    if os.path.splitext(filename)[1] != ".png":
        filename += ".png"
    # Assume label ranses [-1, 254] for int32,
    # and [0, 255] for uint8 as VOC.
    if lbl.min() >= -1 and lbl.max() < 255:
        lbl_pil = Image.fromarray(lbl.astype(np.uint8), mode="P")
        colormap = imgviz.label_colormap()
        lbl_pil.putpalette(colormap.flatten())
        lbl_pil.save(filename)
    else:
        raise ValueError(
            "[%s] Cannot save the pixel-wise class label as PNG. "
            "Please consider using the .npy format." % filename
        )

def crop_image(SAVE_DIR, viz, img, lbl, identy, xc, yc, j, show_resized, y_interval, w, h, save_img=True, view_img=False):
    
    # find x0 coordinate from resized image
    x0 = int( xc/show_resized-w/2 )
    x1 = x0 + w
    y0 = 0
    
    while(y0+h <= img.shape[0]):

        y1 = y0 + h
        
        # crop data from original dataset
        crop_viz = viz[y0:y1, x0:x1,:]
        crop_img = img[y0:y1, x0:x1,:]
        crop_lbl = lbl[y0:y1, x0:x1]
    
        if save_img:
            Image.fromarray(crop_img).save(SAVE_DIR + '/img_' + identy + '_%02d.png' % (j))
            lblsave(SAVE_DIR + '/lbl_' + identy + '_%02d.png' % (j), crop_lbl)
            Image.fromarray(crop_viz).save(SAVE_DIR + '/viz_' + identy + '_%02d.png' % (j))
            j += 1
            y0 += y_interval
        if view_img:
            cv2.imshow('cropping image %d' %j, cv2.cvtColor(crop_viz, cv2.COLOR_RGB2BGR))
            
    print('data saved')
    
    return j

def click_and_crop(event, x, y, flags, param):

    global xc,yc

    rw, rh = w*show_resized, h*show_resized

    if event == cv2.EVENT_LBUTTONDOWN:
        # center point of rectangle
        xc, yc = x, y
        # covert xc if xc is out of range in image
        if xc - rw/2 < 0:
            xc = rw/2
        elif xc + rw/2 > image.shape[1]:
            xc = image.shape[1] - rw/2

    elif event == cv2.EVENT_LBUTTONUP:
        # draw the cropping region and direction
        # cv2.rectangle(image, ( int(xc-rw/2), int(yc-rh/2) ), (  int(xc+rw/2), int(yc+rh/2) ), (0, 0, 255), 3)
        cv2.rectangle(image, ( int(xc-rw/2), 0 ), (  int(xc+rw/2), image.shape[0] ), (255, 0, 0), 3)
        
cv2.setMouseCallback("image", click_and_crop)


def main(Dataset_DIR, SAVE_DIR, show_resized, y_interval, w, h):

    global image, xc, yc
            
    # initialize parameter
    xc, yc = -1, -1
    
    _, _, names = next(os.walk(Dataset_DIR))
    names = [s for s in names if "img" in s]
    
    # for counting images location
    i = 0
    # for counting num of saved_image
    j = 1

    while(True):
        
        if i >= len(names):
            print("there is no more data")
        else:
            _, name = names[i].split('_')
            img = np.asarray(Image.open(Dataset_DIR + 'img_'+ name))
            lbl = np.asarray(Image.open(Dataset_DIR + 'label_'+ name))
            viz = np.asarray(Image.open(Dataset_DIR + 'viz_'+ name))
            print(Dataset_DIR + 'viz_'+ name)
    
        clone = cv2.resize( viz, ( int(viz.shape[1]*show_resized), int(viz.shape[0]*show_resized) ) )
    
        image = clone.copy()
    
        while(True):
    
            cv2.imshow("image", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
            key = cv2.waitKey(1) & 0xFF
    
            # if the 'e' key is pressed, reset the image
            if key == ord('e'):
                image = clone.copy()
            # if the 's' key is pressed, save the cropping image
            elif key == ord('s'):
                identy, _ = name.split('.')
                j = crop_image(SAVE_DIR, viz, img, lbl, identy, xc, yc, j, show_resized, y_interval, w, h, save_img=True, view_img=False)
            # if the 'd' key is pressed, goto the next image
            elif key == ord('d'):
                i += 1
                j = 1
                break
            # if the 'a' key is pressed, goto the previous image
            elif key == ord('a') and i > 0:
                i -= 1
                j = 1
                break
            # if the 'esc' key is pressed, break from the loop
            elif key == 27:
                break
        if key == 27:
            break
    
    # close all opened windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(Dataset_DIR, SAVE_DIR, show_resized, y_interval, w, h)

