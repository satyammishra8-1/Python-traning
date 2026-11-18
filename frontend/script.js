// let Name = "John Doe";
// let Age = 30;
// let Occupation = "Software Developer";
// console.log(`Name: ${Name}`);
// console.log(`Age: ${Age}`);
// console.log(`Occupation: ${Occupation}`);

// let name = "satyam";
// let age = 25;
// let occupation = "Software Engineer";

// console.log(typeof name);
// console.log(typeof age);
// console.log(typeof occupation);

function changeName() {
  document.getElementById("name").innerHTML = "Your name get changed";
}

function changeColor() {
  document.getElementById("name").style.color = "red";
}
function changebgColor() {
  document.getElementById("name").style.backgroundColor = "yellow";
}


function hoverOn() {
  const heading = document.getElementById("name");
  heading.style.color = "blue";
  heading.innerHTML = "Mouse is over me!";
}

function hoverOff() {
  const heading = document.getElementById("name");
  heading.style.color = "black";
  heading.innerHTML = "Satyam Mishra";
}