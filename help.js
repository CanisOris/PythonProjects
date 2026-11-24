async function copyCode(button) {
 const wrapper = button.closest('.code-wrapper, .code-block') || button.parentElement;
 const code = wrapper.querySelector('pre code, pre');
 if (!code) return;
 try { await navigator.clipboard.writeText(code.textContent); button.textContent = 'Copied!'; }
 catch { button.textContent = 'Copy unavailable'; }
 setTimeout(() => { button.textContent = 'Copy'; }, 1500);
}
document.querySelectorAll('.copy-btn').forEach(button => {
 button.removeAttribute('onclick');
 button.addEventListener('click', () => copyCode(button));
});

// Search only the key terms and commands in the main index.
const searchForm = document.getElementById('reference-search');
if (searchForm) {
  const queryInput = document.getElementById('reference-query');
  const nextButton = document.getElementById('next-match');
  const status = document.getElementById('search-status');
  const sections = Array.from(document.querySelectorAll('.main-menu > ul > li'));
  let matches = [];
  let current = -1;

  function clearSearch() {
    document.querySelectorAll('.search-term-match').forEach(item => item.classList.remove('search-term-match'));
    sections.forEach(section => section.classList.remove('current-search-match'));
    matches = [];
    current = -1;
    nextButton.disabled = true;
  }

  function goToMatch(index) {
    sections.forEach(section => section.classList.remove('current-search-match'));
    current = index;
    const section = matches[current];
    const title = section.querySelector('a');
    section.classList.add('current-search-match');
    title.focus({ preventScroll: true });
    section.scrollIntoView({ behavior: 'auto', block: 'start' });
    status.textContent = `${current + 1} of ${matches.length} sections: ${title.textContent.trim()}`;
    nextButton.disabled = matches.length < 2;
  }

  searchForm.addEventListener('submit', event => {
    event.preventDefault();
    clearSearch();
    const query = queryInput.value.trim().toLowerCase();
    if (!query) {
      status.textContent = 'Enter a term or command to jump to its section.';
      queryInput.focus();
      return;
    }
    matches = sections.filter(section => {
      const terms = Array.from(section.querySelectorAll('.key-list > ul > li'));
      const found = terms.filter(term => term.textContent.toLowerCase().includes(query));
      found.forEach(term => term.classList.add('search-term-match'));
      return found.length > 0;
    });
    if (matches.length) {
      goToMatch(0);
    } else {
      status.textContent = `No key terms or commands match “${queryInput.value.trim()}”.`;
    }
  });

  nextButton.addEventListener('click', () => {
    if (matches.length) goToMatch((current + 1) % matches.length);
  });

  queryInput.addEventListener('input', () => {
    clearSearch();
    status.textContent = 'Press Search or Enter to find matching sections.';
  });
}