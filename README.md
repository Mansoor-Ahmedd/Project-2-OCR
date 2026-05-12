# 📄 OCR Pipeline – From Classic Engines to Deep Learning + Information Extraction + Document Intelligence API

**Course:** Introduction to Applied Artificial Intelligence  
**Assignments:** Lab 5 (OCR Basics), Lab 6 (Advanced Preprocessing + CNN), Lab 7 (Information Extraction & NER), Lab 8 (Document Intelligence System API)  
**Student:** Mansoor Ahmed  
**Department:** BSCS  
**Platform:** Kaggle + FastAPI  

---

## 📌 Overview

This repository presents a complete **end-to-end document intelligence pipeline**, developed across four labs:

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

* **🔹 Week 8 – Document Intelligence API**
  * Built a production-ready document classification & extraction API
  * Used OCR + Machine Learning for document understanding
  * Developed REST API using FastAPI with Swagger UI

---

# 🧠 Week 8 – Document Intelligence System

## 📌 Project Overview

This module extends the OCR pipeline into a **production-ready document intelligence system** capable of processing real-world business documents such as:

* Invoices
* Receipts
* Contracts

The system accepts a document image and returns:

* Document type (classification)
* Confidence score
* Extracted entities
* Structured JSON response

The pipeline combines:

* **OCR:** Tesseract OCR
* **Machine Learning:** TF‑IDF + Logistic Regression
* **API Framework:** FastAPI
* **Information Extraction:** Regex + Named Entity Recognition

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

### ✅ Week 8 – Document Classification & Extraction API

* Built a document classification pipeline
* Classified:
  * Invoices
  * Receipts
  * Contracts

* Applied OCR on uploaded document images
* Trained machine learning model using:
  * TF‑IDF Vectorization
  * Logistic Regression

* Extracted:
  * Dates
  * Monetary values
  * Named entities

* Developed REST API using FastAPI
* Generated interactive API documentation with Swagger UI
* Achieved classification accuracy above **90%**

---

## 📁 Project Structure

```text
document-intelligence-api/
│
├── models/
│   ├── vectorizer.pkl
│   └── classifier.pkl
│
├── uploads/
│
├── week5_ocr_basics.ipynb
├── week6_advanced_ocr_cnn.ipynb
├── week7_information_extraction.ipynb
├── week8_document_intelligence_api.ipynb
│
├── receipt_ocr_results.csv
├── extracted_data.json
├── entities.html
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### ▶️ Option 1: Run on Kaggle (Recommended)

1. Create a new notebook on Kaggle
2. Attach datasets:
   * OCR Receipts Text Detection
   * Multi-type document datasets
3. Enable:
   * GPU (optional)
   * Internet access
4. Run notebooks step by step

---

### 💻 Option 2: Run Locally

Install dependencies:

```bash
pip install pytesseract pillow opencv-python pandas matplotlib numpy easyocr tensorflow scikit-learn fastapi uvicorn python-multipart spacy joblib imutils
python -m spacy download en_core_web_sm
```

---

## 🧠 Model Training (Week 8)

### 📌 Dataset Requirements

Use at least **10–15 real images per class**:

* invoices
* receipts
* contracts

### Recommended Kaggle Datasets

* https://www.kaggle.com/datasets/senju14/multi-type-document-ocr-dataset
* https://www.kaggle.com/datasets/ryanznie/sroie-datasetv2-with-labels
* https://www.kaggle.com/datasets/shaz13/real-world-documents-collections

---

## 🚀 Training Pipeline

```python
# Install dependencies
!pip install pytesseract pillow scikit-learn joblib

# OCR extraction
# TF-IDF vectorization
# Logistic Regression training

joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(classifier, 'classifier.pkl')
```

Expected accuracy: **>90% on real documents**

---

## 🚀 FastAPI REST API

### Run the API

```bash
uvicorn main:app --reload
```

### Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

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

```text
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

### 📌 Week 8 – API Response Example

```json
{
  "document_type": "invoice",
  "confidence_score": 0.94,
  "extracted_entities": {
    "date": "2024-03-15",
    "amount": "$1250.50",
    "organization": "ABC Corporation"
  }
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

### Week 8
* OCR + ML enables intelligent document classification
* TF‑IDF performs effectively for document text analysis
* FastAPI simplifies ML model deployment
* REST APIs enable real-world AI applications

---

## 🧰 Technologies Used

* Python 3.10
* Tesseract OCR
* EasyOCR
* OpenCV
* TensorFlow / Keras
* FastAPI
* Uvicorn
* spaCy (NER)
* Scikit-learn
* Logistic Regression
* TF‑IDF Vectorization
* Regex (`re`)
* NumPy, Pandas, Matplotlib

---

## 🚀 How to Reproduce

1. Clone the repository
2. Train the classifier
3. Save models into `/models`
4. Run notebooks (Week 5 → Week 8)
5. Launch FastAPI server
6. Upload documents via Swagger UI

---

## 🔮 Future Improvements

* Integrate deep learning OCR models
* Add transformer-based document understanding
* Support multilingual documents
* Deploy on cloud (AWS/GCP/Azure)
* Add database storage for extracted information

---

## 👨‍💻 Author

**Mansoor Ahmed**  
BSCS – Applied AI
