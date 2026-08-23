# 🌱 AgriSmart - AI Crop Recommendation System

## 📌 Project Overview

AgriSmart is a Machine Learning-based crop recommendation system that predicts a suitable crop based on soil and environmental conditions.

The system uses a Random Forest Classification algorithm to analyze important agricultural parameters such as Nitrogen, Phosphorus, Potassium, temperature, humidity, soil pH, and rainfall.

A Flask web application is used to provide an interactive interface where users can enter agricultural conditions and receive a crop recommendation.

---

## 🎯 Objectives

- Recommend suitable crops using Machine Learning.
- Analyze soil and environmental parameters.
- Build an interactive web application.
- Display prediction confidence.
- Visualize Random Forest feature importance.
- Demonstrate an end-to-end Machine Learning workflow.

---

## 🧠 Machine Learning Model

### Algorithm

Random Forest Classifier

### Input Features

| Feature | Description |
|---|---|
| N | Nitrogen content |
| P | Phosphorus content |
| K | Potassium content |
| Temperature | Temperature in °C |
| Humidity | Relative humidity |
| pH | Soil pH value |
| Rainfall | Rainfall in mm |

### Output

The model predicts a suitable crop based on the given conditions.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS
- JavaScript
- VS Code

---

## 📊 Dataset

The project uses a crop recommendation dataset containing soil and environmental parameters.

The dataset contains:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- Soil pH
- Rainfall
- Crop label

> Note: The current dataset is a synthetic prototype dataset created for demonstrating the complete Machine Learning workflow. It can be replaced with a real-world agricultural dataset for further development.

---

## 🔄 Machine Learning Workflow

```text
Agricultural Dataset
        ↓
Data Preparation
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Random Forest Classifier
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Save Trained Model
        ↓
Flask Web Application
        ↓
User Input
        ↓
Crop Recommendation