// Define a function to create and populate the footer dynamically
const createFooter = ()=> {
    let footer = document.querySelector('footer');

    // Set the innerHTML of the footer with dynamic HTML content
    footer.innerHTML = `
    <div class="footer-content">
    <img src="img/dark-logo.png" class="logo" alt="">
    <div class="footer-ul-bcontent">
        <ul class="category">
            <li class="category-title">men</li>
            <li><a href="#" class="footer-link">t-shirts</a></li>
            <li><a href="#" class="footer-link">sweatshirts</a></li>
            <li><a href="#" class="footer-link">shirts</a></li>
            <li><a href="#" class="footer-link">t-shirts</a></li>
            <li><a href="#" class="footer-link">jeans</a></li>
            <li><a href="#" class="footer-link">trousers</a></li>
            <li><a href="#" class="footer-link">shoes</a></li>
            <li><a href="#" class="footer-link">casuals</a></li>
            <li><a href="#" class="footer-link">formals</a></li>
            <li><a href="#" class="footer-link">watch</a></li>
        </ul>
        <ul class="category">
            <li class="category-title">women</li>
            <li><a href="#" class="footer-link">t-shirts</a></li>
            <li><a href="#" class="footer-link">sweatshirts</a></li>
            <li><a href="#" class="footer-link">shirts</a></li>
            <li><a href="#" class="footer-link">t-shirts</a></li>
            <li><a href="#" class="footer-link">jeans</a></li>
            <li><a href="#" class="footer-link">trousers</a></li>
            <li><a href="#" class="footer-link">shoes</a></li>
            <li><a href="#" class="footer-link">casuals</a></li>
            <li><a href="#" class="footer-link">formals</a></li>
            <li><a href="#" class="footer-link">watch</a></li>
        </ul>
    </div>

</div>


<p class="footer-title"> about company</p>
<p class="info">Embark on a captivating journey as you delve into the 
rich narrative that defines AQStyleHub. Here, the 
seamless fusion of a profound passion for fashion intertwines with a legacy of 
unparalleled style. We invite you to explore the chapters of our story, where each 
stitch and fabric weave together to narrate the evolution of our brand.

!</p>
<p class="info">support emails - help@aqstylehub.com,
    customersupport@aqstylehub.com</p> 
<p class="info">telephone - 180 00 00 001, 180 00 00 002</p> 
<div class="footer-social-container"> 
    <div>
        <a href="#" class="social-link">terms & services</a>
        <a href="#" class="social-link">privacy page</a>
    </div>
    <div>
        <a href="#" class="social-link">instagram</a>
        <a href="#" class="social-link">facebook</a>
        <a href="#" class="social-link">twitter</a>

    </div>
</div>
<p class="footer-credit">AQStyleHub - Supreme Fashion Echelon</p>
    `;
}

// Invoke the function to generate and insert the footer content
createFooter()