import cv2
import time
import sys

from ImageProcessing import FrameProcessor, ProcessingVariables
from DisplayUtils.TileDisplay import show_img, reset_tiles

window_name = 'Playground'
file_name = '/home/kiril/Downloads/SDB Device Output Images/processed/image62.jpg'
version = '_2_2'

erode = 4
threshold = ProcessingVariables.threshold
adjustment = ProcessingVariables.adjustment
iterations = ProcessingVariables.iterations
blur = 7

std_height = 400

frameProcessor = FrameProcessor(std_height, version, True)


def main():
    img_file = file_name
    if len(sys.argv) == 2:
        img_file = sys.argv[1]
    setup_ui()
    frameProcessor.set_image(img_file)
    process_image()
    cv2.waitKey()


def process_image():
    reset_tiles()
    start_time = time.time()
    break_fully = False
    output = ''
    debug_images = []
    for blur in [3,5,7,9]:
	if break_fully:
		break
    	for erode in [2,3,4,5,6,7]:
		if break_fully:
			break
		for iterations in [2,3,4]:
			try:	
				debug_images, output = frameProcessor.process_image(blur, threshold, adjustment, erode, iterations)
				if '.' in output and len(output) == 4:
					output = remove_duplicate_chars(output)
				elif '.' not in output and len(output) == 3:
					output = remove_duplicate_chars(output)
				if output != '' and ((len(output) == 2 and '.' not in output) or (len(output) == 3 and '.' in output) ) and (check_instance(output, float) or check_instance(output, int)):
					break_fully = True			
					break
			except:
				output = output
    if '.' not in output and len(output) == 2 and check_instance(output, int):
	output = int(output) * 1.0 / 10
    elif len(output) == 3 and output[0] == '.' and check_instance(output, float):
	output = float(output) * 100 * 1.0 / 10
    for image in debug_images:
       show_img(image[0], image[1])
    print(output)
    print("Processed image in %s seconds" % (time.time() - start_time))

    cv2.imshow(window_name, frameProcessor.img)
    cv2.moveWindow(window_name, 600, 600)


def remove_duplicate_chars(output):
	s = []	
	for i in range(0, len(output)):
		char = output[i]
		if char not in s and char not in output[i+1:i+2]:
			s.append(char)
	return "".join(s)


def check_instance(val, val_type):
	try:	
		val_type(val)
		return True
	except:
		return False
		

def setup_ui():
    cv2.namedWindow(window_name)
    cv2.createTrackbar('Threshold', window_name, int(threshold), 500, change_threshold)
    cv2.createTrackbar('Iterations', window_name, int(iterations), 5, change_iterations)
    cv2.createTrackbar('Adjust', window_name, int(adjustment), 200, change_adj)
    cv2.createTrackbar('Erode', window_name, int(erode), 5, change_erode)
    cv2.createTrackbar('Blur', window_name, int(blur), 25, change_blur)


def change_blur(x):
    global blur
    print('Adjust: ' + str(x))
    if x % 2 == 0:
        x += 1
    blur = x
    process_image()


def change_adj(x):
    global adjustment
    print('Adjust: ' + str(x))
    adjustment = x
    process_image()


def change_erode(x):
    global erode
    print('Erode: ' + str(x))
    erode = x
    process_image()


def change_iterations(x):
    print('Iterations: ' + str(x))
    global iterations
    iterations = x
    process_image()


def change_threshold(x):
    print('Threshold: ' + str(x))
    global threshold

    if x % 2 == 0:
        x += 1
    threshold = x
    process_image()


if __name__ == "__main__":
    main()
