// class human {
//     constructor(username) {
//         this.username = username;
//     }
//     heal () {
//         console.log(`first aid`)
//     }
// }

// class doctor extends human{
//     constructor(username, rank) {
//         super(username)

//         this.rank = rank;
//     }


//     heal () {
//         console.log(`${this.username} is currently busy`)
//     }
// }
// let person1 = new human("joe")
// person1.heal()

// let house = new doctor('Dr.house', "medical derextor")
// house.heal()

// set - wyoba, masivi ar sheileba elementebis ganmeoreba
// let myArray = [1, 2, 3, 5,]
// let mySet = new Set[myArray]
// console.log(mySet)

// mySet.add(6)
// mySet.delete(1)
// mySet.has(2)
// mySet.clear()
// console.log(mySet.size)
// console.log(mySet)

// let firstProperty = "username"
// let person = {
//     [2 + 10]: "luka"
// }
// console.log(person)
// const myMap = new Map(
//     [
//         ["username", "petre"],
//         ["giorgi", 6],
//         ["nika", 4],
//         [true, 5],
//         [4, "nika"]
//     ]
// )

// myMap.set(["key", "value"])
// console.log(myMap)
// myMap.delete(true)
// console.log(myMap.has("username"))
// console.log(myMap.keys)
// myMap.clear()

// const a = () => {console.log("a")}
// const b = () => {console.log("b")}
// let  testObject = {
//     [a]: a,
//     [b]: b
// }

// console.log(testObject)

// console.log(testMap.get(a))
// console.log(testMap.get(b))



//promise - 
// const promise = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         myNumber += 5

//     }, 4000)
//     let myNumber = 10 + 10;
//     if (myNumber === 10) {
//         resolve("promise fulfield")
//     } else {
//         reject("failed")
//     }
// }
// )

// promise, json
// .then((result) =>{
//     console.log(result)
// })
let main = document.querySelector('main');
let input = document.querySelector('input');
let button = document.querySelector('button');
button.addEventListener("click",  fetchInfo, input.value)


function  rednerInfo() {
    console.log(info)

    main.innerHTML += `
        <div>
        <h2>${info.name}</h2>
        <img src="${info.avatar_url}"/>
        <p>followers: ${info.followers}</p>
        </div>


    `

}



function fetchInfo () {
    let username = input.value;
    let promise = fetch(`https://github.com/dachitetradze7-ux?tab=repositories${username}`)
}

promise
    .then(result => result.json())
    .then(data => console.log(data)) 