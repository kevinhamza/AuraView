import cv2
import dlib
import numpy as np
import requests

# Load Dlib's face detector and face recognition model
face_detector = dlib.get_frontal_face_detector()
face_recognition_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Placeholder for known faces (mock embeddings for demo purposes)
known_faces = {
    "John Doe": np.random.rand(128),
    "Jane Smith": np.random.rand(128)
}

# Get face embedding from the image
def get_face_embedding(face_image):
    shape = shape_predictor(face_image, dlib.rectangle(0, 0, face_image.shape[1], face_image.shape[0]))
    return np.array(face_recognition_model.compute_face_descriptor(face_image, shape))

# Match the face embedding to known faces
def match_face(embedding, tolerance=0.6):
    for name, known_embedding in known_faces.items():
        if np.linalg.norm(embedding - known_embedding) < tolerance:
            return name
    return "Unknown"

# Fetch user information from the server
def fetch_user_info(name):
    response = requests.get("http://127.0.0.1:5000/get_user_info", params={"name": name})
    return response.json() if response.status_code == 200 else {"name": "Unknown", "occupation": "", "social_media": {}}

# Start video capture for real-time face detection
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    for face in faces:
        face_image = frame[face.top():face.bottom(), face.left():face.right()]
        embedding = get_face_embedding(face_image)
        name = match_face(embedding)
        user_info = fetch_user_info(name)

        cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)
        cv2.putText(frame, user_info["name"], (face.left(), face.top() - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(frame, user_info["occupation"], (face.left(), face.top() - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("AR Social Glasses", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
