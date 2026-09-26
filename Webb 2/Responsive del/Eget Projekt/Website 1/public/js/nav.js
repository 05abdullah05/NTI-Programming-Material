// Define a function to create and populate the footer dynamically
const createNav = () => {
    let nav = document.querySelector('.navbar');

    // Set the innerHTML of the footer with dynamic HTML content
    nav.innerHTML = `  
        <div class="nav">
            <img src="img/dark-logo.png" class="brand-logo" alt="">
            <div class="nav-items">
            <div class="search-container women-search">
                <input type="text" id="searchInput" placeholder="Search products...">
                <button id="searchBtn" onclick="searchProducts()">Search</button>
            </div>         
                <a href="login.html"><img src="img/user.png" alt=""></a>
                <a href="cart.html"><img src="img/cart.png" alt=""></a>
            </div>
        </div>
        <ul class="links-container">
            <li class="links-item"><a href="index.html" class="link">home</a></li>
            <li class="links-item"><a href="women.html" class="link">women</a></li>
            <li class="links-item"><a href="product.html" class="link">men</a></li>
            <li class="links-item"><a href="kids.html" class="link">kids</a></li>
            <li class="links-item"><a href="404.html" class="link">accessories</a></li>
        </ul>
    `;


};

// Invoke the function to generate and insert the footer content
createNav();


