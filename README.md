# Face-Recognition
A **Python-based facial recognition system** that detects and identifies faces from images and real-time webcam input using the `face_recognition` and `OpenCV` libraries. It also includes a feature for **automated attendance tracking**, logging recognized individuals with timestamps in a CSV file.

---

## Features

- Face encoding and recognition using deep learning-based models.
- Real-time face detection via webcam.
- Matches live faces with a set of known images.
- Logs attendance with names and current timestamps.
- Visual feedback with bounding boxes and labels.

## Technologies Used

- Python 3.x
- OpenCV
- face_recognition
- NumPy
- OS, DateTime
 
## Project Structure
project-folder/
│
├── Images/ # Folder with known face images (e.g., Zendaya.jpg)
├── Attendance.csv # CSV file to log attendance
├── face_recognition.py # Core script for facial recognition and attendance
└── README.md # Project documentation

---

## Sample Use Case
- Load known face images (e.g., employee or student photos).
- Start the webcam feed.
- System detects and identifies individuals in real-time.
- Matches found are logged in `Attendance.csv` with a timestamp.

## How to Run
1. **Clone the repository**
```bash
git clone https://github.com/yourusername/facial-recognition-attendance.git
cd facial-recognition-attendance
2. Install dependencies
bash
Copy code
pip install opencv-python face_recognition numpy
3. Add face images
Place JPG or PNG images of known individuals in the Images/ folder. The filename (excluding extension) will be used as the person's name.
4. Run the script
python face_recognition.py
5. View results
- Real-time video feed will display recognized faces.
- Attendance is saved in Attendance.csv.
