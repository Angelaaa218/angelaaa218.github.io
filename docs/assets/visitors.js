(() => {
  const counter = document.getElementById('view-counter');
  const ip = document.getElementById('visitor-ip');
  const preview = new URLSearchParams(location.search).get('visitor-preview') === '1';
  const live = location.hostname.toLowerCase() === 'angelaaa218.github.io';

  if (live || preview) {
    const key = live ? 'angelaaa218.github.io' : 'angelaaa218.github.io/local-preview';
    const label = live ? 'Total views' : 'Preview views';
    counter.textContent = `${label}: loading…`;
    const badge = new Image();
    badge.alt = label;
    badge.referrerPolicy = 'no-referrer';
    const link = document.createElement('a');
    link.href = `https://hits.sh/${key}/`;
    link.setAttribute('aria-label', `${label}: view counter statistics`);
    const timeout = setTimeout(() => {
      counter.textContent = `${label}: unavailable`;
    }, 10000);
    badge.onload = () => {
      clearTimeout(timeout);
      link.append(badge);
      counter.replaceChildren(link);
    };
    badge.onerror = () => {
      clearTimeout(timeout);
      counter.textContent = `${label}: unavailable`;
    };
    badge.src = `https://hits.sh/${key}.svg?label=${encodeURIComponent(label)}&color=287b8e&labelColor=646b70`;
  }

  ip.textContent = 'Loading…';
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 8000);
  fetch('https://api64.ipify.org?format=json', {
    signal: controller.signal,
    credentials: 'omit',
    referrerPolicy: 'no-referrer',
    cache: 'no-store'
  })
    .then(response => {
      if (!response.ok) throw new Error('IP service unavailable');
      return response.json();
    })
    .then(data => {
      if (typeof data.ip !== 'string' || !/^[0-9a-fA-F:.]{3,45}$/.test(data.ip)) {
        throw new Error('Invalid IP response');
      }
      ip.textContent = data.ip;
    })
    .catch(() => { ip.textContent = 'Unavailable'; })
    .finally(() => clearTimeout(timeout));
})();
