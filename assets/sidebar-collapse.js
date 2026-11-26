(() => {
  function initialize() {
    document.querySelectorAll('.sidebar .part-link').forEach((heading, index) => {
      const section = heading.nextElementSibling;
      if (!section || section.tagName !== 'NAV' || heading.dataset.collapsible) return;
      heading.dataset.collapsible = 'true';
      section.id ||= 'sidebar-part-' + index;
      heading.setAttribute('role', 'button');
      heading.setAttribute('aria-controls', section.id);
      heading.setAttribute('aria-expanded', 'true');
      function toggle(event) {
        event.preventDefault();
        const expanded = heading.getAttribute('aria-expanded') === 'true';
        heading.setAttribute('aria-expanded', String(!expanded));
        section.hidden = expanded;
      }
      heading.addEventListener('click', toggle);
      heading.addEventListener('keydown', event => {
        if (event.key === ' ') toggle(event);
      });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize);
  else initialize();
  const sidebar = document.querySelector('.sidebar');
  if (sidebar) new MutationObserver(initialize).observe(sidebar, {childList: true, subtree: true});
})();
