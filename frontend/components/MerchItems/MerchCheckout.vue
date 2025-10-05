<template>
  <div class="merch-checkout" ref="checkoutRef">
    <div class="checkout-container">
      <div class="checkout-header">
        <h2 class="checkout-title">Ready to Order?</h2>
        <p class="checkout-subtitle">Complete your purchase in just a few simple steps</p>
        <div class="title-underline"></div>
      </div>

      <div class="checkout-content">
        <!-- Order Summary -->
        <div class="order-summary">
          <h3 class="summary-title">Order Summary</h3>
          
          <div class="product-summary">
            <div class="product-image">
              <div class="product-icon">{{ product?.icon }}</div>
            </div>
            <div class="product-details">
              <h4 class="product-name">{{ product?.title }}</h4>
              <p class="product-desc">{{ product?.description?.substring(0, 80) }}...</p>
              
              <div class="selection-summary">
                <div v-if="selectedSize" class="selection-item">
                  <span class="selection-label">Size:</span>
                  <span class="selection-value">{{ selectedSize }}</span>
                </div>
                <div v-if="selectedColor" class="selection-item">
                  <span class="selection-label">Color:</span>
                  <span class="selection-value">{{ selectedColor }}</span>
                </div>
                <div class="selection-item">
                  <span class="selection-label">Quantity:</span>
                  <div class="quantity-controls">
                    <button class="qty-btn" @click="decrementQuantity" :disabled="quantity <= 1">-</button>
                    <span class="quantity">{{ quantity }}</span>
                    <button class="qty-btn" @click="incrementQuantity" :disabled="quantity >= 10">+</button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="pricing-breakdown">
            <div class="price-line">
              <span class="price-label">Unit Price:</span>
              <span class="price-value">{{ product?.price }}</span>
            </div>
            <div class="price-line">
              <span class="price-label">Quantity:</span>
              <span class="price-value">{{ quantity }}</span>
            </div>
            <div class="price-line subtotal">
              <span class="price-label">Subtotal:</span>
              <span class="price-value">{{ calculateSubtotal }}</span>
            </div>
            <div class="price-line">
              <span class="price-label">Shipping:</span>
              <span class="price-value free">FREE</span>
            </div>
            <div class="price-line total">
              <span class="price-label">Total:</span>
              <span class="price-value">{{ calculateTotal }}</span>
            </div>
          </div>

          <div class="shipping-info">
            <div class="shipping-benefit">
              <span class="benefit-icon">🚚</span>
              <span class="benefit-text">Free shipping on all orders</span>
            </div>
            <div class="shipping-benefit">
              <span class="benefit-icon">↩️</span>
              <span class="benefit-text">30-day return policy</span>
            </div>
            <div class="shipping-benefit">
              <span class="benefit-icon">⚡</span>
              <span class="benefit-text">Fast 3-5 business day delivery</span>
            </div>
          </div>
        </div>

        <!-- Checkout Form -->
        <div class="checkout-form">
          <div class="form-section">
            <h3 class="form-title">Product Options</h3>
            
            <div v-if="product?.sizes && product.sizes.length > 0" class="form-group">
              <label class="form-label">Size *</label>
              <div class="option-grid">
                <button 
                  v-for="size in product.sizes" 
                  :key="size"
                  class="option-button"
                  :class="{ active: selectedSize === size }"
                  @click="selectedSize = size"
                >
                  {{ size }}
                </button>
              </div>
            </div>

            <div v-if="product?.colors && product.colors.length > 0" class="form-group">
              <label class="form-label">Color *</label>
              <div class="option-grid">
                <button 
                  v-for="color in product.colors" 
                  :key="color"
                  class="option-button"
                  :class="{ active: selectedColor === color }"
                  @click="selectedColor = color"
                >
                  {{ color }}
                </button>
              </div>
            </div>
          </div>

          <div class="form-section">
            <h3 class="form-title">Contact Information</h3>
            
            <div class="form-grid">
              <div class="form-group">
                <label class="form-label">First Name *</label>
                <input 
                  type="text" 
                  class="form-input"
                  v-model="customerInfo.firstName"
                  placeholder="Enter your first name"
                  required
                />
              </div>
              
              <div class="form-group">
                <label class="form-label">Last Name *</label>
                <input 
                  type="text" 
                  class="form-input"
                  v-model="customerInfo.lastName"
                  placeholder="Enter your last name"
                  required
                />
              </div>
              
              <div class="form-group full-width">
                <label class="form-label">Email Address *</label>
                <input 
                  type="email" 
                  class="form-input"
                  v-model="customerInfo.email"
                  placeholder="Enter your email address"
                  required
                />
              </div>
              
              <div class="form-group full-width">
                <label class="form-label">Phone Number</label>
                <input 
                  type="tel" 
                  class="form-input"
                  v-model="customerInfo.phone"
                  placeholder="(555) 123-4567"
                />
              </div>
            </div>
          </div>

          <div class="form-section">
            <h3 class="form-title">Shipping Address</h3>
            
            <div class="form-grid">
              <div class="form-group full-width">
                <label class="form-label">Street Address *</label>
                <input 
                  type="text" 
                  class="form-input"
                  v-model="shippingInfo.address"
                  placeholder="Enter your street address"
                  required
                />
              </div>
              
              <div class="form-group">
                <label class="form-label">City *</label>
                <input 
                  type="text" 
                  class="form-input"
                  v-model="shippingInfo.city"
                  placeholder="Enter your city"
                  required
                />
              </div>
              
              <div class="form-group">
                <label class="form-label">State *</label>
                <input 
                  type="text" 
                  class="form-input"
                  v-model="shippingInfo.state"
                  placeholder="Enter your state"
                  required
                />
              </div>
              
              <div class="form-group">
                <label class="form-label">ZIP Code *</label>
                <input 
                  type="text" 
                  class="form-input"
                  v-model="shippingInfo.zipCode"
                  placeholder="12345"
                  required
                />
              </div>
            </div>
          </div>

          <div class="checkout-actions">
            <button 
              class="checkout-btn primary"
              @click="handleCheckout"
              :disabled="!isFormValid || !product?.inStock"
            >
              <span class="btn-icon">🛒</span>
              <span class="btn-text">Place Order - {{ calculateTotal }}</span>
            </button>
            
            <div class="security-badges">
              <div class="security-badge">
                <span class="badge-icon">🔒</span>
                <span class="badge-text">Secure Checkout</span>
              </div>
              <div class="security-badge">
                <span class="badge-icon">✅</span>
                <span class="badge-text">Safe & Encrypted</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
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
const checkoutRef = ref(null)

