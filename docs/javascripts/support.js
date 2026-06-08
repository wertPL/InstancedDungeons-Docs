(function () {
  function mountSupportRail() {
    if (document.querySelector(".support-rail")) {
      return;
    }

    var rail = document.createElement("aside");
    rail.className = "support-rail";
    rail.innerHTML = [
      '<div class="support-rail__item" title="Discord: we_rt">',
      '  <span class="support-rail__label">Discord</span>',
      '  <span class="support-rail__value">we_rt</span>',
      '</div>',
      '<a href="https://buymeacoffee.com/we_rt" target="_blank" rel="noopener" title="Support the project">',
      '  <span class="support-rail__label">Support</span>',
      '  <span class="support-rail__value">Buy Me a Coffee</span>',
      '</a>'
    ].join("");
    document.body.appendChild(rail);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountSupportRail);
  } else {
    mountSupportRail();
  }

  if (window.document$ && document$.subscribe) {
    document$.subscribe(mountSupportRail);
  }
})();
