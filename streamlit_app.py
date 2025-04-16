import streamlit as st

st.title('Сервер')
st.write('На данном сервере находяться все необходимые файлы.')
st.download_button('Скачать', data='/storage/orig.jpg')