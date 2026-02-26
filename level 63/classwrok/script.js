let inputField = document.querySelector("textarea")
btn.onclick = function () {
    console.log("clicked")
}
function manageCharacterLimit() {
    let currentMessage = inputField.value;
    let messageLength = currentMessage.length

    if(messageLength < CharacterLimit) {
        statsP.style.color = "green"
        statsP.textContent =  "characters:" + messageLength + '/' + CharacterLimit
    }

    else{
        statsP.style.color = "red"
        statPs.textContent = "characters limit exceeded"
    }

    
}
    




document.addEventListener("keydown", handleSomething)
inputField.addEventListener('keydown', manageCharacterLimit, false)
let btn = document.querySelector("button");

function press() {
    console.log("pressed")
}

function up() {
    console.log('released')
}
btn.addEventListener("mousedown", press)
btn.addEventListener("mousedown", up )
 btn.removeEventListener("mousedown")

 let images = [
    "http://www.sololearn.com/uploads/slider/1.jpg", 
    "http://www.sololearn.com/uploads/slider/2.jpg", 
    "http://www.sololearn.com/uploads/slider/3.jpg"
];

 const nextBtn = document.getElementById("nextBtn");
 const prevBtn = document.getElementById("prevBtn")
 const image = document.querySelector("img")

 image.src = images[0];
 let currentImageIndex = 0;

 nextBtn.addEventListener("click", function(){
    image.src = images[currentImageIndex];
    currentImageIndex++;
    if(currentImageIndex === images.length - 1){
        currentImageIndex = 0
    }
 })

 prevBtn.onclick = function() {
    image.src = images[currentImageIndex];
    currentImageIndex--;
    if(currentImageIndex === 0){
        currentImageIndex = images.length - 1;
    }
 }


setItem - chamateba
getItem - wamogeba
removeItem - washla

localStorage.setItem("Name", "jon")
let Book = localStorage.getItem("Book")
console.log(Book)
localStorage.removeItem( "jon")
let name = localStorage



