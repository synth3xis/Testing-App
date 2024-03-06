import streamlit as st
import pandas as pd
import numpy as np

table=[10,16,8]

def main():
    st.title("HI THIS IS A TEST")
    st.divider()
    st.header("this webpage is served as a testing ground")
    st.divider()

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.divider()
st.header("verification")
st.header("verification")
st.table(table)
st.checkbox("select this if the total value is >34")


option = st.sidebar.selectbox(
    'Which number do you like best?',
     ["1", "2","3"])

st.sidebar.write('You selected:', option)


data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [3,8,4,23,16],
})

st.bar_chart(data.set_index('Category'))

if __name__ == '__main__':
    main()

