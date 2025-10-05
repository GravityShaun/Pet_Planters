<template>
  <section class="service-area-section">
    <div class="container">
      <div class="info-content">
        <h2 class="section-title" data-draw-line="map-section-title">
          Shipping Nationwide With Love
          <span data-draw-line-box></span>
        </h2>
        <p class="service-list-title">Every PetPlanter includes:</p>
        <ul class="service-list" ref="serviceList">
          <li v-for="(item, index) in serviceAreas" :key="index" class="service-item">{{ item }}</li>
        </ul>
        <a href="/contact" class="cta-button">Start Your Custom Planter</a>
      </div>
      <div class="right-side-container">
        <div class="map-image-container-wrapper">
      <div class="map-image-container" data-speed="1.05">
        <div class="paperOverlayImageOverlay"></div>
        <img src="~/assets/content/images/map.png" alt="Map of our service area in Charleston, SC" class="map-image" />
      </div>
      <div class="mapBackground" data-speed="0.975">
        <div class="paperOverlayImageBackground"></div>
      </div>
      </div>
      <div class="map-description">
        <h3 class="map-subtitle" data-draw-line="map-subtitle">
          Crafted With Care
          <span data-draw-line-box></span>
        </h3>
        <p class="map-text">
          We ship our custom pet planters to pet lovers across the United States. Each piece is carefully packaged to ensure your planter and succulent arrive safely. We're committed to creating lasting memories through thoughtful design and quality craftsmanship.
        </p>
      </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation'

// Register ScrollTrigger plugin
if (process.client) {
  gsap.registerPlugin(ScrollTrigger)
}

const serviceList = ref(null)
const { initUnderlineAnimation } = useUnderlineAnimation()

const serviceAreas = [
  'Custom 3D printed pet planter',
  'Hand-painted details',
  'Premium succulent plant',
  'Care instructions included',
  'Eco-friendly packaging',
  'Free shipping over $50',
  'Satisfaction guaranteed!'
]

onMounted(() => {
  setTimeout(() => {
  if (process.client && serviceList.value) {
    // Animate checklist items with staggered entrance
    gsap.fromTo(
      serviceList.value.querySelectorAll('.service-item'),
      {
        opacity: 0,
        x: -30,
        scale: 0.8
      },
      {
        opacity: 1,
        x: 0,
        scale: 1,
        duration: 0.6,
        stagger: 0.1,
        ease: 'back.out(1.7)',
        scrollTrigger: {
          trigger: serviceList.value,
          start: 'top 80%',
          end: 'bottom 20%',
          toggleActions: 'play none none reverse'
        }
      }
    )

    // Initialize underline animation for section title
    initUnderlineAnimation('[data-draw-line="map-section-title"]', {
      autoAnimate: true,
      duration: 1,
      ease: "power2.inOut",
      delay: 0.25
    })

    // Initialize underline animation for map subtitle
    initUnderlineAnimation('[data-draw-line="map-subtitle"]', {
      autoAnimate: true,
      duration: 1,
      ease: "power2.inOut",
      delay: 0.25
    })

    // Force red color after animation initializes
    setTimeout(() => {
      const element = document.querySelector('[data-draw-line="map-section-title"]')
      const svg = element?.querySelector('svg')
      const path = svg?.querySelector('path')
      if (path) {
        path.setAttribute('stroke', '#fd3d13')
        path.style.stroke = '#fd3d13'
        path.style.strokeWidth = '3px'
      }

      const element2 = document.querySelector('[data-draw-line="map-subtitle"]')
      const svg2 = element2?.querySelector('svg')
      const path2 = svg2?.querySelector('path')
      if (path2) {
        path2.setAttribute('stroke', '#fd3d13')
        path2.style.stroke = '#fd3d13'
        path2.style.strokeWidth = '4px'
      }
    }, 100)
  }
}, 100)
})
</script>

<style scoped>
.service-area-section {
  padding: 100px 0;
padding-bottom: 30vh;
position: relative;
z-index: 1;
padding-top: 20vh;
}

.container {
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  align-items: center;
  gap: 100px;
  width: 85vw;
  margin: 0 auto;
}

/* Left side: Information Content */
.info-content {
  flex-basis: 42%;
  flex-grow: 1;
}

.section-title {
  font-size: 2.35rem;
  font-weight: 700;
  color: #243e2e; /* Primary green from context */
  margin-bottom: 25px;
  line-height: 1.2;
  position: relative;
  overflow: visible;
}

