<template>
  <div class="merch-hero" ref="heroRef">
    <div class="hero-content">
      <div class="product-badge">
        <span class="product-number">{{ product?.id }}</span>
        <span class="product-category">{{ product?.category }}</span>
      </div>
      <div class="product-icon-wrapper">
        <div class="product-icon">{{ product?.icon }}</div>
      </div>
      <h1 class="product-title">{{ product?.title }}</h1>
      <p class="product-subtitle">{{ product?.description }}</p>
      
      <div class="product-pricing">
        <div class="pricing-card">
          <div class="price-label">Price</div>
          <div class="price">{{ product?.price }}</div>
        </div>
        <div class="stock-card">
          <div class="stock-label">Availability</div>
          <div class="stock-status" :class="{ 'in-stock': product?.inStock }">
            {{ product?.inStock ? 'In Stock' : 'Out of Stock' }}
          </div>
        </div>
      </div>
      
      <div class="product-options">
        <div v-if="product?.sizes && product.sizes.length > 0" class="size-options">
          <label class="option-label">Size:</label>
          <div class="option-buttons">
            <button 
              v-for="size in product.sizes" 
              :key="size"
              class="option-btn"
              :class="{ active: selectedSize === size }"
              @click="selectedSize = size"
            >
              {{ size }}
            </button>
          </div>
        </div>
        
        <div v-if="product?.colors && product.colors.length > 0" class="color-options">
          <label class="option-label">Color:</label>
          <div class="option-buttons">
            <button 
              v-for="color in product.colors" 
              :key="color"
              class="option-btn"
              :class="{ active: selectedColor === color }"
              @click="selectedColor = color"
            >
              {{ color }}
            </button>
          </div>
        </div>
      </div>
      
      <div class="hero-actions">
        <button class="hero-cta primary" @click="scrollToCheckout" :disabled="!product?.inStock">
          {{ product?.inStock ? 'Add to Cart' : 'Out of Stock' }}
        </button>
        <button class="hero-cta secondary" @click="scrollToDetails">
          Product Details
        </button>
      </div>
    </div>
    
    <div class="hero-visual">
      <div class="showcase-wrapper">
        <div 
          :class="['product-showcase', getWoodClass()]"
          ref="showcaseRef"
        >
          <div class="paperOverlayGrid"></div>
          <div class="showcase-content">
            <div class="showcase-icon">{{ product?.icon }}</div>
            <div class="showcase-badge">Official Merch</div>
          </div>
        </div>
        <div class="showcase-highlights">
          <div class="highlight-item">
            <span class="highlight-icon">🚚</span>
            <span class="highlight-text">Free Shipping</span>
          </div>
          <div class="highlight-item">
            <span class="highlight-icon">↩️</span>
            <span class="highlight-text">30-Day Returns</span>
          </div>
          <div class="highlight-item">
            <span class="highlight-icon">⭐</span>
            <span class="highlight-text">Quality Guaranteed</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { gsap } from 'gsap'

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['scroll-to-details'])

// Refs
const heroRef = ref(null)
const showcaseRef = ref(null)

// Selected options
const selectedSize = ref(props.product?.sizes?.[0] || '')
const selectedColor = ref(props.product?.colors?.[0] || '')

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
  if (!props.product) return 'wood_overlay_1'
  const index = parseInt(props.product.id) % backgroundClasses.length
  return backgroundClasses[index]
}

function scrollToDetails() {
  emit('scroll-to-details')
}

function scrollToCheckout() {
  const checkoutSection = document.querySelector('.merch-checkout')
  if (checkoutSection) {
    checkoutSection.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  }
}

onMounted(() => {
  initializeAnimations()
})

