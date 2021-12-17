import streamlit as st 
import pickle 
import numpy as np
import webbrowser

def load_model():
    with open("crop-predict.plk", 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

LogisticRegression_loaded = data["model"]
Nitrogen = data['N']
Phosphorus = data['P']
Potassium = data['K']
Temperature = data['temperature']
Ph = data['ph']
Humidity = data['humidity']
Rainfall = data['rainfall']

def show_predict_page():
    from PIL import Image
    img = Image.open("header_sp.jpg")

    st.image(img)
    # st.write("[![Star](<https://img.shields.io/github/stars/><username>/<repo>.svg?logo=github&style=social)](https://github.com/vikramnegiofficial/TSF-Web-Development.github.io)")
    st.title("Empowering Rural Women: Our Greatest Tool For Development")
    

    st.write("### We need some information to predict the salary")

    nitrogen = st.number_input("Nitrogen in your soil ")
    phosphorus = st.number_input("Phosphorus in your soil")
    potassium = st.number_input("Potassium in your soil")
    temperature = st.slider("Average temperature in your area (in celcius)", -10, 50, 5)
    humidity = st.number_input("Average humidity in your area")
    ph = st.slider("Ph of your soil", 0, 14, 1)
    rainfall = st.number_input("Average rainfall in your area(in mm)")
    
    ok = st.button("Submit")
    if ok:
        X = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        X = X.astype(float)

        prediction = LogisticRegression_loaded.predict(X)
        def ltos(s):
            str1=" "
            return (str1.join(s))
        st.subheader(f"Best crop as per given data is {ltos(prediction)}")

        url = "https://github.com/vikramnegiofficial/Our-Women-Farmers"

        git = st.button("Github link")
        if git:
            webbrowser.open_new_tab(git)

