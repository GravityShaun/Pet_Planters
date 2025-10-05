<template>
  <div class="related-services" ref="relatedRef">
    <div class="related-container">
      <div class="section-header">
        <h2 class="section-title">You Might Also Need</h2>
        <p class="section-subtitle">Other {{ service?.category?.toLowerCase() }} services that complement this one</p>
      </div>
      
      <div class="related-grid" v-if="relatedServices.length > 0">
        <NuxtLink
          v-for="relatedService in relatedServices"
          :key="relatedService.id"
          :to="`/service_items/${relatedService.id}`"
          class="related-card"
        >
          <div :class="['related-service-container', getRandomWoodClass()]">
            <div class="paperOverlayGrid"></div>
            <div class="related-content">
              <div class="related-header">
                <div class="related-number">{{ relatedService.id }}</div>
                <div class="related-category">{{ relatedService.category }}</div>
              </div>
              <div class="related-icon">{{ relatedService.icon }}</div>
              <h3>{{ relatedService.title }}</h3>
              <div class="related-footer">
                <span class="related-price">{{ relatedService.priceRange }}</span>
                <span class="related-arrow">→</span>
              </div>
            </div>
          </div>
        </NuxtLink>
      </div>
      
      <div class="related-cta" v-if="relatedServices.length > 0">
        <NuxtLink to="/services" class="view-all-link">
          View All Services
          <span class="link-arrow">→</span>
        </NuxtLink>
      </div>
      <div v-else class="no-related">
        <p>No related services available at this time.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const props = defineProps({
  service: {
    type: Object,
    required: true
  },
  relatedServices: {
    type: Array,
    required: true
  }
})

const relatedRef = ref(null)

// Wood background classes
const backgroundClasses = [
  'wood_overlay_1',
  'wood_overlay_2', 
  'wood_overlay_3',
  'wood_overlay_4',
  'wood_overlay_5',
  'wood_overlay_6'
]

const getRandomWoodClass = () => {
  const randomIndex = Math.floor(Math.random() * backgroundClasses.length)
  return backgroundClasses[randomIndex]
}

onMounted(() => {
  setTimeout(() => {
    initializeAnimations()
  }, 300)
})

function initializeAnimations() {
  // Related services animation
  if (relatedRef.value) {
    // Ensure items are visible by default; animate only if ScrollTrigger runs
    gsap.set('.related-card', { opacity: 1, y: 0 })
    gsap.from('.related-card', {
      y: 60,
      opacity: 0,
      duration: 0.6,
      stagger: 0.15,
      ease: "power2.out",
      scrollTrigger: {
        trigger: relatedRef.value,
        start: "top 90%",
        toggleActions: "play none none reverse"
      }
    })
  }
}
</script>

<style scoped>
.related-services {
  padding: 5rem 2rem;
  margin-top: 5rem;
  padding-bottom: 10rem;
  background: linear-gradient(135deg, rgba(248, 250, 252, 0.5) 0%, rgba(255, 255, 255, 0.8) 100%);
}

.related-container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 1rem;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.section-subtitle {
  font-size: 16px;
  color: #293b2e;
  opacity: 0.7;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
  font-weight: 400;
  max-width: 500px;
  margin: 0 auto;
}

.related-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-bottom: 3rem;
}

.related-card {
  text-decoration: none;
  color: inherit;
  display: block;
  transition: all 0.4s ease;
  position: relative;
}

.related-card:hover {
  transform: translateY(-8px);
}

.related-card:hover .related-service-container {
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.2);
  transform: scale(1.02);
}

.related-service-container {
  position: relative;
  border: 6px solid #04251b;
  background: #04251b;
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 4 / 5;
  transition: all 0.3s ease;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.related-service-container::before {
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

.related-service-container.wood_overlay_1::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_1.jpg");
}

.related-service-container.wood_overlay_2::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_2.jpg");
}

.related-service-container.wood_overlay_3::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_3.jpg");
}

.related-service-container.wood_overlay_4::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_4.jpg");
}

.related-service-container.wood_overlay_5::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_5.jpg");
}

.related-service-container.wood_overlay_6::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_6.jpg");
}

.related-content {
  position: relative;
  z-index: 2;
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 1.8rem;
  background: white;
  margin: 15px;
  border-radius: 8px;
  height: 93%;
  overflow: hidden;
}

/* In-panel overlay so paper texture shows above white but under text */
.related-content::after {
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

.related-content > * {
  position: relative;
  z-index: 2;
}

.related-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.related-number {
  font-size: 11px;
  color: #293b2e;
  opacity: 0.8;
  font-weight: 600;
  letter-spacing: 1.2px;
  background: rgba(41, 59, 46, 0.1);
  padding: 0.3rem 0.6rem;
  border-radius: 12px;
  text-transform: uppercase;
}

.related-category {
  font-size: 9px;
  color: #a15e3c;
  font-weight: 500;
  letter-spacing: 0.8px;
  background: rgba(161, 94, 60, 0.1);
  padding: 0.2rem 0.5rem;
  border-radius: 10px;
  border: 1px solid rgba(161, 94, 60, 0.2);
  text-transform: uppercase;
}

.related-icon {
  font-size: 3rem;
  margin-bottom: 20%;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
  text-align: center;
  margin-top: 25%;
}

.related-content h3 {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: auto;
  line-height: 1.3;
  color: #293b2e;
  letter-spacing: 0.5px;
  text-align: center;
  text-transform: uppercase;
}

.related-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(41, 59, 46, 0.1);
}

.related-price {
  font-size: 13px;
  font-weight: 600;
  color: #a15e3c;
  letter-spacing: 0.3px;
}

.related-arrow {
  font-size: 14px;
  color: #293b2e;
  opacity: 0.6;
  transition: all 0.3s ease;
}

.related-card:hover .related-arrow {
  opacity: 1;
  transform: translateX(3px);
}

.related-cta {
  text-align: center;
}

.view-all-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #293b2e 0%, #1a2621 100%);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  letter-spacing: 0.8px;
  font-size: 13px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(41, 59, 46, 0.2);
  text-transform: uppercase;
}

.view-all-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(41, 59, 46, 0.3);
}

.link-arrow {
  font-size: 14px;
  transition: transform 0.3s ease;
}

.view-all-link:hover .link-arrow {
  transform: translateX(3px);
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
  z-index: 1;
  background-position: bottom right;
  border-radius: 4px;
}

@media (max-width: 1024px) {
  .related-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }
}

@media (max-width: 768px) {
  .related-services {
    padding: 3rem 1rem;
  }

  .related-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .section-title {
    font-size: 2rem;
  }
}

@media (max-width: 480px) {
  .related-grid {
    grid-template-columns: 1fr;
  }
}
</style>