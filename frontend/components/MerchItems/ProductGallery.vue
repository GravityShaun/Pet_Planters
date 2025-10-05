<template>
  <div class="product-gallery-section" ref="galleryRef">
    <div class="gallery-container">
      <div class="gallery-header">
        <h2 class="gallery-title">Product Gallery</h2>
        <p class="gallery-subtitle">Take a closer look at {{ product?.title }}</p>
        <div class="title-underline"></div>
      </div>

      <div class="image-gallery">
        <!-- Main Image Display -->
        <div class="main-gallery-image">
          <div class="main-image-container">
            <div class="image-placeholder main-placeholder">
              <div class="placeholder-icon main-icon">{{ product?.icon }}</div>
              <div class="placeholder-text">{{ product?.title }}</div>
              <div class="image-badge">{{ selectedImageIndex + 1 }} / {{ galleryImages.length }}</div>
            </div>
          </div>
          
          <!-- Image Navigation -->
          <div class="image-controls">
            <button 
              class="nav-btn prev"
              @click="previousImage"
              :disabled="selectedImageIndex === 0"
            >
              ‹
            </button>
            <button 
              class="nav-btn next"
              @click="nextImage"
              :disabled="selectedImageIndex === galleryImages.length - 1"
            >
              ›
            </button>
          </div>
        </div>

        <!-- Thumbnail Grid -->
        <div class="thumbnail-grid">
          <div 
            v-for="(image, index) in galleryImages"
            :key="index"
            class="gallery-thumbnail"
            :class="{ active: selectedImageIndex === index }"
            @click="selectedImageIndex = index"
          >
            <div class="thumb-placeholder">
              <div class="thumb-icon">{{ product?.icon }}</div>
              <div class="thumb-label">{{ image.label }}</div>
            </div>
          </div>
        </div>

        <!-- Gallery Features -->
        <div class="gallery-features">
          <div class="feature-grid">
            <div class="gallery-feature">
              <div class="feature-icon">📸</div>
              <div class="feature-text">High-Quality Images</div>
            </div>
            <div class="gallery-feature">
              <div class="feature-icon">🔍</div>
              <div class="feature-text">Zoom & Detail Views</div>
            </div>
            <div class="gallery-feature">
              <div class="feature-icon">🎨</div>
              <div class="feature-text">Multiple Angles</div>
            </div>
            <div class="gallery-feature">
              <div class="feature-icon">✨</div>
              <div class="feature-text">Product Showcase</div>
            </div>
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
  product: {
    type: Object,
    required: true
  }
})

// Refs
const galleryRef = ref(null)
const selectedImageIndex = ref(0)

// Gallery images (using product images or placeholder data)
const galleryImages = ref([
  { label: 'Front View', url: props.product?.images?.[0] || '/placeholder-front.jpg' },
  { label: 'Back View', url: props.product?.images?.[1] || '/placeholder-back.jpg' },
  { label: 'Side View', url: props.product?.images?.[2] || '/placeholder-side.jpg' },
  { label: 'Detail Shot', url: props.product?.images?.[3] || '/placeholder-detail.jpg' },
  { label: 'Lifestyle', url: props.product?.images?.[4] || '/placeholder-lifestyle.jpg' }
])

// Methods
function nextImage() {
  if (selectedImageIndex.value < galleryImages.value.length - 1) {
    selectedImageIndex.value++
  }
}

function previousImage() {
  if (selectedImageIndex.value > 0) {
    selectedImageIndex.value--
  }
}

onMounted(() => {
    setTimeout(() => {
  initializeAnimations()
    }, 100)
})

