document.getElementById("customer").addEventListener("click", loadCustomer);
console.log("customer button clicked");
document.getElementById("images").addEventListener("click", loadImages);
console.log("images button clicked");

function loadCustomer() {
  fetch("https://playground.mockoon.com/customers")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      console.log(data.name);
      const tableBody = document.getElementById("customer-table-body");
      tableBody.innerHTML = "";
      data.forEach((customer) => {
        const row = `

                <tr>
                    <td>${customer.name}</td>
                    <td>${customer.email}</td>
                    <td>${customer.phone}</td>
                </tr>
            `;

        tableBody.innerHTML = tableBody.innerHTML + row;
      });
    })
    .catch((error) => console.error("Error loading customer data:", error));
}

async function loadImages() {
  await fetch("https://playground.mockoon.com/photos")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      const tableBody = document.getElementById("image-table-body");
      tableBody.innerHTML = "";
      data.forEach((image) => {
        const row = `
            
                        <tr>
                            <td>${image.caption}</td>
                            <td>${image.likes}</td>
                            <td>${image.url}</td>
                        </tr>
                    `;
        tableBody.innerHTML = tableBody.innerHTML + row;
      });
    })
    .catch((error) => console.error("Error loading images:", error));
}
