document.getElementById('search-btn').addEventListener('click', function() {
    let searchInput = document.querySelector('.search').value;
    let section = document.getElementById('section-select').value;
    let location = document.getElementById('location-select').value;
    let priceFrom = document.getElementById('price-from').value;
    let priceTo = document.getElementById('price-to').value;
    let forSale = document.getElementById('for-sale').checked;
    let wanted = document.getElementById('wanted').checked;

    // Prepare the data to be sent to the server
    let requestData = {
        searchInput: searchInput,
        section: section,
        location: location,
        priceFrom: priceFrom,
        priceTo: priceTo,
        forSale: forSale,
        wanted: wanted
    };

    // Send the data to the server using fetch
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Ensure to include CSRF token
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
        // Handle the response data, update UI, etc.
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Get the CSRF token if found
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
