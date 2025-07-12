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

st.markdown("---")

# Store answers in session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False

user_answers = []

for i, q in enumerate(questions):
    st.subheader(f"Soalan {i+1}")
    answer = st.radio(q["question"], q["options"], key=f"q{i}")
    user_answers.append((answer, q["answer"]))

# Submit button
if st.button("Hantar Jawapan"):
    score = 0
    for user_answer, correct_answer in user_answers:
        if user_answer == correct_answer:
            score += 1
    st.session_state.score = score
    st.session_state.submitted = True

# Final result display
if st.session_state.submitted:
    st.success(f"🎉 Anda telah menjawab dengan betul sebanyak **{st.session_state.score} / {len(questions)}** soalan!")
    if st.session_state.score == len(questions):
        st.balloons()
    st.markdown("---")
    st.markdown("👍 Tahniah! Klik butang **Muat Semula** untuk menjawab semula.")
