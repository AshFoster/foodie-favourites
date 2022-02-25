// Global Variables
const params = new URLSearchParams(window.location.search);
let searchHiddenInput = document.querySelector('#search-restaurants');
let searchInput = document.querySelector('#search-input');
let filterForm = document.querySelector('#filter-form');

// CREDIT
// Function idea came from Code Institue's Blog walkthrough project
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    let messagesAlert = document.getElementById('msg-alert');

    if (messagesAlert != null) {
        messagesAlert.classList.remove('mt-3');
    }
    alert.close();
}, 2500);
// END CREDIT

/* 
Sets the value of the cuisine related hidden input on restaurants.html based on url value,
adds 'active' class to the related cuisine list item, and adds 'click' event listeners to all
of the cuisine list items.
*/
function setCuisineFilter() {
    let cuisineFilterURL = params.get('cuisine-filter');
    let cuisineHiddenInput = document.querySelector('#cuisine-filter');
    let cuisineListItems = document.querySelectorAll('.cuisine-item');

    if (cuisineFilterURL != null) {
        cuisineHiddenInput.value = cuisineFilterURL;
    }

    for (let item of cuisineListItems) {

        // Add 'active' class to cuisine item which matches cuisine in url when page is loaded
        if (item.querySelector('.cuisine-name').textContent == cuisineFilterURL) {
            item.classList.add('active');
        } else if (item.querySelector('.cuisine-name').textContent == 'All' && cuisineHiddenInput.value == 'All') {
            item.classList.add('active');
        }
        item.addEventListener('click', function () {

            // Add 'active' class to selected item
            if (!item.classList.contains('active')) {
                item.classList.add('active');
            }

            document.querySelector('#cuisine-filter').value = item.querySelector('.cuisine-name').textContent;

            // Remove 'active' class from other items
            for (let other of cuisineListItems) {
                if (other != item && other.classList.contains('active')) {
                    other.classList.remove('active');
                }
            }
            searchHiddenInput.value = searchInput.value;
            filterForm.submit();
        });
    }
}

/* 
Sets the value of the location related hidden input on restaurants.html based on url value,
adds 'active' class to the related location list item, and adds 'click' event listeners to all
of the location list items.
*/
function setLocationFilter() {
    let locationFilterURL = params.get('location-filter');
    let locationHiddenInput = document.querySelector('#location-filter');
    let locationListItems = document.querySelectorAll('.location-item');

    if (locationFilterURL != null) {
        locationHiddenInput.value = locationFilterURL;
    }

    for (let item of locationListItems) {

        // Add 'active' class to location item which matches location in url when page is loaded
        if (item.querySelector('.location-name').textContent == locationFilterURL) {
            item.classList.add('active');
        } else if (item.querySelector('.location-name').textContent == 'All' && locationHiddenInput.value == 'All') {
            item.classList.add('active');
        }

        item.addEventListener('click', function () {

            // Add 'active' class to selected item
            if (!item.classList.contains('active')) {
                item.classList.add('active');
            }
            document.querySelector('#location-filter').value = item.querySelector('.location-name').textContent;

            // Remove 'active' class from non-selected items
            for (let other of locationListItems) {
                if (other != item && other.classList.contains('active')) {
                    other.classList.remove('active');
                }
            }
            searchHiddenInput.value = searchInput.value;
            filterForm.submit();
        });
    }
}

/* 
Sets the value of the search related hidden input on restaurants.html based
on the search value in the url, then adds event listeners to the search bar
and search button so the search related hidden input is given the value contained 
in the search bar, then submits the filter form.
*/
function setSearchBar() {
    let searchRestaurantsURL = params.get('search-restaurants');
    let searchHiddenInput = document.querySelector('#search-restaurants');
    let searchBtn = document.querySelector('#search-button');

    if (searchRestaurantsURL != null) {
        searchHiddenInput.value = searchRestaurantsURL;
        searchInput.value = searchRestaurantsURL;
    }

    if (searchInput != null) {
        searchInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                searchHiddenInput.value = searchInput.value;
                filterForm.submit();
            }
        });

        searchInput.addEventListener('search', function () {
            searchHiddenInput.value = searchInput.value;
            filterForm.submit();
        });
    }

    if (searchBtn != null) {
        searchBtn.addEventListener('click', function () {
            searchHiddenInput.value = searchInput.value;
            filterForm.submit();
        });
    }
}

/* 
CREDIT
Idea for these functions came from 'The Dumbfounds' YouTube video:
https://www.youtube.com/watch?v=sE_dccbr1I4&list=PLbpAWbHbi5rNUuLTzreCl1g212G7qgzpR&index=6
*/
/* 
Adds event listeners to 'dishes input' and 'add dishes button' on add_restaurant.html so the
value of the input element is added to a list element when the events occur.
*/
function setAddDish() {
    let dishesInput = document.querySelector('#dishes-input');
    let addDishBtn = document.querySelector('#add-dish-button');

    if (dishesInput != null) {
        dishesInput.addEventListener('keydown', function (e) {
            if (e.keyCode !== 13) {
                return;
            }

            e.preventDefault();

            let dishName = this.value;
            this.value = '';
            addNewDish(dishName);
            updateDishesString();
        });

        addDishBtn.addEventListener('click', function (e) {
            e.preventDefault();

            let dishName = dishesInput.value;
            dishesInput.value = '';
            addNewDish(dishName);
            updateDishesString();
        });
    }
}

// Adds new list element with specified name
function addNewDish(name) {
    document.querySelector('#dishes-container').insertAdjacentHTML('beforeend',
        `<li class="dish d-flex justify-content-between my-3 py-2 px-3 bg-lighter-dark-custom text-light-custom rounded-3 box-shadow-custom">
            <span class="name text-start">${name}</span>
            <span onclick="removeDish(this)" class="btn-remove text-end" role="button">X</span>
        </li>`);
}

// Updates 'dishes string' with all list element values
function updateDishesString() {
    let dishes = fetchDishArray();
    let dishesString = document.querySelector('#dishes-string');

    if (dishesString != null) {
        dishesString.value = dishes.join(',');
    }
}

// Creates and returns an array of all list element values
function fetchDishArray() {
    let dishes = [];

    document.querySelectorAll('.dish').forEach(function (e) {
        let name = e.querySelector('.name').textContent;

        if (name == '') {
            return;
        }

        dishes.push(name);
    });

    return dishes;
}

// Removes a specified list element
function removeDish(e) {
    e.parentElement.remove();
    updateDishesString();
}
// END CREDIT

/* 
Set Profile Toggle adds an event listener to the 'profile toggle button' on profile.html
which updates the value of the profile related hidden input element and submits the profile 
toggle form.
*/
function setProfileToggle() {
    let profileToggleBtn = document.querySelector('#btn-posts-favourites-toggle');

    if (profileToggleBtn != null) {
        profileToggleBtn.addEventListener('click', function () {
            let profileToggleURL = params.get('posts-favourites-toggle');
            let profileHiddenInput = document.querySelector('#posts-favourites-toggle');

            if (profileToggleURL == 'Posts' || profileToggleURL == null) {
                profileHiddenInput.value = 'Favourites';
            } else {
                profileHiddenInput.value = 'Posts';
            }
            document.querySelector('#profile-toggle-form').submit();
        });
    }
}


/* 
Once the DOM has finshed loading call necessary functions
*/
document.addEventListener("DOMContentLoaded", function () {

    setCuisineFilter();

    setLocationFilter();

    setSearchBar();

    updateDishesString();

    setAddDish();

    setProfileToggle();
});