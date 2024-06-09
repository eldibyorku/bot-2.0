from PIL import ImageGrab
import numpy as np
from scipy import misc
from scipy.ndimage import zoom
from skimage import io, color, metrics
from PIL import ImageChops
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from PIL import ImageFilter
import imagehash


def capture(top_left, bottom_right):

    # windowFocus.focus()

    # Define the coordinates of the area to capture (left, top, right, bottom)
    area_to_capture = (int(top_left[0]), int(top_left[1]),
                       int(bottom_right[0]), int(bottom_right[1]))

    # Take a screenshot of the area
    screenshot = ImageGrab.grab(bbox=area_to_capture)
    return screenshot
    # windowFocus.minimize()


def save(top_left, bottom_right, name):

    # windowFocus.focus()

    # Define the coordinates of the area to capture (left, top, right, bottom)
    area_to_capture = (int(top_left[0]), int(top_left[1]),
                       int(bottom_right[0]), int(bottom_right[1]))

    # Take a screenshot of the area
    screenshot = ImageGrab.grab(bbox=area_to_capture)

    # Save the screenshot as a file
    screenshot.save(f"{name}.png")

    # windowFocus.minimize()


def compare(capture, saved):
    # Convert both images to grayscale
    saved_image_gray = saved.convert('L')
    screenshot_gray = capture.convert('L')

    # Convert images to numpy arrays for easier comparison
    saved_image_array = np.array(saved_image_gray)
    screenshot_array = np.array(screenshot_gray)

    # Resize the smaller image to match the larger one
    # if saved_image_array.shape != screenshot_array.shape:
    #     screenshot_array = zoom(
    #         screenshot_array, saved_image_array.shape[0] / screenshot_array.shape[0])

    # Calculate Mean Squared Error (MSE)
    mse = np.mean((saved_image_array - screenshot_array)**2)

    # Define a threshold for similarity
    threshold = 40  # Adjust this value based on your needs

    if mse < threshold:
        return True
    else:
        # print(f'mse:{mse}, thres:{threshold}')
        return False


def compare2(capture, saved):

   # Convert both images to grayscale
    saved_image_gray = saved.convert('L')
    screenshot_gray = capture.convert('L')

    # Convert images to numpy arrays for easier comparison
    saved_image_array = np.array(saved_image_gray)
    screenshot_array = np.array(screenshot_gray)

    # Calculate the Structural Similarity Index (SSIM)
    ssim_score = metrics.structural_similarity(
        saved_image_array, screenshot_array)

    # Define a threshold for similarity
    threshold = 0.9  # Adjust this value based on your needs

    if ssim_score >= threshold:
        # print(f'score:{ssim_score}, thres:{threshold}')
        return True

    else:
        # print(f'score:{ssim_score}, thres:{threshold}')
        return False


def compare3(capture, saved):

   # Convert both images to grayscale
    saved_image_gray = saved.convert('L')
    screenshot_gray = capture.convert('L')

    # Convert images to numpy arrays for easier comparison
    saved_image_array = np.array(saved_image_gray)
    screenshot_array = np.array(screenshot_gray)

    # Calculate the Structural Similarity Index (SSIM)
    ssim_score = metrics.structural_similarity(
        saved_image_array, screenshot_array)

    # Define a threshold for similarity
    threshold = 0.9  # Adjust this value based on your needs

    return ssim_score


def compare_exact(capture, saved):
    capture = capture.convert('L')
    saved = saved.convert('L')
    image_one = capture.filter(ImageFilter.BoxBlur(radius=3))
    image_two = saved.filter(ImageFilter.BoxBlur(radius=3))

    phashvalue = imagehash.phash(image_one)-imagehash.phash(image_two)
    ahashvalue = imagehash.average_hash(
        image_one)-imagehash.average_hash(image_two)
    totalaccuracy = phashvalue+ahashvalue

    return totalaccuracy
