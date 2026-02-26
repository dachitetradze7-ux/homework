//  Hoisting - js tviseba romlis mixedvitac jer iqmneba funcqia shemdeg var cvladebis declaratsia xolo shemdeg yvelaferi eshveba zevidan qvevit tanmdimdevrobit
// Scope - cvladebis gamoyeneba funcqciis garet

//  let x = 10;


//  function greet() {
//      let y = 10;
//  }
// greet()
// console.log(y)
// let, var, const
// local cvladi xelmisawvdomia yvelgan kodis blockshi
// global cvladi xelmiswvdomia mxolod adgilobriv kodi blockshi

// function OuterScope() {
//     let username = "LUKA"
//     function InnerScope() {
//         for(let i  = 0; i < 10; i++) {
//             username = username.toLowerCase()
//         }
//         console.log(username)
//     }
//     console.log(username)
//     InnerScope()
// }

// function scope() {
//     var  user = "luka"
// }

// scope()

// console.log(user)
// greet()
// function greet() {
//     console.log("hello world")
// }

// console.log(x)
// var x = 5;

// while (password != "dachi1234") {
//     password = prompt("enter password")
// }

//declaration

// Timers Function
// setTimeout() kods gaushvebs ertxel mititebuli drois shemdeg
// setInterval() kods gaushvebs garkveuli drois intervalebshi
// setTimeout(greet, 3000)
// function greet(username) {
    
//     if (!welconmeHim) {
//         clearTimeout(greetTimer)
//     }

//     console.log(`welcome ${username}`)
// }   

// let count = 0;
// function counter(){
//     if(count >= 15)
//         clearInterval(counterInterval)
// }

// setInterval(greet, 2000, "dachi")

// const counterInterval =  setInterval(counter, 500)

// const form = document.querySelector("form");
// const usernameField = form.elements.username;
// const emailFeild = form.elements.email;
// const telephoneField = form.elements.number;

// function handleSubmit(evenObject) {
    // evenObject.preventDefault();
    // console.log(evenObject)
//     const username = usernameField.value
//     const email = emailFeild.value;
//     const telphone = telephoneField.value

//     tobody.innerHTML += `
//          <tr>
//             <td>${username}</td>
//             <td>${email}</td>
//             <td>${telphone};</td>
//         </tr>

//     `
       
//     form.reset


// }
// form.onsubmit = handleSubmit
    
// let btn = document.querySelector("button")

// function wrapper() {
//     setTimeout(welcome, 3000)
// }
 


// function welcome() {
//     alert("you clicked on button")
// }
// btn.onclick = wrapper

// const box = document.getElementById("child");
// let positionX = 0;
// let positionY = 0;
// let direction = "right"

// function Animate() {
//     if(direction === "right") {
//         positionX++;
//         if(positionX >= 150) {
//             direction = "bottom"
//         }
//     }

//     if(direction === "bottom") {
//         positionY++;
//         if(positionY >= 150)
//             direction = "left"
//     }


//     if(direction === "left") {
//         (positionX <= 0)
//             direction = "top"
//     }

    
//     box.style.left = `${positionX}px`

// }
// setInterval(Animate, 10)


const box = document.getElementById("child");
let positionX = 0;
let positionY = 0;
let direction = "right";

function Animate() {
    if(direction === "right"){
        positionX++;
        if(positionX >= 150) {
            direction = "down";
        }
    }

    if(direction === "down"){
        positionY++;
        if(positionY >= 150) {
            direction = "left";
        }
    }

    if(direction === "left") {
        positionX--;
        if(positionX <= 0) {
            direction = "up";
        }
    }

    if(direction === "up") {
        positionY--;
        if(positionY <= 0) {
            direction = "right";
        }
    }

    box.style.left = `${positionX}px`
    box.style.top = `${positionY}px`
    box.style.right = `${positionX}px`
    box.style.down = `${positionY}px`
}

setInterval(Animate, 10)





