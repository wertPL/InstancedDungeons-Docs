(function () {
  var tocScrollBound = false;
  var navigationToken = 0;
  var transitionDelay = 210;

  function currentPath() {
    return window.location.pathname.replace(/\/+$/, "/");
  }

  function docsBase() {
    var scripts = document.getElementsByTagName("script");
    for (var i = scripts.length - 1; i >= 0; i -= 1) {
      var src = scripts[i].getAttribute("src");
      if (!src || src.indexOf("javascripts/support.js") === -1) {
        continue;
      }
      var supportUrl = new URL(src, window.location.href);
      return supportUrl.pathname.replace(/javascripts\/support\.js$/, "");
    }
    return "/";
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
    if (slug === "item-ids/enchant-ids/") {
      freeSlug = "";
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
      case "Item ID Reference":
        return "item-ids/potions-and-arrows/";
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
      '<span class="version-switch__icon" aria-hidden="true">&#9876;</span>',
      '<span class="version-switch__thumb" aria-hidden="true"></span>',
      '<a class="version-switch__link' + (!links.inPro ? " is-active" : "") + '" data-version="free" href="' + links.free + '">Free</a>',
      '<a class="version-switch__link' + (links.inPro ? " is-active" : "") + '" data-version="pro" href="' + links.pro + '">Pro</a>'
    ].join("");

    var title = header.querySelector(".md-header__title");
    if (title) {
      header.insertBefore(switcher, title);
    } else {
      header.appendChild(switcher);
    }
  }

  function mountSupportRail() {
    document.querySelectorAll(".support-rail").forEach(function (rail) {
      rail.remove();
    });

    var links = versionLinks();
    var items = [];

    if (!links.inPro) {
      items.push({
        href: "https://modrinth.com/plugin/instanced-dungeon",
        label: "Download",
        value: "Modrinth",
        title: "Download on Modrinth"
      });
      items.push({
        href: "https://www.spigotmc.org/resources/instanced-dungeon.132724/",
        label: "Plugin Page",
        value: "SpigotMC",
        title: "View on SpigotMC"
      });
    }

    items.push({
      href: "https://discord.com/invite/sD4HvQh8P4",
      label: "Discord",
      value: "Join Server",
      title: "Join the Discord"
    });
    items.push({
      href: "https://buymeacoffee.com/we_rt",
      label: "Support",
      value: "Buy Me a Coffee",
      title: "Support the project"
    });

    var rail = document.createElement("aside");
    rail.className = "support-rail";
    rail.innerHTML = items.map(function (item) {
      return [
        '<a href="' + item.href + '" target="_blank" rel="noopener" title="' + item.title + '">',
        '  <span class="support-rail__label">' + item.label + '</span>',
        '  <span class="support-rail__value">' + item.value + '</span>',
        '</a>'
      ].join("");
    }).join("");
    document.body.appendChild(rail);
  }

  function syncTocActive() {
    var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".md-nav--secondary .md-nav__link")).filter(function (link) {
      var url = new URL(link.href, window.location.href);
      var rect = link.getBoundingClientRect();
      return url.hash && url.pathname === window.location.pathname && rect.width > 0 && rect.height > 0 && window.getComputedStyle(link).visibility !== "collapse";
    });
    if (!tocLinks.length) {
      return;
    }

    var activeLink = tocLinks[0];
    tocLinks.forEach(function (link) {
      var id = decodeURIComponent(new URL(link.href, window.location.href).hash.slice(1));
      var target = document.getElementById(id);
      if (target && target.getBoundingClientRect().top <= 120) {
        activeLink = link;
      }
    });

    tocLinks.forEach(function (link) {
      link.classList.toggle("md-nav__link--active", link === activeLink);
    });
  }

  function bindTocScroll() {
    if (tocScrollBound) {
      return;
    }
    tocScrollBound = true;
    window.addEventListener("scroll", function () {
      window.requestAnimationFrame(syncTocActive);
    }, { passive: true });
  }

  function markClickedLink(link) {
    var nav = link.closest(".md-nav");
    if (!nav) {
      return;
    }
    nav.querySelectorAll(".md-nav__link--active").forEach(function (active) {
      active.classList.remove("md-nav__link--active");
    });
    link.classList.add("md-nav__link--active");
  }

  function targetFromHash(hash) {
    if (!hash || hash === "#") {
      return null;
    }

    return document.getElementById(decodeURIComponent(hash.slice(1)));
  }

  function scrollToHash(href, behavior) {
    var url = new URL(href, window.location.href);
    var target = targetFromHash(url.hash);
    if (target) {
      target.scrollIntoView({ behavior: behavior || "auto", block: "start" });
      window.requestAnimationFrame(syncTocActive);
      return;
    }

    if (!url.hash) {
      window.scrollTo({ top: 0, behavior: behavior || "auto" });
    }
  }

  function handleHashLink(link, event) {
    if (!link || !link.href) {
      return false;
    }

    var url = new URL(link.href, window.location.href);
    if (url.origin !== window.location.origin || url.pathname !== window.location.pathname || url.search !== window.location.search || !url.hash) {
      return false;
    }

    var target = targetFromHash(url.hash);
    if (!target) {
      return false;
    }

    event.preventDefault();
    event.stopPropagation();
    if (event.stopImmediatePropagation) {
      event.stopImmediatePropagation();
    }

    markClickedLink(link);
    window.history.pushState({ smoothDocs: true }, "", url.href);
    scrollToHash(url.href, "smooth");
    return true;
  }

  function shouldHandleLink(link) {
    if (!link || !link.href || link.target || link.hasAttribute("download")) {
      return false;
    }

    var url = new URL(link.href, window.location.href);
    if (url.origin !== window.location.origin) {
      return false;
    }

    if (url.pathname === window.location.pathname && url.search === window.location.search && url.hash) {
      return false;
    }

    return !!link.closest(".version-switch, .md-tabs, .md-sidebar, .md-content");
  }

  function waitForTransitionPaint(startedAt) {
    return new Promise(function (resolve) {
      window.requestAnimationFrame(function () {
        window.requestAnimationFrame(function () {
          var remaining = transitionDelay - (Date.now() - startedAt);
          window.setTimeout(resolve, Math.max(remaining, 0));
        });
      });
    });
  }

  function replaceMainContent(html, href, token, options) {
    if (token !== navigationToken) {
      return;
    }

    var parsed = new DOMParser().parseFromString(html, "text/html");
    var nextMain = parsed.querySelector(".md-main");
    var currentMain = document.querySelector(".md-main");

    if (!nextMain || !currentMain) {
      window.location.href = href;
      return;
    }

    document.title = parsed.title || document.title;
    currentMain.replaceWith(document.importNode(nextMain, true));
    if (options && options.replace) {
      window.history.replaceState({ smoothDocs: true }, "", href);
    } else {
      window.history.pushState({ smoothDocs: true }, "", href);
    }
    mountEnhancements();
    scrollToHash(href, "auto");
    syncTocActive();
  }

  function navigateTo(href, options) {
    var token = navigationToken + 1;
    navigationToken = token;
    var startedAt = Date.now();
    document.documentElement.classList.add("is-page-transitioning");

    window.fetch(href, { credentials: "same-origin" })
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Unable to load documentation page.");
        }
        return response.text();
      })
      .then(function (html) {
        return waitForTransitionPaint(startedAt).then(function () {
          return html;
        });
      })
      .then(function (html) {
        replaceMainContent(html, href, token, options || {});
      })
      .catch(function () {
        window.location.href = href;
      });
  }

  function mountEnhancements() {
    document.documentElement.classList.remove("is-page-transitioning");
    mountVersionSwitch();
    updateVersionNavigation();
    mountSupportRail();
    syncTocActive();
    bindTocScroll();
  }

  document.addEventListener("click", function (event) {
    var link = event.target.closest("a");
    if (handleHashLink(link, event)) {
      return;
    }

    if (!shouldHandleLink(link)) {
      return;
    }

    event.preventDefault();
    event.stopPropagation();
    if (event.stopImmediatePropagation) {
      event.stopImmediatePropagation();
    }
    markClickedLink(link);

    var version = link.getAttribute("data-version");
    var switcher = link.closest(".version-switch");
    if (version && switcher) {
      switcher.dataset.active = version;
      switcher.querySelectorAll(".version-switch__link").forEach(function (versionLink) {
        versionLink.classList.toggle("is-active", versionLink.getAttribute("data-version") === version);
      });
    }

    navigateTo(link.href);
  }, true);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountEnhancements);
  } else {
    mountEnhancements();
  }

  if (window.document$ && document$.subscribe) {
    document$.subscribe(mountEnhancements);
  }

  window.addEventListener("popstate", function () {
    navigateTo(window.location.href, { replace: true });
  });
})();
