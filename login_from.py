import streamlit as st
#header
st.header("Student Records Management")
#title
st.title("Welcome to the Student Management System")
#subheader
st.subheader("Manage student records efficiently and effectively.")
#horizontal line
st.markdown("--------------------------------------------------------------------")
#text
st.text("Hello!")
#write
st.write({"Name": "k.sri kedharnath","Section":"DS-E"})
st.write(123)
#markdown font styles
st.markdown("**Sports**")
st.markdown("*select any option*")
st.markdown("* Cricket\n* Basket Ball")
st.code("""""
        def add(a, b):
        return a+b
        """, language = "python"
        )
st.latex(r'''
a^2 + b^2 = c^2
'''         )
st.divider()
st.write("end of the section")
if st.button("Click me"):
    st.write("button clicked")
    st.success("operation succesful!")
    st.balloons()
else:
    st.write("Button not clicked yet.")
    st.error("Connection error!")
#text input method to get user input
name = st.text_input("Enter your name:")
if name == "":
    st.warning("Name cannot be empty")
elif not name.isalpha():
    st.error("Inavlid input please enter only alphabets")
else:
    st.success(f"Hello , {name}!")

feedback = st.text_area("Enter feedback:")
st.write (feedback)

if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing")

gender = st.radio("Select gender",("male","Female","Other"))
st.write(f"You selected: {gender}")

#selectbox method to create a dropdown
country = st.selectbox("Select your country:",("India","USA","IRELAND","GERMANY"))
st.write(f"you selected country:{country}")

#multiselect
skills = st.multiselect("Select skills", ["Python","SQL","ML"])
st.write("Skills:", skills)

#slider
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

#file_uploader()
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.success("File upload successfully")
    st.write(f"Filename: {uploaded_file.name}")

#form
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 100)
    submit = st.form_submit_button("Submit")

if submit:
    st.write(name, age)

st.divider()

#columns method to create columns
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Colunmn 1")
    st.write("This is column1")
with col2:
    st.header("Colunmn 2")
    st.write("This is column2")
with col3:
    st.header("Colunmn 3")
    st.write("This is column3")
st.divider()

# container
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)    
st.divider()

st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")

