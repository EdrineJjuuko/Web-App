import streamlit as st
import web_functions

milestones = web_functions.get_milestones()

def add_milestone():
    new_milestone = st.session_state["milestone"] + "\n"
    milestones.append(new_milestone)
    web_functions.write_milestone(milestones)


st.title("My Golfing Journey")
st.subheader("Milestones")
st.write("Unwavering Commitment")
for index, milestone in enumerate(milestones):
    checkbox = st.checkbox(milestone, key=milestone)
    if checkbox:
        milestones.pop(index)
        web_functions.write_milestone(milestones)
        del st.session_state[milestone]
        st.rerun()

st.text_input(label="", placeholder="Add new milestone....", on_change=add_milestone, key="milestone")

