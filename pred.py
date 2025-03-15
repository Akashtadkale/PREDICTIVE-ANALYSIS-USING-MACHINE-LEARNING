import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('placement_model.pkl', 'rb'))

# Streamlit UI
st.title("Placement Predictor")

# User Inputs
cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0, step=0.1)
internships = st.number_input("Number of Internships", min_value=0, step=1)
projects = st.number_input("Number of Projects", min_value=0, step=1)
workshops = st.number_input("Number of Workshops/Certifications", min_value=0, step=1)
aptitude_score = st.number_input("Aptitude Test Score (out of 10)", min_value=0.0, max_value=10.0, step=0.1)
soft_skills = st.number_input("Soft Skills Rating (1.0 to 10.0)", min_value=1.0, max_value=10.0, step=0.1)
extracurricular = st.radio("Extracurricular Activities", ("Yes", "No"))
placement_training = st.radio("Placement Training", ("Yes", "No"))
ssc_marks = st.number_input("SSC Marks (out of 100)", min_value=0, max_value=100, step=1)
hsc_marks = st.number_input("HSC Marks (out of 100)", min_value=0, max_value=100, step=1)

# Convert categorical values to numerical
extracurricular = 1 if extracurricular == "Yes" else 0
placement_training = 1 if placement_training == "Yes" else 0

# Prepare input data
user_data = np.array([cgpa, internships, projects, workshops, aptitude_score, 
                      soft_skills, extracurricular, placement_training, ssc_marks, hsc_marks]).reshape(1, -1)

# Prediction Button
if st.button("Check Placement Prediction"):
    try:
        # Predict using the model
        result = model.predict(user_data)

        # Display result
        if result[0] == 0:
            st.error("Negative Review - Placement Unlikely")
        else:
            st.success("Positive Review - Placement Likely")
    
    except Exception as e:
        st.error(f"Error: {e}")