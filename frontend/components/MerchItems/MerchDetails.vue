<template>
  <div class="merch-details" ref="detailsRef">
    <div class="details-container">
      <div class="details-header">
        <h2 class="details-title">Product Details</h2>
        <div class="title-underline"></div>
      </div>

      <div class="details-content">
        <!-- Product Gallery -->
        <div class="product-gallery">
          <div class="main-image">
            <div class="image-placeholder">
              <div class="placeholder-icon">{{ product?.icon }}</div>
              <div class="placeholder-text">{{ product?.title }}</div>
            </div>
          </div>
          <div class="thumbnail-gallery" v-if="product?.images && product.images.length > 1">
            <div 
              v-for="(image, index) in product.images" 
              :key="index"
              class="thumbnail"
              :class="{ active: selectedImage === index }"
              @click="selectedImage = index"
            >
              <div class="thumb-icon">{{ product?.icon }}</div>
            </div>
          </div>
        </div>

        <!-- Product Information -->
        <div class="product-info">
          <div class="info-section">
            <h3 class="section-title">Product Information</h3>
            <div class="info-grid">
              <div class="info-item">
                <span class="info-label">Category:</span>
                <span class="info-value">{{ product?.category }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Price:</span>
                <span class="info-value price">{{ product?.price }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Availability:</span>
                <span class="info-value" :class="{ 'in-stock': product?.inStock, 'out-stock': !product?.inStock }">
                  {{ product?.inStock ? 'In Stock' : 'Out of Stock' }}
                </span>
              </div>
            </div>
          </div>

          <div class="info-section" v-if="product?.sizes && product.sizes.length > 0">
            <h3 class="section-title">Available Sizes</h3>
            <div class="size-chart">
              <div
                v-for="size in product.sizes"
                :key="size"
                class="size-item"
                :class="{ selected: selectedSize === size }"
                @click="selectedSize = size"
              >
                {{ size }}
              </div>
            </div>
          </div>

          <div class="info-section" v-if="product?.colors && product.colors.length > 0">
            <h3 class="section-title">Available Colors</h3>
            <div class="color-chart">
              <div
                v-for="color in product.colors"
                :key="color"
                class="color-item"
                :class="{ selected: selectedColor === color }"
                @click="selectedColor = color"
              >
                {{ color }}
              </div>
            </div>
          </div>

          <div class="info-section">
            <h3 class="section-title">Description</h3>
            <p class="product-description">{{ product?.description }}</p>
          </div>

          <!-- Features List -->
          <div class="info-section">
            <h3 class="section-title">Features</h3>
            <ul class="features-list">
              <li class="feature-item">
                <span class="feature-icon">✓</span>
                <span class="feature-text">High-quality materials and construction</span>
              </li>
              <li class="feature-item">
                <span class="feature-icon">✓</span>
                <span class="feature-text">Official Joel's Handys branding</span>
              </li>
              <li class="feature-item">
                <span class="feature-icon">✓</span>
                <span class="feature-text">Durable and long-lasting design</span>
              </li>
              <li class="feature-item" v-if="product?.category === 'APPAREL'">
                <span class="feature-icon">✓</span>
                <span class="feature-text">Comfortable fit for all-day wear</span>
              </li>
              <li class="feature-item" v-if="product?.category === 'DRINKWARE'">
                <span class="feature-icon">✓</span>
                <span class="feature-text">Dishwasher safe for easy cleaning</span>
              </li>
              <li class="feature-item" v-if="product?.category === 'WORKWEAR'">
                <span class="feature-icon">✓</span>
                <span class="feature-text">Professional-grade materials</span>
              </li>
            </ul>
          </div>

          <!-- Care Instructions -->
          <div class="info-section">
            <h3 class="section-title">Care Instructions</h3>
            <div class="care-instructions">
              <div class="care-item" v-if="product?.category === 'APPAREL'">
                <span class="care-icon">🧺</span>
                <span class="care-text">Machine wash cold, tumble dry low</span>
              </div>
              <div class="care-item" v-if="product?.category === 'DRINKWARE'">
                <span class="care-icon">🍽️</span>
                <span class="care-text">Dishwasher safe, hand wash recommended</span>
              </div>
              <div class="care-item" v-if="product?.category === 'WORKWEAR'">
                <span class="care-icon">🧤</span>
                <span class="care-text">Wipe clean with damp cloth, air dry</span>
              </div>
              <div class="care-item" v-if="product?.category === 'ACCESSORIES'">
                <span class="care-icon">🧽</span>
                <span class="care-text">Spot clean as needed, store in dry place</span>
              </div>
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

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

// Refs
const detailsRef = ref(null)
const selectedImage = ref(0)
const selectedSize = ref(null)
const selectedColor = ref(null)

onMounted(() => {
  gsap.from(detailsRef.value, {
    opacity: 0,
    y: 50,
    duration: 1.2,
    ease: "power2.out"
  })
})
</script>

<style scoped>
.merch-details {
  padding: 5rem 0;
  position: relative;
  z-index: 2;
  padding-top: 200px;
}


.details-container {
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 2;
  width: 90%
}

.details-header {
  text-align: center;
  margin-bottom: 4rem;
}

.details-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.title-underline {
  width: 80px;
  height: 4px;
  background: linear-gradient(135deg, #a15e3c 0%, #b36e4f 100%);
  margin: 0 auto;
  border-radius: 2px;
}

.details-content {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 4rem;
  align-items: start;
}

.product-gallery {
  position: sticky;
  top: 2rem;
}

.main-image {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border: 2px solid rgba(41, 59, 46, 0.1);
  margin-bottom: 1rem;
}

.image-placeholder {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  padding: 3rem;
  gap: 1rem;
}

.placeholder-icon {
  font-size: 6rem;
  opacity: 0.8;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,0.1));
}

.placeholder-text {
  font-size: 1.2rem;
  font-weight: 600;
  color: #293b2e;
  text-align: center;
  opacity: 0.7;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.thumbnail-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
  gap: 0.8rem;
}

.thumbnail {
  aspect-ratio: 1;
  background: white;
  border: 2px solid rgba(41, 59, 46, 0.1);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  overflow: hidden;
}

.thumbnail:hover, .thumbnail.active {
  border-color: #a15e3c;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(161, 94, 60, 0.2);
}

.thumb-icon {
  font-size: 2rem;
  opacity: 0.8;
}

.product-info {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
}

.info-section {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  border: 1px solid rgba(41, 59, 46, 0.1);
  transition: all 0.3s ease;
}

.info-section:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 1.5rem;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  position: relative;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -0.5rem;
  left: 0;
  width: 40px;
  height: 2px;
  background: #a15e3c;
  border-radius: 1px;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.8rem 0;
  border-bottom: 1px solid rgba(41, 59, 46, 0.1);
}

