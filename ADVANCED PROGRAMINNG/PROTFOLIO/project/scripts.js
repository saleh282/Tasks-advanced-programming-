// ================== JavaScript ==================

// Dark/Light Theme Toggle
function toggleTheme() {
    document.body.classList.toggle('light');
    const toggleBtn = document.querySelector('.toggle-btn');
    if (document.body.classList.contains('light')) {
        toggleBtn.textContent = '🌞';
    } else {
        toggleBtn.textContent = '🌙';
    }
}

// Smooth Scroll for Navbar Links
const navLinks = document.querySelectorAll('.nav-links a');
navLinks.forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        const target = document.querySelector(link.getAttribute('href'));
        target.scrollIntoView({ behavior: 'smooth' });
    });
});

// Optional: Contact Form Alert (simulate send)
const contactForm = document.querySelector('.contact-form');
contactForm.addEventListener('submit', e => {
    e.preventDefault();
    alert('Thank you! Your message has been sent.');
    contactForm.reset();
});
