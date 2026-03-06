import streamlit as st

# ---------- STYLE ----------
st.markdown("""
<style>

/* Sky blue background */
.stApp {
    background-color: #87CEEB;
}

/* Center title */
h1 {
    text-align: center;
}

/* Button styling */
div.stButton > button {
    font-size: 22px;
    padding: 10px 25px;
    border-radius: 10px;
    background-color: #ff4da6;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ---------- SESSION STATE ----------
if "wrong_clicks" not in st.session_state:
    st.session_state.wrong_clicks = 0

if "correct" not in st.session_state:
    st.session_state.correct = False


# ---------- IF CORRECT ----------
if st.session_state.correct:
    st.title("🎉 Congratulations! You are indeed supercalifragilisticexpialidocious")
    st.stop()


# ---------- TITLE ----------
st.title("Let's see🍓")


# ---------- CENTERED QUESTION ----------
st.markdown(
    "<h2 style='text-align: center;'>What are You?</h2>",
    unsafe_allow_html=True
)


# ---------- CHANGING TEXT ----------
texts = [
    "Not Sure",
    "Maybe Average",
    "Hmmm",
    "Think again",
    "Last chance"
]


# ---------- BUTTONS ----------
col1, col2 = st.columns(2)

with col1:
    if st.button("supercalifragilisticexpialidocious😎"):
        st.session_state.correct = True
        st.rerun()

with col2:
    if st.session_state.wrong_clicks < 5:
        if st.button(texts[st.session_state.wrong_clicks]):
            st.session_state.wrong_clicks += 1
            st.rerun()
    else:
        st.button(texts[-1], disabled=True)
