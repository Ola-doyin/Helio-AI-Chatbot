import streamlit as st
import time
import os
import base64

# --- Page setup ---
st.set_page_config(layout="wide", page_title="HelioPal Chatbot")

# --- Asset paths ---
entrance_gif = "./assets/sun_energy_entrance_blk.gif"
loop_gif = "./assets/sun_energy_loop_blk.gif"
chatbot_icon_path = "./assets/chatbot.png"

# --- Utility: Encode images to base64 ---
def to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- Inject CSS styles ---
st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
            font-family: 'Segoe UI', sans-serif;
        }

        header[data-testid="stHeader"] {
            background-color: transparent;
            box-shadow: none;
        }

        header[data-testid="stHeader"] * {
            color: #fc9601 !important;
            font-weight: bold !important;
        }

        .title-row {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 0px 25px;
        }

        .title-text {
            font-size: 120px;
            font-weight: 750;
            color: #FC9601;
            margin-bottom: -25px;
        }

        .subtitle-box {
            font-size: 28px;
            color: #666666;
            margin-bottom: 75px;
            padding: 0px 25px;
        }

        .gif-box {
            display: flex;
            justify-content: flex-end;
            padding-right: 20px;
            margin-top: 25px;
        }

    </style>
""", unsafe_allow_html=True)


# GitHub Link
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        background: transparent;
        font-size: 20px;
        z-index: 100;
    }
    .footer a {
        color: #ffffff;
        text-decoration: none;
    }
    .footer a:hover {
        color: #666;
    }
    </style>

    <div class="footer">
        <a href="https://github.com/Ola-doyin/Helio-AI-Chatbot.git" target="_blank">
            <i class="fab fa-github"></i> GitHub
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Font Awesome for GitHub icon
st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">',
    unsafe_allow_html=True
)



# --- Layout: 3 columns ---
left, spacer, right = st.columns([6, 2, 6])

# --- LEFT: Chat UI ---
with left:
    chatbot_icon_base64 = to_base64(chatbot_icon_path)

    # Title & subtitle
    st.markdown(f"""
        <div class="title-row">
            <div class="title-text">HelioPal</div>
            <img src="data:image/png;base64,{chatbot_icon_base64}" width="100" style="margin-top: 20px;">
        </div>
        <div class="subtitle-box"><b>Your friendly solar sizing and simulation chatbot</b></div>
    """, unsafe_allow_html=True)

    # Description
    st.markdown("""
        <p style="font-size: 18px; line-height: 1.6; color: #f2f2f2; padding: 0px 25px;">
            Whether it’s for a home, business, or off-grid community, just ask your question — from panel sizing to battery autonomy — and HelioPal will calculate and simulate the perfect system for you.
            <br>No jargon. No guesswork. Just accurate, friendly solar guidance.
        </p>
    """, unsafe_allow_html=True)

    form_col1, form_col2= st.columns([0.2, 11.8])   # Adjust 1 → 2 for more rightward nudge


with form_col2:
    st.markdown(
        '<div style="margin-top: 75px; color: #666666;">',
        unsafe_allow_html=True
    )

    with st.form("chat_form"):
        user_input = st.text_input("", placeholder="e.g. Design the system I need for a 3kW load?")
        submitted = st.form_submit_button("Start Chat")
        if submitted and user_input:
            st.session_state["user_input"] = user_input
            st.switch_page("./pages/2_💬_Chat_page.py")

    st.markdown('</div>', unsafe_allow_html=True)


# --- RIGHT: GIF animation ---
with right:
    if not os.path.exists(entrance_gif) or not os.path.exists(loop_gif):
        st.error("One or more GIFs are missing in the assets folder.")
    else:
        placeholder = st.empty()

        # Entrance animation
        with placeholder.container():
            st.markdown(
                f"""
                <div class="gif-box">
                    <img src="data:image/gif;base64,{to_base64(entrance_gif)}" width="650">
                </div>
                """,
                unsafe_allow_html=True
            )

        time.sleep(5)

        # Loop animation
        with placeholder.container():
            st.markdown(
                f"""
                <div class="gif-box">
                    <img src="data:image/gif;base64,{to_base64(loop_gif)}" width="700">
                </div>
                """,
                unsafe_allow_html=True
            )

