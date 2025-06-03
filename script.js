const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const closeBtn = document.querySelector('.close');

document.querySelectorAll('.gallery-img').forEach(img => {
  img.addEventListener('click', () => {
    lightbox.style.display = 'flex';  // flex for centering!
    lightboxImg.src = img.src;
    lightboxImg.alt = img.alt || "Gallery image";
  });
});

closeBtn.onclick = () => {
  lightbox.style.display = 'none';
};

window.onclick = (e) => {
  if (e.target === lightbox) {
    lightbox.style.display = 'none';
  }
};
