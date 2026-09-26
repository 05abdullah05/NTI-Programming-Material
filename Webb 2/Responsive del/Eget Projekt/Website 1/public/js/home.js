// Select all elements with the class 'product-container'
const productContainers = document.querySelectorAll('.product-container');

const nxtBtns = document.querySelectorAll('.nxt-btn');

const preBtns = document.querySelectorAll('.pre-btn');

// Iterate over each 'product-container'
productContainers.forEach((item, i) => {
    // Get the dimensions of the container
    let containerDimensions = item.getBoundingClientRect();
    
    // Extract the width of the container
    let containerWidth = containerDimensions.width;

    // Add click event listener to 'nxt-btn' for scrolling right
    nxtBtns[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    });

    preBtns[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    });
});
