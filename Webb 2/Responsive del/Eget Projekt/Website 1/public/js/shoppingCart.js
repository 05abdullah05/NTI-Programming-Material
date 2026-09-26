// Initialize an empty cart array
var cart = [];

// Function to add an item to the cart
function addToCart() {
  // Define product details
  var productName = "Armband";
  var productPrice = 19.99;

  // Add the product to the cart as an object
  cart.push({ name: productName, price: productPrice });

  // Display the updated cart
  displayCart();
}

// Function to display the cart contents
function displayCart() {
  // Get HTML elements related to cart display
  var cartItemsList = document.getElementById("cart-items");
  var subtotalElement = document.getElementById("subtotal");
  var totalElement = document.getElementById("total");

  // Clear the cart items list
  cartItemsList.innerHTML = "";

  // Initialize subtotal
  var subtotal = 0;

  // Iterate through each item in the cart
  for (var i = 0; i < cart.length; i++) {
    // Create a list item for each cart item
    var cartItem = document.createElement("li");
    cartItem.textContent = cart[i].name + " - $" + cart[i].price.toFixed(2);
    cartItemsList.appendChild(cartItem);

    // Update subtotal with the price of the current item
    subtotal += cart[i].price;
  }

  // Display the subtotal and total in the HTML
  subtotalElement.textContent = "Subtotal: $" + subtotal.toFixed(2);
  totalElement.textContent = "Total: $" + subtotal.toFixed(2);
}
