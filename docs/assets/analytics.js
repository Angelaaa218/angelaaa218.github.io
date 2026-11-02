(() => {
  // Collect only on the published site, never in local or copied previews.
  if (location.protocol !== 'https:' || location.hostname.toLowerCase() !== 'angelaaa218.github.io') return;

  const settings = document.currentScript?.dataset;
  const project = settings?.project || '';
  const security = settings?.security || '';
  if (!/^[0-9]{1,15}$/.test(project) || Number(project) < 1 || !/^[a-zA-Z0-9]{8,64}$/.test(security)) return;
  if (window.homepageAnalyticsLoaded) return;
  window.homepageAnalyticsLoaded = true;

  // These are public installation identifiers, not dashboard credentials.
  // Report privacy must be configured in Statcounter's User/Public Access settings.
  window.sc_project = Number(project);
  window.sc_security = security;
  window.sc_invisible = 1;
  window.sc_https = 1;

  const tracker = document.createElement('script');
  tracker.src = 'https://secure.statcounter.com/counter/counter.js';
  tracker.async = true;
  document.head.appendChild(tracker);
})();
