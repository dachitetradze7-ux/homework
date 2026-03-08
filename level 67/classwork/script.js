// const person = {
//     username: "luka",
//     occupation: "coding",
//     interests: ["ragac", "vigac"],

//     get header() {
//         return`${this.username} is ${this.occupation} and is mostly`


//     },
//     set interests (value) {
//         this.interests.unshift(value)
//     }


// }

// console.log(person.header)
// person.interests = "web development"
// console.log(person.occupation)

// class square {
//     constructor(width) {
//         this.width = width;
//         this.height = width;

//     }

//     get area () {
//         return this.width * this.height
//     }

//     set area(val) {
//         this.height = Math.sqrt(val)
//         this.width = this.height
//     }
// }
// let square1 = new square(4);
// console.log(square1.area)
// square1.area = 36
// console.log(square1.width)

class bank {
    constructor(user, email, password, balance) {
        this.user = user,
        this.email = email,
        this.password = password,
        this.balance = balance
    }
    get password {
         let displayPass = this.password.length * "#"
        for(let i = 0; i < Math.floor(this.password.length / 2); i++) {
            displayPass[i]  = this.password[i] 
        }
            
    }
       
    
}
let account1 = new bank("dachi", "ragac@mail.ru", "1234567", 100)
console.log(account1.password)

class bank {
    constructor(user, email, password, balance) {
        this.user = user,
        this.email = email,
        this.password = password,
        this.balance = balance
    }

    get balance() {
        return `balance is ${this.balance}`;
    }
    set balance(newBalance){
        if(newBalance < 0) {
            console.log("balanci unda iyos positiuri");
        }else{
            this.#balance = newBalance;
        }
    }
}

let account = new bank("dachi", "ragac@mail.ru", "1234567", 100)
console.log(Account)