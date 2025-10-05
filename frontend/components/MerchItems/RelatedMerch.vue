<template>
  <div class="related-merch" ref="relatedRef">
    <div class="related-container">
      <div class="related-header">
        <h2 class="related-title">You Might Also Like</h2>
        <p class="related-subtitle">Check out these other great items from our merchandise collection</p>
        <div class="title-underline"></div>
      </div>

      <div class="related-grid" v-if="relatedProducts && relatedProducts.length > 0">
        <div 
          v-for="item in relatedProducts" 
          :key="item.id"
          class="related-item"
          :style="{ '--bg-color': item.bgColor }"
          @click="navigateToProduct(item)"
        >
          <div class="item-image">
            <div class="item-icon">{{ item.icon }}</div>
            <div class="item-badge">{{ item.category }}</div>
          </div>
          
          <div class="item-content">
            <h3 class="item-title">{{ item.title }}</h3>
            <p class="item-description">{{ truncateDescription(item.description) }}</p>
            
            <div class="item-details">
              <div class="item-price">{{ item.price }}</div>
              <div class="item-stock" :class="{ 'in-stock': item.inStock, 'out-stock': !item.inStock }">
                {{ item.inStock ? 'In Stock' : 'Out of Stock' }}
              </div>
            </div>

            <div class="item-options" v-if="item.colors && item.colors.length > 0">
              <span class="options-label">Colors:</span>
              <div class="color-dots">
                <div 
                  v-for="(color, index) in item.colors.slice(0, 3)" 
                  :key="color"
                  class="color-dot"
                  :title="color"
                >
                  {{ color.charAt(0) }}
                </div>
                <div v-if="item.colors.length > 3" class="color-more">
                  +{{ item.colors.length - 3 }}
                </div>
              </div>
            </div>

            <button 
              class="item-cta"
              @click.stop="navigateToProduct(item)"
              :disabled="!item.inStock"
            >
              {{ item.inStock ? 'View Product' : 'Out of Stock' }}
            </button>
          </div>

          <div class="item-hover-overlay">
            <div class="hover-content">
              <div class="hover-icon">{{ item.icon }}</div>
              <div class="hover-text">Click to View</div>
            </div>
          </div>
        </div>
      </div>

      <div class="browse-all">
        <NuxtLink to="/merch" class="browse-btn">
          <span class="browse-icon">🛍️</span>
          <span class="browse-text">Browse All Merchandise</span>
        </NuxtLink>
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
  },
  relatedProducts: {
    type: Array,
    default: () => []
  }
})

// Refs
const relatedRef = ref(null)

// Methods
function truncateDescription(description) {
  if (!description) return ''
  return description.length > 100 ? description.substring(0, 100) + '...' : description
}

function navigateToProduct(item) {
  // Navigate to the product page
  const router = useRouter()
  router.push(`/merch_items/${item.id}`)
}

onMounted(() => {
  setTimeout(() => {
    initializeAnimations()
  }, 100)
})