.info-label {
  font-weight: 600;
  color: #293b2e;
  opacity: 0.8;
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 0.8px;
}

.info-value {
  font-weight: 600;
  color: #293b2e;
  font-size: 14px;
}

.info-value.price {
  color: #a15e3c;
  font-size: 16px;
}

.info-value.in-stock {
  color: #16a34a;
}

.info-value.out-stock {
  color: #dc2626;
}

.size-chart, .color-chart {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
}

.size-item, .color-item {
  padding: 0.6rem 1.2rem;
  background: rgba(41, 59, 46, 0.05);
  border: 1px solid rgba(41, 59, 46, 0.2);
  border-radius: 6px;
  font-weight: 500;
  font-size: 13px;
  color: #293b2e;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.size-item:hover, .color-item:hover {
  background: rgba(41, 59, 46, 0.1);
  border-color: #a15e3c;
  transform: translateY(-2px);
}

.size-item.selected, .color-item.selected {
  background: #a15e3c;
  color: white;
  border-color: #a15e3c;
  box-shadow: 0 4px 12px rgba(161, 94, 60, 0.3);
}

.product-description {
  font-size: 16px;
  line-height: 1.7;
  color: #293b2e;
  opacity: 0.9;
  font-family: system-ui, -apple-system, sans-serif;
}

.features-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.8rem 0;
  border-bottom: 1px solid rgba(41, 59, 46, 0.05);
}

.feature-item:last-child {
  border-bottom: none;
}

.feature-icon {
  width: 20px;
  height: 20px;
  background: #16a34a;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: bold;
  flex-shrink: 0;
}

.feature-text {
  color: #293b2e;
  font-size: 14px;
  font-weight: 500;
}

.care-instructions {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.care-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(161, 94, 60, 0.05);
  border-radius: 8px;
  border-left: 4px solid #a15e3c;
}

.care-icon {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.care-text {
  color: #293b2e;
  font-size: 14px;
  font-weight: 500;
}

@media (max-width: 768px) {
  .details-content {
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  .product-gallery {
    position: static;
  }

  .details-title {
    font-size: 2rem;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }

  .details-container {
    padding: 0 1rem;
  }

  .info-section {
    padding: 1.5rem;
  }

  .thumbnail-gallery {
    grid-template-columns: repeat(auto-fit, minmax(60px, 1fr));
  }
}

@media (max-width: 480px) {
  .merch-details {
    padding: 3rem 0;
  }

  .details-title {
    font-size: 1.8rem;
  }

  .size-chart, .color-chart {
    justify-content: center;
  }

  .care-item {
    flex-direction: column;
    text-align: center;
    gap: 0.5rem;
  }
}
</style>