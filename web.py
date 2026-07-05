import streamlit as st
import function
todos=function.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]+'\n'
    todos.append(todo)
    function.write_todos(todos)
def remove_todo():
    todo=st.session_state["new_todo"]+'\n'
    todos.remove(todo)
    function.write_todos(todos)
st.title("My To-Do App")
st.subheader("This is my Todos App")
st.write("This app is use to increase your productivity")
for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("Enter a todo:",
              placeholder="Add new todo....",
              on_change=add_todo,
              key="new_todo")