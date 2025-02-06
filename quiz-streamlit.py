import json
import random
import streamlit as st

# Load questions from JSON file
with open("bahasa_melayu_notes.json", "r") as file:
    questions = json.load(file)

# Shuffle questions only once per session
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))

# Streamlit app
def main():
    st.set_page_config(page_title="Fill in the Blanks Quiz", layout="centered")

    # Custom CSS to center content
    st.markdown(
        """
        <style>
        .stApp {
            max-width: 800px;
            margin: auto;
            text-align: center;
        }
        .stButton button {
            width: 150px;
            margin: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Fill in the Blanks Quiz")
    st.write("Test your knowledge by filling in the blanks!")

    total_questions = len(st.session_state.shuffled_questions)

    # Initialize page number if not in session state
    if "page" not in st.session_state:
        st.session_state.page = 0

    # Get current question from shuffled list
    question_data = st.session_state.shuffled_questions[st.session_state.page]
    st.write(f"**Question {st.session_state.page + 1} of {total_questions}**")
    st.write(f"**{question_data['question']}**")

    # User input
    user_answer = st.text_input("Your answer:", key=f"q{st.session_state.page}")

    # Buttons for navigation and answer checking
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.session_state.page > 0:
            if st.button("Previous Question"):
                st.session_state.page -= 1
                st.rerun()
    with col2:
        if st.button("Submit Answer"):
            if user_answer.strip().lower() == question_data["answer"].lower():
                st.success("Correct! 🎉")
            else:
                st.error(f"Incorrect. The correct answer is: **{question_data['answer']}**")
    with col3:
        if st.button("Show Answer"):
            st.info(f"The correct answer is: **{question_data['answer']}**")

    # Next Question button
    if st.session_state.page < total_questions - 1:
        if st.button("Next Question"):
            st.session_state.page += 1
            st.rerun()

if __name__ == "__main__":
    main()
