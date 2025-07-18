import streamlit as st
import numpy as np
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
    st.divider()
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

    column1, column2, column3 = st.columns([1, 1, 1])
    column4, column5, column6 = st.columns([1, 4, 1])
    column7, column8, column9 = st.columns([1, 1, 1])
    column10, column11, column12 = st.columns([1, 1, 1])

    with column2:
        st.markdown("<h5 style='text-align: center;'>Gambar dalam Grayscale</h5>", unsafe_allow_html=True)
        st.image(grayscale_image, width=500, use_container_width=False)
    
    with column5:
        st.markdown("<h5 style='text-align: center;'>Histogram Sebaran Warna Grayscale</h5>", unsafe_allow_html=True)
        st.bar_chart(histogram,  x_label='Rentang Warna Grayscale', y_label='Frekuensi',color='#808080', height=400)

    with column8:
        st.markdown("<h5 style='text-align: center;'>Gambar dalam RGB</h5>", unsafe_allow_html=True)
        st.image(rgb_image, width=500, channels='BGR', use_container_width=False)

    with column10:
        st.markdown("<h5 style='text-align: center;'>Histogram Sebaran Warna Merah</h5>", unsafe_allow_html=True)
        st.bar_chart(histograms['Merah'], x_label='Rentang Warna Merah', y_label='Frekuensi', color='#FF0000', height=300)

    with column11:
        st.markdown("<h5 style='text-align: center;'>Histogram Sebaran Warna Hijau</h5>", unsafe_allow_html=True)
        st.bar_chart(histograms['Hijau'], x_label='Rentang Warna Hijau', y_label='Frekuensi', color='#00FF00', height=300)

    with column12:
        st.markdown("<h5 style='text-align: center;'>Histogram Sebaran Warna Biru</h5>", unsafe_allow_html=True)
        st.bar_chart(histograms['Biru'], x_label='Rentang Warna Biru', y_label='Frekuensi', color='#0000FF', height=300)

    # column1, column2 = st.columns([0.5, 0.5])
    # _, column4 = st.columns([0.5, 0.5])
    # column5, column6 = st.columns([0.5, 0.5])
    # _, column8 = st.columns([0.5, 0.5])

    # with st.container(border=True):
    #     with column1:
    #         st.image(grayscale_image, width=500, use_container_width=False)

    #     with column2:
    #         st.bar_chart(histogram,  x_label='Rentang Warna Grayscale', y_label='Frekuensi',color='#808080', height=500)

    # st.write('')

    # with st.container(border=True):
    #     with column4:
    #         st.markdown("<h5 style='text-align: center;'>Merah</h5>", unsafe_allow_html=True)
    #         st.bar_chart(histograms['Merah'], x_label='Rentang Warna Merah', y_label='Frekuensi', color='#FF0000', height=500)
        
    #     with column5:
    #         st.image(rgb_image, width=500, channels='BGR', use_container_width=False)

    #     with column6:
    #         st.markdown("<h5 style='text-align: center;'>Hijau</h5>", unsafe_allow_html=True)
    #         st.bar_chart(histograms['Hijau'], x_label='Rentang Warna Hijau', y_label='Frekuensi', color='#00FF00', height=500)

    #     with column8:
    #         st.markdown("<h5 style='text-align: center;'>Biru</h5>", unsafe_allow_html=True)
    #         st.bar_chart(histograms['Biru'], x_label='Rentang Warna Biru', y_label='Frekuensi', color='#0000FF', height=500)