<template>
  <div class="service-hero" ref="heroRef">
    <div class="hero-content">
      <div class="service-badge">
        <span class="service-number">{{ service?.id }}</span>
        <span class="service-category">{{ service?.category }}</span>
      </div>
      <div class="service-icon-wrapper">
        <div class="service-icon">{{ service?.icon }}</div>
      </div>
      <h1 class="service-title" data-draw-line="service-hero-title">
        <span v-html="formattedTitle"></span>
        <span data-draw-line-box></span>
      </h1>
      <p class="service-subtitle">{{ service?.description }}</p>
      
      <div class="service-pricing">
        <div class="pricing-card">
          <div class="paperOverlayGrid_2"></div>
          <div class="price-label">Starting from</div>
          <div class="price-range">{{ service?.priceRange }}</div>
        </div>
        <div class="duration-card">
          <div class="paperOverlayGrid_2"></div>
          <div class="duration-label">Duration</div>
          <div class="duration">{{ service?.duration }}</div>
        </div>
      </div>
      
      <div class="hero-actions">
        <NuxtLink to="/contact" class="hero-cta primary">
          Get Free Quote
        </NuxtLink>
        <button class="hero-cta secondary" @click="scrollToDetails">
          Learn More
        </button>
      </div>
    </div>
    
    <div class="hero-visual">
      <div class="showcase-wrapper">
        <div 
          :class="['service-showcase', getWoodClass()]"
          ref="showcaseRef"
        >
          <div class="paperOverlayGrid"></div>
          <div class="showcase-content">
            <div class="showcase-icon">{{ service?.icon }}</div>
            <div class="showcase-badge">Professional Service</div>
          </div>
        </div>
        <div class="showcase-highlights">
            <div class="highlight-item">
              <div class="paperOverlayGrid_2"></div>
              <span class="highlight-icon">⭐</span>
              <span class="highlight-text">Expert Technicians</span>
            </div>
            <div class="highlight-item">
              <div class="paperOverlayGrid_2"></div>
              <span class="highlight-icon">🛡️</span>
              <span class="highlight-text">Fully Insured</span>
            </div>
            <div class="highlight-item">
              <div class="paperOverlayGrid_2"></div>
              <span class="highlight-icon">✅</span>
              <span class="highlight-text">Satisfaction Guaranteed</span>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { gsap } from 'gsap'
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation'

const props = defineProps({
  service: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['scroll-to-details'])

// Composables
const { initUnderlineAnimation } = useUnderlineAnimation()

// Refs
const heroRef = ref(null)
const showcaseRef = ref(null)

// Title content
const formattedTitle = computed(() => props.service?.title || '')

// Wood background classes
const backgroundClasses = [
  'wood_overlay_1',
  'wood_overlay_2', 
  'wood_overlay_3',
  'wood_overlay_4',
  'wood_overlay_5',
  'wood_overlay_6'
]

const getWoodClass = () => {
  if (!props.service) return 'wood_overlay_1'
  const index = parseInt(props.service.id) % backgroundClasses.length
  return backgroundClasses[index]
}

function scrollToDetails() {
  emit('scroll-to-details')
}

onMounted(() => {
  setTimeout(() => {
    initializeAnimations()
  }, 100)
})

function initializeAnimations() {
  // Initialize underline animation
  initUnderlineAnimation('[data-draw-line="service-hero-title"]', {
    autoAnimate: true,
    duration: 1,
    ease: "power2.inOut",
    delay: 0.5
  })

  // Hero animation
  if (heroRef.value) {
    gsap.from('.hero-content', {
      y: 50,
      opacity: 0,
      duration: 0.8,
      stagger: 0.1,
      ease: "power2.out",
      delay: 0.2
    })

    gsap.from('.hero-visual', {
      x: 100,
      opacity: 0,
      duration: 1,
      ease: "power2.out",
      delay: 0.4
    })
  }

  // Showcase hover effect
  if (showcaseRef.value) {
    showcaseRef.value.addEventListener('mouseenter', () => {
      gsap.to(showcaseRef.value, {
        scale: 1.05,
        rotateY: 10,
        duration: 0.3,
        ease: "power2.out"
      })
    })

    showcaseRef.value.addEventListener('mouseleave', () => {
      gsap.to(showcaseRef.value, {
        scale: 1,
        rotateY: 0,
        duration: 0.3,
        ease: "power2.out"
      })
    })
  }
}
</script>

<style scoped>
.service-hero {
  display: flex;
  align-items: center;
  gap: 3rem;
  position: relative;
  width: 85%;
  margin-left: 9%;
  padding-bottom: 15rem;
  padding-top: 15rem;
}

.service-hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="m 60,0 L 0,0 0,60" fill="none" stroke="%23293b2e" stroke-width="0.5" opacity="0.05"/></pattern></defs><rect width="100%" height="100%" fill="url(%23grid)" /></svg>') repeat;
  pointer-events: none;
  z-index: 0;
}

