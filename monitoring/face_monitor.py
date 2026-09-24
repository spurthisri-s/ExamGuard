import cv2
import numpy as np


# ------------------------------------------------
# HAAR CASCADE FACE DETECTOR
# ------------------------------------------------

_FACE_CASCADE_PATH = (
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml"
)


_face_cascade = cv2.CascadeClassifier(
    _FACE_CASCADE_PATH
)


# ------------------------------------------------
# CHECK CASCADE
# ------------------------------------------------

if _face_cascade.empty():

    raise RuntimeError(
        "Could not load Haar Cascade classifier. "
        "Check your OpenCV installation."
    )


# ------------------------------------------------
# FACE DETECTION
# ------------------------------------------------

def detect_face(image_data):
    """
    Receives raw JPEG image bytes from the
    browser webcam.

    Returns:

        True  -> face detected
        False -> no face detected

    This performs face-presence detection only.

    It does NOT perform:

        - face recognition
        - identity verification
        - liveness detection
    """

    if not image_data:

        return False


    # Convert bytes into NumPy array

    image_array = np.frombuffer(
        image_data,
        np.uint8
    )


    # Decode JPEG

    frame = cv2.imdecode(
        image_array,
        cv2.IMREAD_COLOR
    )


    if frame is None:

        return False


    # Convert to grayscale

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    # Improve contrast slightly

    gray = cv2.equalizeHist(
        gray
    )


    # Detect faces

    faces = _face_cascade.detectMultiScale(

        gray,

        scaleFactor=1.1,

        minNeighbors=5,

        minSize=(60, 60)
    )


    return len(faces) > 0