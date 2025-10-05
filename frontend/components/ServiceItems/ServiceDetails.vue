<template>
  <div class="service-details-section" ref="detailsRef">
    <div class="details-container">
      <!-- <div class="service-header">
        <h1 class="service-title">{{ service?.title || 'Professional Service' }}</h1>

      </div> -->
      
      <div class="content-layout">
        <div class="main-content">
          <!-- <div class="service-description">
            <div class="paperOverlayItem_1"></div>
            <p class="description-text">
              {{ service?.description || defaultDescription }}
            </p>
          </div> -->
          
          <div class="service-overview">
            <div class="paperOverlayItem_1"></div>
            <h2 class="overview-title">Service Overview</h2>
            <div class="overview-content">
              <p v-for="paragraph in service?.overview || defaultOverview" :key="paragraph" class="overview-paragraph">
                {{ paragraph }}
              </p>
            </div>
          </div>
          
          <div class="service-details">
            <div class="paperOverlayItem_1"></div>
            <h2 class="details-title">What's Included</h2>
            <div class="details-content">
              <div class="feature-grid">
                <div v-for="(feature, index) in service?.features || defaultFeatures" :key="feature.title" :class="['feature-item', getWoodClass(index)]">
                  <div class="paperOverlayItem"></div>
                  <div class="feature-content">
                    <h3 class="feature-title">{{ feature.title }}</h3>
                    <p class="feature-description">{{ feature.description }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="sidebar">
          <div class="info-card">
            <div class="paperOverlayItem"></div>
            <h3 class="card-title">Service Information</h3>
            <div class="info-list">
              <div class="info-item">
                <span class="info-label">Duration:</span>
                <span class="info-value">{{ service?.duration || 'Varies by scope' }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Service Area:</span>
                <span class="info-value">{{ service?.serviceArea || 'Local & surrounding areas' }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Materials:</span>
                <span class="info-value">{{ service?.materials || 'Professional grade included' }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Warranty:</span>
                <span class="info-value">{{ service?.warranty || 'Quality guarantee' }}</span>
              </div>
            </div>
          </div>
          
          <div class="contact-card">
            <div class="paperOverlayItem"></div>
            <h3 class="card-title">Get Started</h3>
            <p class="contact-text">Ready to discuss your project? Contact us for a personalized consultation and quote.</p>
            <button class="contact-button">Request Quote</button>
          </div>
        </div>
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
  }
})

const detailsRef = ref(null)

// Wood background classes
const backgroundClasses = [
  'wood_overlay_1',
  'wood_overlay_2',
  'wood_overlay_3',
  'wood_overlay_4',
  'wood_overlay_5',
  'wood_overlay_6'
]

const getWoodClass = (index) => {
  return backgroundClasses[index % backgroundClasses.length]
}

// Default content for services that don't have specific details
const defaultDescription = "Our professional handyman services combine years of experience with attention to detail, ensuring your project is completed to the highest standards. We take pride in delivering quality workmanship that stands the test of time."

const defaultOverview = [
  "Every project begins with a thorough assessment of your needs and space. Our experienced professionals bring not just technical expertise, but also creative problem-solving skills to ensure your vision becomes reality.",
  "We use only high-quality materials and proven techniques, backed by comprehensive insurance and a commitment to excellence. From small repairs to complex installations, we approach each job with the same dedication to craftsmanship.",
  "Communication is key to our process. We keep you informed throughout the project, explaining our approach and ensuring you're completely satisfied with both the process and the final result."
]

const defaultFeatures = [
  {
    title: "Professional Assessment",
    description: "Comprehensive evaluation of your project requirements with detailed recommendations and transparent pricing."
  },
  {
    title: "Quality Materials",
    description: "We source and provide all necessary materials from trusted suppliers, ensuring durability and longevity."
  },
  {
    title: "Expert Installation",
    description: "Skilled craftsmen handle every aspect of installation with precision and attention to detail."
  },
  {
    title: "Clean Completion",
    description: "Complete cleanup and site restoration, leaving your space better than we found it."
  }
]

onMounted(() => {
  setTimeout(() => {
    initializeAnimations()
  }, 100)
})

function initializeAnimations() {
  if (detailsRef.value) {
    // Set initial states
    gsap.set('.service-description, .service-overview, .service-details', {
      opacity: 0,
      y: 30
    })

    gsap.set('.feature-item', {
      opacity: 0,
      y: 40
    })

    gsap.set('.info-card, .contact-card', {
      opacity: 0,
      x: 30
    })

    // Header animation
    gsap.from('.service-header', {
      y: 40,
      opacity: 0,
      duration: 0.8,
      ease: "power2.out",
      scrollTrigger: {
        trigger: detailsRef.value,
        start: "top 80%",
        toggleActions: "play none none reverse"
      }
    })

    // Content sections animation
    gsap.to('.service-description, .service-overview, .service-details', {
      y: 0,
      opacity: 1,
      duration: 1,
      stagger: 0.15,
      ease: "power3.out",
      scrollTrigger: {
        trigger: '.main-content',
        start: "top 70%",
        toggleActions: "play none none reverse"
      }
    })

    // Feature cards stagger animation
    gsap.to('.feature-item', {
      y: 0,
      opacity: 1,
      duration: 0.8,
      stagger: 0.08,
      ease: "power3.out",
      scrollTrigger: {
        trigger: '.feature-grid',
        start: "top 75%",
        toggleActions: "play none none reverse"
      }
    })

    // Sidebar animation
    gsap.to('.info-card, .contact-card', {
      x: 0,
      opacity: 1,
      duration: 0.8,
      stagger: 0.15,
      ease: "power3.out",
      scrollTrigger: {
        trigger: '.sidebar',
        start: "top 70%",
        toggleActions: "play none none reverse"
      }
    })
  }
}
</script>

<style scoped>
.service-details-section {
  padding: 0rem 2rem;
  position: relative;
  margin-bottom: 15rem;
}

.service-details-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at 30% 20%, rgba(161, 94, 60, 0.03) 0%, transparent 50%),
              radial-gradient(circle at 70% 80%, rgba(41, 59, 46, 0.03) 0%, transparent 50%);
  pointer-events: none;
}

