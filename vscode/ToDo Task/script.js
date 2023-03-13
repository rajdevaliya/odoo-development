// =========second code=========
// select everything
// select the todo-form
const todoForm = document.querySelector('.todo-form');
// select the input box
const todoInput = document.querySelector('.form-control');
// select the <ul> with class="todo-items"
const todoItemsList = document.querySelector('.todo-items');
const todoItemsList1 = document.querySelector(".todo-list2")
// array which stores every todos
let todos = [];
// add an eventListener on form, and listen for submit event
todoForm.addEventListener('submit', function(event) {
  // prevent the page from reloading when submitting the form
  event.preventDefault();
  addTodo(todoInput.value); // call addTodo function with input box current value
});
// function to add todo
function addTodo(item) {
  //if empty
  if (item == ''){alert("please add tod")}
  // if item is not empty
  else if (item !== '') {
    // make a todo object, which has id, name, and completed properties
    const todo = {
      id: Date.now(),
      name: item,
      completed: false,
      complete: false
    };
// then add it to todos array
    todos.push(todo);
    addToLocalStorage(todos); // then store it in localStorage
// finally clear the input box value
    todoInput.value = '';
  }
}
// function to add todos to local storage
function addToLocalStorage(todos) {
  // conver the array to string then store it.
  localStorage.setItem('todos', JSON.stringify(todos));
  // render them to screen
  renderTodos(todos);
  renderTodos1(todos);
}
// function to render given todos to screen
function renderTodos(todos) {
  // clear everything inside <ul> with class=todo-items
  todoItemsList.innerHTML = '';
  todos.forEach(function(item){
    const checked = item.completed ? 'checked': null;
    const visible = item.completed ? 'none' : 'block';
    const li = document.createElement('li');
    li.setAttribute('id', item.id);
    li.style.display = `${visible}`
    li.innerHTML = `
       <input type="checkbox" class="checkbox" ${checked}>       
       ${item.name}
      <button class="delete-button">X</button>`
    todoItemsList.append(li);

   }) 
}
function renderTodos1(todos) {
  // clear everything inside <ul> with class=todo-items
  todoItemsList1.innerHTML = '';
  todos.forEach(function(item){
    let checked = item.complete ?  'checked': null;
    let visible = item.complete ? 'block': 'none'
    const li = document.createElement('li');
    li.setAttribute('id', item.id);
    li.setAttribute("style", `display:${visible}`)
    li.innerHTML = `
       <input type="checkbox" class="checkbox" ${checked}>       
       ${item.name}
      <button class="delete-button">X</button>`
    todoItemsList1.append(li);

   }) 
}
// function func(id, value){
//   let x = document.getElementById(id)
//   console.log(x)
//   if (x.style.display === "none") {
//     x.style.display = "inline";
//   } else {
//     x.style.display = "none";
//   }

// }


// function helps to get everything from local storage
function getFromLocalStorage() {
  const reference = localStorage.getItem('todos');
  // if reference exists
  if (reference) {
    // converts back to array and store it in todos array
    todos = JSON.parse(reference);
    renderTodos(todos);
    renderTodos1(todos);
  }
}
// toggle the value to completed and not completed
function toggle(id) {
  todos.forEach(function(item) {
    // use == not ===, because here types are different. One is number and other is string
    if (item.id == id) {
      // toggle the value
      item.completed = !item.completed;
      item.complete = !item.complete
    }
  });
addToLocalStorage(todos);
}
// deletes a todo from todos array, then updates localstorage and renders updated list to screen
function deleteTodo(id) {
  // filters out the <li> with the id and updates the todos array
  todos = todos.filter(function(item) {
    // use != not !==, because here types are different. One is number and other is string
    return item.id != id;
  });
// update the localStorage
  addToLocalStorage(todos);
}
// // initially get everything from localStorage
getFromLocalStorage();
// after that addEventListener <ul> with class=todoItems. Because we need to listen for click event in all delete-button and checkbox
todoItemsList.addEventListener('click', function(event) {
  // check if the event is on checkbox
  if (event.target.type === 'checkbox') {
    // toggle the state
    toggle(event.target.parentElement.getAttribute('id'));
  }
// check if that is a delete-button
  if (event.target.classList.contains('delete-button')) {
    // get id from id attribute's value of parent <li> where the delete-button is present
    deleteTodo(event.target.parentElement.getAttribute('id'));
  }
});
todoItemsList1.addEventListener('click', function(event) {
  // check if the event is on checkbox
  if (event.target.type === 'checkbox') {
    // toggle the state
    toggle(event.target.parentElement.getAttribute('id'));
  }
// check if that is a delete-button
  if (event.target.classList.contains('delete-button')) {
    // get id from id attribute's value of parent <li> where the delete-button is present
    deleteTodo(event.target.parentElement.getAttribute('id'));
  }
});




// ==First code without localStorage ===============

// // Create a new list item when clicking on the "Add" button
// let elementCount = 0;

// function newElement() {
//     elementCount++
//     let myUL = document.getElementById("myUL");
//     var inputValue = document.getElementById("myInput").value;
//     localStorage.setItem(elementCount, inputValue);
//     let data = localStorage.getItem(elementCount)
//     let html = `<li class="li"><input id="${elementCount}" name="h" type="checkbox" onclick="myFunction(this.id, this.checked)" class="form-check-input">${data}</li>`
    
    

//     if (inputValue === '') {
//         alert("You must write something!");
//     }
//     else {
//         myUL.insertAdjacentHTML("afterbegin", html)
//         console.log(myUL)

//     }
//     document.getElementById("myInput").value = "";
// }


// function myFunction(id, value){
//     let parent = document.getElementById(id).parentElement
//     let text = parent.textContent
//     let myul = document.getElementById(id).parentElement;
    
//     if(value == true){
//         myul.remove()
//         let html = `<li class="li"><input id="${id}" name="h" type="checkbox" onclick="myFunction(this.id, this.checked)" class="form-check-input" checked>${text}</li>`
//         let item = document.getElementById("item");
//         item.insertAdjacentHTML("afterbegin", html)
//     }
//     else if(value == false){
//         myul.remove()
//         let html = `<li class="li"><input id="${id}" name="h" type="checkbox" onclick="myFunction(this.id, this.checked)" class="form-check-input">${text}</li>`
//         let item = document.getElementById("myUL");
//         item.insertAdjacentHTML("afterbegin", html)

    
        
//     }
// }







// ==================rough work===============
 
// if(inputValue !== ''){
//     let elements = document.getElementsByClassName("li");
//     alert()
//     console.log(elements)
//     for(let i=0; i < elements.length; i++){
//         let text2 = elements[i].textContent;
//         if(inputValue == text2){alert()}
//     }
// } 

    // var li = document.createElement("li");

    // var t = document.createTextNode(inputValue);
    // let tick = document.createElement("input");
    // tick.type = "checkbox";
    // tick.className = "form-check-input";
    // li.append(tick)

    // li.appendChild(t);

    // for(let i=0; i < elements.length; i++){
    //     let text2 = elements[i].textContent;
    //     if(text == text2){elements[i].remove()}
    // }