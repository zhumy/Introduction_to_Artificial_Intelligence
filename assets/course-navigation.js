(() => {
 const pages = Array.from(document.querySelectorAll('section.v4-page'));
 function currentIndex() {
   let best = 0, score = Infinity;
   pages.forEach((page, index) => {
     const bounds = page.getBoundingClientRect();
     const distance = Math.abs(bounds.top - 20);
     if (bounds.bottom > 40 && distance < score) {best = index; score = distance;}
   });
   return best;
 }
 document.addEventListener('keydown', event => {
   if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
   if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
   if (event.target.closest('input,textarea,select,button,a,audio,video,canvas,[contenteditable="true"],[role="slider"],[role="dialog"]')) return;
   const index = currentIndex() + (event.key === 'ArrowRight' ? 1 : -1);
   if (index < 0 || index >= pages.length) return;
   event.preventDefault();
   location.hash = pages[index].id;
 });
})();