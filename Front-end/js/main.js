(function () {
  function attachNav() {
    
    var anchors = document.querySelectorAll(
      'a[href$="explorasi.html"], a[href$="generate-page.html"], a[href$="tabel-periodik.html"]'
    );

    anchors.forEach(function (a) {
      a.addEventListener("click", function (e) {
        var href = a.getAttribute("href");
        if (!href) return;

        
        e.preventDefault();

        
        var variant = "slide"; 
        if (href.endsWith("explorasi.html")) variant = "reveal";
        if (href.endsWith("tabel-periodik.html")) variant = "mosaic";

        
        var coords = { x: e.clientX, y: e.clientY };

        
        if (window.navigateWithTransition) {
          window.navigateWithTransition(href, 750, variant, coords);
        } else {
          
          window.location.href = href;
        }
      });
    });
  }

  
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", attachNav);
  } else {
    attachNav();
  }
})();