.service-details-section::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    repeating-linear-gradient(
      90deg,
      transparent,
      transparent 98px,
      rgba(41, 59, 46, 0.015) 100px
    ),
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 98px,
      rgba(41, 59, 46, 0.015) 100px
    );
  pointer-events: none;
  opacity: 0.3;
}

.paperOverlayItem {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  opacity: 0.5;
  background-size: 150%;
  background-repeat: repeat;
  background-image: url("~/assets/content/images/paper_overlay_7.jpg");
  mix-blend-mode: multiply;
  pointer-events: none;
  z-index: 0;
  background-position: bottom right;
}

.paperOverlayItem_1 {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  opacity: 0.5;
  background-size: 50%;
  background-repeat: repeat;
  background-image: url("~/assets/content/images/paper_overlay_7.jpg");
  mix-blend-mode: multiply;
  pointer-events: none;
  z-index: 0;
  background-position: bottom right;
}

.details-container {
  margin: 0 auto;
  position: relative;
  z-index: 1;
  width: 90%
}

.service-header {
  text-align: center;
  margin-bottom: 5rem;
  padding-bottom: 0rem;
}

.service-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 1rem;
  letter-spacing: 0.5px;
  line-height: 1.2;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
}

.service-meta {
  display: flex;
  gap: 2rem;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

.price-range,
.duration {
  padding: 0.5rem 1.5rem;
  background: rgba(161, 94, 60, 0.1);
  color: #a15e3c;
  border-radius: 25px;
  font-weight: 600;
  font-size: 0.9rem;
  border: 1px solid rgba(161, 94, 60, 0.2);
}

.content-layout {
  display: grid;
  grid-template-columns: 1fr 400px;
  gap: 1.5rem;
  align-items: start;
}

.main-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.service-description {
  background: white;
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  border: 2px solid rgb(41, 59, 46);
  position: relative;
  overflow: hidden;
}

.description-text {
  font-size: 16px;
  line-height: 1.6;
  color: #293b2e;
  margin: 0;
  opacity: 0.85;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
  font-weight: 400;
  position: relative;
  z-index: 1;
}

.service-overview {
  background: white;
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  border: 2px solid rgb(41, 59, 46);
  position: relative;
  overflow: hidden;
}

.overview-title,
.details-title {
  font-size: 18px;
  font-weight: 600;
  color: #293b2e;
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid rgba(161, 94, 60, 0.2);
  letter-spacing: 0.5px;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
  position: relative;
  z-index: 1;
}

.overview-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  position: relative;
  z-index: 1;
}