function initializeAnimations() {
  if (galleryRef.value) {
    gsap.from('.gallery-header', {
      scrollTrigger: {
        trigger: '.product-gallery-section',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      y: 50,
      opacity: 0,
      duration: 0.8,
      ease: "power2.out"
    })

    gsap.from('.main-gallery-image', {
      scrollTrigger: {
        trigger: '.image-gallery',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      x: -100,
      opacity: 0,
      duration: 1,
      ease: "power2.out"
    })

    gsap.from('.thumbnail-grid', {
      scrollTrigger: {
        trigger: '.image-gallery',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      y: 50,
      opacity: 0,
      duration: 0.8,
      ease: "power2.out",
      delay: 0.3
    })

    gsap.from('.gallery-features', {
      scrollTrigger: {
        trigger: '.gallery-features',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      y: 30,
      opacity: 0,
      duration: 0.6,
      ease: "power2.out"
    })
  }
}
</script>

<style scoped>
.product-gallery-section {
  padding: 5rem 0;
  position: relative;
}

.product-gallery-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="m 60,0 L 0,0 0,60" fill="none" stroke="%23293b2e" stroke-width="0.5" opacity="0.03"/></pattern></defs><rect width="100%" height="100%" fill="url(%23grid)" /></svg>') repeat;
  pointer-events: none;
  z-index: 0;
}

.gallery-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
}

.gallery-header {
  text-align: center;
  margin-bottom: 4rem;
}

.gallery-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.gallery-subtitle {
  font-size: 1.1rem;
  color: #293b2e;
  opacity: 0.8;
  margin-bottom: 1.5rem;
  font-family: system-ui, -apple-system, sans-serif;
}

.title-underline {
  width: 80px;
  height: 4px;
  background: linear-gradient(135deg, #a15e3c 0%, #b36e4f 100%);
  margin: 0 auto;
  border-radius: 2px;
}

.image-gallery {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(41, 59, 46, 0.1);
}

.main-gallery-image {
  position: relative;
  margin-bottom: 2rem;
}

.main-image-container {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  aspect-ratio: 16/9;
}

.image-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  position: relative;
}

.main-placeholder {
  background: linear-gradient(135deg, rgba(161, 94, 60, 0.1) 0%, rgba(161, 94, 60, 0.05) 100%);
}

.placeholder-icon.main-icon {
  font-size: 8rem;
  opacity: 0.7;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,0.1));
  animation: galleryFloat 6s ease-in-out infinite;
}

@keyframes galleryFloat {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-10px) scale(1.05); }
}

.placeholder-text {
  font-size: 1.5rem;
  font-weight: 600;
  color: #293b2e;
  text-align: center;
  opacity: 0.8;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.image-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(161, 94, 60, 0.9);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.5px;
  backdrop-filter: blur(10px);
}

.image-controls {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 0 1rem;
  pointer-events: none;
}

.nav-btn {
  width: 50px;
  height: 50px;
  background: rgba(255, 255, 255, 0.9);
  border: 2px solid rgba(41, 59, 46, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: 600;
  color: #293b2e;
  cursor: pointer;
  transition: all 0.3s ease;
  pointer-events: auto;
  backdrop-filter: blur(10px);
}

.nav-btn:hover:not(:disabled) {
  background: #293b2e;
  color: white;
  transform: scale(1.1);
}

.nav-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.thumbnail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.gallery-thumbnail {
  aspect-ratio: 1;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.gallery-thumbnail:hover, .gallery-thumbnail.active {
  border-color: #a15e3c;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(161, 94, 60, 0.3);
}

.thumb-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.thumb-icon {
  font-size: 2rem;
  opacity: 0.7;
}

.thumb-label {
  font-size: 10px;
  font-weight: 600;
  color: #293b2e;
  opacity: 0.8;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.gallery-features {
  border-top: 1px solid rgba(41, 59, 46, 0.1);
  padding-top: 2rem;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.gallery-feature {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 1rem;
  background: rgba(161, 94, 60, 0.05);
  border-radius: 8px;
  border-left: 4px solid #a15e3c;
  transition: all 0.3s ease;
}

.gallery-feature:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(161, 94, 60, 0.2);
}

.feature-icon {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.feature-text {
  font-size: 14px;
  font-weight: 600;
  color: #293b2e;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

@media (max-width: 768px) {
  .gallery-title {
    font-size: 2rem;
  }

  .gallery-container {
    padding: 0 1rem;
  }

  .thumbnail-grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .feature-grid {
    grid-template-columns: 1fr;
  }

  .image-controls {
    padding: 0 0.5rem;
  }

  .nav-btn {
    width: 40px;
    height: 40px;
    font-size: 1.2rem;
  }
}

@media (max-width: 480px) {
  .product-gallery-section {
    padding: 3rem 0;
  }

  .gallery-title {
    font-size: 1.8rem;
  }

  .thumbnail-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .placeholder-icon.main-icon {
    font-size: 6rem;
  }

  .placeholder-text {
    font-size: 1.2rem;
  }
}
</style>