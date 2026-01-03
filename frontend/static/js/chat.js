let sessionId = null;

async function createSession() {
    try {
        const response = await fetch('/api/session/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        });
        
        const data = await response.json();
        if (data.success) {
            sessionId = data.session_id;
            console.log('Session created:', sessionId);
        }
    } catch (error) {
        console.error('Error creating session:', error);
    }
}

function addMessage(content, role = 'user') {
    const messagesContainer = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}`;
    
    const messageParagraph = document.createElement('p');
    messageParagraph.textContent = content;
    messageDiv.appendChild(messageParagraph);
    
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    
    if (!message) {
        return;
    }
    
    if (!sessionId) {
        await createSession();
    }
    
    addMessage(message, 'user');
    input.value = '';
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                session_id: sessionId,
                message: message
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            addMessage(data.response || data.message, 'assistant');
        } else {
            addMessage('Sorry, I encountered an error. Please try again.', 'system');
        }
    } catch (error) {
        console.error('Error sending message:', error);
        addMessage('Sorry, I encountered an error. Please try again.', 'system');
    }
}

document.getElementById('send-button').addEventListener('click', sendMessage);

document.getElementById('user-input').addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

window.addEventListener('load', () => {
    createSession();
});
