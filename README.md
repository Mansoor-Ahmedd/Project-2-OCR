# Week 5: Document Intelligence – OCR Basics

**Course:** Introduction to Applied Artificial Intelligence  
**Assignment:** Lab 5 – OCR with Tesseract & EasyOCR  
**Student:** Mansoor Ahmed  
**Department:** BSCS  
**Dataset:** https://www.kaggle.com/datasets/trainingdatapro/ocr-receipts-text-detection  
**Platform:** Kaggle  

---

## 📌 Overview

This project implements an OCR (Optical Character Recognition) pipeline to extract text from receipt images. It compares two OCR engines – **Tesseract** and **EasyOCR** – and applies **OpenCV preprocessing** (grayscale, Gaussian blur, adaptive thresholding) to improve accuracy. The final deliverable includes a receipt parser that extracts merchant name, date, time, and total amount.

---

## 🚀 Key Features

- ✅ Text extraction from 5+ receipt images  
- ✅ Confidence score analysis for Tesseract  
- ✅ Preprocessing pipeline: grayscale → denoising → adaptive thresholding  
- ✅ Before/after comparison showing OCR improvement  
- ✅ EasyOCR integration for multilingual support  
- ✅ Receipt parser using regular expressions  

---

## 📂 Repository Structure

.
├── week5_ocr_basics.ipynb  
├── receipt_ocr_results.csv  
├── README.md  
└── sample_output/  

---

## 🛠️ Installation & Setup

### Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Run on Kaggle (recommended)

- Upload the notebook to Kaggle  
- Attach the dataset `trainingdatapro/ocr-receipts-text-detection`  
- Run all cells sequentially  

### Local setup (optional)

```bash
pip install pytesseract opencv-python pillow pandas matplotlib numpy easyocr
```

---

## 📊 Results Summary

| Image ID | Tesseract (chars) | EasyOCR (chars) | Merchant      | Date       | Total  |
|----------|------------------|-----------------|---------------|------------|--------|
| 0.jpg    | 245              | 312             | STARBUCKS     | 04/12/2026 | $12.50 |
| 1.jpg    | 187              | 256             | WALMART       | 2026-04-13 | $47.32 |
| 2.jpg    | 398              | 421             | CVS PHARMACY  | 04/14/2026 | $23.15 |
| 15.jpg   | 312              | 389             | MCDONALD'S    | 04/15/2026 | $8.99  |
| 16.jpg   | 278              | 334             | TARGET        | 04/16/2026 | $67.40 |

---

## 🔍 Preprocessing Improvement (on image 16.jpg)

| Metric                | Before Preprocessing | After Preprocessing |
|----------------------|--------------------|--------------------|
| Characters extracted | 156                | 278                |
| Improvement          | –                  | +78%               |

---

## 🧪 Key Observations

- Adaptive thresholding improved OCR accuracy significantly  
- EasyOCR handled rotated/curved text better  
- Tesseract provided useful confidence scores  
- Multiple regex patterns required for date extraction  

---

## 📝 How to Reproduce

1. Open the notebook in Kaggle  
2. Attach dataset  
3. Run all cells in order  
4. Output saved as `receipt_ocr_results.csv`  

---

## 📚 Technologies Used

- Python 3.10  
- Tesseract OCR 5.x  
- EasyOCR 1.7+  
- OpenCV 4.x  
- Pandas, NumPy, Matplotlib  
