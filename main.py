import helper_lang as hlang
import streamlit as st

st.title("Meet Automatia!")


"""
## Automatia
It is a chatbot designed to support you at any problem that you would have. So don't hesitate to ask something to Automatia!
"""

input_ = st.text_input(label="Ask anything to Automatia!")

response = hlang.chain.invoke({"name":"Automatia",
                                "input": input_})

st.write(response)