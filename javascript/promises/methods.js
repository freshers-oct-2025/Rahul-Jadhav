const p1 = Promise.resolve("A done");
const p2 = Promise.resolve("B done");
const p3 = Promise.reject("C failed");

Promise.all([p1, p2])
  .then((results) => console.log(results))
  .catch((error) => console.error(error));

Promise.all([p1, p3])
  .then((results) => console.log(results))
  .catch((error) => console.error(error));

const p4 = Promise.resolve("Success");
const p5 = Promise.reject("Failed");

Promise.allSettled([p4, p5]).then((results) => console.log(results));

const fast = new Promise((res) => setTimeout(res, 100, "Fast"));
const slow = new Promise((res) => setTimeout(res, 300, "Slow"));

Promise.race([fast, slow]).then((result) => console.log(result));

const p6 = Promise.reject("Failed 1");
const p7 = Promise.resolve("Success!");
const p8 = Promise.reject("Failed 2");

Promise.any([p6, p7, p8])
  .then((result) => console.log(result))
  .catch((err) => console.error(err));
