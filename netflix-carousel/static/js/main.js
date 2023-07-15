document.addEventListener('DOMContentLoaded', () => {
    const scrollContainer = document.querySelector('.carousel');
    const leftButton = document.getElementById('left');
    const rightButton = document.getElementById('right');

    leftButton.addEventListener('click', () => {
        scrollContainer.scrollBy({
            left: -510,
            behavior: 'smooth'
        });
    });

    rightButton.addEventListener('click', () => {
        scrollContainer.scrollBy({
            left: 510,
            behavior: 'smooth'
        });
    });
});
function sub() {
    page_size = documnent.getElementById('trans');
    var url = "http://127.0.0.1:5000?page_size" + page_size;
    window.location.href = url; 
}
    const carousel = document.querySelector('.carousel');

    function autoScroll() {
        carousel.scrollLeft += 2; // Adjust the scroll speed as needed
    }
    
    let scrollInterval = setInterval(autoScroll,5); // Adjust the scroll interval as needed
    
    carousel.addEventListener('mouseenter', () => {
        clearInterval(scrollInterval);
    });
    
    carousel.addEventListener('mouseleave', () => {
        scrollInterval = setInterval(autoScroll, 5);
    });