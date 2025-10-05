<template>
  <section class="products-section">
    <div class="paperOverlay"></div>
    <div class="products-container">
      <h2 class="section-title">
        Joel's 
        <span class="text-draw" data-draw-line>
          Merch Store
          <div class="text-draw__box" data-draw-line-box></div>
        </span>
      </h2>
      <p class="section-subtitle">Quality merchandise from your trusted handyman</p>
      <div class="products-grid" ref="productsGrid">
        <div v-for="(product, index) in products" :key="index" class="product-card" :data-index="index">
          <NuxtLink :to="`/merch_items/${product.id}`" style="text-decoration: none;">
          <div class="product-image-container">
            <img :src="product.image" :alt="product.name" class="product-image" />
            <div class="product-overlay">
              <button class="view-button">View Details</button>
            </div>
          </div>
          <div class="product-info">
            <h3 class="product-name">{{ product.name }}</h3>
            <p class="product-price">${{ product.price.toFixed(2) }}</p>
          </div>
          </NuxtLink>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';
import merch_1 from '~/assets/content/images/merch/merch_1.png'
import merch_10 from '~/assets/content/images/merch/merch_10.png'
import merch_4 from '~/assets/content/images/merch/merch_4.png'
import merch_6 from '~/assets/content/images/merch/merch_6.png'
import merch_7 from '~/assets/content/images/merch/merch_7.png'
import merch_8 from '~/assets/content/images/merch/merch_8.png'
import merch_9 from '~/assets/content/images/merch/merch_9.png'

const { $gsap: gsap } = useNuxtApp();
const { initUnderlineAnimation } = useUnderlineAnimation();

const productsGrid = ref(null);
const products = ref([
  {
    id: '01',
    name: 'Long Sleeve',
    price: 34.99,
    description: 'Look cool and formal whether you are at church or drinking with the boys under the bridge. Always be prepared.',
    image: merch_1
  },
  {
    id: '02',
    name: 'Hats & Beanies',
    price: 24.99,
    description: 'For when you need to hide that "I just rolled out of bed to fix the sink" hair. Warning: May make you look surprisingly competent.',
    image: merch_4
  },
  {
    id: '03',
    name: 'Mix Tapes',
    price: 19.99,
    description: 'Joel\'s greatest hits featuring "Hammer Time" and "Another Nail in the Wall." Side B includes his emotional ballad "I Left My Wrench at Your Place."',
    image: merch_10
  },
  {
    id: '04',
    name: 'Roller Blades',
    price: 89.99,
    description: 'Get to job sites 47% faster while looking absolutely ridiculous. Perfect for the handyman who values efficiency over dignity.',
    image: merch_6
  },
  {
    id: '05',
    name: 'T-Shirts',
    price: 29.99,
    description: 'Comes pre-stained with paint, caulk, and regret. Machine washable, but why would you? It adds character.',
    image: merch_7
  },
  {
    id: '06',
    name: 'Pickle Ball Paddles',
    price: 44.99,
    description: 'For when fixing houses doesn\'t provide enough mid-life crisis energy. Also doubles as a flyswatter in emergencies.',
    image: merch_8
  },
  {
    id: '07',
    name: 'Umbrella',
    price: 39.99,
    description: 'It can get wet when joel is not around so make sure you dont slip and buy an umbrella!',
    image: merch_9
  }
]);

// Animation functions
function animateProductsIn() {
  const productCards = document.querySelectorAll('.product-card');
  
  gsap.set(productCards, { 
    y: 50, 
    opacity: 0
  });
  
  gsap.to(productCards, {
    y: 0,
    opacity: 1,
    duration: 0.8,
    stagger: 0.1,
    ease: "power2.out",
    delay: 0.3
  });
}

function setupHoverEffects() {
  const productCards = document.querySelectorAll('.product-card');
  
  productCards.forEach(card => {
    const image = card.querySelector('.product-image');
    const overlay = card.querySelector('.product-overlay');
    const button = card.querySelector('.view-button');
    
    // Create hover animation timeline
    const hoverTl = gsap.timeline({ paused: true });
    
    hoverTl
      .to(image, { scale: 1.05, duration: 0.3, ease: "power2.out" })
      .to(overlay, { opacity: 1, duration: 0.3 }, 0)
      .to(button, { y: 0, opacity: 1, duration: 0.3, ease: "power2.out" }, 0.1);
    
    // Add event listeners
    card.addEventListener('mouseenter', () => hoverTl.play());
    card.addEventListener('mouseleave', () => hoverTl.reverse());
    
    // Setup initial states
    gsap.set(overlay, { opacity: 0 });
    gsap.set(button, { y: 10, opacity: 0 });
  });
}

onMounted(() => {
  animateProductsIn();
  setupHoverEffects();
  initUnderlineAnimation();
});
</script>

<style scoped>
.products-section {
  background-color: #fff;
  color: #243e2e;
  min-height: 100vh;
  position: relative;
  z-index: 1;
  padding-bottom: 30vh;
  padding-top: 15vh;
}

.products-container {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.section-title {
  font-size: 3.5rem;
  text-align: center;
  margin-bottom: 2rem;
  color: #243e2e;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.section-subtitle {
  font-size: 1.3rem;
  text-align: center;
  margin-bottom: 8rem;
  color: #243e2e;
  opacity: 0.8;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

/* Draw underline styles matching the homepage */
.text-draw {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

.text-draw__box {
  color: #fd3d13;
  width: 100%;
  height: 0.625em;
  position: relative;
  margin-top: -0.3em;
  margin-left: 5%;
}

.text-draw__box-svg {
  width: 100%;
  height: 100%;
  position: absolute;
  overflow: visible !important;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2.5rem;
  position: relative;
}

.product-card {
  background-color: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(36, 62, 46, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  cursor: pointer;
  border: 1px solid rgba(36, 62, 46, 0.1);
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(36, 62, 46, 0.15);
}

.product-image-container {
  position: relative;
  height: 300px;
  overflow: hidden;
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform-origin: center;
}

.product-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(36, 62, 46, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
}

.view-button {
  background-color: #fff;
  color: #243e2e;
  border: 2px solid #fd3d13;
  padding: 0.8rem 1.5rem;
  border-radius: 30px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.view-button:hover {
  background-color: #fd3d13;
  color: #fff;
  border-color: #fd3d13;
}

.product-info {
  padding: 1.5rem;
}

.product-name {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: #243e2e;
  font-weight: 600;
}

.product-price {
  font-size: 1.1rem;
  font-weight: 700;
  color: #fd3d13;
}

@media (max-width: 992px) {
  .products-section {
    padding: 4rem 5vw;
  }

  .section-title {
    font-size: 2.8rem;
  }

  .section-subtitle {
    font-size: 1.2rem;
    margin-bottom: 3rem;
  }
}

@media (max-width: 768px) {
  .products-section {
    padding: 3rem 5vw;
  }

  .products-grid {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
  }
  
  .section-title {
    font-size: 2.2rem;
    margin-bottom: 1rem;
  }

  .section-subtitle {
    font-size: 1.1rem;
    margin-bottom: 2.5rem;
  }
  
  .product-image-container {
    height: 250px;
  }
}

@media (max-width: 576px) {
  .products-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .section-title {
    font-size: 1.8rem;
  }

  .section-subtitle {
    font-size: 1rem;
  }
}
</style>
