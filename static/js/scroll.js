// Get references to the navbar links and corresponding sections
const portfolioLink = document.getElementById('portfolio-link');
const aboutLink = document.getElementById('about-link');
const contactLink = document.getElementById('contact-link');
const portfolioSection = document.getElementById('portfolio-section');
const aboutSection = document.getElementById('about-section');
const contactSection = document.getElementById('contact-section');

// Add event listeners to the navbar links
portfolioLink.addEventListener('click', () => {
  portfolioSection.scrollIntoView({ behavior: 'smooth' });
});

aboutLink.addEventListener('click', () => {
  aboutSection.scrollIntoView({ behavior: 'smooth' });
});

contactLink.addEventListener('click', () => {
  contactSection.scrollIntoView({ behavior: 'smooth' });
});
