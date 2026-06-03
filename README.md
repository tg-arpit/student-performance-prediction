# 🎓 Student Performance Prediction System

A Machine Learning project that predicts whether a student will **Pass** or **Fail** based on academic and attendance-related factors such as study hours, attendance percentage, and previous scores.

---

## 📌 Project Overview

Educational institutions often need to identify students who may be at risk of failing. This project uses a Machine Learning classification model to analyze student performance data and predict the likelihood of passing or failing.

The project demonstrates the complete Machine Learning workflow:

- Data Collection
- Data Exploration
- Data Preprocessing
- Model Training
- Model Evaluation
- Model Deployment Preparation
- Version Control using Git & GitHub

---

## 🎯 Objectives

- Predict student performance using historical academic data.
- Apply Machine Learning classification techniques.
- Learn Git and GitHub version control practices.
- Build a structured and reproducible ML project.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Manipulation |
| Scikit-Learn | Machine Learning |
| Joblib | Model Serialization |
| Git | Version Control |
| GitHub | Repository Management |

---

## 📂 Project Structure

```text
Student-Performance-Prediction/
│
├── data/
│   └── student_data.csv
│
├── src/
│   ├── train.py
│   ├── predict.py
│   └── student_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset Description

The dataset contains the following features:

| Feature | Description |
|-----------|------------|
| study_hours | Number of study hours per day |
| attendance | Student attendance percentage |
| previous_score | Previous examination score |
| pass | Target variable (0 = Fail, 1 = Pass) |

### Sample Dataset

| study_hours | attendance | previous_score | pass |
|------------|------------|---------------|------|
| 2 | 60 | 40 | 0 |
| 5 | 75 | 55 | 1 |
| 8 | 90 | 70 | 1 |
| 1 | 50 | 35 | 0 |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Student-Performance-Prediction.git
```

### 2. Navigate to Project Directory

```bash
cd Student-Performance-Prediction
```

### 3. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Model Training

Run the training script:

```bash
cd src
python train.py
```

### Expected Output

```text
Model Accuracy: 1.00
Model saved successfully!
```

The trained model will be saved as:

```text
student_model.pkl
```

---

## 🔮 Making Predictions

Run:

```bash
python predict.py
```

### Example

```text
Enter Study Hours: 7
Enter Attendance (%): 85
Enter Previous Score: 65

Prediction: PASS
```

---

## 🧠 Machine Learning Workflow

### Step 1: Load Dataset

- Read CSV data using Pandas.

### Step 2: Explore Dataset

- Check features and target variable.
- Understand data distribution.

### Step 3: Preprocess Data

- Separate features and target.
- Split data into training and testing sets.

### Step 4: Train Model

- Logistic Regression classifier.

### Step 5: Evaluate Model

- Accuracy Score

### Step 6: Save Model

- Save trained model using Joblib.

---

## 📈 Model Used

### Logistic Regression

Logistic Regression is a supervised Machine Learning algorithm used for binary classification problems.

In this project:

- Output = Pass / Fail
- Fast and efficient
- Easy to interpret
- Suitable for small datasets

---

## 🔄 Git Workflow

### Initialize Repository

```bash
git init
```

### Add Files

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Initial project setup"
```

### Connect Remote Repository

```bash
git remote add origin https://github.com/tg-arpit/Student-Performance-Prediction.git
```

### Push to GitHub

```bash
git branch -M main
git push -u origin main
```

---

## 👥 Collaboration Workflow

Create a new branch:

```bash
git checkout -b feature-update
```

Commit changes:

```bash
git add .
git commit -m "Added new feature"
```

Push branch:

```bash
git push origin feature-update
```

Create a Pull Request on GitHub.

---

## 📋 Requirements

```text
pandas
scikit-learn
joblib
```

Install:

```bash
pip install -r requirements.txt
```

---

## 📸 Future Improvements

- Add larger datasets
- Use Random Forest Classifier
- Build a Flask Web Application
- Create Streamlit Dashboard
- Deploy on Render or Heroku
- Add Data Visualization

---

## 🎓 Learning Outcomes

Through this project, you will learn:

- Data preprocessing
- Machine Learning model training
- Model evaluation
- Saving and loading models
- Git version control
- GitHub repository management
- Collaborative development workflow

---

## 📄 License

This project is developed for educational and learning purposes.


⭐ If you found this project useful, consider giving it a star on GitHub.