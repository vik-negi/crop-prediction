import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import ipywidgets
from ipywidgets import interact

import matplotlib.pyplot as plt
from PIL import Image



def show_explore_page():
    
    img = Image.open("rural-women-in-India.jpg")
    st.image(img)
    st.write("A study conducted on the status of women farmers in Uttar Pradesh shows that only 6% of women own land, less than 1% have participated in government training programs, 4% have access to institutional credit and only 8% have control over agricultural income.")
    st.write("“A day’s farm work pays about Rs 250 but women earn even less, sometimes around Rs 100,” said Kranti Azad, 27, a farmer from Devlaha village in Ayodhya, 135 km east of Lucknow. “But now that those who work in the cities are back, women’s daily earnings are almost down to Rs 50.” Like Azad, millions of women for whom agriculture is the only source of income in rural India are now struggling with diminished savings and lost livelihood opportunities.")


    st.subheader("Various Crop in India")
    img_2 = Image.open("key-crop-yields.png")
    st.image(img_2)
    img_3 = Image.open("image1170x530cropped.jpg")
    st.image(img_3)
    # st.title("Explore the data")
   
