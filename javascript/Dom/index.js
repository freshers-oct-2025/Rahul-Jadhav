document.getElementById("fpara");
document.getElementById("fheading");
document.getElementsByClassName("textMatter");
document.querySelector("fpara");
document.querySelectorAll(".textMatter");

let element = document.getElementById("fdiv");
console.log(element.textContent);

let heading = document.createElement("h2");
heading.textContent = "This is a new heading";

let body = document.querySelector("body");
body.appendChild(heading);
