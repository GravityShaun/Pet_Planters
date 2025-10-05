import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';

export default defineNuxtPlugin((nuxtApp) => {
  if (process.server) return;
  const { initUnderlineAnimation } = useUnderlineAnimation();

  const initAll = () => {
    const nodes = document.querySelectorAll('[data-draw-line]');
    nodes.forEach((el) => initUnderlineAnimation(el));
  };

  // Run on window load (after fonts/styles)
  if (document.readyState === 'complete') {
    initAll();
  } else {
    window.addEventListener('load', initAll, { once: true });
  }

  // Re-run on route navigation in SPA context
  nuxtApp.hook('page:finish', () => {
    // small nextTick to ensure DOM is painted
    requestAnimationFrame(() => initAll());
  });
});


