// alert('hello');
// document.getElementById("h").innerHTML = "Raj"
// document.write('raj')  //This works only with async (pre loaded js) not with difer

// let x = 'hello';
// let y = 20;
// // const y = 20;
// // y = 30;
// var z = x +" "+2
// console.log(z)
// console.log('hello')
// let x = 'raj' ;
// // x++;
// console.log('Hello'+" "+x)
// console.log(`hello ${x}`)
// console.log(5 < 4 || 4 < 5)

// let age = 19;
// let votercard = 'yes';

// if(age >= 18 && votercard == 'yes'){
//     alert('you can vote');
// } else if(age < 18 && votercard == 'yes'){
//     alert('get your voter id card')
// } else {
//     alert('you can not vote');
// }
// if(age >= 18){
//     if(votercard == 'yes'){
//         alert('go and vote');
//     } else {alert('Go and make voter id card')}

// } else {
//     alert('you can not vote');
// }

// let isloggedin = 1; //is user logged in true or false

// if(isloggedin == 0){
//     document.write('Login')
// } else{
//     document.write('Logout')
// }

// let isloggedin = 1;
// let option = isloggedin == 0 ? 'Login': 'Logout'; ternary operator
// document.write(option);

// let user;
// // user = 'Raj';
// alert(user ?? 'Guest user'); // nulish coaliscing operator



// switch statement----------------------------

// if input = 1 , y , yes return continue...
// if input = 0 , n, no   return End...
// let input;
// input = 1;
// if(input === 1){document.write("Continue")}
// else if(input === "y"){document.write("Continue")}
// else if(input === "yes"){document.write("Continue")}
// else if(input === 0){document.write("End")}
// else if(input === "n"){document.write("End")}
// else if(input === "no"){document.write("End")}
// else{"wrong input"}

// switch(input){
//     case 1:
//         // document.write("continue");
//         // break;
//     case "y":
//         // document.write("continue");
//         // break;
//     case "yes":
//         document.write("continue");
//         break;
//     case 0:
//         // document.write("End");
//         // break;
//     case "n":
//         // document.write("End");
//         // break;
//     case "no":
//         document.write("End");
//         break;
//     default :
//     document.write("Wrong input");
//         break;

// }

// -------------------loops-----------------

// let counter = 1;

// while(counter >= 10){
//     document.write("Tech Gun ")
//     counter++
// }

// let count = 1;
// let sum = 0;
// while(count <= 200){
//     if(count % 2 == 0){
//         sum += count;
//     } count++;
// }document.write(sum)

// let count = 1;

// do{document.write("JavaScript "); count++}
// while(count <= 10)

// for(let count = 1; count <= 10; count++){
//     document.write(count+" ")
// }

// --------------break , continue, Nested loop----
// outer: for(let count = 1; count <= 10; count++){
//     // if(count == 5){break;}
//     document.write(count, "<br>")
//     for(let count2 = 1; count2 < 3; count2++){
//         if(count == 2){break outer;}
//         document.write('JavaScript <br>')

//     }
// }

// -------------alert, prompt, confirm function------------

// let age = prompt('Enter your age :', 20);
// if(age){
//     document.write("your age is "+ age + "<br>");
// } else{document.write("you have not entered anything <br>")};

// let response = confirm("Are you sure you want to delet ?")
// if(response){document.write("you have deleted")}
// else{document.write("you have failed to delete")}

// ----------datatype conversion ----------------
// let type = '5' *'2';
// console.log(type)
// console.log(typeof type);
// let type = 5;
// console.log(typeof type)
// let type2 = Boolean(type)
// console.log(type2) 
// console.log(typeof type2)

// let str = "Hello json";

// console.log(str.length);

// ---------------------for loop in array--------

// let book = ["Maths", "Physics", "Bio", "computer science"]
// for(i=0; i < book.length; i++ ){
//     document.write(`Eliment ${i} is ${book[i]} \n <br>`)
// }

// book.forEach(myfunc);
// function myfunc(value){console.log(value)}

// --------------------function--- 
// document.write('hello <br>')
// function multiTable(num){
//     for(i=1; i <=10; i++){
//         document.write(`${num} * ${i} = ${num*i} <br>`);
//     }
// }
// multiTable(25);

