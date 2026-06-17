(function () {
  function currentPath() {
    return window.location.pathname.replace(/\/+$/, "/");
  }

  function docsBase() {
    var path = currentPath();
    var proIndex = path.indexOf("/pro/");
    if (proIndex >= 0) {
      return path.slice(0, proIndex + 1);
    }
    var known = [
      "getting-started/",
      "examples/",
      "commands/",
      "permissions/",
      "configuration/",
      "objectives/",
      "towers/",
      "complete-2-0-reference/",
      "stages/",
      "loot-and-rewards/",
      "event-commands/",
      "help/",
      "troubleshooting/",
      "changelog/",
      "legacy-1-0-x/"
    ];
    for (var i = 0; i < known.length; i += 1) {
      var suffix = known[i];
      if (path.endsWith("/" + suffix)) {
        return path.slice(0, path.length - suffix.length);
      }
    }
    return path;
  }

  function versionLinks() {
    var base = docsBase();
    var path = currentPath();
    var proPrefix = base + "pro/";
    var inPro = path.indexOf(proPrefix) === 0;
    var slug = "";

    if (inPro) {
      slug = path.slice(proPrefix.length);
    } else if (path.indexOf(base) === 0) {
      slug = path.slice(base.length);
    }

    if (slug === "" || slug === "/") {
      slug = "";
    }
    if (slug === "legacy-1-0-x/") {
      slug = "";
    }

    return {
      inPro: inPro,
      free: base + slug,
      pro: proPrefix + slug
    };
  }

  function mountVersionSwitch() {
    var header = document.querySelector(".md-header__inner");
    if (!header) {
      return;
    }

    var existing = document.querySelector(".version-switch");
    if (existing) {
      existing.remove();
    }

    var links = versionLinks();
    var switcher = document.createElement("nav");
    switcher.className = "version-switch";
    switcher.setAttribute("aria-label", "Documentation version");
    switcher.innerHTML = [
      '<span class="version-switch__icon" aria-hidden="true">⚔</span>',
      '<a class="version-switch__link' + (!links.inPro ? " is-active" : "") + '" href="' + links.free + '">Free</a>',
      '<a class="version-switch__link' + (links.inPro ? " is-active" : "") + '" href="' + links.pro + '">Pro</a>'
    ].join("");

    var title = header.querySelector(".md-header__title");
    if (title) {
      header.insertBefore(switcher, title);
    } else {
      header.appendChild(switcher);
    }
  }

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

  function mountEnhancements() {
    mountVersionSwitch();
    mountSupportRail();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountEnhancements);
  } else {
    mountEnhancements();
  }

  if (window.document$ && document$.subscribe) {
    document$.subscribe(mountEnhancements);
  }
})();
