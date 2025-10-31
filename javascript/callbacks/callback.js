function processData(data) {
  console.log("Processing data: " + data);
}

function deleteData(data) {
  console.log("Deleting data: " + data);
}

function func(methodName) {
  methodName("Rahul");
}

func(deleteData);
