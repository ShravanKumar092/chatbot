document.getElementById('send-btn').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return; // Prevent empty messages

    // Append user's message to the chat box as 'user-message'
    appendMessage('You: ' + userInput, 'user-message');

    // Clear the input field
    document.getElementById('user-input').value = '';

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput }),
        });

        const data = await response.json();
        console.log("Response data:", data);  // Log the response for debugging

        if (response.ok) {
            // Ensure we only append one line of response
            if (data.response) {
                appendMessage('Bot: ' + data.response, 'bot-message');
            } else {
                appendMessage('Bot: [No response received]', 'bot-message');
            }
        } else {
            appendMessage('Bot: Error: ' + data.error, 'bot-message');
        }
    } catch (error) {
        console.error('Error:', error);
        appendMessage('Bot: Something went wrong!', 'bot-message');
    }
});

// Function to append messages to the chat box
function appendMessage(message, className) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.className = 'chat-message ' + className; // Add a class based on message type
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);

    // Auto-scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}
