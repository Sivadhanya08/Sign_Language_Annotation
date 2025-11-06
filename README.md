Sign Language Video Annotation and Keypoint Extraction

Project Overview
This project demonstrates an end-to-end workflow for sign language gesture recognition, including video annotation and keypoint extraction. The goal is to create a labeled dataset of hand gestures from sign language videos, preparing it for future machine learning and computer vision applications.

Using Label Studio, the videos were annotated with gesture labels such as HELLO, THANK YOU, YES, NO, LOVE, and PLEASE. Then, MediaPipe Hands and OpenCV were used to extract detailed hand landmark keypoints (x, y, z coordinates) from each frame, saving them as structured JSON files.

Tools and Technologies

| Category           | Tools                 |
| ------------------ | --------------------- |
| Annotation         | Label Studio          |
| Keypoint Detection | MediaPipe Hands       |
| Video Processing   | OpenCV                |
| Programming        | Python                |
| Data Handling      | NumPy                 |
| Visualization      | Matplotlib (optional) |

Workflow

1. Video Annotation

* Imported sign language clips into Label Studio
* Configured labels for gestures such as HELLO, THANK YOU, LOVE, YES, and NO
* Exported annotations in JSON format

2. Keypoint Extraction

* Processed each video using the extract_keypoints.py script
* Extracted left and right hand landmarks per frame using MediaPipe
* Saved results as structured .json files under the keypoints directory

3. Dataset Preparation

* Combined labeled annotations and extracted keypoints
* Created a ready-to-train dataset for gesture recognition models

Folder Structure

SignLanguage-Keypoint-Annotation/
│
├── videos/                    
│   ├── hello_sample.mp4
│   ├── thankyou_sample.mp4
│
├── keypoints/                 
│   ├── hello_sample.json
│   ├── thankyou_sample.json
│
├── annotation_samples/        
│   └── sign_language_annotations.json
│
├── extract_keypoints.py       
├── requirements.txt          
└── README.md                  


Example JSON Output
Each file contains frame-by-frame keypoint coordinates for detected hands:

json
[
  {
    "hands": [
      [
        {"x": 0.432, "y": 0.512, "z": -0.034},
        {"x": 0.438, "y": 0.489, "z": -0.031}
      ]
    ]
  }
]

How to Run the Project

1. Clone the Repository

bash
git clone https://github.com/<your-username>/SignLanguage-Keypoint-Annotation.git
cd SignLanguage-Keypoint-Annotation


2. Install Dependencies

bash
pip install -r requirements.txt

3. Run the Keypoint Extraction Script

bash
python extract_keypoints.py

Extracted keypoints will be saved automatically inside the keypoints folder.

Key Learnings

* Built a complete video annotation and keypoint extraction pipeline
* Understood how to prepare custom datasets for AI/ML training
* Learned to work with MediaPipe, OpenCV, and Label Studio
* Created a structured, reusable dataset for gesture recognition

Future Enhancements

* Train a model to recognize gestures from extracted keypoints
* Extend to full-body and facial keypoints using MediaPipe Holistic
* Integrate with a 3D avatar for real-time sign translation

Tags
AI, MachineLearning, ComputerVision, SignLanguage, LabelStudio, MediaPipe, DataAnnotation, OpenCV, Python

License
This project is open-source under the MIT License. You are free to use, modify, and distribute it for educational or research purposes.

Author
Sivadhanya S
Computer Science and Engineering Student
Email: sivadhanya5757@gmail.com
LinkedIn: www.linkedin.com/in/sivadhanya-s-432a7425a
GitHub: GitHub: https://github.com/Sivadhanya08/Sign_Language_Annotation

