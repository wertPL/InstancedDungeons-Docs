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
      "spawners-and-mobs/",
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

    var freeSlug = slug;
    if (slug === "spawners-and-mobs/") {
      freeSlug = "loot-and-rewards/";
    }

    return {
      base: base,
      inPro: inPro,
      free: base + freeSlug,
      pro: proPrefix + slug
    };
  }

  function topNavTarget(label) {
    switch (label) {
      case "Home":
        return "";
      case "Start":
        return "getting-started/";
      case "Configuration":
        return "configuration/";
      case "Systems":
        return "stages/";
      case "Help":
        return "help/";
      default:
        return null;
    }
  }

  function updateVersionNavigation() {
    var links = versionLinks();
    var path = currentPath();

    document.querySelectorAll(".md-tabs__link").forEach(function (link) {
      var label = link.textContent.trim();
      var item = link.closest(".md-tabs__item");
      if (!item) {
        return;
      }

      item.classList.remove("is-hidden-by-version");

      if (label === "Pro Version") {
        item.classList.add("is-hidden-by-version");
        return;
      }

      if (links.inPro && label.indexOf("Legacy") === 0) {
        item.classList.add("is-hidden-by-version");
        return;
      }

      var target = topNavTarget(label);
      if (target === null) {
        return;
      }

      var versionPrefix = links.inPro ? "pro/" : "";
      var href = links.base + versionPrefix + target;
      if (links.inPro && label === "Systems") {
        href = links.base + "pro/spawners-and-mobs/";
      }
      link.href = href;
      link.classList.remove("md-tabs__link--active");

      if ((target === "" && path === href) || (target !== "" && path.indexOf(href) === 0)) {
        link.classList.add("md-tabs__link--active");
      }
    });
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
    switcher.dataset.active = links.inPro ? "pro" : "free";
    switcher.setAttribute("aria-label", "Documentation version");
    switcher.innerHTML = [
      '<span class="version-switch__thumb" aria-hidden="true"></span>',
      '<a class="version-switch__link' + (!links.inPro ? " is-active" : "") + '" data-version="free" href="' + links.free + '">Free</a>',
      '<a class="version-switch__link' + (links.inPro ? " is-active" : "") + '" data-version="pro" href="' + links.pro + '">Pro</a>'
    ].join("");

    switcher.querySelectorAll(".version-switch__link").forEach(function (link) {
      link.addEventListener("click", function (event) {
        handleVersionSwitch(event, link, switcher);
      });
    });

    var title = header.querySelector(".md-header__title");
    if (title) {
      header.insertBefore(switcher, title);
    } else {
      header.appendChild(switcher);
    }
  }

  function replaceMainContent(html, href) {
    var parsed = new DOMParser().parseFromString(html, "text/html");
    var nextMain = parsed.querySelector(".md-main");
    var currentMain = document.querySelector(".md-main");

    if (!nextMain || !currentMain) {
      window.location.href = href;
      return;
    }

    document.title = parsed.title || document.title;
    currentMain.replaceWith(document.importNode(nextMain, true));
    window.history.pushState({ versionSwitch: true }, "", href);
    window.scrollTo({ top: 0, behavior: "auto" });
    mountEnhancements();
  }

  function handleVersionSwitch(event, link, switcher) {
    var version = link.getAttribute("data-version");
    var href = link.href;

    if (!version || !href || href === window.location.href) {
      return;
    }

    event.preventDefault();
    switcher.dataset.active = version;
    document.documentElement.classList.add("is-version-transitioning");

    window.fetch(href, { credentials: "same-origin" })
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Unable to load documentation page.");
        }
        return response.text();
      })
      .then(function (html) {
        replaceMainContent(html, href);
      })
      .catch(function () {
        window.location.href = href;
      });
  }

  function mountEnhancements() {
    document.documentElement.classList.remove("is-version-transitioning");
    document.querySelectorAll(".support-rail").forEach(function (rail) {
      rail.remove();
    });
    mountVersionSwitch();
    updateVersionNavigation();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountEnhancements);
  } else {
    mountEnhancements();
  }

  if (window.document$ && document$.subscribe) {
    document$.subscribe(mountEnhancements);
  }

  window.addEventListener("popstate", function () {
    window.location.reload();
  });
})();
