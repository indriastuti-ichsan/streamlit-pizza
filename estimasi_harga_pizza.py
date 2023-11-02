import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_pizza.sav','rb'))

st.title('Estimasi Harga Pizza')
diameter = st.number_input ("Masukkan Diameter Pizza", 0)
n_topping = st.radio("Masukkan Jumlah Topping ",
    ["0", "1", "2"])

predict = ''

if st.button('Hitung Estimasi Harga'):
    predict = model.predict(
        [[diameter, n_topping]]
    )
    st.write ('Estimasi Harga Pizza = ',predict)
