document.addEventListener('DOMContentLoaded', function() {
    const filters = document.querySelectorAll('.filter');
    
    filters.forEach(filter => {
        filter.addEventListener('click', function() {
            this.classList.toggle('selected');
            this.style.transform = 'translateY(-5px) scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
});