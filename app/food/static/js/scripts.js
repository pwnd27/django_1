const menu = document.querySelector('.menu-person')

function menu_person(event) {
    if (event.target.closest('.person')) {
        menu.classList.toggle('_active');
    }
    if (!event.target.closest('.menu-person') && !event.target.closest('.person')) {
        menu.classList.remove('_active');
    }
}

document.addEventListener('click', menu_person)