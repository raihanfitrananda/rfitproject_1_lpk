import streamlit as st

st.title(" Hi, User Welcome to Rfitproject")
st.write(
    "Let's start building! For help and inspiration, head over to [Rfit.Instagram](https://www.instagram.com/rfitran_/#)."
)
def tambah(x, y): return x + y
def kurang(x, y): return x - y
def kali(x, y):   return x * y
def bagi(x, y):   
    if y == 0: return "Error! Bagi dengan nol gak bisa."
    return x / y

while True:
    print("\n=== KALKULATOR SIMPEL ===")
    print("1. Tambah (+)\n2. Kurang (-)\n3. Kali (*)\n4. Bagi (/)\n5. Keluar")
    
    pilihan = input("Pilih operasi (1/2/3/4/5): ")
    
    if pilihan == '5':
        print("Terima kasih! Sampai jumpa.")
        break
        
    if pilihan in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input harus berupa angka ya!")
            continue

        if pilihan == '1':   print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2': print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3': print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4': print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
    else:
        print("Pilihan gak valid, silakan coba lagi.")
