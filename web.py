import streamlit as st
import function
todos=function.get_todos()
st.title("My To-Do App")
st.subheader("This is my Todos App")
st.write("This app is use to increase your productivity")
for todo in todos:
    st.checkbox(todo)

st.text_input("Enter a todo:",placeholder="Add new todo....")