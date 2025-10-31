let person = {
  firstName: "Rahul",
  lastName: "Jadhav",
  age: 23,
  mobno: 1234567890,
  fullName: function () {
    return this.firstName + " " + this.lastName;
  },
};

console.log(person.firstName);
console.log(person["lastName"]);
console.log("Object:", person);
console.log("Full Name:", person.fullName());

person.age = 24;
console.log("Updated Age:", person.age);

delete person.mobno;
console.log("After Deleting mobno:", person);

console.log("firstName" in person);

for (let key in person) {
  console.log(key + ":", person[key]);
}

const student = {
  name: "Rahul",
  marks: {
    math: 85,
    science: 90,
    english: 78,
  },
};
console.log(student.marks.science);

const users = [
  { name: "Rahul", age: 23 },
  { name: "Anita", age: 22 },
  { name: "Sunil", age: 24 },
];
console.log(users[1].name);

for (let user of users) {
  console.log(user.name, "is", user.age, "years old.");
}

const car = {
  brand: "Toyota",
  model: "Camry",
  year: 2020,
};

console.log(Object.keys(car));
console.log(Object.values(car));
console.log(Object.entries(car));

const obj1 = { a: 1, b: 2 };
const obj2 = { c: 4 };

const mergerd = { ...obj1, ...obj2 };
console.log(mergerd);