// function add(){
//     if(arguments.length == 0){document.write("Enter numbers to add")}
//     else{
//         let sum = 0;
//         for(let i = 0; i<arguments.length; i++){sum = sum + arguments[i]}
//         document.write(`sum is ${sum}`)
//     }
// }

// add(5, 7, 35)

// function add(a, b){
//     d = [a,b];
//     return d-}
// let c = add(5,5)
// document.write(c)

// ===================object oriented programming==========

// let person = {
//     firstName : "Java",
//     lastName : "Script",
//     sayhello(){
//         console.log(`hello i am ${this.firstName} and i have a ${car.brand} car`)
//     }
// };
// let car = {
//     brand : "TATA",
//     model : "safari"
// }
// person.firstName = 'python'
// person.age = 25
// person.sayhello = function(){
//     document.write("hello")
// }
// person.sayhello();
// console.log(person.age)
// for(let key in person){
//     console.log(key +" "+ person[key])
// }

// math and random 
// // let m = Math.round((Math.random()*10)+1)
// let m = Math.round(Math.random() * (25 - 15))  + 15; 

// document.write(m)

// ========date module====
// let x = new Date(2018, 11, 25, 10, 38)
// let x = new Date()
// let y = new Date()
// y.setDate(x.getDate()+50)
// document.write(x)
// document.write("<br>")
// document.write(y)

// ==============getter and setter=========
//get == to access data without ()
// let person = {
//     name : 'python',
//     age : 40,
//     get getname(){
//         return this.name.toUpperCase()
//     }, 
//     set setname(n){
//         this.name = n.toUpperCase();
//     }
// }
// person.setname = 'javascript'

// console.log(person.getname);
// console.log(person.name);


// ==========object constructor=========
// function Student(firstName, lastName, age, cls){
//     this.firstName = firstName;
//     this.lastName = lastName;
//     this.age = age;
//     this.class = cls;
// }

// let student1 = new Student('java', 'script', 25, 10)
// console.log(student1.firstName)

// ======= Objectoro
// .prototype.name =========
// to add property in constructor

// ======object in object======

// ============= Hoisting ==
// ==storage_session.html
// //local storage and session ======
// localStorage.setItem("name1", "python")
// localStorage.setItem("name2", "java")
// // console.log(localStorage.name2)

// // to clear any particular item
// localStorage.removeItem("name1")


// let name = localStorage.getItem("name1")
// console.log(name);
// // localStorage.clear() to clear entire storage
// // console.log(localStorage);

// //to pass array in localstorage
// let impArray = ["adrak", "pyaz", "bhindi"]
// localStorage.setItem("sabji", JSON.stringify(impArray))
// let sabji = JSON.parse (localStorage.getItem("sabji"))
// console.log(sabji)
// console.log(sabji[1])
// // console.log(typeof sabji)
// let ask = (question, yes, no) => confirm(question) ? yes() : no();
// ask(
// 'Do you agree?',
// () => console.log('You agreed'),
// () => console.log('You interrupted execution'),
// )



// ===========oops ==========

// class Queue {
//     constructor() {
//       this.elements = {};
//       this.head = 0;
//       this.tail = 0;
//     }
//     enqueue(element) {
//       this.elements[this.tail] = element;
//       this.tail++;
//     }
//     dequeue() {
//       const item = this.elements[this.head];
//       delete this.elements[this.head];
//       this.head++;
//       return item;
//     }
//     peek() {
//       return this.elements[this.head];
//     }
//     get length() {
//       return this.tail - this.head;
//     }
//     get isEmpty() {
//       return this.length === 0;
//     }
//   }

// let q = new Queue();
// for (let i = 1; i <= 7; i++) {
//   q.enqueue(i);
// }
// // get the current item at the front of the queue
// console.log(q.peek()); // 1

// // // get the current length of queue
// console.log(q.length); // 7

// // // dequeue all elements
// // while (!q.isEmpty) {
// //   console.log(q.dequeue());
// // }

// // to see all elements 
// console.log(q.elements);

// console.log(Math.floor(Math.random() * (10 - 1 + 1)));
// console.log(10-1+1);