.hero-content {
  flex: 1;
  max-width: 650px;
  position: relative;
  z-index: 1;
}

.service-badge {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.service-number {
  font-size: 12px;
  color: #293b2e;
  opacity: 0.8;
  font-weight: 600;
  letter-spacing: 1.5px;
  background: rgba(41, 59, 46, 0.1);
  padding: 0.5rem 0.8rem;
  border-radius: 20px;
  text-transform: uppercase;
}

.service-category {
  font-size: 10px;
  color: #a15e3c;
  font-weight: 500;
  letter-spacing: 1px;
  background: rgba(161, 94, 60, 0.1);
  padding: 0.3rem 0.8rem;
  border-radius: 15px;
  border: 1px solid rgba(161, 94, 60, 0.2);
  text-transform: uppercase;
}

.service-icon-wrapper {
  margin-bottom: 2rem;
  position: relative;
}

.service-icon {
  font-size: 5rem;
  display: block;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,0.1));
  animation: iconFloat 6s ease-in-out infinite;
}

@keyframes iconFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

.service-title {
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1.25;
  color: #293b2e;
  position: relative;
  display: block;
  width: 100%;
}

.service-title [data-draw-line-box] {
  display: block;
  width: 100%;
  height: 3px !important;
  margin-top: -8px;
}

.service-title [data-draw-line-box] svg {
  width: 100% !important;
  height: 0px !important;
  display: block !important;
}

.service-title [data-draw-line-box] svg path {
  stroke: #fd3d13 !important;
  stroke-width: 4px !important;
  fill: none !important;
}

.service-subtitle {
  font-size: 18px;
  line-height: 1.6;
  margin-bottom: 3rem;
  color: #293b2e;
  opacity: 0.85;
  text-transform: none;
  font-weight: 400;
  margin-top: 25%;
}

.service-pricing {
  display: flex;
  gap: 1.5rem;
  align-items: stretch;
  margin-bottom: 2.5rem;
}

.pricing-card, .duration-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  border: 2px solid rgba(41, 59, 46, 0.1);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  min-width: 140px;
  position: relative;
  z-index: 0;
  overflow: hidden;
}

.pricing-card:hover, .duration-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
  border-color: rgba(161, 94, 60, 0.3);
}

.price-label, .duration-label {
  font-size: 10px;
  color: #293b2e;
  opacity: 0.7;
  font-weight: 500;
  letter-spacing: 1px;
  margin-bottom: 0.5rem;
  display: block;
  text-transform: uppercase;
}

.price-range {
  font-size: 20px;
  font-weight: 700;
  color: #a15e3c;
  letter-spacing: 0.3px;
}

/* Ensure text content sits above paper overlays in pricing/duration cards */
.pricing-card .price-label,
.pricing-card .price-range,
.duration-card .duration-label,
.duration-card .duration {
  position: relative;
  z-index: 2;
}

.duration {
  font-size: 16px;
  color: #293b2e;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.hero-cta {
  padding: 1rem 2rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  letter-spacing: 0.8px;
  font-size: 13px;
  transition: all 0.3s ease;
  border: 2px solid transparent;
  cursor: pointer;
  background: none;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  text-transform: uppercase;
}

.hero-cta.primary {
  background: linear-gradient(135deg, #a15e3c 0%, #b36e4f 100%);
  color: white;
  box-shadow: 0 4px 15px rgba(161, 94, 60, 0.3);
}

.hero-cta.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(161, 94, 60, 0.4);
}

.hero-cta.secondary {
  color: #293b2e;
  border-color: #293b2e;
  background: white;
}

.hero-cta.secondary:hover {
  background: #293b2e;
  color: white;
  transform: translateY(-2px);
}

.hero-visual {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  z-index: 1;
}

.showcase-wrapper {
  position: relative;
}

.service-showcase {
  width: 320px;
  height: 420px;
  position: relative;
  border: 6px solid #04251b;
  background: #04251b;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transform-style: preserve-3d;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
  transition: all 0.4s ease;
}

.service-showcase:hover {
  transform: translateY(-5px) rotateY(5deg);
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.2);
}

.service-showcase::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-size: 100%;
  background-repeat: repeat;
  border-radius: 8px;
  z-index: 0;
}