function initializeAnimations() {
  if (relatedRef.value) {
    // Animate header
    gsap.from('.related-header', {
      scrollTrigger: {
        trigger: '.related-merch',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      y: 50,
      opacity: 0,
      duration: 0.8,
      ease: "power2.out"
    })

    // Animate grid items
    gsap.from('.related-item', {
      scrollTrigger: {
        trigger: '.related-grid',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      y: 100,
      opacity: 0,
      duration: 0.8,
      stagger: 0.2,
      ease: "power2.out"
    })

    // Animate browse button
    gsap.from('.browse-all', {
      scrollTrigger: {
        trigger: '.browse-all',
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
.related-merch {
  padding: 5rem 0;
  position: relative;
}

.related-merch::before {
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

.related-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
}

.related-header {
  text-align: center;
  margin-bottom: 4rem;
}

.related-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.related-subtitle {
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

.related-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.related-item {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border: 2px solid rgba(41, 59, 46, 0.1);
  transition: all 0.4s ease;
  cursor: pointer;
  position: relative;
  transform-style: preserve-3d;
}

.related-item:hover {
  transform: translateY(-8px) rotateX(5deg);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  border-color: var(--bg-color);
}

.item-image {
  height: 200px;
  background: linear-gradient(135deg, var(--bg-color) 0%, color-mix(in srgb, var(--bg-color) 80%, black) 100%);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.item-image::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="dots" width="40" height="40" patternUnits="userSpaceOnUse"><circle cx="20" cy="20" r="1.5" fill="white" opacity="0.1"/></pattern></defs><rect width="100%" height="100%" fill="url(%23dots)" /></svg>') repeat;
  pointer-events: none;
}

.item-icon {
  font-size: 4rem;
  position: relative;
  z-index: 2;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,0.2));
  animation: itemFloat 4s ease-in-out infinite;
}

@keyframes itemFloat {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-8px) scale(1.05); }
}

.item-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(255, 255, 255, 0.9);
  color: var(--bg-color);
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  z-index: 2;
}

.item-content {
  padding: 1.5rem;
}

.item-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #293b2e;
  margin-bottom: 0.8rem;
  line-height: 1.3;
}

.item-description {
  font-size: 14px;
  line-height: 1.5;
  color: #293b2e;
  opacity: 0.8;
  margin-bottom: 1rem;
  font-family: system-ui, -apple-system, sans-serif;
}

.item-details {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(41, 59, 46, 0.1);
}

.item-price {
  font-size: 1.1rem;
  font-weight: 700;
  color: #a15e3c;
  letter-spacing: 0.5px;
}

.item-stock {
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.item-stock.in-stock {
  color: #16a34a;
}

.item-stock.out-stock {
  color: #dc2626;
}

.item-options {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin-bottom: 1.5rem;
}

.options-label {
  font-size: 12px;
  font-weight: 500;
  color: #293b2e;
  opacity: 0.8;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.color-dots {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.color-dot {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--bg-color);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 600;
  color: white;
  text-transform: uppercase;
  border: 2px solid rgba(41, 59, 46, 0.2);
  transition: all 0.2s ease;
}

.color-dot:hover {
  transform: scale(1.1);
  border-color: var(--bg-color);
}

.color-more {
  font-size: 10px;
  color: #293b2e;
  opacity: 0.7;
  font-weight: 500;
  padding: 0.2rem 0.4rem;
  background: rgba(41, 59, 46, 0.1);
  border-radius: 10px;
}

.item-cta {
  width: 100%;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 8px;
  background: linear-gradient(135deg, var(--bg-color) 0%, color-mix(in srgb, var(--bg-color) 80%, black) 100%);
  color: white;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.item-cta:not(:disabled):hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

.item-cta:disabled {
  background: #ccc;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.item-hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.6) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: all 0.3s ease;
  z-index: 10;
}

.related-item:hover .item-hover-overlay {
  opacity: 1;
}

.hover-content {
  text-align: center;
  color: white;
  transform: translateY(20px);
  transition: all 0.3s ease;
}

.related-item:hover .hover-content {
  transform: translateY(0);
}

.hover-icon {
  font-size: 3rem;
  margin-bottom: 0.5rem;
  filter: drop-shadow(0 2px 8px rgba(0,0,0,0.3));
}

.hover-text {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.browse-all {
  text-align: center;
}

.browse-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
  padding: 1rem 2.5rem;
  background: linear-gradient(135deg, #a15e3c 0%, #b36e4f 100%);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(161, 94, 60, 0.3);
}

.browse-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(161, 94, 60, 0.4);
}

.browse-icon {
  font-size: 1.2rem;
}

@media (max-width: 768px) {
  .related-grid {
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
  }

  .related-title {
    font-size: 2rem;
  }

  .related-container {
    padding: 0 1rem;
  }

  .related-item {
    transform: none;
  }

  .related-item:hover {
    transform: translateY(-4px);
  }

  .item-hover-overlay {
    display: none;
  }
}

@media (max-width: 480px) {
  .related-merch {
    padding: 3rem 0;
  }

  .related-grid {
    grid-template-columns: 1fr;
  }

  .related-title {
    font-size: 1.8rem;
  }

  .item-details {
    flex-direction: column;
    gap: 0.5rem;
    align-items: flex-start;
  }

  .browse-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>