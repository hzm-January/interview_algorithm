import cv2
import numpy as np

def stitch_images(img1, img2):
    """Stitch two images together."""
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Detect SIFT keypoints and descriptors
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    # Match features using FLANN-based matcher
    index_params = dict(algorithm=1, trees=5)  # FLANN KDTree index
    search_params = dict(checks=50)  # Higher means more accurate matches
    matcher = cv2.FlannBasedMatcher(index_params, search_params)
    matches = matcher.knnMatch(des1, des2, k=2)

    # Apply Lowe's ratio test
    good_matches = [m for m, n in matches if m.distance < 0.7 * n.distance]

    # Draw matches
    match_img = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None,
                                flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    scale_factor = 0.5  # Scale down the image for better visibility
    match_img_resized = cv2.resize(match_img,
                                   (int(match_img.shape[1] * scale_factor), int(match_img.shape[0] * scale_factor)))
    cv2.imshow("Feature Matches", match_img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Extract matched points
    pts1 = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    pts2 = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # Find homography matrix
    H, _ = cv2.findHomography(pts2, pts1, cv2.RANSAC, 5.0)

    # Warp second image and stitch
    height, width, _ = img1.shape
    result = cv2.warpPerspective(img2, H, (width * 2, height))
    result[0:height, 0:width] = img1

    return result

def correct_image(image):
    """Correct stitching errors, distortions, and color."""
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE for better contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    corrected_gray = clahe.apply(gray)

    # Convert back to BGR
    corrected_image = cv2.cvtColor(corrected_gray, cv2.COLOR_GRAY2BGR)

    return corrected_image

def extract_license_plate(image):
    """Extract license plate region."""
    # Convert to grayscale and apply edge detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter for rectangular contours
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:  # Looking for quadrilaterals
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            if 2 < aspect_ratio < 6:  # Typical license plate aspect ratio
                license_plate = image[y:y + h, x:x + w]
                return license_plate

    return None

def process_license_plate_images(img1_path, img2_path, extract_plate=False):
    """Main function to process and recover license plate."""
    # Load images
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Step 1: Stitch images
    stitched_image = stitch_images(img1, img2)

    # # Step 2: Correct stitched image
    # corrected_image = correct_image(stitched_image)
    #
    # # Step 3 (Optional): Extract license plate
    # if extract_plate:
    #     license_plate = extract_license_plate(corrected_image)
    #     if license_plate is not None:
    #         return license_plate
    #     else:
    #         print("License plate not detected.")
    #
    # return corrected_image

    return stitched_image

# Example usage
if __name__ == "__main__":
    img1_path = "img/image_01.jpg"  # Path to first image
    img2_path = "img/image_02.jpg"  # Path to second image

    # Process images
    result = process_license_plate_images(img1_path, img2_path, extract_plate=True)

    # Show and save results
    if result is not None:
        scale_factor = 0.5  # Scale down the image for better visibility
        result = cv2.resize(result,
                                       (int(result.shape[1] * scale_factor), int(result.shape[0] * scale_factor)))
        cv2.imshow("Result", result)
        # cv2.imwrite("output.jpg", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
