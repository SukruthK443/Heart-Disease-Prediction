# Heart Disease Prediction Web App

This is a web application that predicts the likelihood of heart disease based on user input. Using machine learning algorithms, the app provides real-time predictions of heart disease risk. The model was built using a dataset containing medical parameters, and the app is deployed using Streamlit for easy accessibility.

## 📊 Dataset
The model uses a dataset with the following parameters:
- **Age**: Age of the patient
- **Sex**: Gender of the patient (Male/Female)
- **ChestPainType**: Type of chest pain experienced
- **RestingBP**: Resting blood pressure
- **Cholesterol**: Cholesterol level in the blood
- **FastingBS**: Fasting blood sugar (1: true, 0: false)
- **RestingECG**: Resting electrocardiographic results
- **MaxHR**: Maximum heart rate achieved
- **ExerciseAngina**: Exercise-induced angina (Yes/No)
- **Oldpeak**: Depression induced by exercise relative to rest
- **ST_Slope**: Slope of the peak exercise ST segment

## ⚙️ Features

- **Machine Learning Model**: The app uses a Random Forest classifier trained on the dataset to predict the likelihood of heart disease based on the input parameters.
- **User-Friendly Interface**: Built with Streamlit, the app has an interactive interface that allows users to input medical data and receive predictions instantly.
- **Input Validation**: The app handles errors and provides helpful instructions, ensuring smooth user interaction.
- **Real-Time Predictions**: As users input their data, they can see predictions in real-time with a clear risk assessment.

## 🚀 How to Use

1. **Input your information**: Provide details like age, cholesterol levels, heart rate, and other medical parameters.
2. **Get Prediction**: After entering the required data, the model will predict the likelihood of heart disease based on your inputs.
3. **Results**: The prediction will be displayed, with additional information to help users interpret the results.

## 🔧 Technologies Used

- **Python**: Programming language for the model and web app.
- **Streamlit**: Used for creating the interactive web interface.
- **Scikit-learn**: Machine learning library for training and deploying the model.
- **Joblib**: Used for saving and loading the machine learning model.

## 🛠️ Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone [https://github.com/SukruthK443/Heart-Disease-Prediction.git]
    cd Heart-Disease-Prediction
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run Heart_app.py
    ```

4. The app will open in your default web browser, where you can input your medical data and get predictions.

## 🌐 Live Demo

You can try the live version of this app here:  
[Heart Disease Prediction Web App]((https://huggingface.co/spaces/Sukruthk/Heart_Disease_Prediction))

## 💡 Future Improvements

- Implement more machine learning models and compare their performances.
- Add user authentication for saving prediction history.
- Incorporate a feature to upload medical history and generate reports.
- Improve the accuracy of the model using more advanced algorithms.

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.


