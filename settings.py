import streamlit as st

def show_settings():
    

    st.markdown("""
        <style>
            .delete-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px;
                border-radius: 8px;
                border-top: 1px solid #eee;
                margin-top: 20px;
                margin-bottom: 10px;
            }
            .delete-text {
                flex: 1;
                margin-right: 20px;
            }
            .delete-button {
                background-color: #850038;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
            }
            .manage-button {
                background-color: white;
                color: #850038;
                border: solid 1px #850038;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
            }
            .switch {
                position: relative;
                display: inline-block;
                width: 60px;
                height: 34px;
            }
            .switch input { 
                opacity: 0;
                width: 0;
                height: 0;
            }
            .slider {
                position: absolute;
                cursor: pointer;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background-color: #ccc;
                transition: .4s;
                border-radius: 50px;
            }
            .slider:before {
                position: absolute;
                content: "";
                height: 26px;
                width: 26px;
                left: 4px;
                bottom: 4px;
                background-color: white;
                transition: .4s;
                border-radius: 50%;
            }
            input:checked + .slider {
                background-color: #850038;
            }
            input:focus + .slider {
                box-shadow: 0 0 1px #850038;
            }
            input:checked + .slider:before {
                transform: translateX(26px);
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.title("Settings")
        st.markdown("""
            <div class="delete-container">
                <div class="delete-text">
                    <h4>Privacy</h4>
                    <p>I want to train the model with my data to improve its accuracy and efficiency. For example, this could include customer feedback or transaction records. Your data will not be sold to third parties.</p>
                </div>
               <label class="switch">
                        <input type="checkbox">
                        <span class="slider round"></span>
                    </label>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="delete-container">
                <div class="delete-text">
                    <h4>Incognito</h4>
                    <p>I want the agent to operate in Incognito mode for more privacy and security. After you close the tab, all your data will be forgotten.</p>
                </div>
                    <label class="switch">
                        <input type="checkbox">
                        <span class="slider round"></span>
                    </label>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="delete-container">
                <div class="delete-text">
                    <h4>Archive all chats</h4>
                    <p>Keep your important prompts safe, so you do not lose them.</p>
                </div>
                <button class="manage-button" type="submit">Manage</button>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="delete-container">
                <div class="delete-text">
                    <h4>Delete all chats</h4>
                    <p>By deleting all chats, all your information that you gave it will be permanently removed.</p>
                </div>
                <button class="delete-button" type="submit">Delete</button>
            </div>
        """, unsafe_allow_html=True)
