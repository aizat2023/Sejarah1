import streamlit as st
import random
import pandas as pd

# Load or create leaderboard
LEADERBOARD_FILE = "leaderboard.csv"
try:
    leaderboard = pd.read_csv(LEADERBOARD_FILE)
except:
    leaderboard = pd.DataFrame(columns=["Nama", "Skor", "Tahap"])

# App Config
st.set_page_config(page_title="Kuiz Sejarah", page_icon="📘")
st.title("🎮 Kuiz Gamifikasi: Zaman Prasejarah")

# Get student name
student_name = st.text_input("Masukkan nama anda:")

# Choose difficulty
difficulty = st.selectbox("Pilih Tahap:", ["Mudah (3 soalan)", "Biasa (5 soalan)", "Cabaran (10 soalan)"])
question_count = {"Mudah (3 soalan)": 3, "Biasa (5 soalan)": 5, "Cabaran (10 soalan)": 10}[difficulty]

# Questions
all_questions = [
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
    },
    {
        "question": "Zaman Paleolitik menggunakan alat daripada...",
        "options": ["Plastik", "Logam", "Batu kasar", "Tembaga"],
        "answer": "Batu kasar"
    },
    {
        "question": "Zaman Neolitik bermula sekitar tahun...",
        "options": ["5000 SM", "2000 M", "800 SM", "2020 M"],
        "answer": "5000 SM"
    },
    {
        "question": "Zaman Logam dikenali kerana...",
        "options": ["Penggunaan emas", "Penggunaan gangsa dan besi", "Penggunaan duit", "Penggunaan plastik"],
        "answer": "Penggunaan gangsa dan besi"
    },
    {
        "question": "Manusia Mesolitik hidup berhampiran...",
        "options": ["Padang pasir", "Gurun", "Gua dan sungai", "Bangunan moden"],
        "answer": "Gua dan sungai"
    },
    {
        "question": "Apakah jenis kepercayaan Zaman Neolitik?",
        "options": ["Ateis", "Animisme", "Sains", "Rasionalisme"],
        "answer": "Animisme"
    }
]

random.shuffle(all_questions)
quiz_questions = all_questions[:question_count]

user_answers = []
if student_name:
    for i, q in enumerate(quiz_questions):
        st.subheader(f"Soalan {i+1}")
        answer = st.radio(q["question"], q["options"], key=f"q{i}")
        user_answers.append((answer, q["answer"]))

    if st.button("🎯 Hantar Jawapan"):
        score = sum(1 for ans, correct in user_answers if ans == correct)
        st.success(f"✅ {student_name}, anda betul {score} daripada {question_count} soalan.")

        # Gamified feedback
        if score == question_count:
            st.balloons()
            st.success("🏅 Anda Seorang Ahli Sejarah Hebat!")
        elif score >= question_count * 0.7:
            st.info("👏 Anda Sejarawan Muda!")
        elif score >= question_count * 0.4:
            st.warning("👍 Anda Penjelajah Zaman. Teruskan usaha!")
        else:
            st.error("💡 Anda boleh buat lebih baik. Cuba lagi!")

        # 🔐 Bonus question if perfect score
        if score == question_count:
            st.subheader("🔥 Soalan Bonus!")
            bonus_q = {
                "question": "Siapakah pengasas Kesultanan Melayu Melaka?",
                "options": ["Parameswara", "Hang Tuah", "Sultan Mahmud", "Raja Chulan"],
                "answer": "Parameswara"
            }
            bonus_ans = st.radio(bonus_q["question"], bonus_q["options"], key="bonus")
            if st.button("Hantar Bonus"):
                if bonus_ans == bonus_q["answer"]:
                    st.success("🎉 Betul! Anda layak ke Hall of Fame!")
                    score += 1

        # 🧠 Random fact
        facts = [
            "Fakta: Zaman Logam bermula sekitar 1500 SM!",
            "Tahukah anda? Parameswara berasal dari Palembang.",
            "Fakta: Tamadun awal seperti Mesopotamia wujud 5000 tahun dahulu!",
            "Fakta: Manusia Paleolitik menggunakan alat batu tanpa pemprosesan halus."
        ]
        st.markdown("---")
        st.info(random.choice(facts))

        # 📝 Reflection
        st.markdown("### ✍️ Refleksi")
        st.text_area("Apa yang anda pelajari daripada kuiz ini?")

        # 🏆 Save to leaderboard
        new_row = {"Nama": student_name, "Skor": score, "Tahap": difficulty}
        leaderboard.loc[len(leaderboard)] = new_row
        leaderboard.to_csv(LEADERBOARD_FILE, index=False)

        # Show leaderboard
        st.markdown("---")
        st.markdown("## 🏆 Leaderboard (Top 5)")
        top_scores = leaderboard.sort_values(by="Skor", ascending=False).head(5)
        st.dataframe(top_scores)
else:
    st.info("📝 Sila masukkan nama anda untuk memulakan kuiz.")
