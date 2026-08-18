import streamlit as st
st.title("Hello teman-teman 👋")
st.markdown(
    """ 
    hitung BMI mu disini dan ketahuilah berat idealmu
    """
)
nama = st.text_input("masukkan nama anda : ")
berat_badan = st.number_input("masukkan berat badan anda : ",min_value=1)
tinggi_badan = st.number_input("masukkan tinggi badan anda (cm) : ",min_value=1)
st.write ("nama anda : ",nama)
st.write ("berat badan anda : ",berat_badan)
st.write ("tinggi badan anda : ",tinggi_badan)
BMI = berat_badan / (tinggi_badan/100)**2
st.write ("body mass index anda : ",BMI)
if BMI < 17:
    st.error("Keterangan: Underweight (Kekurangan berat badan)")
elif BMI <= 25:
    st.success("Keterangan: Ideal (Normal)")
else:
    st.warning("Keterangan: Overweight (Kelebihan berat badan)")
