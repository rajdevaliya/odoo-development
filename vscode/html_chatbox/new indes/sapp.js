function appendTypingMessage(message) {
    const chatWindow = document.getElementById('chat-window');

    const messageContainer = document.createElement('pre');
    messageContainer.classList.add('message-container');
    messageContainer.classList.add('bot-message');

    const messageElement = document.createElement('div');
    messageElement.classList.add('message');

    messageContainer.appendChild(messageElement);
    chatWindow.appendChild(messageContainer);

    let index = 0;
    const typingInterval = setInterval(() => {
        messageElement.textContent += message[index];
        index++;
        if (index === message.length) {
            clearInterval(typingInterval);
        }
    }, 50);
}
appendTypingMessage(`function appendTypingMessage(message) {
    const chatWindow = document.getElementById('chat-window');
    
    const messageContainer = document.createElement('div');
    messageContainer.classList.add('message-container');
    messageContainer.classList.add('bot-message');
    
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    
    messageContainer.appendChild(messageElement);
    chatWindow.appendChild(messageContainer);
    
    let index = 0;
    const typingInterval = setInterval(() => {
      messageElement.textContent += message[index];
      index++;
      if (index === message.length) {
        clearInterval(typingInterval);
      }
    }, 50);
  }
  `)