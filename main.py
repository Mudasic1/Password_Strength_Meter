import re
import streamlit as st

st.set_page_config(page_icon="🔒", page_title="Password Strength Generator", layout="centered")

background_image_url = "https://img.freepik.com/free-vector/stream-binary-code-design-vector_53876-161363.jpg"

st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
            backdrop-filter: blur(10px);
        }}
        
        .blur-layer {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            backdrop-filter: blur(6px);
            background: rgba(0, 0, 0, 0.3);
            z-index: -1;
        }}

        
        h1 {{
            color: #4ffc !important; 
            text-align: center;
        }}

        
        p {{
            color: #FFD700 !important;  
            text-align: center;
        }}

       
        .created-by {{
            background-color: #44cc;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            display: flex;
            align-items: center;
            position: fixed;
            bottom: 20px;
            left: 20px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
            z-index: 999;
        }}
        .created-by span {{
            margin-left: 8px;
        }}
    </style>
    <div class="blur-layer"></div>
    """,
    unsafe_allow_html=True
)

# Page Title
st.title("🔐 Password Strength Generator")  
st.write("Enter your password below to check its security level. 🔎")  


st.markdown(
    '<div class="created-by">🤘<span>Created by M Mudasir Chandio</span></div>',
    unsafe_allow_html=True
)

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9).**")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Display Password Strength Results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Feedback
    if feedback:
        with st.expander("🔎 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong.")

# Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")  
