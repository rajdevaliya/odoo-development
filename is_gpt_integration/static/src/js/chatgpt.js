odoo.define('is_gpt_integration.chatgpt_chatbox', function(require) {
    'use strict';
    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    var rpc = require('web.rpc');

    var chatArea = document.getElementById('chat-content');
    var inputField = document.getElementById('input_field');
    var inputButton = document.getElementById('input_button');
    var lastMessage = chatArea.lastElementChild;
    lastMessage.scrollIntoView()
    let counter = 0;
    var isScrollingUp = true;

    publicWidget.registry.chatgpt = publicWidget.Widget.extend({
        selector: '.body-gpt',
        events: {
            'keydown #input_field': '_onClickGpt',
            'scroll #chat-content' : '_onScrollChatArea',
            'click #input_button' : '_onClickButtonGpt',
        },
        _onClickButtonGpt: function(event){
            if (inputField.value !== "") {
                this._senderResponseToHtml(inputField.value);
                inputField.value = "";
            }
        },
        _onScrollChatArea: function(){
            var scrollPosition = chatArea.scrollTop;
            var scrollHeight = chatArea.scrollHeight;
            var clientHeight = chatArea.clientHeight;
            console.log(scrollPosition, scrollHeight, clientHeight)
            isScrollingUp = scrollHeight - scrollPosition === clientHeight;

        },
        
        _onClickGpt: function(event){
            if (event.key === "Enter" && inputField.value !== "") {
                this._senderResponseToHtml(inputField.value);
                inputField.value = "";
            }
        },
        _senderResponseToHtml: function(message) {
            let time = new Date()
            let html = `<div class="media media-chat media-chat-reverse">
            <div class="media-body">
                <p>${message}</p>
                <p class="meta"><time>${time.toLocaleTimeString()}</time></p>
            </div>
            </div>`;
            chatArea.insertAdjacentHTML("beforeend", html);
            var lastMessage = chatArea.lastElementChild;
            lastMessage.scrollIntoView()
            this._gptResponseGenerate(message);
        
        },
        _gptResponseToHtml: function(message) {
            console.log(message)
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
                const cursor = document.createElement('span');
                cursor.className = 'cursor';
                content.appendChild(cursor);
                var lastMessage = chatArea.lastElementChild;
                if (isScrollingUp) {
                    lastMessage.scrollIntoView({ behavior: "smooth" });
            
                }
                if (index === message.length) {
                    clearInterval(typingInterval);
                    content.removeChild(cursor);

        
                }
            }, 50);

        
        },
        _gptResponseGenerate: function(message) {
            let self = this;
            const conversation = [{ "role": "system", "content": "You are a helpful assistant." }];
            conversation.push({ "role": "user", "content": message });
            const apiKey = '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';
            fetch(`https://api.openai.com/v1/chat/completions`,
            {
                body: JSON.stringify({
                    "model": "gpt-3.5-turbo",
                    "messages": conversation,
                    "temperature": 0.3,
                    "max_tokens":50,
                }), 
                method: "POST",
                headers: {
                    "content-type": "application/json",
                    Authorization: "Bearer "+ apiKey,
            }
            })
            .then(response => response.json())
            .then(function (data){
                console.log(data.choices[0].message.content)
                conversation.push({ "role": "user", "content": data.choices[0].message.content});
                self._gptResponseToHtml(data.choices[0].message.content);
            }).catch(data => console.log(data))
        
        }

    })

})