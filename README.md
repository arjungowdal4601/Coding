# Health Insurance Cost Predictor 🚑💰

Welcome to the **Health Insurance Cost Predictor** project! This repository contains a machine learning application that predicts health insurance costs based on user inputs. The project features a pre-trained model, a custom preprocessing pipeline, and a sleek Streamlit interface for a seamless user experience. 🎉

---

## 📂 Project Structure

```
your_project/
├── artifact/
│   ├── insurance_premium_model.joblib   # Pre-trained model artifact 🤖
│   ├── scaler.joblib                     # Fitted MinMaxScaler 🚀
├── model.py                              # Preprocessing & prediction functions 📊
├── app.py                                # Streamlit UI for user interaction 🖥️
├── README.md                             # This file 📖
└── requirements.txt                      # Project dependencies 📦
```

---

## ✨ Features

- **User-Friendly Interface:**  
  Enter your details and get real-time predictions with an intuitive UI.

- **Custom Preprocessing:**  
  Includes feature engineering, scaling (with MinMaxScaler), and a normalized risk score computation.

- **Robust Prediction Model:**  
  A machine learning model built using scikit-learn for accurate predictions.

- **Easy to Deploy:**  
  Run the application locally with a single command using Streamlit.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+**
- Install the required packages using `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```
  
  Or install them manually:
  ```bash
  pip install streamlit joblib pandas scikit-learn
  ```

### Running the Application

1. **Ensure Artifacts are Ready:**  
   Verify that the `artifact/` folder contains:
   - `insurance_premium_model.joblib`
   - `scaler.joblib`

2. **Start the App:**  
   Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

3. **Open in Browser:**  
   Navigate to `http://localhost:8501` to use the predictor.

---

## 🛠️ How It Works

1. **Input Data:**  
   Users provide details such as age, number of dependents, income, genetic risk, and other health-related information via the UI.

2. **Preprocessing:**  
   The input data is scaled using MinMaxScaler and transformed with custom logic, including computing a normalized risk score from medical history.

3. **Prediction:**  
   The processed features are passed to the pre-trained model, which returns a health insurance cost prediction.

4. **Result Display:**  
   The predicted cost is instantly displayed on the UI for easy interpretation.

---

## 🔬 Model Training

If you need to update or re-train the model:

### Adjust the Training Pipeline
Ensure that unnecessary features (e.g., `income_level` if unused) are dropped. Re-run your preprocessing steps, including fitting the MinMaxScaler on the final feature set.

### Save Updated Artifacts
Save your updated model and scaler to the `artifact/` folder:

```python
from joblib import dump

dump(model, "artifact/insurance_premium_model.joblib")
dump({"scaler": scaler, "cols_to_scale": cols_to_scale}, "artifact/scaler.joblib")
```

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request. Please adhere to the existing code style and include clear commit messages.

---

## 🙏 Acknowledgments

- **Streamlit**: For the amazing UI framework.
- **Scikit-Learn**: For robust machine learning tools.
- **Joblib**: For efficient model persistence.
- A big thank you to all contributors and users who provided feedback!
