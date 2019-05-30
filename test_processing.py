import os
import time
import cv2

from DisplayUtils.Colors import bcolors
from ImageProcessing import FrameProcessor, ProcessingVariables

std_height = 400

# thresh = 73  # 1-50 mod 2 25
# erode = 3  # 3-4 2
# adjust = 15  # 10-40 30
# blur = 9  # 5-15 mod 2 7

erode = 4
threshold = ProcessingVariables.threshold
adjustment = ProcessingVariables.adjustment
iterations = ProcessingVariables.iterations
blur = 7

version = '_2_3'
test_folder = ''

frameProcessor = FrameProcessor(std_height, version, False, write_digits=True)


def test_img(path, show_result=True):
    img = cv2.imread(path)
    frameProcessor.set_image(img)
    frameProcessor.set_file_name(path.replace(".jpg",""))
    output = ""
    break_fully = False
    output = ''
    print(path)
    for blur in [1,3,5,7,9]:
	if break_fully:
		break
    	for erode in [1,2,3,4,5,6,7]:
		if break_fully:
			break
		for iterations in [1,2,3,4]:
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
    print(output)


def get_expected_from_filename(filename):
    expected = filename.split('.')[0]
    expected = expected.replace('A', '.')
    expected = expected.replace('Z', '')
    return expected

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
		

def run_tests(show_result=False):
    count = 0
    correct = 0

    start_time = time.time()
    for i in range(59):
        i = i + 1
        test_img(str(i)+'.jpg', show_result)


def main():
    start_time = time.time()
    acc = run_tests()
    print("--- %s seconds ---" % (time.time() - start_time))

    # bulk_run()


if __name__ == "__main__":
    main()
