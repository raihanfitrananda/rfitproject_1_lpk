import streamlit as st

st.title(" Hi, User Welcome to Rfitproject")
st.write(
    "Let's start building! For help and inspiration, head over to [Rfit.Instagram](https://www.instagram.com/rfitran_/#)."
)
# Program Monitoring Tekanan Gas Pada Instrumen GC
# Kelompok 12

print("=== SISTEM MONITORING TEKANAN GAS ===")
print("Instruksi: Masukkan nilai tekanan (Psi).")
print("Batas Aman: < 200 Psi | Batas Bahaya: > 250 Psi\n")

pemeriksaan = 1
total_target = 5  # Kita akan melakukan 5 kali pengukuran sampel

while pemeriksaan <= total_target:
    try:
        # Input tekanan dari sensor
        tekanan = float(input(f"[{pemeriksaan}/{total_target}] Masukkan tekanan saat ini: "))
        
        # Logika Break: Jika tekanan melonjak di atas 250 Psi
        if tekanan>250 :
            print(f"\n>> STATUS: BAHAYA! (Tekanan: {tekanan} Psi)")
            print(">> Emergency Break diaktifkan. Sistem berhenti otomatis.")
            break
        elif tekanan <200 :
            print ("Gas Terjadi Kebocoran!")
            print(">> Emergency Break diaktifkan. Sistem berhenti otomatis.")
            break
            
        print(f"Status: Normal ({tekanan} Psi)\n")
        pemeriksaan += 1
except ValueError:
        print("Input tidak valid! Masukkan angka saja.")

# Logika Else: Berjalan jika loop selesai tanpa terkena 'break'
else:
    print("\n" + "="*35)
    print("LAPORAN: GAS STABIL")
    print("Pengukuran Sampel Dapat dilakukan .")
    print("="*35)

print("\n--- Program Selesai ---")
