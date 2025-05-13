# 🩺 Heart Sound Analysis using AI and Signal Processing

A machine learning-powered application that analyzes heartbeat audio recordings and classifies them as **Normal** or **Abnormal**. Built for real-time cardiac screening using acoustic data.

## 🚀 Project Highlights

- 🎯 Achieved **90.43% accuracy** using a **Random Forest classifier**
- 🎵 Extracted **MFCC features** from raw heartbeat audio using **Librosa**
- 📊 Trained on real patient data from **PhysioNet’s PCG Dataset**
- 🌐 Deployed using **Streamlit** on **Hugging Face Spaces** for public access


## 🛠 Tech Stack

- **Python**  
- **Scikit-learn**  
- **Librosa**  
- **Streamlit**  
- **Joblib**  
- **Hugging Face Spaces**


## 📁 Project Structure

```
smart-stethoscope-ai/
│
├── app.py # Streamlit app
├── smart_stethoscope_rf_model.pkl # Trained Random Forest model
├── requirements.txt # Dependencies
└── README.md # Project documentation
```

## 📊 Model Training

- Extracted **MFCC (Mel-Frequency Cepstral Coefficients)** from `.wav` files  
- Used **Random Forest Classifier** for final deployment  
- Evaluated performance using **accuracy, precision, recall, F1-score**


## 🖥️ Deployment

The app is live and accessible via **Hugging Face Spaces**:

👉 [Click here to try the app](https://sanghavai2724-smart-stethoscope-ai.hf.space/)  


## 💡 Future Improvements

- Add support for spectrogram visualizations  
- Integrate real-time stethoscope input from hardware  
- Expand classification to include murmurs, extra sounds, and more  


## 🧠 Author

**Sanghavai M L**  
AI & ML Enthusiast | Biomedical Engineering | [LinkedIn](www.linkedin.com/in/sanghavai-ml) 


## 📄 License

This project is open-source under the [MIT License](LICENSE).
