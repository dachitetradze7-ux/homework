

// let btn = document.getElementById("welcomeBtn")

// function greeting() {
//     alert("hello js!")
//     btn.textcontent = 'change color'

// }

// function add(num1, num2) {
//     return num1 + num2;
// }
  
//     let result = add(2, 1)



// let person = {
//     username: "dachi tetradze",
//     city: "tbilisi",
//     id: 2332222223,
//     getcity: function() {
//         console.log; {this}
//     }

// }

// console.log(greeting)


// btn.onclick = greeting()

// let hi  = greeting()
// console.log(hi)

let btn = document.getElementById("sendBtn");
let userfield = document.getElementById("username");
let welcomeHeader = document.getElementById("welcomeHeader")

btn.onclick = function () {
    welcomeHeader.textContent = "hello" + userfield.value
}


let saidYes =   confirm("sure?");


let movie = prompr("favourite movie")
console.log("green mile")

let username = prompt("enter username")
alert("hello" + username)