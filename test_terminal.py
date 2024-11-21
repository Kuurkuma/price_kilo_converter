import streamlit as st
import time

# Custom CSS for terminal-like appearance
st.markdown(
    """
    <style>
    .terminal {
        background-color: black;
        color: green;
        font-family: monospace;
        padding: 20px;
        border-radius: 5px;
        height: 400px;
        overflow-y: auto;
        white-space: pre-wrap;  /* Preserves line breaks */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for terminal output
if "terminal_output" not in st.session_state:
    st.session_state.terminal_output = []

# Add terminal container
terminal_placeholder = st.empty()

def update_terminal():
    """Updates the terminal container with the current output."""
    terminal_html = '<div class="terminal">'
    for line in st.session_state.terminal_output:
        terminal_html += f"{line}<br>"
    terminal_html += "</div>"
    terminal_placeholder.markdown(terminal_html, unsafe_allow_html=True)

# Add lines with a delay
def add_lines_with_delay(lines, delay=0.5):
    """Adds lines to the terminal with a delay between each."""
    for line in lines:
        st.session_state.terminal_output.append(line)
        update_terminal()
        time.sleep(delay)  # Delay between lines

# Input for commands
command = st.text_input("Enter command:", key="terminal_input")

# Initial presentation
if "initialized" not in st.session_state:
    add_lines_with_delay([
        "______________",
         "Hello Motherfucker !",
        "I am your terminal.",
        "You can use me to hack the world",
        "First let's try basic commands..."
    ], delay=1)
    st.session_state["initialized"] = True

# Handle command execution
if st.button("Execute"):
    if command:
        st.session_state.terminal_output.append(f"$ {command}")
        update_terminal()
        
        # Simulate command output with delay
        if command == "hello world":
            add_lines_with_delay(["<span style='color: red;'>Go fuck yourself with your bloody Hello World !!</span>"], delay=0.2)
        elif command == "error":
            add_lines_with_delay(["<span style='color: red;'>Error: Invalid command</span>"], delay=0.2)
        elif command == "clear":
            st.session_state.terminal_output = ['better now !']
            update_terminal()
        elif command == "exit":
            add_lines_with_delay([" no, no, no! you can't leave me !!"], delay=0.2)
        else:
            add_lines_with_delay([f"Don't know your shitty command: {command}"], delay=0.2)

# Update terminal display
update_terminal()