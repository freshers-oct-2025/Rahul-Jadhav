function printCounting() {
  for (let i = 1; i <= 100; i++) {
    console.log(i);
  }
}

printCounting();

function printNumber(num) {
  console.log("Number is:", num);
}

printNumber(10);

function getMyName(firstName, lastName) {
  let fullName = firstName + " " + lastName;
  return fullName;
}

let fullName = getMyName("Rahul", "Jadhav");
console.log("Full Name:", fullName);

let getExp = (x, y) => {
  let ans = x ** y;
  return ans;
};
console.log("Exponentiation:", getExp(2, 3));
