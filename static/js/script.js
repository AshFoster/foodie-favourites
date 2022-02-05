// CREDIT
// Function idea came from Code Institue's Blog walkthrough project
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    let messagesAlert = document.getElementById('msg-alert');

    if (messagesAlert != null) {
        messagesAlert.classList.remove('mt-2');
    }
    alert.close();
}, 2500);
// END CREDIT


// CREDIT
// Idea for this section of code came from 'The Dumbfounds' YouTube video:
// https://www.youtube.com/watch?v=sE_dccbr1I4&list=PLbpAWbHbi5rNUuLTzreCl1g212G7qgzpR&index=6
document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('#dishes-input').addEventListener('keydown', function (e) {
        if (e.keyCode !== 13) {
            return;
        }

        e.preventDefault();

        let dishName = this.value;
        this.value = '';
        addNewDish(dishName);
        updateDishesString();
    })
});

function addNewDish(name) {
    document.querySelector('#dishes-container').insertAdjacentHTML('beforeend',
        `<li class="dish d-flex justify-content-between my-3 py-2 px-3 bg-lighter-dark-custom text-light-custom rounded-3 box-shadow-custom">
            <span class="name text-start">${name}</span>
            <span onclick="removeDish(this)" class="btn-remove text-end" role="button">X</span>
        </li>`)
}

function updateDishesString() {
    dishes = fetchDishArray();
    document.querySelector('#dishes-string').value = dishes.join(',')
}

function fetchDishArray() {
    let dishes = [];

    document.querySelectorAll('.dish').forEach(function (e) {
        let name = e.querySelector('.name').innerHTML;

        if (name == '') {
            return;
        }

        dishes.push(name);
    })

    return dishes;
}

function removeDish(e) {
    e.parentElement.remove();
    updateDishesString();
}
// END CREDIT