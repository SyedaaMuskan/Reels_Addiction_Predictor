# Reels Addiction Level Predictor 🚀

Predict the addiction level of Gen-Z users on Instagram Reels using **machine learning**. This project includes a **custom synthetic dataset**, full **feature engineering**, and a **scikit-learn pipeline** for classification into **Normal, Addicted, and Severely Addicted** categories.

---

## 💡 Project Overview

- **Goal:** Predict Reels addiction level based on user behavior.  
- **Problem Type:** Multi-class classification  
- **Target Audience:** Gen-Z social media users  
- **Tools & Libraries:** Python, Pandas, NumPy, Scikit-learn  

---

## 🛠️ What Makes This Project Unique

- **Custom Dataset:** Created from scratch to simulate user behavior:
  - Reels watched per day  
  - Average session minutes  
  - Sleep hours  
  - Attention span  
  - Mood after watching Reels  
  - Breaks taken  
  - Phone pickups  

- **Feature Engineering:** Handles numerical, ordinal, and categorical features.  
- **ML Pipeline:** Implemented a **scikit-learn pipeline** combining preprocessing and **Logistic Regression**.  
- **Evaluation:** Precision, Recall, F1-score, and Accuracy metrics.

---

## 📝 Dataset Details

| Feature             | Type         | Description |
|--------------------|--------------|-------------|
| reels_per_day       | Numerical    | Number of Reels watched per day |
| avg_session_minutes | Numerical    | Average minutes per session |
| night_sleep         | Numerical    | Nightly sleep hours |
| attention_span      | Ordinal      | low / medium / high |
| mood_after_reels    | Categorical | happy / neutral / sad |
| breaks_taken        | Ordinal      | rare / sometimes / frequent |
| phone_pickups       | Numerical    | Number of phone pickups |
| addiction_level     | Target       | 0: Normal, 1: Addicted, 2: Severely Addicted |

> ⚠️ **Note:** Dataset is synthetic and created for educational purposes.

---
cd Reels_Addiction_Predictor

