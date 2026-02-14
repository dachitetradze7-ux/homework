const andOperation1 = document.getElementById("and1");
const andOperation2 = document.getElementById("and2");
let andBtn = document.getElementById("andSend");
const andResult = document.getElementById("andRes");

andBtn.onclick  = function () {
    let val1 = andOperation1.checked;
    let val2 = andOperation2.checked;
    let logicalResult = val1 && val2;
    andResult.textContent = 'result of operation: ' + String(val1) + String(val2)

}



