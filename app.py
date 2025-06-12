import streamlit as st
# trying again
from streamlit_option_menu import option_menu

# Import page functions
from settings import show_settings
from myidea import show_my_ideas
from ask_mia import show_ask_mia
from idea_validator import show_idea_validator

# THIS MUST BE FIRST
st.set_page_config(page_title="Innovation Portal", page_icon="💡", layout="wide")

st.markdown("""
    <style>
        .sidebar .sidebar-content {
            padding-top: 2rem;
        }
        img {
            border-radius: 50%;
            width: 100px;
            margin: 0 auto;
            display: block;
        }
        .profile-name {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            margin-top: 10px;
            color: #850038;
        }
        .profile-title {
            text-align: center;
            font-size: 14px;
            color: gray;
            margin-bottom: 20px;
        }
     /* Force icon color for active menu item */
        .nav-link.active i, .nav-link.active span[class^="menu-icon"] {
            color: #850038 !important;
        }
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar layout
with st.sidebar:
    st.markdown('<div class="sidebar-container">', unsafe_allow_html=True)
    st.image("shape.jpg", use_container_width=False, width=120)
    st.markdown('<div class="profile-name">Anna van Drake</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-title">CEO WedoIT</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    selected = option_menu(
        None,
        ["Home", "Idea Validation", "My Ideas", "Ask MIA", "Settings"],
        icons=["home", "clipboard-check", "lightbulb", "question-circle", "gear"],
        menu_icon=None,
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#F0F2F6"},
            "nav-link": {"color": "black", "font-size": "16px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {
                "background-color": "#850038",
                "color": "white",
                "font-weight": "400",
                # "icon": {"color": "#850038"}  
            },
        }
    )

# Main content area
if selected == "Settings":
    show_settings()
elif selected == "My Ideas":
    show_my_ideas()
elif selected == "Ask MIA":
    show_ask_mia()
elif selected == "Idea Validation":
    show_idea_validator()

