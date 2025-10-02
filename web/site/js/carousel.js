// Array com as imagens e legendas para o carrossel
const carouselItems = [
  {
    image: "image/king.png",
    caption: "Xadrez - Um clássico jogo de estratégia",
  },
  {
    image: "image/cerveja.png",
    caption: "Cerveja gelada para acompanhar os jogos",
  },
  {
    image: "image/hamburguer.png",
    caption: "Deliciosos hambúrgueres para saborear",
  },
  {
    image: "image/cards.png",
    caption: "Um jogos de cartas",
  },
];

class Carousel {
  constructor(container, items) {
    this.container = container;
    this.items = items;
    this.currentIndex = 0;
    this.track = container.querySelector(".carousel-track");
    this.dotsContainer = container.querySelector(".carousel-dots");
    this.prevButton = container.querySelector(".prev");
    this.nextButton = container.querySelector(".next");
    this.autoplayInterval = null;

    this.initialize();
  }

  initialize() {
    console.log("Iniciando carrossel...");
    // Cria os slides
    this.items.forEach((item, index) => {
      const slide = document.createElement("div");
      slide.className = "carousel-slide";

      const img = document.createElement("img");
      img.src = item.image;
      img.alt = item.caption;
      img.style.width = "100%";
      img.style.height = "100%";
      img.style.objectFit = "cover";

      slide.appendChild(img);
      this.track.appendChild(slide);

      // Cria os pontos de navegação
      const dot = document.createElement("div");
      dot.className = "carousel-dot";
      if (index === 0) dot.classList.add("active");
      dot.addEventListener("click", () => this.goToSlide(index));
      this.dotsContainer.appendChild(dot);
    });

    // Configura os botões de navegação
    this.prevButton.addEventListener("click", () => this.prev());
    this.nextButton.addEventListener("click", () => this.next());

    // Inicia o autoplay
    this.startAutoplay();

    // Pausa o autoplay quando o mouse está sobre o carrossel
    this.container.addEventListener("mouseenter", () => this.stopAutoplay());
    this.container.addEventListener("mouseleave", () => this.startAutoplay());

    // Mostra o primeiro slide
    this.updateSlidePosition();
  }

  updateSlidePosition() {
    this.track.style.transform = `translateX(-${this.currentIndex * 100}%)`;

    // Atualiza os pontos de navegação
    const dots = this.dotsContainer.getElementsByClassName("carousel-dot");
    Array.from(dots).forEach((dot, index) => {
      dot.classList.toggle("active", index === this.currentIndex);
    });
  }

  next() {
    this.currentIndex = (this.currentIndex + 1) % this.items.length;
    this.updateSlidePosition();
  }

  prev() {
    this.currentIndex =
      (this.currentIndex - 1 + this.items.length) % this.items.length;
    this.updateSlidePosition();
  }

  goToSlide(index) {
    this.currentIndex = index;
    this.updateSlidePosition();
  }

  startAutoplay() {
    if (this.autoplayInterval) return;
    this.autoplayInterval = setInterval(() => this.next(), 2500); // Muda a cada 2.5 segundos
  }

  stopAutoplay() {
    if (this.autoplayInterval) {
      clearInterval(this.autoplayInterval);
      this.autoplayInterval = null;
    }
  }
}

// Inicializa o carrossel quando a página carregar
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM carregado, procurando container do carrossel...");
  const container = document.querySelector(".carousel-container");

  if (container) {
    console.log("Container encontrado, inicializando carrossel...");
    new Carousel(container, carouselItems);
  } else {
    console.error("Container do carrossel não encontrado!");
  }
});
