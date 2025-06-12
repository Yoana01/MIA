import streamlit as st

def show_my_ideas():

    st.markdown("""
        <style>
            .delete-container {
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
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
            .progress{
                background-color: #FFD500;
                border: none;
                border-radius: 8px;
                padding: 4px 8px;}
             .refinement{
                background-color: #E50909;
                border: none;
                color: white;
                border-radius: 8px;
                padding: 4px 8px;}
            .validated{
                background-color: #2EB709; 
                color: white;
                border: none;
                border-radius: 8px;
                padding: 4px 8px;}
            .archieved{
                background-color: #3773E0;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 4px 8px;}
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.title("My Ideas")
        st.markdown("""
            <div class="delete-container">
                <div class="delete-text">
                    <h4>Idea 1</h4>
                    <p>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. </p>
                    <button class="delete-button" type="submit">Share</button>
                </div>
                <button class="progress" type="submit">In Progress</button>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
             <div class="delete-container">
                <div class="delete-text">
                    <h4>Idea 2</h4>
                    <p>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. </p>
                    <button class="delete-button" type="submit">Share</button>
                </div>
                <button class="refinement" type="submit">Refinement Needed</button>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
             <div class="delete-container">
                <div class="delete-text">
                    <h4>Idea 3</h4>
                    <p>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. </p>
                    <button class="delete-button" type="submit">Share</button>
                </div>
                <button class="validated" type="submit">Validated</button>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
             <div class="delete-container">
                <div class="delete-text">
                    <h4>Idea 4</h4>
                    <p>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. </p>
                    <button class="delete-button" type="submit">Share</button>
                </div>
                <button class="archieved" type="submit">Achieved</button>
            </div>
        """, unsafe_allow_html=True)