// Function to filter products based on a search term
function filterProducts(searchTerm) {
    // Get all product cards
    var productCards = document.querySelectorAll(".product-card");

    // Loop through each product card
    productCards.forEach(function (card) {
        // Extract the product title/name from the card and change it to lowercase
        var productTitle = card.querySelector(".product-brand").innerText.toLowerCase();
        // Check if the search term is present in the product title
        if (productTitle.includes(searchTerm)) {
            // If the search term is present display the product card
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}

// Add an event listener to the search input for real-time filtering
document.getElementById("searchInput").addEventListener("input", function () {
    // Get the current value of the search input
    var searchTerm = this.value.toLowerCase();
    // Call the filterProducts function with the current search term
    filterProducts(searchTerm);
});
