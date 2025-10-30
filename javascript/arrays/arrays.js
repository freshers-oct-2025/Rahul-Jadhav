let obj = {
  myName: "Rahul",
  age: 23,
  skills: ["HTML", "CSS", "JavaScript", "Java"],
};
console.log("Object:", obj);

let arr = [10, 20, 30, 40, 50];
console.log("Array:", arr);
console.log("First Element:", arr[0]);
console.log("Array Length:", arr.length);

for (let i = 0; i < arr.length; i++) {
  console.log("Element at index", i, "is", arr[i]);
}

console.log();
console.log("Using for...of loop:");

for (let value of arr) {
  console.log("Value:", value);
}

arr[0] = 100;
console.log("Updated Array:", arr);

let arr2 = new Array("Rahul", 1, true);
console.log(arr2);

arr.push(60);
console.log("After push:", arr);

arr.pop();
console.log("After pop:", arr);

arr.shift();
console.log("After shift:", arr);

arr.unshift(5);
console.log("After unshift:", arr);

const arr3 = [10, 20, 30];

let ansArray = arr3.map((number) => {
  return number * number;
});

console.log(ansArray);

arr3.map((number, index) => {
  console.log("Index:", index, "Value:", number);
});

let arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let evenaArray = arr4.filter((num) => {
  return num % 2 === 0;
});
console.log(evenaArray);

let ans = arr3.reduce((acc, curr) => {
  return acc + curr;
});

console.log("Sum using reduce:", ans);
