// const nums = [10, 23, 56]
// for(let i in nums) {

// }

//ecmascript 6 onjects
// let lastName = "username"

// const account = {
//     username: "dachi",
//     password: "12345678"
// }
// console.log(account)

// let person = {
//     firstName: "dachi",
//     [lastName]: "tetradze"
// }
// console.log(person)

// let account = {
//     username:  "dachi",
//     balacne: 50,

//     deposit: function () {
//         this.balance += amount
//     }
// }

// account.deposit(25)
// account.deposit(50)

// console.log(account)

// const fullName = fname => fname + "!"
// console.log(fullName("dachi", "tetradze"))

// let userINput = "luka"
// let account = {
//     [userINput]: 500
// }
// let account1 = {
//     username: "luka",
//     score: 20
// }




// let account1Duplicate  = Object.assign(account1)
// console.log(account1)
// account1.username = "dachi"
// consol.log(account1Duplicate)
// const dataArr = ["weqwe", "weqr", "adsfs"]
// let [data1, data2, data3] = dataArr;
// console.log(data1)
// console.log(data2)
// console.log(data3)

// console.log(dataArr)

// const personAccount = {
//     username: "dachi",
//     dinosaur: false,
//     height: 1.80
// }
// const {username: firstName, dinosaur: humans, height} = personAccount
// console.log(firstName)
// console.log(dinosaur)
// console.log(height)
// const {username="jon doe", dinosaur=true, height} = personAccount
// console.log(username)
// console.log(dinosaur)
// console.log(height)

// console.log(personAccount)

//rest, spread
// const nums = [11, 30, 60]
// const numbers = [10, 20,  40, 60]
// const [ num1, num2, ...others] = numbers
// console.log(num1)
// console.log(num2)
// console.log(others)
function anything(...otherArguments) {
    console.log(`First: ${argument1}`)
    console.log(`Others: ${otherArguments}`)
}

anything("asdf", true, 343452, "adsrffgd")

