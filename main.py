import streamlit as st

st.set_page_config(page_title="Kuiz Sejarah", page_icon="📘")
st.title("🎮 Kuiz Gamifikasi: Zaman Prasejarah")

# ✅ Get student name
student_name = st.text_input("Masukkan nama anda:")

if student_name:
    st.markdown(f"**Selamat datang, {student_name}!** 🎓")

    # Soalan & jawapan
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

    # Session state setup
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    if "score" not in st.session_state:
        st.session_state.score = 0

    user_answers = []

    for i, q in enumerate(questions):
        st.subheader(f"Soalan {i+1}")
        answer = st.radio(q["question"], q["options"], key=f"q{i}")
        user_answers.append((answer, q["answer"]))

    # Submit button
    if st.button("🎯 Hantar Jawapan"):
        score = 0
        for user_answer, correct_answer in user_answers:
            if user_answer == correct_answer:
                score += 1
        st.session_state.score = score
        st.session_state.submitted = True

    # Result
    if st.session_state.submitted:
        score = st.session_state.score
        total = len(questions)
        st.markdown("---")
        st.success(f"✅ {student_name}, anda betul **{score} daripada {total} soalan!**")

        # Badge
        if score == total:
            st.balloons()
            st.success("🏅 **Tahniah! Anda Seorang Ahli Sejarah Hebat!** 🎉")
        elif score >= 4:
            st.info("👏 **Bagus! Anda Sejarawan Muda!**")
        elif score >= 2:
            st.warning("👍 Anda Penjelajah Zaman. Cuba lagi untuk lebih baik.")
        else:
            st.error("💡 Anda boleh buat lebih baik. Cuba lagi!")

        # Retry button
        if st.button("🔁 Cuba Semula"):
            st.session_state.submitted = False
            st.session_state.score = 0
            st.experimental_rerun()

else:
    st.info("📝 Sila masukkan nama anda untuk mula kuiz.")
