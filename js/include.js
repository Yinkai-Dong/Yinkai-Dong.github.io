document.addEventListener('DOMContentLoaded', function() {
    // Load all HTML includes
    document.querySelectorAll('[data-include]').forEach(element => {
        const file = element.getAttribute('data-include');
        fetch(file)
            .then(response => response.text())
            .then(html => {
                element.innerHTML = html;
            })
            .catch(error => console.error('Error loading component:', error));
    });
});