function initializeAnimations() {
  // Hero animation
  if (heroRef.value) {
    gsap.from('.hero-content > *', {
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
.merch-hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  gap: 3rem;
  position: relative;
  overflow: hidden;
  width: 85%;
  margin-left: 9%;
}

.merch-hero::before {
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

.product-badge {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.product-number {
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

.product-category {
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

.product-icon-wrapper {
  margin-bottom: 2rem;
  position: relative;
}

.product-icon {
  font-size: 5rem;
  display: block;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,0.1));
  animation: iconFloat 6s ease-in-out infinite;
}

@keyframes iconFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

.product-title {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.05;
  color: #293b2e;
  background: linear-gradient(135deg, #293b2e 0%, #1a2621 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-transform: uppercase;
}

.product-subtitle {
  font-size: 18px;
  line-height: 1.6;
  margin-bottom: 3rem;
  color: #293b2e;
  opacity: 0.85;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
  font-weight: 400;
  max-width: 550px;
}

.product-pricing {
  display: flex;
  gap: 1.5rem;
  align-items: stretch;
  margin-bottom: 2rem;
}

.pricing-card, .stock-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  border: 2px solid rgba(41, 59, 46, 0.1);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  min-width: 140px;
}

.pricing-card:hover, .stock-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
  border-color: rgba(161, 94, 60, 0.3);
}

.price-label, .stock-label {
  font-size: 10px;
  color: #293b2e;
  opacity: 0.7;
  font-weight: 500;
  letter-spacing: 1px;
  margin-bottom: 0.5rem;
  display: block;
  text-transform: uppercase;
}

.price {
  font-size: 20px;
  font-weight: 700;
  color: #a15e3c;
  letter-spacing: 0.3px;
}

.stock-status {
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 0.5px;
  color: #dc2626;
}

.stock-status.in-stock {
  color: #16a34a;
}

.product-options {
  margin-bottom: 2.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.size-options, .color-options {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.option-label {
  font-size: 14px;
  color: #293b2e;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.option-buttons {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
}

.option-btn {
  padding: 0.6rem 1.2rem;
  border: 2px solid rgba(41, 59, 46, 0.2);
  background: white;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 500;
  color: #293b2e;
  cursor: pointer;
  transition: all 0.3s ease;
}

.option-btn:hover {
  border-color: rgba(161, 94, 60, 0.4);
  background: rgba(161, 94, 60, 0.05);
}

.option-btn.active {
  border-color: #a15e3c;
  background: #a15e3c;
  color: white;
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

.hero-cta.primary:not(:disabled):hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(161, 94, 60, 0.4);
}

.hero-cta.primary:disabled {
  background: #ccc;
  cursor: not-allowed;
  box-shadow: none;
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

.product-showcase {
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

.product-showcase:hover {
  transform: translateY(-5px) rotateY(5deg);
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.2);
}

.product-showcase::before {
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

.product-showcase.wood_overlay_1::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_1.jpg");
}

.product-showcase.wood_overlay_2::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_2.jpg");
}

.product-showcase.wood_overlay_3::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_3.jpg");
}

.product-showcase.wood_overlay_4::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_4.jpg");
}

.product-showcase.wood_overlay_5::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_5.jpg");
}

.product-showcase.wood_overlay_6::before {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_6.jpg");
}

.showcase-content {
  position: relative;
  z-index: 2;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: white;
  margin: 15px;
  border-radius: 8px;
  gap: 1rem;
}

.showcase-icon {
  font-size: 7rem;
  filter: drop-shadow(0 6px 15px rgba(0,0,0,0.15));
  animation: showcaseFloat 4s ease-in-out infinite;
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
  border: 1px solid rgba(41, 59, 46, 0.1);
  transition: all 0.3s ease;
  animation: slideInRight 0.6s ease-out forwards;
  opacity: 0;
  transform: translateX(20px);
  text-transform: uppercase;
}

.highlight-item:nth-child(1) { animation-delay: 0.2s; }
.highlight-item:nth-child(2) { animation-delay: 0.4s; }
.highlight-item:nth-child(3) { animation-delay: 0.6s; }

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

@media (max-width: 768px) {
  .merch-hero {
    flex-direction: column;
    gap: 3rem;
    padding: 2rem 1rem;
    text-align: center;
    min-height: 70vh;
  }

  .product-title {
    font-size: 2.5rem;
  }

  .product-subtitle {
    font-size: 16px;
  }

  .product-pricing {
    justify-content: center;
  }

  .pricing-card, .stock-card {
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

  .product-showcase {
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
  .product-pricing {
    flex-direction: column;
    gap: 1rem;
    width: 100%;
  }

  .pricing-card, .stock-card {
    width: 100%;
  }

  .product-title {
    font-size: 2rem;
  }

  .product-showcase {
    width: 250px;
    height: 320px;
  }

  .showcase-highlights {
    flex-direction: column;
    gap: 0.8rem;
  }

  .option-buttons {
    justify-content: center;
  }
}
</style>