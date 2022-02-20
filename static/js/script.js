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

/* 
Once the DOM has finshed loading add event listeners to some elements
*/
document.addEventListener("DOMContentLoaded", function () {
    const params = new URLSearchParams(window.location.search)
    let cuisineFilterURL = params.get('cuisine-filter');
    let locationFilterURL = params.get('location-filter');
    let searchRestaurantsURL = params.get('search-restaurants');
    let cuisineHiddenInput = document.querySelector('#cuisine-filter')
    let locationHiddenInput = document.querySelector('#location-filter')
    let searchHiddenInput = document.querySelector('#search-restaurants')
    let cuisineListItems = document.querySelectorAll('.cuisine-item');
    let locationListItems = document.querySelectorAll('.location-item');
    let dishesInput = document.querySelector('#dishes-input');
    let profileToggleBtn = document.querySelector('#btn-posts-favourites-toggle');
    let filterForm = document.querySelector('#filter-form');
    let searchInput = document.querySelector('#search-input');
    let searchBtn = document.querySelector('#search-button');

    if (cuisineFilterURL != null) {
        cuisineHiddenInput.value = cuisineFilterURL
    }

    if (locationFilterURL != null) {
        locationHiddenInput.value = locationFilterURL
    }

    if (searchRestaurantsURL != null) {
        searchHiddenInput.value = searchRestaurantsURL
        searchInput.value = searchRestaurantsURL
    }

    for (let item of cuisineListItems) {
        if (item.querySelector('.cuisine-name').textContent == cuisineFilterURL) {
            item.classList.add('active');
        } else if (item.querySelector('.cuisine-name').textContent == 'All' && cuisineHiddenInput.value == 'All') {
            item.classList.add('active');
        }
        item.addEventListener('click', function () {
            if (!item.classList.contains('active')) {
                item.classList.add('active');
            }
            document.querySelector('#cuisine-filter').value = item.querySelector('.cuisine-name').textContent
            for (let other of cuisineListItems) {
                if (other != item && other.classList.contains('active')) {
                    other.classList.remove('active');
                }
            };
            searchHiddenInput.value = searchInput.value;
            filterForm.submit();
        })
    };

    for (let item of locationListItems) {
        if (item.querySelector('.location-name').textContent == locationFilterURL) {
            item.classList.add('active');
        } else if (item.querySelector('.location-name').textContent == 'All' && locationHiddenInput.value == 'All') {
            item.classList.add('active');
        }
        item.addEventListener('click', function () {
            if (!item.classList.contains('active')) {
                item.classList.add('active');
            }
            document.querySelector('#location-filter').value = item.querySelector('.location-name').textContent
            for (let other of locationListItems) {
                if (other != item && other.classList.contains('active')) {
                    other.classList.remove('active');
                }
            };
            searchHiddenInput.value = searchInput.value;
            filterForm.submit();
        })
    };

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
        })
    }



    // CREDIT
    // Idea for these functions came from 'The Dumbfounds' YouTube video:
    // https://www.youtube.com/watch?v=sE_dccbr1I4&list=PLbpAWbHbi5rNUuLTzreCl1g212G7qgzpR&index=6
    updateDishesString();

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
        })
    }
    // END CREDIT

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
});

// CREDIT
// Idea for these functions came from 'The Dumbfounds' YouTube video:
// https://www.youtube.com/watch?v=sE_dccbr1I4&list=PLbpAWbHbi5rNUuLTzreCl1g212G7qgzpR&index=6
function addNewDish(name) {
    document.querySelector('#dishes-container').insertAdjacentHTML('beforeend',
        `<li class="dish d-flex justify-content-between my-3 py-2 px-3 bg-lighter-dark-custom text-light-custom rounded-3 box-shadow-custom">
            <span class="name text-start">${name}</span>
            <span onclick="removeDish(this)" class="btn-remove text-end" role="button">X</span>
        </li>`)
}

function updateDishesString() {
    let dishes = fetchDishArray();
    let dishesString = document.querySelector('#dishes-string');

    if (dishesString != null) {
        document.querySelector('#dishes-string').value = dishes.join(',');
    }
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