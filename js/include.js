document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('[data-include]').forEach(element => {
        const file = element.getAttribute('data-include').replace(/^\//, ''); // 移除开头的斜杠
        fetch(file)
            .then(response => response.text())
            .then(html => {
                element.innerHTML = html;
            })
            .catch(error => console.error('Error loading component:', error));
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const profileImg = document.querySelector('#profile');
    if (profileImg) {
        const img = new Image();
        img.onload = function() {
            profileImg.classList.add('loaded');
        };
        img.src = profileImg.src;
    }
});