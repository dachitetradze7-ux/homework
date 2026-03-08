// map, filter, forEach, reduce
// itrable - shegvilia gadavoraot ciklit
// formula -  iterable.map(function)


// let myArr = [4, 5, 6, 7, 8, 9, 100]

// function isEven (num) {
//     return num % 2 === 0;
// }
// function squareNumbers (element) {
//     return element ** 2;
// }
// let filterArr = myArr.filter(isEven)
// console.log(filterArr)

// let result = myArr.forEach(num => num  * 2)
// console.log(myArr)
// let total = myArr.reduce((preValue, currentValue,) =>{
//     return preValue + currentValue;

// })

// console.log(total)
// class myArray {
//     constructor(value) {
//         this.value = value;
//     }
// }

// function manualMap(iterable, callback) {
//     let result = [];
//     for(let item of iterable) {
//         result.push(callback(item))
//     }
//     return result

// }

// function manualFilter(iterable, callback) {
//     let result = [];
//     for(let item of iterable) {
//         if (callback(item)){
//             result.push(item);
//         }
//     }
//     return result
// }
// import Account, {getAccountEmail, getAccountFullName} from "./user.js";
// let user1 = new Account("luka", "gurgenidze", "ragaca1@gmail.com", "1234567")
// console.log(getAccountFullName(user1))
// console.log(getAccountEmail(user1))

// async & await
async function getData () {
    const response = await new Promise((resolve, reject) =>{
        setTimeout(() => {
            resolve("rwret")

        }, 2000)
    })
    // const data = await response.json();
    console.log(response)
    
}



getData()
console.log("hello goa")
