import streamlit as st
import os

# --- SETTINGS ---
# Yahan apna pasandida password rakhein
MY_PASSWORD = "somsahu"
PHOTO_FOLDER = "photos"

st.set_page_config(page_title="My Secret Gallery", page_icon="🔒")

# --- LOGIN LOGIC ---
if "login_status" not in st.session_state:
    st.session_state["login_status"] = False

def check_login():
    if st.session_state["pass_input"] == MY_PASSWORD:
        st.session_state["login_status"] = True
    else:
        st.error("Galat Password! Dubara koshish karein.")

# --- UI DISPLAY ---
if not st.session_state["login_status"]:
    st.title("🔒 Private Gallery Access")
    st.text_input("Password Enter Karein:", type="password", key="pass_input")
    st.button("Open Gallery", on_click=check_login)
else:
    st.title("📸 Meri Private Photos")
    st.write("Ye photos sirf aap dekh sakte hain.")
    
    # Photos load karne ka logic
    if os.path.exists(PHOTO_FOLDER):
        all_files = os.listdir(PHOTO_FOLDER)
        # Sirf images filter karna
        images = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        
        if images:
            # 3 columns mein photos dikhayega
            cols = st.columns(3)
            for idx, img_name in enumerate(images):
                with cols[idx % 3]:
                    img_path = os.path.join(PHOTO_FOLDER, img_name)
                    st.image(img_path, use_container_width=True)
        else:
            st.info("Folder mein koi photos nahi mili.")
    
    if st.button("Logout"):
        st.session_state["login_status"] = False
        st.rerun()