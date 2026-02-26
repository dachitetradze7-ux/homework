// const form = document.querySelector("form")

// let loggedUser = "";

// function loadData () {
//     let savedUser = localStorage.getItem("username")

//     if(savedUser) {
//         loggedUser
//     }
// }

// loadData();
// checkLoggedIn();






// const userField = form.elements.username;
// const emailFsield = form.elements.email;
// const passwordField = form.elements.password;



// function logOut()  {
//     localStorage.removeItem("username")
// }

// function checkLoggedIn() {
//     if(loggedUser) {
//        document.body.innerHTML = `
//        <h2>username: ${loggedUser}</h2>
//        <h2>email: ${localStorage.getItem("email")}</h2>
//        <h2>password: ${localStorage.getItem("password")}</h2>
//        <button onClick="${logOut()}">logout</button>
//        `
//     }
// }



// function saveData(user, email, pass) {
//     localStorage.setItem("username", user);
//     localStorage.setItem("email", email);
//     localStorage.setItem("password", pass);
// }
// function localStorage(accounts, account) {
//     localStorage.setItem("accounts", accounts)
//     localStorage.setItem("account", account)
// }



// function handleSubmit (e, randomNumber) {
//     e.preventDefault()
    
//     let username = userField.value;
//     let email = userField.value;
//     let password = userField.value;

   
//     if (username.length <= 8) {
//         alert("username must be 8 characters")
//         return
//     }

//     if(username.includes(" ")) {
//         alert("must not contains space")
//         return
//     }

//     if(password < 8) {
//         alert("password must be 8 characters long")
//         return
//     }

//   loggedUser = username
//   saveData(username, email, password)
//   alert("account created successfully")


    
// }


// form.addEventListener("submit", handleSubmit, )


// let balance = 200
// console.log(`balance ${balance}$`)

// function varTest() {
//     var x = 1;

//     if(true) {
//         var x =2 
//         console.log(x)
//     }
//     console.log(x)
// }
// varTest()


// const religious = ["Christianity", "Islam", "Buddhism", "Pagan", "Hindi", "Judaism"]
// for (let x of religious) {
//     console.log(index)
// }

// for(let char of "luka") {
//     console.log(char)
// }

let  p = document.querySelector("p")
p.addEventListener("click", (e) => {
    console.log(e + "sgsdy")
})