// let x = "5";
// console.log(toString x)
// mydiv = $("mydiv")
// console.log(mydiv);
// let board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// let s = '';
// for (let i = 0, j = 1; i < board.length; i++, j++) {
//   s += board[i] + ' ';
//   if (j % 2 == 0) {
//     console.log(s);
//     s = ' ';
//   }
// }
// function requiredArg() {
//     throw new Error('The argument is required');
//  }
//  function add(x = requiredArg(), y = requiredArg()){
//     return x + y;
//  }
 
// //  console.log(add(10))
// function subtract( x = y, y = 1 ) {
//     return x - y;
// }
// console.log(subtract())

// ====object constructor
// function Person(fname,lname){
//     this.fname = fname,
//     this.lname = lname,
//     this.getfullname = function(){
//         return (`${this.fname} ${this.lname}`)
//     }
// }
// let person  = new Person("Hello", "world");
// console.log(person.getfullname())

// ==== prototype
// let person = {name : "john"}
// console.log(Object.prototype);
// ==constructor
// function Person(name){
//     this.name = name
// }
// // console.log(Person.prototype);
// let p1 = Person("hello");
// let p2 = Person("world")
// console.log(p1.constructor.prototype);
// let teacher = {
//     teach: function (subject) {
//         return "I can teach " + subject;
//     }
// };

// let person = {
//     name: "John Doe",
//     greet: function () {
//         return "Hi, I'm " + this.name;
//     }
// };
// teacher.__proto__ = person;
// console.log(teacher.name);
// console.log(teacher.greet());

// let driver = Object.create(person, {
//     name1 : {value : "odoo"},
//     drive : {value : function(){
//         return `i am ${this.name} and i can drive`
//     }}
// })
// console.log(driver.drive());
// console.log(Object.getPrototypeOf(driver) === person); //true
// console.log(Object.getPrototypeOf(person) === driver); //false
// console.log(Object.getPrototypeOf(person) === Object.prototype); //true
// person.__proto__ = driver; // not possible
// console.log(person.name1);
this.color = 'red';
// console.log(window.color);

// let car = {
//     brand: 'Honda',
//     getBrand: function () {
//         return this.brand;
//     }
// }
// console.log(car.getBrand());// Honda
// let brand = car.getBrand; 
// console.log(brand()); // undefined
//because it converted into a strict mode
// to fix this issue
// let brand = car.getBrand.bind(car);
// console.log(brand());

// function getbrand(prefix){
//     console.log(prefix + this.brand)
// }
// let honda = {brand : "honda"};
// let audi = {brand : 'audi'}
// getbrand.call(honda, "this is a ")
// getbrand.call(audi, "this is an ")
// getbrand.apply(honda, ["this is a"])
// getbrand.apply(audi, ["this is an "])

// const canFetch = typeof globalThis.fetch === 'function';
// console.log(canFetch);
// console.log(globalThis);

// ===configurable, enumerable, writable, set, get, value
// 'use strict';
// let obj = {};
// Object.defineProperty(obj, 'ssn',{
//     configurable : false,
//     value : '012-321-556'
// })
// // console.log(obj.ssn);
// delete obj.ssn;
// console.log(obj.ssn);

// 'use strict';

// let person = {};

// Object.defineProperty(person, 'ssn', {
//     configurable: false,
//     value: '012-38-9119'
// });

// delete person.ssn;
// console.log(person.ssn);
// Object.defineProperty(person, 'ssn', {
//     configurable: true
// });
// let person = {
//     firstName: 'John',
//     lastName: 'Doe'
// }

// Object.defineProperty(person, 'fullName', {
//     get: function () {
//         return this.firstName + ' ' + this.lastName;
//     },
//     set: function (value) {
//         let parts = value.split(' ');
//         if (parts.length == 2) {
//             this.firstName = parts[0];
//             this.lastName = parts[1];
//         } else {
//             throw 'Invalid name format';
//         }
//     }
// });
// console.log(person.fullName);
// person.fullName = "heello world"
// console.log(person.fullName);

// let product = {};
// Object.defineProperties(product,{
//     price : {value : 1020},
//     tax : {value : 5.10},
//     total : { get: function () {
//         return this.price * (1 + this.tax);
//     }}
// })
// for(let i in product){
//     console.log(i + ":" + product[i])
// }

