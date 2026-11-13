// Mobile menu toggle.
(function () {
  var b = document.querySelector(".burger"), n = document.getElementById("nav");
  if (b && n) b.addEventListener("click", function () {
    var open = n.classList.toggle("open");
    b.setAttribute("aria-expanded", open ? "true" : "false");
  });
})();
// Booking form -> WhatsApp message. No data is sent anywhere else.
(function () {
  var f = document.getElementById("booking");
  if (!f) return;
  var err = f.querySelector(".err");
  f.addEventListener("submit", function (e) {
    e.preventDefault();
    var bad = [];
    Array.prototype.forEach.call(f.elements, function (el) {
      if (!el.name) return;
      var invalid = el.required && !String(el.value).trim();
      if (!invalid && el.checkValidity && !el.checkValidity()) invalid = true;
      el.setAttribute("aria-invalid", invalid ? "true" : "false");
      if (invalid) bad.push(el);
    });
    if (bad.length) {
      var names = bad.map(function (el) {
        var s = el.closest("label").querySelector("span");
        return s ? s.textContent.replace("*", "").trim() : el.name;
      });
      err.textContent = err.getAttribute("data-msg") + ": " + names.join(", ");
      err.hidden = false;
      bad[0].focus();
      return;
    }
    err.hidden = true;
    var lines = [f.getAttribute("data-intro")];
    Array.prototype.forEach.call(f.elements, function (el) {
      if (!el.name) return;
      var label = el.closest("label").querySelector("span").textContent.replace("*", "").trim();
      var v = el.type === "checkbox" ? (el.checked ? "✓" : "") : String(el.value).trim();
      if (v) lines.push(label + ": " + v);
    });
    lines.push(location.href.split("#")[0]);
    location.href = "https://wa.me/" + f.getAttribute("data-wa") + "?text=" + encodeURIComponent(lines.join("\n"));
  });
})();
