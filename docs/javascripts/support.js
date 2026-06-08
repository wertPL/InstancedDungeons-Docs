(function () {
  function mountSupportRail() {
    if (document.querySelector(".support-rail")) {
      return;
    }

    var rail = document.createElement("aside");
    rail.className = "support-rail";
    rail.innerHTML = [
      '<a href="https://modrinth.com/plugin/instanced-dungeon" target="_blank" rel="noopener" title="Download on Modrinth">',
      '  <span class="support-rail__label">Download</span>',
      '  <span class="support-rail__value">Modrinth</span>',
      '</a>',
      '<a href="https://www.spigotmc.org/resources/instanced-dungeon.132724/" target="_blank" rel="noopener" title="View on SpigotMC">',
      '  <span class="support-rail__label">Plugin Page</span>',
      '  <span class="support-rail__value">SpigotMC</span>',
      '</a>',
      '<a href="https://discord.com/invite/sD4HvQh8P4" target="_blank" rel="noopener" title="Join the Discord">',
      '  <span class="support-rail__label">Discord</span>',
      '  <span class="support-rail__value">Join Server</span>',
      '</a>',
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
