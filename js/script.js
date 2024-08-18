document.addEventListener("DOMContentLoaded", function() {
    const descriptionContainer = document.getElementById("descriptionContainer");
    const openButton = document.getElementById("openButton");
    const closeButton = document.getElementById("closeDescription");

    openButton.addEventListener("click", function() {
        descriptionContainer.style.display = "block";
        openButton.style.display = "none";
    });

    closeButton.addEventListener("click", function() {
        descriptionContainer.style.display = "none";
        openButton.style.display = "block";
    });
});
