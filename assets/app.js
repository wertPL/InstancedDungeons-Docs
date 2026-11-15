(function () {
  var rootEl = document.documentElement;
  var bodyEl = document.body;
  var currentEdition = bodyEl.getAttribute("data-edition") || "free";
  var rootPrefix = bodyEl.getAttribute("data-root") || "";
  var docMain = document.querySelector(".doc-main");
  var NAV_KEY = "id-docs-nav-state";

  function saveNavState(state) {
    var raw = JSON.stringify(state);
    try {
      sessionStorage.setItem(NAV_KEY, raw);
    } catch (e) {}
    try {
      window.name = "idnav:" + raw;
    } catch (e) {}
  }

  function readAndClearNavState() {
    var raw = null;
    try {
      raw = sessionStorage.getItem(NAV_KEY);
      sessionStorage.removeItem(NAV_KEY);
    } catch (e) {}
    if (!raw && typeof window.name === "string" && window.name.indexOf("idnav:") === 0) {
      raw = window.name.slice(6);
      window.name = "";
    }
    if (!raw) return null;
    try {
      return JSON.parse(raw);
    } catch (e) {
      return null;
    }
  }

  // Theme
  var savedTheme = null;
  try {
    savedTheme = localStorage.getItem("id-docs-theme");
  } catch (e) {}
  if (savedTheme === "light" || savedTheme === "dark") {
    rootEl.setAttribute("data-theme", savedTheme);
  }

  var themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = rootEl.getAttribute("data-theme") === "light" ? "dark" : "light";
      rootEl.setAttribute("data-theme", next);
      try {
        localStorage.setItem("id-docs-theme", next);
      } catch (e) {}
    });
  }

  // Mobile sidebar
  var mobileBtn = document.getElementById("mobile-menu-btn");
  var sidebarLeft = document.getElementById("sidebar-left");
  if (mobileBtn && sidebarLeft) {
    mobileBtn.addEventListener("click", function () {
      sidebarLeft.classList.toggle("is-open");
    });
  }

  // Reset leaving state on browser back/forward cache restore
  window.addEventListener("pageshow", function () {
    if (docMain) docMain.classList.remove("is-leaving");
    var sw = document.querySelector(".edition-switch");
    if (sw) {
      sw.classList.remove("is-switching");
      sw.setAttribute("data-active", currentEdition);
    }
  });

  // Edition switcher and top category sliding indicators
  var navState = readAndClearNavState();
  var editionSwitch = document.querySelector(".edition-switch");
  var editionThumb = editionSwitch ? editionSwitch.querySelector(".edition-thumb") : null;
  var topNav = document.querySelector(".top-nav");
  var topNavThumb = topNav ? topNav.querySelector(".top-nav-thumb") : null;
  var activeTopLink = topNav ? topNav.querySelector(".top-nav-link.is-active") : null;

  if (editionSwitch && editionThumb && navState && navState.fromEdition && navState.fromEdition !== currentEdition && !navState.editionAnimated) {
    editionThumb.style.transition = "none";
    editionSwitch.setAttribute("data-active", navState.fromEdition);
    editionThumb.offsetWidth;
    requestAnimationFrame(function () {
      editionThumb.style.transition = "";
      editionSwitch.setAttribute("data-active", currentEdition);
    });
  }

  function positionTopThumb(linkEl, instant) {
    if (!topNav || !topNavThumb || !linkEl || linkEl.offsetWidth === 0) return;
    if (instant) {
      topNavThumb.style.transition = "none";
    }
    topNavThumb.style.transform = "translateX(" + linkEl.offsetLeft + "px)";
    topNavThumb.style.width = linkEl.offsetWidth + "px";
    topNavThumb.style.opacity = "1";
    topNav.classList.add("has-thumb");
    if (instant) {
      topNavThumb.offsetWidth;
      topNavThumb.style.transition = "";
    }
  }

  if (topNav && topNavThumb && activeTopLink) {
    if (
      navState &&
      navState.fromEdition === currentEdition &&
      typeof navState.fromTopLeft === "number" &&
      typeof navState.fromTopWidth === "number" &&
      !navState.topAnimated &&
      Math.abs(navState.fromTopLeft - activeTopLink.offsetLeft) > 1
    ) {
      topNavThumb.style.transition = "none";
      topNavThumb.style.transform = "translateX(" + navState.fromTopLeft + "px)";
      topNavThumb.style.width = navState.fromTopWidth + "px";
      topNavThumb.style.opacity = "1";
      topNav.classList.add("has-thumb");
      topNavThumb.offsetWidth;
      requestAnimationFrame(function () {
        positionTopThumb(activeTopLink, false);
      });
    } else {
      positionTopThumb(activeTopLink, true);
    }

    window.addEventListener("resize", function () {
      positionTopThumb(activeTopLink, true);
    });
  }

  function isModifiedClick(e) {
    return e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0;
  }

  if (editionSwitch) {
    editionSwitch.querySelectorAll(".edition-link").forEach(function (link) {
      link.addEventListener("click", function (e) {
        if (isModifiedClick(e)) return;
        var targetEdition = link.getAttribute("data-edition-target");
        if (!targetEdition || targetEdition === currentEdition) return;
        e.preventDefault();
        editionSwitch.classList.add("is-switching");
        editionSwitch.setAttribute("data-active", targetEdition);
        editionSwitch.querySelectorAll(".edition-link").forEach(function (l) {
          l.classList.toggle("is-active", l === link);
        });
        if (docMain) docMain.classList.add("is-leaving");
        saveNavState({ fromEdition: currentEdition, editionAnimated: true });
        var dest = link.href;
        setTimeout(function () {
          window.location.href = dest;
        }, 190);
      });
    });
  }

  if (topNav) {
    topNav.querySelectorAll(".top-nav-link").forEach(function (link) {
      link.addEventListener("click", function (e) {
        if (isModifiedClick(e) || link === activeTopLink) return;
        e.preventDefault();
        positionTopThumb(link, false);
        topNav.querySelectorAll(".top-nav-link").forEach(function (l) {
          l.classList.toggle("is-active", l === link);
        });
        if (docMain) docMain.classList.add("is-leaving");
        saveNavState({
          fromEdition: currentEdition,
          fromTopLeft: activeTopLink ? activeTopLink.offsetLeft : 0,
          fromTopWidth: activeTopLink ? activeTopLink.offsetWidth : 0,
          topAnimated: true
        });
        var dest = link.href;
        setTimeout(function () {
          window.location.href = dest;
        }, 170);
      });
    });
  }

  document.querySelectorAll(".sidebar-left a, .page-nav-card").forEach(function (link) {
    link.addEventListener("click", function (e) {
      if (isModifiedClick(e)) return;
      if (activeTopLink && activeTopLink.offsetWidth > 0) {
        saveNavState({
          fromEdition: currentEdition,
          fromTopLeft: activeTopLink.offsetLeft,
          fromTopWidth: activeTopLink.offsetWidth,
          topAnimated: false
        });
      }
    });
  });

  // Copy code buttons
  document.querySelectorAll(".copy-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var block = btn.closest(".code-block");
      var codeEl = block ? block.querySelector("pre code") : null;
      if (!codeEl) return;
      var text = codeEl.innerText || codeEl.textContent || "";
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text);
      } else {
        var ta = document.createElement("textarea");
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
      }
      var prev = btn.textContent;
      btn.textContent = "Copied";
      btn.classList.add("is-copied");
      setTimeout(function () {
        btn.textContent = prev;
        btn.classList.remove("is-copied");
      }, 1400);
    });
  });

  // Right TOC scroll spy
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc-item a"));
  if (tocLinks.length > 0) {
    var targets = tocLinks.map(function (link) {
      var id = link.getAttribute("href").replace(/^#/, "");
      return { link: link, el: document.getElementById(id) };
    }).filter(function (item) { return item.el !== null; });

    function updateToc() {
      var active = targets[0];
      for (var i = 0; i < targets.length; i++) {
        if (targets[i].el.getBoundingClientRect().top <= 110) {
          active = targets[i];
        }
      }
      tocLinks.forEach(function (l) {
        l.classList.toggle("is-active", active && l === active.link);
      });
    }
    window.addEventListener("scroll", updateToc, { passive: true });
    updateToc();
  }

  // Edition-isolated search
  var searchBackdrop = document.getElementById("search-backdrop");
  var searchInput = document.getElementById("search-input");
  var searchResults = document.getElementById("search-results");
  var searchOpenBtn = document.getElementById("search-open");
  var selectedIdx = 0;
  var currentMatches = [];

  function openSearch() {
    if (!searchBackdrop) return;
    searchBackdrop.classList.add("is-open");
    if (searchInput) {
      searchInput.value = "";
      renderSearchResults("");
      setTimeout(function () { searchInput.focus(); }, 20);
    }
  }

  function closeSearch() {
    if (!searchBackdrop) return;
    searchBackdrop.classList.remove("is-open");
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function renderSearchResults(query) {
    if (!searchResults) return;
    var indexByEdition = window.ID_SEARCH_DATA || {};
    var pool = Array.isArray(indexByEdition[currentEdition]) ? indexByEdition[currentEdition] : [];
    var q = (query || "").trim().toLowerCase();

    if (!q) {
      currentMatches = pool.slice(0, 8);
    } else {
      var terms = q.split(/\s+/);
      var scored = [];
      pool.forEach(function (entry) {
        var titleL = entry.title.toLowerCase();
        var secL = entry.section.toLowerCase();
        var bodyL = entry.text.toLowerCase();
        var score = 0;
        for (var i = 0; i < terms.length; i++) {
          var t = terms[i];
          if (titleL.indexOf(t) >= 0) score += 10;
          else if (secL.indexOf(t) >= 0) score += 6;
          else if (bodyL.indexOf(t) >= 0) score += 2;
          else return;
        }
        scored.push({ entry: entry, score: score });
      });
      scored.sort(function (a, b) { return b.score - a.score; });
      currentMatches = scored.slice(0, 12).map(function (s) { return s.entry; });
    }

    selectedIdx = 0;
    if (currentMatches.length === 0) {
      searchResults.innerHTML = '<div class="search-empty">No matching topics found in ' + currentEdition.toUpperCase() + ' documentation.</div>';
      return;
    }

    searchResults.innerHTML = currentMatches.map(function (item, idx) {
      var href = rootPrefix + item.url;
      var cls = "search-result-item" + (idx === 0 ? " is-selected" : "");
      var heading = item.title + (item.section && item.section !== item.title ? " - " + item.section : "");
      return [
        '<a class="' + cls + '" href="' + href + '">',
        '  <div class="search-result-top">',
        '    <span class="search-result-title">' + escapeHtml(heading) + '</span>',
        '    <span class="search-result-badge">' + escapeHtml(item.group) + '</span>',
        '  </div>',
        '  <div class="search-result-snippet">' + item.snippet + '</div>',
        '</a>'
      ].join("");
    }).join("");
  }

  function updateSelection() {
    var items = searchResults ? searchResults.querySelectorAll(".search-result-item") : [];
    for (var i = 0; i < items.length; i++) {
      items[i].classList.toggle("is-selected", i === selectedIdx);
      if (i === selectedIdx) {
        items[i].scrollIntoView({ block: "nearest" });
      }
    }
  }

  if (searchOpenBtn) {
    searchOpenBtn.addEventListener("click", openSearch);
  }
  if (searchBackdrop) {
    searchBackdrop.addEventListener("click", function (e) {
      if (e.target === searchBackdrop) closeSearch();
    });
  }
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      renderSearchResults(searchInput.value);
    });
  }

  document.addEventListener("keydown", function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      if (searchBackdrop && searchBackdrop.classList.contains("is-open")) closeSearch();
      else openSearch();
      return;
    }
    if (!searchBackdrop || !searchBackdrop.classList.contains("is-open")) return;
    if (e.key === "Escape") {
      e.preventDefault();
      closeSearch();
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      if (currentMatches.length > 0) {
        selectedIdx = (selectedIdx + 1) % currentMatches.length;
        updateSelection();
      }
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      if (currentMatches.length > 0) {
        selectedIdx = (selectedIdx - 1 + currentMatches.length) % currentMatches.length;
        updateSelection();
      }
    } else if (e.key === "Enter") {
      var items = searchResults ? searchResults.querySelectorAll(".search-result-item") : [];
      if (items[selectedIdx]) {
        e.preventDefault();
        window.location.href = items[selectedIdx].getAttribute("href");
      }
    }
  });
})();