// Form state
const selectedSize = ref(props.product?.sizes?.[0] || '')
const selectedColor = ref(props.product?.colors?.[0] || '')
const quantity = ref(1)

const customerInfo = ref({
  firstName: '',
  lastName: '',
  email: '',
  phone: ''
})

const shippingInfo = ref({
  address: '',
  city: '',
  state: '',
  zipCode: ''
})

// Computed properties
const calculateSubtotal = computed(() => {
  if (!props.product?.price) return '$0.00'
  const price = parseFloat(props.product.price.replace('$', ''))
  return `$${(price * quantity.value).toFixed(2)}`
})

const calculateTotal = computed(() => {
  return calculateSubtotal.value // Since shipping is free
})

const isFormValid = computed(() => {
  const requiredCustomer = customerInfo.value.firstName && 
                          customerInfo.value.lastName && 
                          customerInfo.value.email
  
  const requiredShipping = shippingInfo.value.address && 
                          shippingInfo.value.city && 
                          shippingInfo.value.state && 
                          shippingInfo.value.zipCode
  
  const requiredOptions = (!props.product?.sizes || selectedSize.value) &&
                         (!props.product?.colors || selectedColor.value)
  
  return requiredCustomer && requiredShipping && requiredOptions
})

// Methods
function incrementQuantity() {
  if (quantity.value < 10) {
    quantity.value++
  }
}

function decrementQuantity() {
  if (quantity.value > 1) {
    quantity.value--
  }
}

function handleCheckout() {
  if (!isFormValid.value || !props.product?.inStock) return
  
  const orderData = {
    product: props.product,
    selectedSize: selectedSize.value,
    selectedColor: selectedColor.value,
    quantity: quantity.value,
    customer: customerInfo.value,
    shipping: shippingInfo.value,
    total: calculateTotal.value
  }
  
  // In a real application, this would submit to a payment processor
  console.log('Order submitted:', orderData)
  alert(`Thank you for your order! We'll send a confirmation email to ${customerInfo.value.email}`)
}

onMounted(() => {
  initializeAnimations()
})

