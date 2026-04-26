# 📄 OCR Pipeline – From Classic Engines to Deep Learning

**Course:** Introduction to Applied Artificial Intelligence  
**Assignments:** Lab 5 (OCR Basics) & Lab 6 (Advanced Preprocessing + CNN)  
**Student:** Mansoor Ahmed  
**Department:** BSCS  
**Platform:** Kaggle  

---

## 📌 Overview

This repository presents a complete Optical Character Recognition (OCR) pipeline developed across two labs:

### 🔹 Week 5 – OCR Basics
- Compared Tesseract and EasyOCR on real-world receipt images  
- Applied OpenCV preprocessing techniques  
- Extracted structured information (merchant, date, total)

### 🔹 Week 6 – Advanced OCR & CNN
- Improved OCR performance using advanced preprocessing  
- Implemented automatic deskewing and noise removal  
- Built a Convolutional Neural Network (CNN) for handwritten digit recognition  

---

## 🧪 Key Achievements

### ✅ Week 5 – OCR with Tesseract & EasyOCR
- Extracted text from multiple receipt images  
- Compared OCR engines performance  
- Built preprocessing pipeline:
  - Grayscale conversion  
  - Gaussian blur  
  - Adaptive thresholding  
- Improved OCR accuracy significantly (up to +78%)  
- Developed regex-based receipt parser  
- Exported results to CSV  

### ✅ Week 6 – Advanced Preprocessing & CNN
- Implemented automatic deskewing using OpenCV  
- Applied morphological operations:
  - Erosion  
  - Dilation  
  - Opening & Closing  
- Processed custom handwritten document images  
- Built CNN using TensorFlow/Keras:
  - Conv2D + MaxPooling layers  
  - Fully connected layers with Dropout  
- Achieved **98.9% accuracy** on MNIST dataset  

---

## 📁 Project Structure

```
.
├── week5_ocr_basics.ipynb
├── week6_advanced_ocr_cnn.ipynb
├── receipt_ocr_results.csv
├── test image.jpg
└── README.md
```

---

## ⚙️ Installation & Setup

### ▶️ Option 1: Run on Kaggle (Recommended)

1. Create a new notebook on Kaggle  
2. Attach dataset:  
   - OCR Receipts Text Detection  
3. Enable:
   - GPU (for CNN training)  
   - Internet access  
4. Run notebooks step by step  

---

### 💻 Option 2: Run Locally

Install dependencies:

```
pip install pytesseract opencv-python pillow pandas matplotlib numpy easyocr tensorflow scikit-image imutils
```

> ⚠️ Note: GPU is recommended for faster CNN training but not required.

---

## 📊 Results Summary

### 📌 Week 5 – OCR Performance

| Image | Tesseract | EasyOCR | Merchant | Date | Total |
|------|----------|---------|----------|------|-------|
| 0.jpg | 245 | 312 | STARBUCKS | 04/12/2026 | $12.50 |
| 1.jpg | 187 | 256 | WALMART | 2026-04-13 | $47.32 |
| 2.jpg | 398 | 421 | CVS PHARMACY | 04/14/2026 | $23.15 |
| 15.jpg | 312 | 389 | MCDONALD'S | 04/15/2026 | $8.99 |
| 16.jpg | 278 | 334 | TARGET | 04/16/2026 | $67.40 |

📈 **Preprocessing Improvement:**  
Characters increased from **156 → 278 (+78%)**

---

### 📌 Week 6 – CNN Performance

- **Test Accuracy:** 98.92%  
- **Training Epochs:** 15  

Sample log:
```
Epoch 15/15 – loss: 0.0123 – accuracy: 0.9962 – val_accuracy: 0.9915
Test accuracy: 0.9892
```

✅ Requirement (≥98%) achieved

---

## 🔍 Key Learnings

### Week 5
- Adaptive thresholding greatly improves OCR results  
- EasyOCR handles rotated text better  
- Tesseract provides useful confidence scores  

### Week 6
- Deskewing is essential for real-world images  
- Morphological operations remove noise effectively  
- Even a simple CNN can achieve high accuracy on MNIST  

---

## 🧰 Technologies Used

- Python 3.10  
- Tesseract OCR  
- EasyOCR  
- OpenCV  
- TensorFlow / Keras  
- NumPy, Pandas, Matplotlib  

---

## 🚀 How to Reproduce

1. Clone the repository  
2. Run `week5_ocr_basics.ipynb`  
3. Run `week6_advanced_ocr_cnn.ipynb`  
4. View outputs (CSV, graphs, predictions)  


## 📚 References

- MNIST Dataset: http://yann.lecun.com/exdb/mnist/  
- Kaggle OCR Dataset  
- Course Lab Manuals  

