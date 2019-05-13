import os
import time

from DisplayUtils.Colors import bcolors
from ImageProcessing import FrameProcessor, ProcessingVariables

std_height = 500

# thresh = 73  # 1-50 mod 2 25
# erode = 3  # 3-4 2
# adjust = 15  # 10-40 30
# blur = 9  # 5-15 mod 2 7

erode = 4
threshold = ProcessingVariables.threshold
adjustment = ProcessingVariables.adjustment
iterations = ProcessingVariables.iterations
blur = 7

version = '_2_0'
test_folder = '/home/kiril/Downloads/SDB Device Output Images/processed'

frameProcessor = FrameProcessor(std_height, version, False, write_digits=False)


def test_img(path, show_result=True):
    frameProcessor.set_image(path)
    (debug_images, calculated) = frameProcessor.process_image(blur, threshold, adjustment, erode, iterations)
    print(path)
    print(calculated)


def get_expected_from_filename(filename):
    expected = filename.split('.')[0]
    expected = expected.replace('A', '.')
    expected = expected.replace('Z', '')
    return expected


def run_tests(show_result=True):
    count = 0
    correct = 0

    start_time = time.time()
    for file_name in os.listdir(test_folder):
        test_img(test_folder + '/' + file_name, show_result)


def main():
    start_time = time.time()
    acc = run_tests()
    print("--- %s seconds ---" % (time.time() - start_time))

    # bulk_run()


if __name__ == "__main__":
    main()
