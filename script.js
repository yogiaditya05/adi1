document.addEventListener('DOMContentLoaded', () => {
  // --- Scroll reveal ---
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  reveals.forEach(el => observer.observe(el));

  // --- Nav scroll effect ---
  const nav = document.querySelector('nav');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });

  // --- Mobile nav toggle ---
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle) {
    toggle.addEventListener('click', () => {
      links.classList.toggle('open');
      const spans = toggle.querySelectorAll('span');
      const isOpen = links.classList.contains('open');
      spans[0].style.transform = isOpen ? 'rotate(45deg) translate(5px, 5px)' : '';
      spans[1].style.opacity = isOpen ? '0' : '1';
      spans[2].style.transform = isOpen ? 'rotate(-45deg) translate(5px, -5px)' : '';
    });

    document.querySelectorAll('.nav-links a').forEach(a => {
      a.addEventListener('click', () => {
        links.classList.remove('open');
        toggle.querySelectorAll('span').forEach(s => { s.style.transform = ''; s.style.opacity = '1'; });
      });
    });
  }

  // --- Contact form ---
  const form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = form.querySelector('button');
      btn.textContent = 'Sent!';
      btn.style.background = '#4a9'; 
      setTimeout(() => { btn.textContent = 'Send Message'; btn.style.background = ''; }, 2500);
      form.reset();
    });
  }
  // --- Fetch Results ---
  const resultsContainer = document.getElementById('results-container');
  if (resultsContainer) {
    const MOCK_API = 'https://485ab272-b860-4c62-80f4-fa6a80a8c9d1.mock.pstmn.io/students';
    
    fetch(MOCK_API)
      .then(res => res.json())
      .then(data => {
        resultsContainer.innerHTML = '';
        data.forEach(student => {
          const isOwner = student.name.toLowerCase().includes('aditya') || student.roll_number === '0827rl231005';
          const card = document.createElement('div');
          card.className = `project-card reveal visible ${isOwner ? 'highlighted' : ''}`;
          card.innerHTML = `
            <div class="project-info">
              <span class="project-tag">${student.city} ${isOwner ? '• You' : ''}</span>
              <h3>${student.name}</h3>
              <p>${student.roll_number ? `Roll: ${student.roll_number}` : `Student ID: ${student.id}`}</p>
              <div class="stat-number" style="font-size: 1.5rem; margin-top: 0.5rem;">${student.marks}%</div>
            </div>
            <div class="project-link">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
            </div>
          `;
          resultsContainer.appendChild(card);
        });
      })
      .catch(err => {
        console.error('Error fetching results:', err);
        resultsContainer.innerHTML = '<div class="reveal visible" style="color: #f44">Failed to load results. Please check your connection.</div>';
      });
  }
});