// let param = {name: "hello", second: "world"};
// for(let i in param){
//     console.log(i + param[i]);
// }

// let decorator = {color : "red"};
// let circle = Object.create(decorator)
// circle.radius = 50;
// let circle = Object.create(decorator, {
//     radius : {value : 50,enumerable:true}
// }) //for... in will not work
// console.log(circle.radius);
// console.log(circle.propertyIsEnumerable('radius')); // => false
// console.log(circle.hasOwnProperty("color")); // => false
// for(let i in circle){console.log(i);}

// const value = Object.values(circle); //it ill give enumerable values of own object
// console.log(value);
// let kv  = Object.entries(circle); // will give arrray of own enumerable
// console.log(kv);

// let widget = {color : "red"}
// let hello = {hello : 'world'}
// let newwidget = Object.assign({}, hello, widget);
// console.log(newwidget);
// console.log(Boolean(null)); //false
// console.log(null === null); // true
// console.log(NaN === NaN); //false

//==object destructuring ===
// let person = {
//     firstName: 'John',
//     lastName: 'Doe',
//     currentage : 20,
//     getfullname(){return firstName+ ' '+ lastName}
// };
// let {firstName : fname, lastName: lname} = person;
// console.log(fname);//john
// console.log(lname); //doe

//==direct
// let {firstName, lastName, getfullname} = person
// console.log(firstName);
// console.log(lastName);
// console.log(getfullname());

//==assign default value
// let {firstName, lastName, middlename ='', currentage:age =25} = person
// console.log(middlename)
// console.log(age);
// let employee = {
//     id: 1001,
//     name: {
//         firstName: 'John',
//         lastName: 'Doe'
//     }
// };
// let {name :{firstName, lastName}, name} = employee
// console.log(firstName+ ' ' + lastName);
// console.log(name);

//---optional chaining operator
// function getUser(id) {

//     if(id <= 0) {
//         return null;
//     }

//     // get the user from database
//     // and return null if id does not exist
//     // ...
    
//     // if user was found, return the user
//     return {
//         id: id,
//         username: 'admin',
//         profile: {
//             avatar: '/avatar.png',
//             language: 'English'
//         }
//     }
// }
// console.log(getUser(0));
// let user = getUser(2);
// // let profile = user && user.profile; //and operator searchs false 
// let profile = user ?. profile // it will checks user first for undefined
// console.log(profile); // undefined

// let avatar = user ?. profile ?. avatar
// console.log(avatar);

// //== with nullish coaliscing
// let defaultProfile =  { default: '/default.png', language: 'English'};

// let user = getUser(0);
// let profile = user ?. profile ?? defaultProfile;
// console.log(profile);

//with function call
// let file = {
//     read() {
//         return 'file content';
//     },
//     write(content) {
//         console.log(`Writing ${content} to file...`);
//         return true;
//     }
// };
// let data = file.read();
// console.log(data);

// let compressedData = file.compress();
// console.log(compressedData);
// let compressedData = file.compress?.();
// console.log(compressedData);

// function createMachine(name, status) {
//     return {
//         name,
//         status
//     };
// }
// console.log(createMachine("AI", "working"));

//==class
// class Person{
//     constructor(name){
//         this.name = name
//     }
//     get getname(){
//         return `my name is ${this.name}`
//     }
// }

// let p1 = new Person("odoo")
// console.log(p1.name);
// console.log(p1.getname);

// class Person {
//     constructor(name) {
//         this.name = name;
//     }
//     get name() {
//         return `hi `+this._name;
//     }
//     set name(newName) {
//         newName = newName.trim();
//         if (newName === '') {
//             throw 'The name cannot be empty';
//         }
//         this._name = newName;
//     }
// }
// let p1 = new Person("jone doe")
// console.log(p1.name);
// p1.name = "hello world"
// console.log(p1.name);

let meeting = {
    atandees : [],
    add(atandee){
        console.log(`${atandee} is joined...`);
        this.atandees.push(atandee);
        return this
    },
    get latest(){
        let count = this.atandees.length;
        return count == 0 ? undefined : this.atandees[count - 1];
    }

}
meeting.add("rahul").add("hema").add("mj");
console.log(meeting.latest)











































































































































































