st.title("Intent-Based Chatbot")
st.write("Ask me anything, and I'll try my best to help!")
if "messages" not in st.session_state:
        st.session_state.messages = []
user_input = st.text_input("You: ", key="input")
if user_input:
        # Add user message to chat history
        st.session_state.messages.append(("You", user_input))

        intent = bot(user_input)
        if intent:
            response = random.choice(intent["responses"])
        else:
            response = random.choice(data["intents"][-1]["responses"])  # Default response

        # Add bot response to chat history
        st.session_state.messages.append(("Bot", response))

    # Display chat history
for sender, message in st.session_state.messages:
        if sender == "You":
            st.write(f"**You:** {message}")
        else:
            st.write(f"**Bot:** {message}")        
