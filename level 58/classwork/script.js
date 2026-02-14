// let book  = {
//     title: "green mile",
//     author: "vigaca "
//     getAuthor() {

//     }
// }
// console.log(book["title"])
// console.log(book["author"])

// console.log(book.length)


// function Book(title, author, year, pages) {
//     this.title = title;
//     this.author = author;
//     this.year = year;
//     this.pages = pages;

// }
// ww2 =  new Book("world war 2", "hitler", 1939, 500)



// sovietUnion = new Book("The Soviet Union", "stalin", 1922, 400)

// console.log(ww2.title)

// console.log(ww2.pages)
// console.log(ww2.author)
// console.log(ww2.year)

// console.log(sovietUnion.pages)
// console.log(sovietUnion.year)
// console.log(sovietUnion.title)
// console.log(sovietUnion.author)

// var Dachi = {
//     name: "Dachi",
//     age: 16

// let book = {
//     title: "batman",
//     author: "vigaca ucnobi"
// }

// stack = gamoiyeneba cvladebistvis da functions gamozaxebistvis 
// heap  = didi moculoba da sanam ar wavshlit darcheba

// let bookName = {
//     title: "batmani"

// }

// let secondBookName = bookName;
// bookName.title = "superman"

// console.log(bookName)
// console.log(secondBookName)


// let languages  = ["html", "css", "js"]
// languages.push("python")
// console.log(languages)
// languages.pop(2)


// let cities = {
//     [0]: "samtredia",
//     [1]: "sachxere",
//     [3]: "mcxeta"
// }

let name = document.getElementById("name");
let password = document.getElementById("password");
let email = document.getElementById("email");
let button = document.getElementById("button");

button.onclick = function() {
    let name = document.getElementById("name").value;
    let password = document.getElementById("password").value;
    let email = document.getElementById("email").value;
    

}

function arr(name, passowrd, email) {
    this.arrName = name;
    this.arrPassword = password;
    this.arrEmail = email;
}

let database = []
    database.push(new arr(name, email, password))

