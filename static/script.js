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

    const menu = document.getElementById('file-upload');
    if (menu) {
        menu.addEventListener('change', function() {
            const fileName = this.files[0] ? this.files[0].name : '';
            document.getElementById('filename').innerText = fileName;
        });
    }

    const form = document.querySelector('form'); 
    const restrictions = document.getElementById('restrictions');
    form.addEventListener('submit', function() {
        const selected = Array.from(document.querySelectorAll('.filter.selected')).map(filter => filter.innerText).join(', ');
        if(restrictions){
            restrictions.value = selected;
        }
    });
});