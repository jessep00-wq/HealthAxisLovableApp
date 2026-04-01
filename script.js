(function setYear() {
  const yearEl = document.getElementById('year');
  if (!yearEl) {
    console.error('Footer year placeholder not found.');
    return;
  }

  yearEl.textContent = String(new Date().getFullYear());
})();
