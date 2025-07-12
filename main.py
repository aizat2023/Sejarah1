import streamlit as st

st.title("📘 Kuiz Sejarah Tingkatan 1: Zaman Prasejarah")

questions = [
    {
        "question": "Apakah ciri kehidupan manusia Zaman Paleolitik?",
        "options": ["Menetap di rumah panjang", "Bercucuk tanam", "Hidup secara nomad", "Membina empayar"],
        "answer": "Hidup secara nomad"
    },
    {
        "question": "Zaman Neolitik terkenal dengan...",
        "options": ["Penggunaan besi", "Kehidupan berburu", "Aktiviti pertanian dan menternak", "Tiada teknologi"],
        "answer": "Aktiviti pertanian dan menternak"
    },
    {
        "question": "Apakah alat utama yang digunakan pada Zaman Logam?",
        "options": ["Batu kasar", "Alat gangsa dan besi", "Kayu runcing", "Alat tulang"],
        "answer": "Alat gangsa dan besi"
    },
    {
        "question": "Manusia Zaman Mesolitik biasanya tinggal di mana?",
        "options": ["Gua batu kapur", "Kawasan pertanian", "Istana", "Kapal layar"],
        "answer": "Gua batu kapur"
    },
    {
        "question": "Antara berikut, yang manakah bukan sebahagian dari zaman prasejarah?",
        "options": ["Zaman Logam", "Zaman Neolitik", "Zaman Mesolitik", "Zaman Angkasa"],
        "answer": "Zaman Angkasa"
    }
]

score = 0
st.markdown("---")

for i, q in enumerate(questions):
    st.subheader(f"Soalan {i+1}")
    answer = st.radio(q["question"], q["options"], key=i)
    if st.button(f"Sahkan Jawapan {i+1}", key=f"btn_{i}"):
        if answer == q["answer"]:
            st.success("✅ Betul!")
        else:
            st.error(f"❌ Salah! Jawapan sebenar: {q['answer']}")

st.markdown("---")
st.write("Selesai! Klik semula untuk semak semula atau muat semula untuk mula semula.")
