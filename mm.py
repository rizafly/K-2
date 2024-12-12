import streamlit as st
import numpy as np
import matplotlib as plt
from scipy.integrate import quad
from scipy.misc import derivative

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Matematika Lanjutan", layout="wide")
st.title("Kalkulator Matematika Lanjutan")

# Tab navigasi
menu = ["Kalkulator Integral", "Turunan", "Matriks", "Visualisasi Grafik"]
choice = st.sidebar.selectbox("Pilih fitur", menu)

# 1. Kalkulator Integral
if choice == "Kalkulator Integral":
    st.header("Kalkulator Integral")
    expr = st.text_input("Masukkan ekspresi (contoh: x**2 + 3*x + 2)")
    variable = st.text_input("Variabel yang diintegralkan (contoh: x)")
    lower_limit = st.text_input("Batas bawah (opsional, kosongkan untuk integral tak tentu)")
    upper_limit = st.text_input("Batas atas (opsional, kosongkan untuk integral tak tentu)")

    if st.button("Hitung Integral"):
        try:
            # Definisikan fungsi untuk diintegralkan
            def func(x):
                return eval(expr)

            # Hitung integral
            if lower_limit and upper_limit:
                result, _ = quad(func, float(lower_limit), float(upper_limit))
            else:
                result, _ = quad(func, -np.inf, np.inf)  # Integral tak tentu
            st.success(f"Hasil: {result}")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

# 2. Kalkulator Turunan
elif choice == "Turunan":
    st.header("Kalkulator Turunan")
    expr = st.text_input("Masukkan ekspresi (contoh: sin(x) + x**2)")
    variable = st.text_input("Variabel yang diturunkan (contoh: x)")
    order = st.number_input("Order turunan (contoh: 1 untuk turunan pertama)", min_value=1, step=1)

    if st.button("Hitung Turunan"):
        try:
            # Definisikan fungsi untuk dihitung turunan
            def func(x):
                return eval(expr)

            # Hitung turunan
            result = derivative(func, 0, dx=1e-6, n=order)
            st.success(f"Hasil: {result}")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

# 3. Operasi Matriks
elif choice == "Matriks":
    st.header("Operasi Matriks")
    st.write("Masukkan matriks dalam format Python. Contoh: [[1, 2], [3, 4]]")

    matrix_a = st.text_area("Matriks A")
    matrix_b = st.text_area("Matriks B (opsional untuk operasi dua matriks)")
    operation = st.selectbox("Pilih operasi", ["Determinan", "Invers", "Penjumlahan", "Perkalian"])

    if st.button("Hitung Operasi Matriks"):
        try:
            A = np.matrix(eval(matrix_a))
            if operation == "Determinan":
                result = np.linalg.det(A)
            elif operation == "Invers":
                result = np.linalg.inv(A)
            elif operation == "Penjumlahan":
                B = np.matrix(eval(matrix_b))
                result = A + B
            elif operation == "Perkalian":
                B = np.matrix(eval(matrix_b))
                result = A @ B
            st.success(f"Hasil: \n{result}")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

# 4. Visualisasi Grafik
elif choice == "Visualisasi Grafik":
    st.header("Visualisasi Grafik")
    expr = st.text_input("Masukkan ekspresi fungsi (contoh: x**2 - 4*x + 3)")
    variable = st.text_input("Variabel independen (contoh: x)", value="x")
    x_min = st.number_input("Nilai minimum x", value=-10)
    x_max = st.number_input("Nilai maksimum x", value=10)

    if st.button("Tampilkan Grafik"):
        try:
            # Definisikan fungsi untuk plot
            def func(x):
                return eval(expr)

            x_vals = np.linspace(x_min, x_max, 500)
            y_vals = func(x_vals)

            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, label=f"f({variable}) = {expr}")
            ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
            ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
            ax.legend()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
