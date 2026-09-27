// Select all product images and the image slider container
const productImages = document.querySelectorAll(".product-images img");
const productImageSlide = document.querySelector(".image-slider");

// Initialize the index of the active image slide
let activeImageSlide = 0;

// Event listeners for product image clicks
productImages.forEach((item, i) => {
    item.addEventListener('click', () => {
        // Update the active image slide and apply styling changes
        productImages[activeImageSlide].classList.remove('active');
        item.classList.add('active');
        productImageSlide.style.backgroundImage = `url('${item.src}')`;
        activeImageSlide = i;
    })

})

// Select all size radio buttons and initialize the index of the checked button
const sizeBtns = document.querySelectorAll('.size-radio-btn');
let checkedBtn = 0;

// Event listeners for size button clicks
sizeBtns.forEach((item, i) => {
    item.addEventListener('click', () => {
        // Update the checked size button and apply styling changes
        sizeBtns[checkedBtn].classList.remove('check');
        item.classList.add('check');
        checkedBtn = i;
    });
});


// This code bit is already commented in kids.js and women.js since this is copied from them!!!
function filterProducts(searchTerm) {
    var productCards = document.querySelectorAll(".product-card");

    productCards.forEach(function (card) {
        var productTitle = card.querySelector(".product-brand").innerText.toLowerCase();

        if (productTitle.includes(searchTerm)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}

document.getElementById("searchInput").addEventListener("input", function () {
    var searchTerm = this.value.toLowerCase();
    filterProducts(searchTerm);
});

