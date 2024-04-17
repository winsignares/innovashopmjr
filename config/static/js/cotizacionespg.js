// Define variables for current page and cards per page
let currentPage = 1;
const cardsPerPage = 4; // Change this value based on your design

// Function to show cards for the current page
function showPage(page) {
    const cards = document.querySelectorAll('.card');
    const startIndex = (page - 1) * cardsPerPage;
    const endIndex = page * cardsPerPage;
    
    cards.forEach((card, index) => {
        if (index >= startIndex && index < endIndex) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Show initial page
showPage(currentPage);

// Event listener for next page button
document.getElementById('next-page').addEventListener('click', function() {
    const totalCards = document.querySelectorAll('.card').length;
    const totalPages = Math.ceil(totalCards / cardsPerPage);
    
    if (currentPage < totalPages) {
        currentPage++;
        showPage(currentPage);
    }
});

// Event listener for previous page button
document.getElementById('prev-page').addEventListener('click', function() {
    if (currentPage > 1) {
        currentPage--;
        showPage(currentPage);
    }
});