.section-title [data-draw-line-box] {
  display: block;
  width: 100%;
  height: 1px !important;
  margin-top: -24px;
}

.section-title [data-draw-line-box] svg {
  width: 100% !important;
  height: 0px !important;
  display: block !important;
}

.section-title [data-draw-line-box] svg path {
  stroke: #fd3d13 !important;
  stroke-width: 3px !important;
  fill: none !important;
}

.section-description {
  font-size: 1.1rem;
  color: #2a2a2a; /* Dark text from context */
  line-height: 1.7;
  margin-bottom: 30px;
  font-weight: 500;
}

.service-list-title {
  font-size: 1.2rem;
  font-weight: 900;
  color: #1a1a1a;
  margin-bottom: 15px;
  margin-top: 85px;
}

.service-list {
  list-style: none;
  padding: 0;
  margin: 25px 0 40px 0;
}

.service-list li,
.service-item {
  font-size: 1.2rem;
  color: #2a2a2a;
  font-weight: 500;
  padding-left: 30px;
  position: relative;
  margin-bottom: 18px;
}

.service-list li::before,
.service-item::before {
  content: '✔';
  color: #106c43;
  font-size: 1.2rem;
  position: absolute;
  left: 0;
  top: 0;
}

.cta-button {
  display: inline-block;
  background: linear-gradient(135deg, #106c43, #293b2e); /* Gradient from context */
  color: white;
  border: none;
  padding: 18px 40px;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 12px;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.3s ease;
  box-shadow: 0 5px 15px rgba(16, 108, 67, 0.2);
}

.cta-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(16, 108, 67, 0.3);
}

/* Right side: Map Image */
.map-image-container {
  height: 100%;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
  align-self: stretch; /* Make panel stretch to container height */
}

.map-image-container-wrapper{
  position: relative;
  margin-bottom: 10vh;
  width:85%;
  margin-left: 10%
}

.map-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.mapBackground{
  width: 100%;
  height: 100%;
  background-color: #243e2e;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: visible;
  position: relative;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border: 2px solid #fd3d13;
  position: absolute;
  top: 32px;
  left: 20px;
  z-index: -1;
  overflow: hidden;
}

.right-side-container {
  width: 55%;
  flex-basis: 70%;
}

.map-description {
    margin-top: 50px;
    margin-left: 10%
}
.map-description h3 {
    font-size: 2rem;
    font-weight: 700;
    color: #243e2e;
    margin-bottom: 15px;
    line-height: 1.3;
    position: relative;
    overflow: visible;
}

.map-subtitle [data-draw-line-box] {
  display: block;
  width: 100%;
  height: 3px !important;
  margin-top: -12px;
}

.map-subtitle [data-draw-line-box] svg {
  width: 100% !important;
  height: 0px !important;
  display: block !important;
}

.map-subtitle [data-draw-line-box] svg path {
  stroke: #fd3d13 !important;
  stroke-width: 4px !important;
  fill: none !important;
}
.map-description p {
    font-size: 1.1rem;
    color: #2a2a2a;
    line-height: 1.7;
    font-weight: 500;
    margin: 0;
    width:85%;
    margin-top: 45px;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .container {
    flex-direction: column-reverse; /* Puts map on top on smaller screens */
    gap: 50px;
  }

  .info-content,
  .map-image-container {
    flex-basis: auto; /* Reset basis for stacking */
  }

  .map-image-container {
    width: 100%;
    height: 400px; /* Give map a fixed height on mobile */
  }
  
  .section-title {
    font-size: 2.5rem;
  }
}

@media (max-width: 768px) {
  .service-area-section {
    padding: 80px 0;
  }

  .section-title {
    font-size: 2.2rem;
  }

  .section-description, .service-list li {
    font-size: 1rem;
  }
  
  .map-image-container {
    height: 300px;
  }
}



.paperOverlayImageBackground {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    opacity:1;
    background-size: 1000%;
    background-repeat: repeat;
    background-image: url("~/assets/content/images/paper_overlay_5.jpg");
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 1;
  }

  .paperOverlayImageOverlay{
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    opacity:0.5;
    background-size: 200%;
    background-repeat: repeat;
    background-image: url("~/assets/content/images/paper_overlay_5.jpg");
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 1;
  }
</style>
