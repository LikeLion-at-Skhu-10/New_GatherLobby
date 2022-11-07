const slides = document.querySelector('.slides-box');
const slideimg = document.querySelectorAll('.slide-li img');
let currentIdx = 0; 
const slideCount = slideimg.length;
const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
const slideWidth = 38;
makeClone();
initfunction();
autoSlide();

function makeClone() {
    let cloneSlide_first = slideimg[0].cloneNode(true);
    let cloneSlide_last = slides.lastElementChild.cloneNode(true);
    slides.append(cloneSlide_first);
    slides.insertBefore(cloneSlide_last, slides.firstElementChild);

}

function initfunction() {
    slides.style.width = (slideWidth) * (slideCount+2) + 'vw';
    slides.style.left = -(slideWidth) + 'vw';
}

function autoSlide() {
    setInterval(function () {
        if (currentIdx <= slideCount -1){
            slides.style.left = -(currentIdx + 2) * (slideWidth) + 'vw';
            slides.style.transition = `${0.5}s ease-out`;
        }
        if (currentIdx === slideCount - 1) {
            setTimeout(function () {
                slides.style.left = -(slideWidth) + 'vw';
                slides.style.transition = `${0}s ease-out`;
            }, 500);
            currentIdx = -1;
        }
        currentIdx += 1;
    }, 4000);
}

next.addEventListener('click', function(){
    if (currentIdx <= slideCount -1){
        slides.style.left = -(currentIdx + 2) * (slideWidth) + 'vw';
        slides.style.transition = `${0.5}s ease-out`;
    }
    if (currentIdx === slideCount - 1) {
        setTimeout(function () {
            slides.style.left = -(slideWidth) + 'vw';
            slides.style.transition = `${0}s ease-out`;
        }, 500);
        currentIdx = -1;
    }
    currentIdx += 1;
});

prev.addEventListener('click', function(){
    if (currentIdx >=0) {
        slides.style.left = -currentIdx * (slideWidth)+'vw';
        slides.style.transition = `${0.5}s ease-out`;
    }
    if (currentIdx === 0){
        setTimeout(function() {
            slides.style.left = -slideCount * (slideWidth) +'vw';
            slides.style.transition = `${0}s ease-out`;
        }, 500);
        currentIdx = slideCount;
    }
    currentIdx -= 1;
});
