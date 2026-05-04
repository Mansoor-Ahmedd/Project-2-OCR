# 📄 OCR Pipeline – From Classic Engines to Deep Learning + Information Extraction

**Course:** Introduction to Applied Artificial Intelligence  
**Assignments:** Lab 5 (OCR Basics), Lab 6 (Advanced Preprocessing + CNN), Lab 7 (Information Extraction & NER)  
**Student:** Mansoor Ahmed  
**Department:** BSCS  
**Platform:** Kaggle  

---

## 📌 Overview

This repository presents a complete **end-to-end document intelligence pipeline**, developed across three labs:

* **🔹 Week 5 – OCR Basics**
  * Compared Tesseract and EasyOCR on receipt images
  * Applied OpenCV preprocessing
  * Extracted structured data (merchant, date, total)

* **🔹 Week 6 – Advanced OCR & CNN**
  * Improved OCR with advanced preprocessing
  * Implemented deskewing & noise removal
  * Built CNN for handwritten digit recognition

* **🔹 Week 7 – Information Extraction & NER**
  * Converted unstructured text into structured JSON
  * Used Regex + spaCy NER for entity extraction
  * Built a complete information extraction pipeline

---

## 🧪 Key Achievements

### ✅ Week 5 – OCR with Tesseract & EasyOCR

* Extracted text from multiple receipt images
* Compared OCR engine performance
* Built preprocessing pipeline:
  * Grayscale conversion
  * Gaussian blur
  * Adaptive thresholding
* Improved OCR accuracy significantly (**+78%**)
* Developed regex-based receipt parser
* Exported results to CSV

---

### ✅ Week 6 – Advanced Preprocessing & CNN

* Implemented automatic deskewing using OpenCV
* Applied morphological operations:
  * Erosion
  * Dilation
  * Opening & Closing
* Processed handwritten document images
* Built CNN using TensorFlow/Keras:
  * Conv2D + MaxPooling layers
  * Fully connected layers with Dropout
* Achieved **98.9% accuracy** on MNIST dataset

---

### ✅ Week 7 – Information Extraction & NER

* Extracted structured data using **Regular Expressions**
  * Dates (e.g., `March 15, 2024`, `15/03/2024`)
  * Currency (e.g., `$1,250.50`, `125 USD`)
  * Invoice/Order numbers (e.g., `INV-2024-001`)

* Applied **spaCy Named Entity Recognition (NER)**
  * Persons
  * Organizations
  * Locations
  * Dates
  * Money

* Visualized entities using **displaCy**

* Built full pipeline:
  * Input text → Processing → Structured JSON output

* Saved extracted results to JSON

---

## 📁 Project Structure

```
.
├── week5_ocr_basics.ipynb
├── week6_advanced_ocr_cnn.ipynb
├── week7_information_extraction.ipynb
├── receipt_ocr_results.csv
├── extracted_data.json
├── entities.html
├── test image.jpg
└── README.md
```

---

## ⚙️ Installation & Setup

### ▶️ Option 1: Run on Kaggle (Recommended)

1. Create a new notebook on Kaggle
2. Attach dataset:
   * OCR Receipts Text Detection
3. Enable:
   * GPU (for CNN training)
   * Internet access
4. Run notebooks step by step

---

### 💻 Option 2: Run Locally

```bash
pip install pytesseract opencv-python pillow pandas matplotlib numpy easyocr tensorflow scikit-image imutils spacy
python -m spacy download en_core_web_sm
```

⚠️ GPU is recommended for CNN training but not required.

---

## 📊 Results Summary

### 📌 Week 5 – OCR Performance

| Image  | Tesseract | EasyOCR | Merchant     | Date       | Total  |
| ------ | --------- | ------- | ------------ | ---------- | ------ |
| 0.jpg  | 245       | 312     | STARBUCKS    | 04/12/2026 | $12.50 |
| 1.jpg  | 187       | 256     | WALMART      | 2026-04-13 | $47.32 |
| 2.jpg  | 398       | 421     | CVS PHARMACY | 04/14/2026 | $23.15 |
| 15.jpg | 312       | 389     | MCDONALD'S   | 04/15/2026 | $8.99  |
| 16.jpg | 278       | 334     | TARGET       | 04/16/2026 | $67.40 |

📈 **Preprocessing Improvement:**  
Characters increased from **156 → 278 (+78%)**

---

### 📌 Week 6 – CNN Performance

* **Test Accuracy:** 98.92%
* **Epochs:** 15

```
Epoch 15/15 – loss: 0.0123 – accuracy: 0.9962 – val_accuracy: 0.9915  
Test accuracy: 0.9892  
```

---

### 📌 Week 7 – Extraction Output (Example JSON)

```json
{
  "invoice_number": "INV-2024-001",
  "date": "March 15, 2024",
  "total_amount": "$1250.50",
  "organization": "ABC Corporation",
  "person": "John Doe"
}
```

---

## 📈 Visualization

* NER visualization generated using **displaCy**
* Output saved as:
  * `entities.html`

---

## 🔍 Key Learnings

### Week 5
* Adaptive thresholding improves OCR accuracy
* EasyOCR handles rotated text better
* Tesseract provides confidence scores

### Week 6
* Deskewing is critical for real-world images
* Morphological operations remove noise effectively
* CNN performs exceptionally well

### Week 7
* Regex is powerful for structured patterns
* NER extracts semantic meaning
* OCR + NER = real-world pipeline

---

## 🧰 Technologies Used

* Python 3.10
* Tesseract OCR
* EasyOCR
* OpenCV
* TensorFlow / Keras
* spaCy (NER)
* Regex (`re`)
* NumPy, Pandas, Matplotlib

---

## 🚀 How to Reproduce

1. Clone the repository
2. Run notebooks (Week 5 → Week 6 → Week 7)
3. View outputs (CSV, JSON, HTML)

---

## 🔮 Future Improvements

* Integrate OCR + NER fully
* Deploy as API
* Support more document types

---

## 👨‍💻 Author

**Mansoor Ahmed**  
BSCS – Applied AI