.service-showcase.wood_overlay_1::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_1.jpg");
}

.service-showcase.wood_overlay_2::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_2.jpg");
}

.service-showcase.wood_overlay_3::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_3.jpg");
}

.service-showcase.wood_overlay_4::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_4.jpg");
}

.service-showcase.wood_overlay_5::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_5.jpg");
}

.service-showcase.wood_overlay_6::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_6.jpg");
}

.showcase-content {
  position: relative;
  z-index: 0;
  height: 93%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: white;
  margin: 15px;
  border-radius: 8px;
  gap: 4rem;
}

/* In-panel overlay so paper texture shows above white but under icon/badge */
.showcase-content::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  opacity: .6;
  background-size: 120%;
  background-repeat: repeat;
  background-image: url("~/assets/content/images/paper_overlay_7.jpg");
  mix-blend-mode: multiply;
  pointer-events: none;
  z-index: 1;
  border-radius: 6px;
}

.showcase-content > * {
  position: relative;
  z-index: 2;
}

.showcase-icon {
  font-size: 7rem;
  filter: drop-shadow(0 6px 15px rgba(0,0,0,0.15));
}

@keyframes showcaseFloat {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-8px) scale(1.02); }
}

.showcase-badge {
  background: linear-gradient(135deg, #a15e3c 0%, #b36e4f 100%);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  box-shadow: 0 2px 8px rgba(161, 94, 60, 0.3);
}

.showcase-highlights {
  position: absolute;
  right: -120px;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 1rem;
}



.highlight-item:nth-child(1) { animation-delay: 0.2s; }
.highlight-item:nth-child(2) { animation-delay: 0.4s; }
.highlight-item:nth-child(3) { animation-delay: 0.6s; }

.highlight-item {
  background: white;
  padding: 0.8rem 1rem;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 11px;
  font-weight: 500;
  color: #293b2e;
  border: 2px solid #293b2e;
  transition: all 0.3s ease;
  text-transform: uppercase;
  overflow: hidden;
  position: relative;
}

@keyframes slideInRight {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.highlight-item:hover {
  transform: translateX(-3px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.highlight-icon {
  font-size: 14px;
}

.highlight-text {
  font-weight: 600;
  letter-spacing: 0.3px;
}

/* Ensure highlight item content sits above overlay */
.highlight-item .highlight-icon,
.highlight-item .highlight-text {
  position: relative;
  z-index: 2;
}

/* Paper overlay */
.paperOverlayGrid {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  opacity: .6;
  background-size: 120%;
  background-repeat: repeat;
  background-image: url("~/assets/content/images/paper_overlay_7.jpg");
  mix-blend-mode: multiply;
  pointer-events: none;
  z-index: 0;
  background-position: bottom right;
  border-radius: 4px;
}

.paperOverlayGrid_2 {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  opacity: .6;
  background-size: 270%;
  background-repeat: repeat;
  background-image: url("~/assets/content/images/paper_overlay_7.jpg");
  mix-blend-mode: multiply;
  pointer-events: none;
  z-index: 1;
  border-radius: 4px;
  transform: rotate(180deg);
}

@media (max-width: 768px) {
  .service-hero {
    flex-direction: column;
    gap: 3rem;
    padding: 2rem 1rem;
    text-align: center;
    min-height: 70vh;
  }

  .service-title {
    font-size: 2.5rem;
  }

  .service-subtitle {
    font-size: 16px;
  }

  .service-pricing {
    justify-content: center;
  }

  .pricing-card, .duration-card {
    min-width: 120px;
  }

  .hero-actions {
    flex-direction: column;
    width: 100%;
  }

  .hero-cta {
    width: 100%;
    justify-content: center;
  }

  .showcase-wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
  }

  .service-showcase {
    width: 280px;
    height: 360px;
  }

  .showcase-highlights {
    position: static;
    flex-direction: row;
    justify-content: center;
    margin-top: 2rem;
    transform: none;
  }

  .highlight-item {
    animation: none;
    opacity: 1;
    transform: none;
  }

  .showcase-icon {
    font-size: 5rem;
  }
}

@media (max-width: 480px) {
  .service-pricing {
    flex-direction: column;
    gap: 1rem;
    width: 100%;
  }

  .pricing-card, .duration-card {
    width: 100%;
  }

  .service-title {
    font-size: 2rem;
  }

  .service-showcase {
    width: 250px;
    height: 320px;
  }

  .showcase-highlights {
    flex-direction: column;
    gap: 0.8rem;
  }
}
</style>