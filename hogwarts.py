import streamlit as st

# App Header
st.title("🧙‍♂️ Sorting Hat Quiz App")
st.write("Answer the questions below to find out where you belong!")

# Initialize house scores using Streamlit's session_state 
# (session_state remembers scores as the user clicks buttons)
if "gryffindor" not in st.session_state:
    st.session_state.gryffindor = 0
    st.session_state.slytherin = 0
    st.session_state.hufflepuff = 0
    st.session_state.ravenclaw = 0

# --- Question 1 ---
st.subheader("Q1) Do you like dawn or dusk?")
q1_choice = st.radio(
    "Select your option:", 
    ("1. Dawn", "2. Dusk"), 
    index=None, 
    key="q1"
)

if q1_choice == "1. Dawn":
    st.session_state.gryffindor += 1
    st.session_state.ravenclaw += 1
    st.session_state.slytherin += 2
    st.session_state.hufflepuff += 2
elif q1_choice == "2. Dusk":
    st.session_state.gryffindor += 2
    st.session_state.ravenclaw += 2
    st.session_state.slytherin += 1
    st.session_state.hufflepuff += 1

st.divider()

# --- Question 2 ---
st.subheader("Q2) When I'm dead, I want people to remember me as:")
q2_choice = st.radio(
    "Select your option:",
    ("1. The Good", "2. The Great", "3. The Wise", "4. The Bold"),
    index=None,
    key="q2"
)

if q2_choice == "1. The Good":
    st.session_state.hufflepuff += 2
elif q2_choice == "2. The Great":
    st.session_state.slytherin += 2
elif q2_choice == "3. The Wise":
    st.session_state.ravenclaw += 2
elif q2_choice == "4. The Bold":
    st.session_state.gryffindor += 2

st.divider()

# --- Question 3 ---
st.subheader("Q3) Which kind of instrument most pleases your ear?")
q3_choice = st.radio(
    "Select your option:",
    ("1. The violin", "2. The trumpet", "3. The piano", "4. The drum"),
    index=None,
    key="q3"
)

if q3_choice == "1. The violin":
    st.session_state.slytherin += 4
elif q3_choice == "2. The trumpet":
    st.session_state.hufflepuff += 4
elif q3_choice == "3. The piano":
    st.session_state.ravenclaw += 4
elif q3_choice == "4. The drum":
    st.session_state.gryffindor += 4

st.divider()

# --- Live Scoreboard Display ---
st.header("🏆 Live House Scores")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Gryffindor", st.session_state.gryffindor)
col2.metric("Ravenclaw", st.session_state.ravenclaw)
col3.metric("Hufflepuff", st.session_state.hufflepuff)
col4.metric("Slytherin", st.session_state.slytherin)