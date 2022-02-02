// Function idea came from Code Institue's Blog walkthrough project
setTimeout(function () {
    let messagesContainer = document.getElementById('msg-alert');
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    messagesContainer.classList.remove('mt-2', 'mt-lg-4');
    alert.close();
}, 2500);