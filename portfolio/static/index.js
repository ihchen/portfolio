var dropdownLinks = document.getElementsByClassName('dropdown');

for(var i = 0; i < dropdownLinks.length; i++) {
    dropdownLinks[i].addEventListener("click", function() {
        this.classList.toggle('open');
    });
    dropdownLinks[i].addEventListener("mouseenter", function() {
        this.classList.add('open');
    });
    dropdownLinks[i].addEventListener("mouseleave", function() {
        this.classList.remove('open');
    });
}
