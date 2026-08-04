/* ============================================================
   Passt — shared language toggle and quiz handler
   ------------------------------------------------------------
   Every module page defines its own  const T = { en: {...}, de: {...} }
   before loading this file. Strings are keyed, elements carry
   data-i18n="key". English renders first; German sits behind the
   toggle, so the button always shows the OTHER language.
   ============================================================ */

let currentLang = 'en';

function toggleLang() {
  currentLang = currentLang === 'en' ? 'de' : 'en';
  document.documentElement.lang = currentLang;

  const btn = document.querySelector('.lang-toggle');
  if (btn) btn.textContent = currentLang === 'en' ? 'DE' : 'EN';

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (T[currentLang] && T[currentLang][key]) el.innerHTML = T[currentLang][key];
  });

  // Some modules mark whole spans instead of using keys.
  document.querySelectorAll('[data-lang]').forEach(el => {
    el.style.display = (el.getAttribute('data-lang') === currentLang) ? '' : 'none';
  });

  if (typeof renderMathInElement !== 'undefined') {
    renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\(', right: '\\)', display: false }
      ],
      throwOnError: false
    });
  }

  if (typeof onLangChange === 'function') onLangChange(currentLang);
}

/* Translate a key in the current language, with an English fallback. */
function t(key) {
  return (T[currentLang] && T[currentLang][key]) || (T.en && T.en[key]) || key;
}

/* ---- Quiz ------------------------------------------------- */
function answerQuiz(quizId, btn, isCorrect) {
  const quiz     = document.getElementById(quizId);
  const feedback = document.getElementById(quizId + '-feedback');
  if (!quiz || !feedback) return;

  quiz.querySelectorAll('.quiz-btn').forEach(b => b.classList.add('disabled'));
  btn.classList.add(isCorrect ? 'correct' : 'wrong');
  feedback.className = 'quiz-feedback ' + (isCorrect ? 'success' : 'fail');
  feedback.innerHTML = t(quizId + (isCorrect ? '.ok' : '.no'));
  feedback.style.display = 'block';
}

/* ---- KaTeX on first load ---------------------------------- */
window.addEventListener('load', () => {
  if (typeof renderMathInElement !== 'undefined') {
    renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\(', right: '\\)', display: false }
      ],
      throwOnError: false
    });
  }
});
