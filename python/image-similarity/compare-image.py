import numpy
import cv2
import matplotlib.pyplot as plt

def mean_square_error(imageA, imageB):
    err = numpy.sum((imageA.astype("float")  - imageB.astype("float"))**2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    return err

def compare_images(imageA, imageB, title):
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f" % (mean_square_error(imageA, imageB)))
 
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
 
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
 
	plt.show()

def split_image_to_cells(image, n):
    # n * n grid
    w = image.shape[1]
    h = image.shape[0]

    cells = []

    for i in range(n):
        x1 = int(i * w/n)
        x2 = int((i+1) * w/n)
        for j in range(n):
            y1 = int(j * h/n)
            y2 = int((j+1) * h/n)
            cells.append(image[y1:y2, x1:x2])

    return cells

if __name__ == "__main__":
    original = cv2.imread("image1.png")
    contrast = cv2.imread("image2.png")

    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)

    n = 3

    original_cells = split_image_to_cells(original, n)
    contrast_cells = split_image_to_cells(contrast, n)

    fig = plt.figure("Images")
    images = ("Original", original), ("Contrast", contrast)
    
    for (i, (name, image)) in enumerate(images):
        ax = fig.add_subplot(1, 2, i + 1)
        ax.set_title(name)
        plt.imshow(image, cmap = plt.cm.gray)
        plt.axis("off")
    
    for i in range (n*n):
        compare_images(original_cells[i], contrast_cells[i], "cell %d" % i)