// sticky-nav
const sticky = document.querySelector('header');

window.onscroll = () => {
  this.scrollY > 180
    ? sticky.classList.add('sticky')
    : sticky.classList.remove('sticky');
};

// side-nav
const sideNavBtn = document.querySelector('.side-nav-btn');
const sideNav = document.querySelector('.side-nav');
const closeNav = document.querySelector('.nav-close');
const background = document.querySelector('.background');
const mouse = document.querySelector('.cursor-close');

document.addEventListener('mousemove', (e) => {
  let x = e.x;
  let y = e.y;

  mouse.style.top = y + 'px';
  mouse.style.left = x + 'px';
});

sideNavBtn.addEventListener('click', () => {
  sideNavBtn.classList.toggle('active');
  sideNav.classList.toggle('active');
  background.classList.toggle('active');
});

closeNav.addEventListener('click', () => {
  sideNavBtn.classList.remove('active');
  sideNav.classList.remove('active');
  background.classList.remove('active');
});

background.addEventListener('click', () => {
  sideNavBtn.classList.remove('active');
  sideNav.classList.remove('active');
  background.classList.remove('active');
});
