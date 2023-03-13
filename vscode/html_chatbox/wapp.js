const chatArea = document.getElementById('chat-content');
const inputField = document.getElementById('input_field');
const inputButton = document.getElementById('input_button');
const lastMessage = chatArea.lastElementChild;
lastMessage.scrollIntoView()
let counter = 0;
let isScrollingDown = true;

chatArea.addEventListener("sc", () => {
  // Check if user is scrolling up or down
  isScrollingDown = chatArea.scrollTop + chatArea.clientHeight === chatArea.scrollHeight;
});
inputField.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && inputField.value !== "") {
        event.preve
        senderResponseToHtml(inputField.value);
        inputField.value = "";
    }
});


function senderResponseToHtml(message) {
    let time = new Date()
    let html = `<div class="media media-chat media-chat-reverse">
    <div class="media-body">
        <p>${message}</p>
        <p class="meta"><time>${time.toLocaleTimeString()}</time></p>
    </div>
    </div>`;
    chatArea.insertAdjacentHTML("beforeend", html);
    const lastMessage = chatArea.lastElementChild;
    lastMessage.scrollIntoView({behavior: "smooth"})
    gptResponseGenerate(message);

};
function gptResponseToHtml(message) {
    let ids = counter++
    let time = new Date()
    let html = `<div class="media media-chat">
    <img class="avatar"
        src="https://img.icons8.com/color/36/000000/administrator-male.png" alt="...">
    <div class="media-body">
        <p id="${ids}"></p>
        <p class="meta"><time>${time.toLocaleTimeString()}</time></p>
    </div>
</div>`
    chatArea.insertAdjacentHTML("beforeend", html);
    let content = document.getElementById(String(ids));
    let index = 0;
    const typingInterval = setInterval(() => {
        content.textContent += message[index];
        index++;
        const lastMessage = chatArea.lastElementChild;
        // chatArea.scrollTop = chatArea.scrollHeight;
        // lastMessage.scrollIntoView({behavior: "smooth"});
        if (isScrollingDown) {
            lastMessage.scrollIntoView({ behavior: "smooth" });
          }
        // console.log(lastMessage.scrollTop,lastMessage.scrollHeight);
        // console.log(chatArea.scrollTop, chatArea.scrollHeight)
        if (index === message.length) {
            clearInterval(typingInterval);

        }
    }, 50);

    // content.scrollTop = content.scrollHeight;


};

function gptResponseGenerate(message) {
    const conversation = [{ "role": "system", "content": "You are a helpful assistant." }];
    conversation.push({ "role": "user", "content": message });
    const apiKey = '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';
    fetch(`https://api.openai.com/v1/chat/completions`,
    {
        body: JSON.stringify({
            "model": "gpt-3.5-turbo",
            "messages": conversation,
            "temperature": 0.3,
            "max_tokens":250,
        }), 
        method: "POST",
        headers: {
            "content-type": "application/json",
            Authorization: "Bearer "+ apiKey,
    }
    })
    .then(response => response.json())
    .then(function (data){
        conversation.push({ "role": "user", "content": data.choices[0].message.content});
        gptResponseToHtml(data.choices[0].message.content);
    }).catch(data => console.log(data))

};
