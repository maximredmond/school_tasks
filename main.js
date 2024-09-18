const imageContainer = document.getElementById("images");

imageContainer.innerHTML = '<img src="R.jpeg" width="500" style="float: right; margin-right: 100px;">';

let counter = 0;

function nextImage() {
    counter = counter + 1;
    if (counter % 4 == 0) {
        imageContainer.innerHTML = '<img src="1.jpeg" width="500">';
    } else if (counter % 4 == 1) {
        imageContainer.innerHTML = '<img src="2.jpeg" width="500">';
    } else if (counter % 4 == 2) {
        imageContainer.innerHTML = '<img src="3.jpeg" width="500">';
    } else if (counter % 4 == 3) {
        imageContainer.innerHTML = '<img src="4.jpeg" width="500">';
    }
}