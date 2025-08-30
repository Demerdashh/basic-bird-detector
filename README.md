# Bird Detector — OpenCV (Simple contour-based detector)

A simple, lightweight bird detection demo using OpenCV contour detection and thresholding.  
This project is intended as an educational example to show how basic image pre-processing, thresholding, contour extraction and bounding boxes work — no machine learning involved.

---

## Demo
Given an input image with birds, the script applies grayscale conversion, thresholding, and contour filtering, then draws bounding boxes around detected birds and saves the result.

Example input/output image is included in the `example/` folder.

---

## 📂 Project Structure
<img width="845" height="285" alt="Screenshot 2025-08-31 003332" src="https://github.com/user-attachments/assets/5c4aed0e-6e69-4139-a317-7a9473dcac69" />

---

## Features
- Read image from disk
- Convert to grayscale and threshold (binary inverse)
- Find contours and filter by area
- Draw bounding boxes and label detections

---
## 👤 Author

Built with ❤️ by Youssef Ahmed El Demerdash
