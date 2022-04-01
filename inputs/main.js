function init() {
    // with a small delay, scroll to the top of the page, so that the
    // header remains in view after clicking an anchor
    let scrollToHeader = function(event) {
        setTimeout(function() {
        window.scrollTo(0, 0);
        }, 3);
    };
    // for every <a> element, scroll to header after it's clicked
    document.querySelectorAll("a").forEach(function(el) {
        el.addEventListener("click", scrollToHeader);
    });
}
