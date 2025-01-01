import streamlit as st
from profiles import create_profile,get_notes, get_profile
from form_submit import update_personal_info, add_note,delete_note
from fitness import get_macros

st.markdown("""
<style>
            .stForm {
            backgroung-color: LightBlue;}
            </style>
"""
          , unsafe_allow_html=True  )

st.title("AI powered Fitness tool")


@st.fragment()
def  health_form():
    with st.form("personal_data"):
        st.header("Personal data")
        profile = st.session_state.profile

        name = st.text_input("name",value=profile["general"].get("name", ""))
        age=st.number_input("Age",min_value=1,max_value=120,step=1,value=profile["general"]["age"])
        weight =  st.number_input("weight(lbs)",min_value=10,max_value=500,step=1,value=profile["general"]["weight"])
        height= st.number_input("Hieght(cm)",min_value=0.0,max_value=250.0,step=0.1,value=float(profile["general"]["height"]))
        genders = ['Male','Female','other']
        gender=st.radio('gender',genders,genders.index(profile["general"].get("gender","Male")))
        activities=(
            "sedentary",
            "lightly Active",
            "Moderately Active",
            "Very Actuve",
            "Super Active",

        )
        activity_level = st.selectbox("activity Level",activities,index=activities.index(profile["general"].get("activity_level","Sedentary")))

        personal_data_submit = st.form_submit_button("save")
        if personal_data_submit:
            if all([name,age,weight,height,gender,activity_level]):
                with st.spinner():
                    update_personal_info(profile,"general",name=name,weight=weight,height=height, age=age,gender=gender,activity_level=activity_level)
                    st.success("Information saved")

            else:
                st.warning("Please fill all information!")


@st.fragment()
def macros():
    st.subheader('Ask AI')
    user_question = st.text_input("Ask AI a question: ")
    if st.button("Ask AI"):
        with st.spinner():
            result = get_macros(st.session_state.profile, user_question)
            st.write(result)
    






def forms():
    if "profile" not in st.session_state:
        profile_id = 1
        profile = get_profile(profile_id)
        if not profile:
            profile_id,profile = create_profile(profile_id)

        st.session_state.profile = profile
        st.session_state.profile_id = profile_id

    if "notes" not in st.session_state:
        st.session_state.notes = get_notes(st.session_state.profile_id)


         
    health_form()
    
    macros()


if __name__ == "__main__":
    forms()


