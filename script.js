// script.js
document
  .getElementById("descriptionForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from reloading the page

    const description = document.getElementById("description").value;

    fetch("/generate_3d_model", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ description: description }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          alert(data.message); // For now, we'll just alert the user
          // Future: Here, you would load and display the generated 3D model
        } else {
          alert(data.message);
        }
      })
      .catch((error) => console.error("Error:", error));
  });
