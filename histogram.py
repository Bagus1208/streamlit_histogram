import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

st.set_page_config(
    page_title='Histogram', 
    layout='wide', 
    page_icon=':bar_chart:',
)
st.markdown("<h1 style='text-align: center;'>Selamat Datang di Website Kelompok 4 R8P</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Pengolahan Citra Tentang Histogram</h1>", unsafe_allow_html=True)

st.divider(width='stretch')
st.markdown(
    '''
    ##### Website ini akan memberikan informasi rentang warna grayscale dan RGB dalam bentuk histogram 📊
    '''
)

st.text('')
uploaded_file = st.file_uploader('**Pilih file gambar**', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.markdown("<h3 style='text-align: center;'>Histogram Rentang Warna Gambar Grayscalse dan RGB</h3>", unsafe_allow_html=True)
    image_file = Image.open(uploaded_file)
    image_array = np.array(image_file)
    grayscale_image = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    rgb_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)

    image = np.array(image_array)
    total_pixels = image.shape[0] * image.shape[1]

    histogram, bins = np.histogram(image.flatten(), 256, [0, 256])

    normalization = st.toggle('Normalisasi')

    if normalization:
        histogram = histogram / total_pixels

    channels = {
        'Merah': rgb_image[:, :, 0],
        'Hijau': rgb_image[:, :, 1],
        'Biru': rgb_image[:, :, 2]
    }

    histograms = {}
    for color, channel in channels.items():
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        if normalization:
            histograms[color] = hist / total_pixels
        else:
            histograms[color] = hist

    column1, column2 = st.columns([0.5, 0.5])
    column3, column4 = st.columns([0.5, 0.5])

    with st.container(border=True):
        with column1:
            st.image(grayscale_image, width=500, use_container_width=False)

        with column2:
            st.bar_chart(histogram, color='#808080', height=500)

    st.write('')

    with st.container(border=True):
        with column3:
            st.image(rgb_image, width=500, channels='BGR', use_container_width=False)

        with column4:
            st.markdown("<h5 style='text-align: center;'>Merah</h5>", unsafe_allow_html=True)
            st.bar_chart(histograms['Merah'], color='#FF0000', height=500)
            st.write('Hijau')
            st.bar_chart(histograms['Hijau'], color='#00FF00', height=500)
            st.write('Biru')
            st.bar_chart(histograms['Biru'], color='#0000FF', height=500)



    # with column1:
    #     container1.image(grayscale_image, width=300, use_container_width=False)
    #     st.write('')
    #     st.image(rgb_image, width=500, channels='BGR', use_container_width=False)

    # with column2:
    #     container1.bar_chart(histogram)

    #     channels = {
    #         'Merah': rgb_image[:, :, 0],
    #         'Hijau': rgb_image[:, :, 1],
    #         'Biru': rgb_image[:, :, 2]
    #     }

    #     histograms = {}
    #     for color, channel in channels.items():
    #         hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    #         histograms[color] = hist / total_pixels
        
    #     st.bar_chart(histograms['Merah'], height=500)
    #     st.bar_chart(histograms['Hijau'], height=500)
    #     st.bar_chart(histograms['Biru'], height=500)