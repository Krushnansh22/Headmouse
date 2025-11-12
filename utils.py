import numpy as np

def eye_aspect_ratio(eye):
    # Compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])

    # Compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = np.linalg.norm(eye[0] - eye[3])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # Return the eye aspect ratio
    return ear

def mouth_aspect_ratio(mouth):
    # Compute the euclidean distances between the three sets of
    # vertical mouth landmarks (x, y)-coordinates
    # These indices (13-19) are for the *inner* mouth
    A = np.linalg.norm(mouth[13] - mouth[19]) 
    B = np.linalg.norm(mouth[14] - mouth[18])
    C = np.linalg.norm(mouth[15] - mouth[17])

    # Compute the euclidean distance between the horizontal
    # mouth landmark (x, y)-coordinates
    D = np.linalg.norm(mouth[12] - mouth[16])

    # Compute the mouth aspect ratio
    mar = (A + B + C) / (2.0 * D) # Use 2.0 for float division

    # Return the mouth aspect ratio
    return mar

def direction(nose_point, anchor_point, w, h):
    # Calculate the change in x and y
    # This is the new function that matches the main script
    dx = nose_point[0] - anchor_point[0]
    dy = nose_point[1] - anchor_point[1]

    # Determine direction based on whether the change
    # is greater than the width (w) or height (h) thresholds
    if np.abs(dx) > w:
        return 'right' if dx > 0 else 'left'
    
    if np.abs(dy) > h:
        return 'down' if dy > 0 else 'up'
    
    # If no significant movement, return 'center'
    return 'center'