.overview-paragraph {
  font-size: 14px;
  line-height: 1.6;
  color: #293b2e;
  margin: 0;
  opacity: 0.85;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
  font-weight: 400;
}

.service-details {
  background: white;
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  border: 2px solid rgb(41, 59, 46);
  position: relative;
  overflow: hidden;
}

.feature-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 2rem;
  position: relative;
  z-index: 1;
}

.feature-item {
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  border-radius: 15px;
  box-shadow: 0 4px 5px rgba(0, 0, 0, 0.35);
}

.feature-item .paperOverlayItem {
  background-size: 250%;
  transform: rotate(180deg);
  opacity: 0.3;
  z-index: 1;
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.2);
}

.feature-content {
  padding: 1.5rem;
  position: relative;
  z-index: 2;
  height: 100%;
}

.feature-item.wood_overlay_1 {
  position: relative;
  border: 5px solid transparent;
  background:
    linear-gradient(white, white) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_1.jpg") border-box;
  background-size: auto, 100px;
}

.feature-item.wood_overlay_2 {
  position: relative;
  border: 5px solid transparent;
  background:
    linear-gradient(white, white) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_2.jpg") border-box;
  background-size: auto, 90px;
}

.feature-item.wood_overlay_3 {
  position: relative;
  border: 5px solid transparent;
  background:
    linear-gradient(white, white) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_3.jpg") border-box;
  background-size: auto, 120px;
}

.feature-item.wood_overlay_4 {
  position: relative;
  border: 5px solid transparent;
  background:
    linear-gradient(white, white) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_4.jpg") border-box;
  background-size: auto, 80px;
}

.feature-item.wood_overlay_5 {
  position: relative;
  border: 5px solid transparent;
  background:
    linear-gradient(white, white) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_5.jpg") border-box;
  background-size: auto, 110px;
}

.feature-item.wood_overlay_6 {
  position: relative;
  border: 5px solid transparent;
  background:
    linear-gradient(white, white) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_6.jpg") border-box;
  background-size: auto, 80px;
}

.feature-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
}

.feature-title {
  font-size: 16px;
  font-weight: 600;
  color: #293b2e;
  margin-bottom: 0.8rem;
  letter-spacing: 0.5px;
  text-transform: none;
}

.feature-description {
  font-size: 14px;
  line-height: 1.6;
  color: #293b2e;
  margin: 0;
  opacity: 0.85;
  text-transform: none;
  font-weight: 400;
}

.sidebar {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  position: sticky;
  top: 2rem;
}

.info-card,
.contact-card {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  border: 2px solid rgb(41, 59, 46);
  position: relative;
  overflow: hidden;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #293b2e;
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid rgba(41, 59, 46, 0.1);
  letter-spacing: 0.5px;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
  position: relative;
  z-index: 1;
}

.info-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  position: relative;
  z-index: 1;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  padding: 0.8rem 0;
  border-bottom: 1px solid rgba(41, 59, 46, 0.05);
}

.info-item:last-child {
  border-bottom: none;
}

.info-label {
  font-weight: 600;
  color: #293b2e;
  font-size: 14px;
  min-width: 80px;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
}

.info-value {
  color: #293b2e;
  font-size: 14px;
  text-align: right;
  flex: 1;
  opacity: 0.85;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
  font-weight: 400;
}

.contact-text {
  color: #293b2e;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  opacity: 0.85;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
  font-weight: 400;
  font-size: 14px;
  position: relative;
  z-index: 1;
}

.contact-button {
  width: 100%;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #a15e3c 0%, #b36e4f 100%);
  color: white;
  border: none;
  border-radius: 15px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(161, 94, 60, 0.3);
  position: relative;
  z-index: 1;
}

.contact-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(161, 94, 60, 0.4);
}

@media (max-width: 1024px) {
  .content-layout {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  
  .sidebar {
    position: static;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    display: grid;
  }
}

@media (max-width: 768px) {
  .service-details-section {
    padding: 2rem 1rem;
  }
  
  .service-title {
    font-size: 2rem;
  }
  
  .service-meta {
    gap: 1rem;
  }
  
  .main-content {
    gap: 2rem;
  }
  
  .service-description,
  .service-overview,
  .service-details,
  .info-card,
  .contact-card {
    padding: 1.5rem;
  }
  
  .feature-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .sidebar {
    grid-template-columns: 1fr;
  }
}
</style>