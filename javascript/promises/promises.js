let promise = new Promise((resolve, reject) => {
  let success = true;
  if (success) {
    resolve("Promise Resolved Successfully");
  } else {
    reject("Promise Rejected");
  }
});
Promise.then((message) => {
  console.log(message);
}).catch((error) => {
  console.log(error);
});
