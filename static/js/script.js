// Function idea came from Code Institue's Blog walkthrough project
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    document.getElementById('msg-alert').classList.remove('mt-2');
    alert.close();
}, 2500);