function initializeAnimations() {
  if (checkoutRef.value) {
    gsap.from('.checkout-header', {
      scrollTrigger: {
        trigger: '.merch-checkout',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      y: 50,
      opacity: 0,
      duration: 0.8,
      ease: "power2.out"
    })

    gsap.from('.order-summary', {
      scrollTrigger: {
        trigger: '.checkout-content',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      x: -100,
      opacity: 0,
      duration: 1,
      ease: "power2.out"
    })

    gsap.from('.checkout-form', {
      scrollTrigger: {
        trigger: '.checkout-content',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      x: 100,
      opacity: 0,
      duration: 1,
      ease: "power2.out",
      delay: 0.2
    })
  }
}
</script>

<style scoped>
.merch-checkout {
  padding: 5rem 0;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  position: relative;
}

.checkout-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
}

.checkout-header {
  text-align: center;
  margin-bottom: 4rem;
}

.checkout-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.checkout-subtitle {
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

.checkout-content {
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: 3rem;
  align-items: start;
}

.order-summary {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(41, 59, 46, 0.1);
  position: sticky;
  top: 2rem;
}

.summary-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 1.5rem;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  border-bottom: 2px solid #a15e3c;
  padding-bottom: 0.5rem;
}

.product-summary {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid rgba(41, 59, 46, 0.1);
}

.product-image {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border: 2px solid rgba(41, 59, 46, 0.1);
}

.product-icon {
  font-size: 2rem;
  opacity: 0.8;
}

.product-details {
  flex: 1;
}

.product-name {
  font-size: 1.1rem;
  font-weight: 600;
  color: #293b2e;
  margin-bottom: 0.5rem;
}

.product-desc {
  font-size: 13px;
  color: #293b2e;
  opacity: 0.7;
  margin-bottom: 1rem;
  line-height: 1.4;
}

.selection-summary {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.selection-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
}

.selection-label {
  font-weight: 500;
  color: #293b2e;
  opacity: 0.8;
}

.selection-value {
  font-weight: 600;
  color: #293b2e;
}

.quantity-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.qty-btn {
  width: 24px;
  height: 24px;
  border: 1px solid rgba(41, 59, 46, 0.3);
  background: white;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-weight: 600;
  font-size: 12px;
  color: #293b2e;
  transition: all 0.2s ease;
}

.qty-btn:hover:not(:disabled) {
  background: #293b2e;
  color: white;
}

.qty-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.quantity {
  font-weight: 600;
  font-size: 14px;
  color: #293b2e;
  min-width: 20px;
  text-align: center;
}

.pricing-breakdown {
  margin-bottom: 2rem;
}

.price-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0;
  font-size: 14px;
}

.price-line.subtotal {
  border-top: 1px solid rgba(41, 59, 46, 0.1);
  margin-top: 0.5rem;
  padding-top: 1rem;
  font-weight: 600;
}

.price-line.total {
  border-top: 2px solid #a15e3c;
  margin-top: 0.5rem;
  padding-top: 1rem;
  font-size: 16px;
  font-weight: 700;
}

.price-label {
  color: #293b2e;
  opacity: 0.8;
}

.price-value {
  font-weight: 600;
  color: #293b2e;
}

.price-value.free {
  color: #16a34a;
}

.shipping-info {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.shipping-benefit {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.6rem;
  background: rgba(161, 94, 60, 0.05);
  border-radius: 6px;
  border-left: 3px solid #a15e3c;
}

.benefit-icon {
  font-size: 1.2rem;
}

.benefit-text {
  font-size: 12px;
  font-weight: 500;
  color: #293b2e;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.checkout-form {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(41, 59, 46, 0.1);
}

.form-section {
  margin-bottom: 2.5rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid rgba(41, 59, 46, 0.1);
}

.form-section:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.form-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #293b2e;
  margin-bottom: 1.5rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group.full-width {
  grid-column: 1 / -1;
}

.form-label {
  font-size: 13px;
  font-weight: 600;
  color: #293b2e;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.form-input {
  padding: 0.8rem 1rem;
  border: 2px solid rgba(41, 59, 46, 0.2);
  border-radius: 8px;
  font-size: 14px;
  color: #293b2e;
  background: white;
  transition: all 0.3s ease;
}

.form-input:focus {
  outline: none;
  border-color: #a15e3c;
  box-shadow: 0 0 0 3px rgba(161, 94, 60, 0.1);
}

.option-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
  gap: 0.8rem;
}

.option-button {
  padding: 0.6rem 1rem;
  border: 2px solid rgba(41, 59, 46, 0.2);
  background: white;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  color: #293b2e;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.option-button:hover {
  border-color: rgba(161, 94, 60, 0.4);
  background: rgba(161, 94, 60, 0.05);
}

.option-button.active {
  border-color: #a15e3c;
  background: #a15e3c;
  color: white;
}

.checkout-actions {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  align-items: center;
}

.checkout-btn {
  width: 100%;
  padding: 1.2rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
}

.checkout-btn.primary {
  background: linear-gradient(135deg, #a15e3c 0%, #b36e4f 100%);
  color: white;
  box-shadow: 0 4px 15px rgba(161, 94, 60, 0.3);
}

.checkout-btn.primary:not(:disabled):hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(161, 94, 60, 0.4);
}

.checkout-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.btn-icon {
  font-size: 1.2rem;
}

.security-badges {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
}

.security-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 12px;
  color: #293b2e;
  opacity: 0.8;
}

.badge-icon {
  font-size: 1rem;
  color: #16a34a;
}

.badge-text {
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

@media (max-width: 768px) {
  .checkout-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .order-summary {
    position: static;
  }

  .checkout-title {
    font-size: 2rem;
  }

  .form-grid {
    grid-template-columns: 1fr;
  }

  .checkout-container {
    padding: 0 1rem;
  }

  .security-badges {
    flex-direction: column;
    gap: 0.8rem;
  }
}

@media (max-width: 480px) {
  .merch-checkout {
    padding: 3rem 0;
  }

  .checkout-title {
    font-size: 1.8rem;
  }

  .product-summary {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }

  .product-image {
    align-self: center;
  }

  .option-grid {
    grid-template-columns: repeat(auto-fit, minmax(60px, 1fr));
  }
}
</style>