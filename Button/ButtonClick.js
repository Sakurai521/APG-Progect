document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll("button");

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            if (!button.classList.contains("clicked")) {
                button.classList.add("clicked");

                setTimeout(function () {
                    button.classList.remove("clicked");
                }, 1000);
            }
        });
    });
});
