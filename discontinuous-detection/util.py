from PIL import Image
import cv2
from matplotlib import pyplot as plt
import numpy as np

def plot_images(images, image_names, columns=None, rows=None):
    rows = rows  or (int(np.sqrt(len(images) + 1)) )
    columns = columns or rows
    plt.figure(figsize=(columns * 4, rows * 4))
    
    for i, filtered_image in enumerate(images):
        # make check if i = 10 because columns will break
        plt.subplot(rows, columns, i + 1)
        plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
        plt.title(image_names[i])
        plt.axis("off")

    plt.tight_layout()
    plt.show()
    
def normalize(source):
    return cv2.normalize(source, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)