let firstName = "Rahul";
let lastName = "Jadhav";

let text = `Welcome ${firstName}, ${lastName}!`;
document.getElementById("demo").innerHTML = text;

let msg = "HELLO WORLD";
console.log(msg.charAt(0));
console.log(msg.charCodeAt(0));

document.getElementById("demo1").innerHTML = msg.charAt(0);
document.getElementById("demo2").innerHTML = msg.charCodeAt(0);
console.log(msg.concat(" from Thinkitive"));

let str1 = "Hello";
let str2 = "World";
console.log(str1.concat(" ", str2));
document.getElementById("demo3").innerHTML = str1.concat(" ", str2);

let str = "   Hello World!   ";
console.log(str.trim());
document.getElementById("demo4").innerHTML = str.trim();

let phrase = "JavaScript is fun";
console.log(phrase.indexOf("is"));
console.log(phrase.lastIndexOf("n"));

let sample = "  JavaScript, strings, testing  ";

console.log(sample.toLowerCase());
console.log(sample.toUpperCase());

console.log(sample.slice(2, 12));
console.log(sample.substring(2, 12));

console.log(sample.includes("strings"));
console.log(sample.startsWith("  Java"));
console.log(sample.endsWith("ing  "));

console.log("ha".repeat(3));

console.log(sample.trim().split(","));
console.log("a b c".split(" "));
