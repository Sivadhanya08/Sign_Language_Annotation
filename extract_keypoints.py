import cv2
import mediapipe as mp
import os
import json

# Paths
video_folder = r"D:\22bcs008\archive (1)\Sign_Language_Practice_Dataset"
output_folder = r"D:\22bcs008\archive (1)\Sign_Language_Practice_Dataset\keypoints"
os.makedirs(output_folder, exist_ok=True)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

for video_name in os.listdir(video_folder):
    if not video_name.endswith(".mp4"):
        continue

    video_path = os.path.join(video_folder, video_name)
    cap = cv2.VideoCapture(video_path)
    frame_data = []

    with mp_hands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            keypoints = {}
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    hand_points = []
                    for lm in hand_landmarks.landmark:
                        hand_points.append({"x": lm.x, "y": lm.y, "z": lm.z})
                    if "hands" not in keypoints:
                        keypoints["hands"] = []
                    keypoints["hands"].append(hand_points)

            if keypoints:
                frame_data.append(keypoints)

        cap.release()

    # Save results to JSON
    json_path = os.path.join(output_folder, video_name.replace(".mp4", ".json"))
    with open(json_path, "w") as f:
        json.dump(frame_data, f, indent=4)

    print(f"✅ Keypoints extracted: {video_name}")
