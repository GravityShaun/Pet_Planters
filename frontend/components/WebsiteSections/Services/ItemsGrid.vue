<template>
  <div class="portfolio-wrapper">
    <div class="container">
      <BigText :text="heroText" />
      
      <!-- Sticky Category Filter -->
  
      <div class="category-filter" ref="categoryFilterRef">
        <button 
          v-for="category in categories"
          :key="category"
          :class="['category-btn', { active: activeCategory === category }, activeCategory === category ? `category-btn-${categoryWoodTextures[category]}` : '']"
          @click="setActiveCategory(category)"
        >
          {{ category }}
        </button>
      </div>
    

      <div class="portfolio-grid" ref="portfolioGridRef">
        <div
          v-for="(item, index) in portfolioItems"
          :key="item.id"
          :class="['grid-item', item.class]"
          :ref="el => cardRefs[index] = el"
          :style="{ display: item.visible ? 'block' : 'none' }"
          :data-category="item.category"
          :data-id="item.id"
        >
          <NuxtLink 
            :to="`/service_items/${item.id}`" 
            class="service-link"
            @mouseenter="handleHover(index, true)"
            @mouseleave="handleHover(index, false)"
          >
            <div 
              :class="['service-container', getWoodClass(index)]"
            >
              <div class="service-box">
                <div class="paperOverlayGrid"></div>
                <div class="service-content">
                  <div class="service-number">{{ item.id }}</div>
                  <div class="service-icon">{{ item.icon }}</div>
                  <div class="service-description">
                    <h3>{{ item.title }}</h3>
                    <p>{{ item.description }}</p>
                    <div class="service-details">
                      <span class="price-range">{{ item.priceRange }}</span>
                      <span class="duration">{{ item.duration }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div 
              class="service-title" 
              :ref="el => titleRefs[index] = el"
            >
              {{ item.title }}
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick, watch, onUnmounted } from 'vue';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { Flip } from 'gsap/Flip';
import BigText from '~/components/FontFx/BigText.vue';

// Register GSAP plugins
gsap.registerPlugin(ScrollTrigger, Flip);

const categoryFilterRef = ref(null);
const portfolioGridRef = ref(null);
const heroText = "SERVICES";
const activeCategory = ref('ALL');
const isFlipping = ref(false);
const midFlipping = ref(false);

const categories = ['ALL', 'REPAIRS', 'ELECTRICAL', 'PLUMBING', 'ASSEMBLY', 'ORGANIZATION', 'PAINTING', 'OUTDOOR', 'MAINTENANCE'];

// Map each category to a specific wood texture
const categoryWoodTextures = {
  'ALL': 'wood_overlay_1',
  'REPAIRS': 'wood_overlay_2',
  'ELECTRICAL': 'wood_overlay_3',
  'PLUMBING': 'wood_overlay_4',
  'ASSEMBLY': 'wood_overlay_5',
  'ORGANIZATION': 'wood_overlay_6',
  'PAINTING': 'wood_overlay_1',
  'OUTDOOR': 'wood_overlay_2',
  'MAINTENANCE': 'wood_overlay_3'
};

const portfolioItems = ref([
  // First half - Original layout
  { 
    id: '01', 
    class: 'grid-item-01', 
    bgColor: '#a15e3c',
    icon: '🔧', 
    title: 'Drywall Repair & Patching', 
    description: 'Professional drywall installation, hole repair, texture matching, and patching for water damage or wear. Includes priming and paint touch-ups.',
    priceRange: '$80-250',
    duration: '2-4 hours',
    category: 'REPAIRS',
    visible: true
  },
  { 
    id: '03', 
    class: 'grid-item-03', 
    bgColor: '#04251b',
    icon: '🪚', 
    title: 'Trim & Molding Installation', 
    description: 'Crown molding, baseboards, door casings, and window trim installation. Custom cuts, precision fitting, and professional finishing.',
    priceRange: '$150-400',
    duration: '3-6 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '05', 
    class: 'grid-item-05', 
    bgColor: '#c88562',
    icon: '💡', 
    title: 'Light Fixture Installation', 
    description: 'Ceiling fans, chandeliers, recessed lighting, and switch replacements. Includes electrical safety checks and proper mounting.',
    priceRange: '$100-300',
    duration: '1-3 hours',
    category: 'ELECTRICAL',
    visible: true
  },
  { 
    id: '06', 
    class: 'grid-item-06', 
    bgColor: '#e7c6b3',
    icon: '🚿', 
    title: 'Faucet & Fixture Repair', 
    description: 'Leaky faucet repairs, toilet fixes, showerhead installation, and basic plumbing maintenance. Quick diagnosis and reliable solutions.',
    priceRange: '$75-200',
    duration: '1-2 hours',
    category: 'PLUMBING',
    visible: true
  },
  { 
    id: '09', 
    class: 'grid-item-09', 
    bgColor: '#04251b',
    icon: '🎨', 
    title: 'Interior Painting', 
    description: 'Room painting, accent walls, cabinet refinishing, and touch-up work. Quality prep work, premium paints, and clean finish.',
    priceRange: '$150-400/room',
    duration: '1-2 days',
    category: 'PAINTING',
    visible: true
  },
  { 
    id: '11', 
    class: 'grid-item-11', 
    bgColor: '#a15e3c',
    icon: '🚪', 
    title: 'Door & Window Services', 
    description: 'Door hanging, window caulking, weatherstripping, lock installation, and hardware replacement. Improved security and energy efficiency.',
    priceRange: '$100-350',
    duration: '2-4 hours',
    category: 'REPAIRS',
    visible: true
  },
  { 
    id: '13', 
    class: 'grid-item-13', 
    bgColor: '#c88562',
    icon: '📦', 
    title: 'Furniture Assembly', 
    description: 'IKEA, Wayfair, and custom furniture assembly. Bed frames, desks, shelving units, and complex multi-piece installations.',
    priceRange: '$60-150',
    duration: '1-3 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '17', 
    class: 'grid-item-17', 
    bgColor: '#e7c6b3',
    icon: '🏠', 
    title: 'Deck & Fence Repairs', 
    description: 'Deck board replacement, railing repairs, fence post stabilization, and staining. Extends outdoor structure lifespan.',
    priceRange: '$120-450',
    duration: '2-6 hours',
    category: 'OUTDOOR',
    visible: true
  },
  { 
    id: '20', 
    class: 'grid-item-20', 
    bgColor: '#04251b',
    icon: '⚡', 
    title: 'Home Maintenance Package', 
    description: 'Seasonal maintenance including gutter cleaning, caulk renewal, HVAC filter changes, and preventive repairs. Keep your home in top condition.',
    priceRange: '$200-500',
    duration: '3-5 hours',
    category: 'MAINTENANCE',
    visible: true
  },
  
  // Second half - Mirrored layout
  { 
    id: '21', 
    class: 'grid-item-21', 
    bgColor: '#c88562',
    icon: '🔨', 
    title: 'Kitchen Cabinet Hardware', 
    description: 'Cabinet handle and knob installation, drawer slide replacement, soft-close hinges, and cabinet door adjustments.',
    priceRange: '$90-280',
    duration: '2-4 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '23', 
    class: 'grid-item-23', 
    bgColor: '#e7c6b3',
    icon: '🪟', 
    title: 'Window Blind Installation', 
    description: 'Custom blind mounting, cordless options, motorized systems, and window treatment hardware. Perfect fit guaranteed.',
    priceRange: '$80-200/window',
    duration: '1-2 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '25', 
    class: 'grid-item-25', 
    bgColor: '#04251b',
    icon: '🧰', 
    title: 'Garage Organization', 
    description: 'Wall-mounted storage systems, pegboard installation, overhead racks, and tool organization solutions.',
    priceRange: '$180-450',
    duration: '3-6 hours',
    category: 'ORGANIZATION',
    visible: true
  },
  { 
    id: '26', 
    class: 'grid-item-26', 
    bgColor: '#a15e3c',
    icon: '🌡️', 
    title: 'Thermostat Installation', 
    description: 'Smart thermostat setup, programmable controls, WiFi connectivity, and HVAC system compatibility checks.',
    priceRange: '$120-250',
    duration: '1-2 hours',
    category: 'ELECTRICAL',
    visible: true
  },
  { 
    id: '29', 
    class: 'grid-item-29', 
    bgColor: '#e7c6b3',
    icon: '🔒', 
    title: 'Home Security Upgrades', 
    description: 'Deadbolt installation, security camera mounting, motion sensor lights, and smart doorbell setup.',
    priceRange: '$100-350',
    duration: '2-4 hours',
    category: 'ELECTRICAL',
    visible: true
  },
  { 
    id: '31', 
    class: 'grid-item-31', 
    bgColor: '#c88562',
    icon: '🛠️', 
    title: 'Closet Organization', 
    description: 'Custom shelving systems, closet rod installation, shoe racks, and storage optimization solutions.',
    priceRange: '$150-400',
    duration: '3-5 hours',
    category: 'ORGANIZATION',
    visible: true
  },
  { 
    id: '33', 
    class: 'grid-item-33', 
    bgColor: '#04251b',
    icon: '🏡', 
    title: 'Bathroom Accessories', 
    description: 'Towel bars, toilet paper holders, shower caddies, and medicine cabinet installation. Complete bathroom setup.',
    priceRange: '$75-180',
    duration: '1-3 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '37', 
    class: 'grid-item-37', 
    bgColor: '#a15e3c',
    icon: '🌿', 
    title: 'Outdoor Project Assembly', 
    description: 'Patio furniture, grills, planters, and outdoor storage shed assembly. Weather-resistant installation.',
    priceRange: '$100-300',
    duration: '2-5 hours',
    category: 'OUTDOOR',
    visible: true
  },
  { 
    id: '40', 
    class: 'grid-item-40', 
    bgColor: '#e7c6b3',
    icon: '📺', 
    title: 'TV & Electronics Mounting', 
    description: 'Wall-mounted TVs, soundbar installation, cable management, and entertainment center setup. Clean, professional finish.',
    priceRange: '$120-280',
    duration: '2-3 hours',
    category: 'ELECTRICAL',
    visible: true
  },
]);

const titleRefs = ref([]);
const cardRefs = ref([]);

// Background classes for wood overlay
const backgroundClasses = [
  'wood_overlay_1',
  'wood_overlay_2', 
  'wood_overlay_3',
  'wood_overlay_4',
  'wood_overlay_5',
  'wood_overlay_6'
];

const backgroundAssignments = ref([]);

// Utility functions
const getWoodClass = (index) => {
  return backgroundAssignments.value[index] || '';
};

const initializeBackgrounds = () => {
  backgroundAssignments.value = portfolioItems.value.map(() => {
    const randomIndex = Math.floor(Math.random() * backgroundClasses.length);
    return backgroundClasses[randomIndex];
  });
};

// Note: Filtering is handled directly in setActiveCategory function

function setActiveCategory(category) {
  if (!portfolioGridRef.value || isFlipping.value) return;

  isFlipping.value = true;
  
  // Kill existing ScrollTriggers on cards to prevent conflicts
  ScrollTrigger.getAll().forEach(st => {
    if (cardRefs.value.some(card => card === st.trigger)) {
      st.kill();
    }
  });

  const grid = portfolioGridRef.value;
  const allItems = cardRefs.value.filter(Boolean);
  
  // When filtering, we want to make sure cards are in their final state
  if (category !== 'ALL') {
    allItems.forEach(card => {
        gsap.set(card, { y: 0, opacity: 1, scale: 1, rotationX: 0 });
        const innerElements = card.querySelectorAll('.service-number, .service-icon, .service-description h3, .service-description p, .service-details, .service-title');
        gsap.set(innerElements, { opacity: 1, y: 0, scale: 1 });
    });
  }

  // Get the state of all items before any changes
  const state = Flip.getState(allItems);

  // Update the active category
  activeCategory.value = category;

  // Toggle a class on the grid to switch between layouts
  if (category === 'ALL') {
    grid.classList.remove('is-filtered');
  } else {
    grid.classList.add('is-filtered');
  }

  // Update visibility property on the data.
  // We'll let Flip handle the visual appearing/disappearing.
  portfolioItems.value.forEach(item => {
    item.visible = (category === 'ALL' || item.category === category);
  });

  // Let Flip handle the animation from the old state to the new one
  Flip.from(state, {
    duration: 0.9,
    ease: "expo.inOut",
    stagger: 0.04,
    delay: 0,
    simple: true,
    scale: true,
    onStart: () => {
      setTimeout(() => {
        window.$smoothScroll.scrollToElement('.portfolio-grid', -250);
      }, 10);
    
        initializeCardAnimations();
        // Re-apply type scaling soon after layout starts animating
        setTimeout(() => applyResponsiveTypeScale(), 50);
    },
    onComplete: () => {
      isFlipping.value = false;
      // if (category === 'ALL') {
      //   // Re-initialize animations only when going back to the full grid
      //   initializeCardAnimations();
      // }
      // Refresh ScrollTrigger to account for layout changes
      ScrollTrigger.refresh();
      // Ensure type scaling matches new sizes
      applyResponsiveTypeScale();
    },
    onEnter: elements => gsap.from(elements, {
      opacity: 0,
      scale: 0.5,
      duration: 0.6,
      ease: "expo.out",
      stagger: 0.04,
      delay: 0.15,
    }),
    onLeave: elements => gsap.to(elements, {
      opacity: 0,
      scale: 0.5,
      duration: 0.3,
      stagger: 0.03,
      ease: "expo.in",
    })
  });
}

function handleHover(index, isEntering) {
  const titleElement = titleRefs.value[index];
  if (!titleElement) return;

  if (isEntering) {
    gsap.to(titleElement, {
      color: "#a15e3c",
      x: 12,
      "--before-opacity": 1,
      "--before-x": "0px",
      duration: 0.3,
      ease: "cubic-bezier(0.23, 1, 0.32, 1)"
    });
  } else {
    gsap.to(titleElement, {
      color: "#1a1a1a",
      x: 0,
      "--before-opacity": 0,
      "--before-x": "-8px",
      duration: 0.3,
      ease: "cubic-bezier(0.23, 1, 0.32, 1)"
    });
  }
}

function initializeCardAnimations() {



  // Set initial state for all cards - faster reveal
  gsap.set(cardRefs.value, {
    y: 80, // Reduced from 150
    opacity: 0,
    scale: 0.98, // Less dramatic scaling
    rotationX: 4, // Reduced rotation
    delay: 0,
  });

  // Set initial state for individual elements
  cardRefs.value.forEach(card => {
    if (!card) return;
    
    gsap.set(card.querySelector('.service-number'), { opacity: 0, y: 15 });
    gsap.set(card.querySelector('.service-icon'), { opacity: 0, y: 20, scale: 0.9 });
    gsap.set(card.querySelector('.service-description h3'), { opacity: 0, y: 15 });
    gsap.set(card.querySelector('.service-description p'), { opacity: 0, y: 18 });
    gsap.set(card.querySelector('.service-details'), { opacity: 0, y: 20 });
    gsap.set(card.querySelector('.service-title'), { opacity: 0, y: 10 });
  });

  // Create faster staggered animation for each card
  cardRefs.value.forEach((card, index) => {
    if (!card) return;

    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: card,
        start: "top 98%", // Trigger even sooner
        end: "bottom 5%",
        toggleActions: "play none none reverse",
      }
    });

    // Faster main card reveal with reduced stagger delay
    tl.set(card, { opacity: 1, y: 0, scale: 1, rotationX: 0 })
    .to(card, {
      y: 0,
      opacity: 1,
      scale: 1,
      rotationX: 0,
      duration: 0.8, // Reduced from 1.2
      delay: index * 0.05, // Reduced from 0.15
      ease: "power2.out", // Faster ease
    })
    // Faster service number reveal
    .to(card.querySelector('.service-number'), {
      opacity: 1,
      y: 0,
      duration: 0.4, // Reduced from 0.6
      ease: "power2.out"
    }, `-=0.7`) // Start earlier
    // Faster icon reveal
    .to(card.querySelector('.service-icon'), {
      opacity: 1,
      y: 0,
      scale: 1,
      duration: 0.5, // Reduced from 0.8
      ease: "back.out(1.2)" // Less dramatic bounce
    }, `-=0.6`)
    // Faster title reveal
    .to(card.querySelector('.service-description h3'), {
      opacity: 1,
      y: 0,
      duration: 0.4, // Reduced from 0.6
      ease: "power2.out"
    }, `-=0.4`)
    // Faster description reveal
    .to(card.querySelector('.service-description p'), {
      opacity: 1,
      y: 0,
      duration: 0.4, // Reduced from 0.7
      ease: "power2.out"
    }, `-=0.3`)
    // Faster service details reveal
    .to(card.querySelector('.service-details'), {
      opacity: 1,
      y: 0,
      duration: 0.4, // Reduced from 0.6
      ease: "power2.out"
    }, `-=0.25`)
    // Faster service title reveal
    .to(card.querySelector('.service-title'), {
      opacity: 1,
      y: 0,
      duration: 0.3, // Reduced from 0.5
      ease: "power2.out"
    }, `-=0.15`)
    // Faster final enhancement
    .to(card.querySelector('.service-box'), {
      boxShadow: "0 8px 30px rgba(0, 0, 0, 0.12)",
      duration: 0.3, // Reduced from 0.4
      ease: "power2.out"
    }, `-=0.3`);
  });
}

// Watch for category changes and re-initialize animations
watch(activeCategory, () => {
  nextTick(() => {
    // This watcher is no longer needed with the new logic.
    // The logic is now self-contained in setActiveCategory.
    // ScrollTrigger.refresh() is called on animation complete.
  });
});

// ===== GSAP-driven responsive type scaling based on card width =====
const BASE_FONT_ATTR = 'data-base-font-size';

function getTypeScaleForWidth(width) {
  if (width >= 420) return 1.5;
  if (width >= 340) return 1.35;
  if (width >= 280) return 1.15;
  if (width >= 220) return 1.0;
  return 0.85;
}

function setScaledFontSize(element, scale) {
  if (!element) return;
  let base = parseFloat(element.getAttribute(BASE_FONT_ATTR));
  if (!base || Number.isNaN(base)) {
    base = parseFloat(getComputedStyle(element).fontSize);
    if (!Number.isNaN(base)) {
      element.setAttribute(BASE_FONT_ATTR, String(base));
    }
  }
  if (!Number.isNaN(base)) {
    gsap.set(element, { fontSize: base * scale });
  }
}

function scaleTextForCard(card) {
  if (!card) return;
  const width = card.clientWidth || card.getBoundingClientRect().width || 0;
  const scale = getTypeScaleForWidth(width);
  const selectors = [
    '.service-description h3',
    '.service-description p',
    '.price-range',
    '.duration',
    '.service-title',
    '.service-number'
  ];
  selectors.forEach(sel => setScaledFontSize(card.querySelector(sel), scale));
}

function applyResponsiveTypeScale() {
  // Run on next frame to ensure layout has settled
  requestAnimationFrame(() => {
    cardRefs.value.forEach(scaleTextForCard);
  });
}

onMounted(async () => {
  await nextTick();

  // Initialize random wood backgrounds
  initializeBackgrounds();

  activeCategory.value = 'ALL';

  // Pin the category filter
  if (categoryFilterRef.value) {
    const shouldPin = window.matchMedia('(min-width: 1024px)').matches;
    if (shouldPin) {
      ScrollTrigger.create({
        trigger: categoryFilterRef.value,
        start: 'top 10%',
        endTrigger: '.portfolio-wrapper',
        end: 'bottom top+=10%', // Adjust end point slightly
        pin: true,
        pinSpacing: false, // Element is absolutely positioned
      });
    }
  }
  
  // Initialize title refs
  titleRefs.value.forEach(title => {
    if (title) {
      title.style.setProperty('--before-opacity', '0');
      title.style.setProperty('--before-x', '-8px');
    }
  });

  // Initialize card animations with shorter delay
  setTimeout(() => {
    initializeCardAnimations();
    // Apply initial responsive type scale
    applyResponsiveTypeScale();
  }, 100); // Reduced from 200ms

  // Update on resize/orientation changes
  window.addEventListener('resize', applyResponsiveTypeScale);
  window.addEventListener('orientationchange', applyResponsiveTypeScale);
});

onUnmounted(() => {
  window.removeEventListener('resize', applyResponsiveTypeScale);
  window.removeEventListener('orientationchange', applyResponsiveTypeScale);
});
</script>


  
  <style>
  .portfolio-wrapper {
    width: 95%;
    min-height: 100vh;
    text-transform: uppercase;
    font-size: 12px;
    color: #1a1a1a;
    margin: 0 auto;
    padding-bottom:20vh
  }
  
  .portfolio-wrapper * {
    box-sizing: border-box;
  }
  
  .container {
    width: 100%;
    padding: 2rem;
    position: relative;
  }
  
  .category-filter {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    padding: 1rem;
    margin-bottom: 4rem;
    position: absolute;
    top: 27vh;
    z-index: 10;
    z-index: 100;
  }

  .category-btn {
    background-color: transparent;
    border: 1px solid #d4c9c2;
    color: #4b4b4b;
    padding: 0.6rem 1.2rem;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    border-radius: 999px;
    cursor: pointer;
    transition: all 0.3s ease;
    outline: none;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
  }
  
  .category-btn:hover {
    border-color: #a15e3c;
    color: #a15e3c;
    transform: translateY(-2px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  }

  .category-btn.active {
    background-color: #000000;
    color: white;
    border-color: #a15e3c;
    box-shadow: 0 4px 12px rgba(161, 94, 60, 0.3);
    transform: translateY(-2px);
    transition: all 1.2s ease;
  }

  .category-btn.active:hover {
    background-color: #b36e4f;
    border-color: #b36e4f;
  }

  /* Wood texture classes for active category buttons */
  .category-btn-wood_overlay_1.active {
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_1.jpg");
    background-size: cover;
    background-position: center;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    border-color: #04251b;
    background-color: #000000;
    mix-blend-mode: multiply;
  }

  .category-btn-wood_overlay_2.active {
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_2.jpg");
    background-size: cover;
    background-position: center;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    border-color: #04251b;
    background-color: #000000;
    mix-blend-mode: multiply;
  }

  .category-btn-wood_overlay_3.active {
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_3.jpg");
    background-size: cover;
    background-position: center;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    border-color: #04251b;
    background-color: #000000;
    mix-blend-mode: multiply;
  }

  .category-btn-wood_overlay_4.active {
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_4.jpg");
    background-size: cover;
    background-position: center;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    border-color: #04251b;
    background-color: #000000;
    mix-blend-mode: multiply;
  }

  .category-btn-wood_overlay_5.active {
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_5.jpg");
    background-size: cover;
    background-position: center;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    border-color: #04251b;
    background-color: #000000;
    mix-blend-mode: multiply;
  }

  .category-btn-wood_overlay_6.active {
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_6.jpg");
    background-size: cover;
    background-position: center;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    border-color: #04251b;
    background-color: #000000;
    mix-blend-mode: multiply;
  }

  /* Override hover styles for wood texture buttons */
  .category-btn-wood_overlay_1.active:hover,
  .category-btn-wood_overlay_2.active:hover,
  .category-btn-wood_overlay_3.active:hover,
  .category-btn-wood_overlay_4.active:hover,
  .category-btn-wood_overlay_5.active:hover,
  .category-btn-wood_overlay_6.active:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.2);
    border-color: #04251b;
  }

  .portfolio-grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 0.5rem;
    margin-top: 15vh;
  }
  
  /* New styles for filtered state */
  .portfolio-grid.is-filtered {
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
  }


  .portfolio-grid.is-filtered .grid-item {
    grid-column: auto;
    margin-bottom: 3rem;
  }
  
  .grid-item {
    position: relative;
    margin-bottom: 20vh;
    opacity: 1;
    transform: none;
    will-change: transform, opacity;
    display: flex;
    flex-direction: column;
    min-height: calc(35vh + 50px); /* Increased height for taller service boxes */
    container-type: inline-size;
  }

  .service-link {
    text-decoration: none;

  }


  
  /* First half - Original layout */
  .grid-item-01 { grid-column: 1 / 3; }
  .grid-item-03 { grid-column: 5 / 7; }
  .grid-item-05 { grid-column: 11 / 13; }
  .grid-item-06 { grid-column: 1 / 3; }
  .grid-item-09 { grid-column: 7 / 12; }
  .grid-item-11 { grid-column: 1 / 3; }
  .grid-item-13 { grid-column: 5 / 7; }
  .grid-item-17 { grid-column: 1 / 3; }
  .grid-item-20 { grid-column: 9 / 12; }
  
  /* Second half - Mirrored layout (flipped vertically) */
  .grid-item-21 { grid-column: 11 / 13; }  /* Mirror of 01 */
  .grid-item-23 { grid-column: 7 / 9; }    /* Mirror of 03 */
  .grid-item-25 { grid-column: 1 / 3; }    /* Mirror of 05 */
  .grid-item-26 { grid-column: 11 / 13; }  /* Mirror of 06 */
  .grid-item-29 { grid-column: 1 / 6; }    /* Mirror of 09 */
  .grid-item-31 { grid-column: 11 / 13; }  /* Mirror of 11 */
  .grid-item-33 { grid-column: 7 / 9; }    /* Mirror of 13 */
  .grid-item-37 { grid-column: 11 / 13; }  /* Mirror of 17 */
  .grid-item-40 { grid-column: 1 / 4; }    /* Mirror of 20 */

  /* Slightly wider items on desktop when ALL category is active */
  .portfolio-grid:not(.is-filtered) .grid-item-01 { grid-column: 1 / 4; }
  .portfolio-grid:not(.is-filtered) .grid-item-03 { grid-column: 5 / 8; }
  .portfolio-grid:not(.is-filtered) .grid-item-05 { grid-column: 10 / 13; }
  .portfolio-grid:not(.is-filtered) .grid-item-06 { grid-column: 1 / 4; }
  .portfolio-grid:not(.is-filtered) .grid-item-09 { grid-column: 7 / 13; }
  .portfolio-grid:not(.is-filtered) .grid-item-11 { grid-column: 1 / 4; }
  .portfolio-grid:not(.is-filtered) .grid-item-13 { grid-column: 5 / 8; }
  .portfolio-grid:not(.is-filtered) .grid-item-17 { grid-column: 1 / 4; }
  .portfolio-grid:not(.is-filtered) .grid-item-20 { grid-column: 9 / 13; }

  .portfolio-grid:not(.is-filtered) .grid-item-21 { grid-column: 10 / 13; }
  .portfolio-grid:not(.is-filtered) .grid-item-23 { grid-column: 7 / 10; }
  .portfolio-grid:not(.is-filtered) .grid-item-25 { grid-column: 1 / 4; }
  .portfolio-grid:not(.is-filtered) .grid-item-26 { grid-column: 10 / 13; }
  .portfolio-grid:not(.is-filtered) .grid-item-29 { grid-column: 1 / 7; }
  .portfolio-grid:not(.is-filtered) .grid-item-31 { grid-column: 10 / 13; }
  .portfolio-grid:not(.is-filtered) .grid-item-33 { grid-column: 7 / 10; }
  .portfolio-grid:not(.is-filtered) .grid-item-37 { grid-column: 10 / 13; }
  .portfolio-grid:not(.is-filtered) .grid-item-40 { grid-column: 1 / 5; }

  .portfolio-grid:not(.is-filtered){ gap: 2.25rem; }
  
  .service-box {
    aspect-ratio: 4 / 6;
    position: relative;
    overflow: visible;
    cursor: pointer;
    border-radius: 4px;
    background-color: white;
    color: #293b2e;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    backdrop-filter: blur(10px);
    will-change: transform;
    margin: 12px;
    min-height: 350px;
  }

  @media (max-width: 1050px) {
    .service-box {
      aspect-ratio: auto;
      min-height: 320px;
    }
  }

  .service-content {
    display: flex;
    flex-direction: column;
    padding: 20px;
    height: 100%;
    position: relative;
    z-index: 2;
  }

  /* In-panel paper overlay so texture shows over the white panel but under text */
  .service-content::after {
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
    border-radius: 4px;
  }

  .service-content > * {
    position: relative;
    z-index: 2;
  }
  
  .service-box:hover {
    transform: translateY(0px) scale(1.05);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
  }

  @media (hover: none) and (pointer: coarse) {
    .service-box:hover {
      transform: none;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }
  }

  /* Scale hover less as the grid item gets wider */
  @container (min-width: 260px) {
    .service-box:hover {
      transform: translateY(0px) scale(1.04);
    }
  }

  @container (min-width: 360px) {
    .service-box:hover {
      transform: translateY(0px) scale(1.03);
    }
  }

  @container (min-width: 480px) {
    .service-box:hover {
      transform: translateY(0px) scale(1.02);
    }
  }

  @container (min-width: 640px) {
    .service-box:hover {
      transform: translateY(0px) scale(1.015);
    }
  }
  
  /* Increase type sizes for wider grid items (container queries) */
  @container (min-width: 360px) {
    .service-number { font-size: 11px; }
    .service-icon { font-size: 3rem; }
    .service-description h3 { font-size: 16px; }
    .service-description p { font-size: 11px; }
    .price-range { font-size: 13px; }
    .duration { font-size: 9px; }
    .service-title { font-size: 12px; height: 30px; line-height: 30px; }
  }

  @container (min-width: 480px) {
    .service-number { font-size: 12px; }
    .service-icon { font-size: 3.2rem; }
    .service-description h3 { font-size: 18px; }
    .service-description p { font-size: 12px; }
    .price-range { font-size: 14px; }
    .duration { font-size: 10px; }
    .service-title { font-size: 13px; height: 32px; line-height: 32px; }
  }

  @container (min-width: 640px) {
    .service-number { font-size: 13px; }
    .service-icon { font-size: 3.4rem; }
    .service-description h3 { font-size: 20px; }
    .service-description p { font-size: 13px; }
    .price-range { font-size: 15px; }
    .duration { font-size: 11px; }
    .service-title { font-size: 14px; height: 34px; line-height: 34px; }
  }
  
  .service-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
    border-radius: 12px;
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  
  .service-box:hover::before {
    opacity: 1;
  }
  
  .service-number {
    font-size: 10px;
    color: #293b2e;
    opacity: 0.7;
    margin-bottom: 8px;
    align-self: flex-start;
    font-weight: 500;
    letter-spacing: 1px;
    will-change: transform, opacity;
  }
  
  .service-icon {
    font-size: 2.8rem;
    margin: 12px 0 16px 0;
    display: block;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    will-change: transform, opacity;
  }
  
  .service-description {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  .service-description h3 {
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    line-height: 1.1;
    color: #293b2e;
    will-change: transform, opacity;
    word-break: break-word;
    overflow-wrap: anywhere;
  }
  
  .service-description p {
    font-size: 14px;
    line-height: 1.4;
    margin: 0 0 10px 0;
    color: #293b2e;
    opacity: 0.8;
    text-transform: none;
    font-family: system-ui, -apple-system, sans-serif;
    font-weight: 400;
    will-change: transform, opacity;
    word-break: break-word;
    overflow-wrap: anywhere;
  }
  
  .service-box .service-details {
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-top: auto;
    border-top: 1px solid rgba(41, 59, 46, 0.2);
    padding-top: 8px;
    will-change: transform, opacity;
  }
  
  .price-range {
    font-size: 12px;
    font-weight: 600;
    color: #293b2e;
    letter-spacing: 0.5px;
  }
  
  .duration {
    font-size: 8px;
    color: #293b2e;
    opacity: 0.7;
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }
  
  .service-title {
    margin-top: 12px;
    font-size: 11px;
    color: #1a1a1a;
    transform: translateX(0px);
    will-change: transform, color, opacity;
    position: relative;
    display: inline-block;
    font-weight: 500;
    letter-spacing: 0.5px;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);
    flex-shrink: 0;
    height: 28px;
    line-height: 28px;
    word-break: break-word;
    overflow-wrap: anywhere;
  }
  
  .service-title::before {
    content: "→";
    position: absolute;
    left: -16px;
    top: 0;
    opacity: var(--before-opacity, 0);
    transform: translateX(var(--before-x, -8px));
    color: #a15e3c;
    font-weight: 600;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);
  }
  
  html {
    scroll-behavior: smooth;
  }

  /* ===== WOOD BORDERS WITH COLORED OUTER BORDER ===== */
  .service-container.wood_overlay_1 {
    position: relative;
    border: 5px solid #04251b;
    background: #04251b;
    border-radius: 5px;
  }

  .service-container.wood_overlay_1::before {
    content: '';
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_1.jpg");
    background-size: 100%;
    background-repeat: repeat;
    border-radius: 8px;
    z-index: 0;
  }

  .service-container.wood_overlay_2 {
    position: relative;
    border: 5px solid #04251b;
    background: #04251b;
    border-radius: 5px;
  }

  .service-container.wood_overlay_2::before {
    content: '';
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_2.jpg");
    background-size: 100%;
    background-repeat: repeat;
    border-radius: 8px;
    z-index: 0;
  }

  .service-container.wood_overlay_3 {
    position: relative;
    border: 5px solid #04251b;
    background: #04251b;
    border-radius: 5px;
  }

  .service-container.wood_overlay_3::before {
    content: '';
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_3.jpg");
    background-size: 100%;
    background-repeat: repeat;
    border-radius: 8px;
    z-index: 0;
  }

  .service-container.wood_overlay_4 {
    position: relative;
    border: 5px solid #04251b;
    background: #04251b;
    border-radius: 5px;
  }

  .service-container.wood_overlay_4::before {
    content: '';
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_4.jpg");
    background-size: 100%;
    background-repeat: repeat;
    border-radius: 8px;
    z-index: 0;
  }

  .service-container.wood_overlay_5 {
    position: relative;
    border: 5px solid #04251b;
    background: #04251b;
    border-radius: 5px;
  }

  .service-container.wood_overlay_5::before {
    content: '';
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_5.jpg");
    background-size: 100%;
    background-repeat: repeat;
    border-radius: 8px;
    z-index: 0;
  }

  .service-container.wood_overlay_6 {
    position: relative;
    border: 5px solid #04251b;
    background: #04251b;
    border-radius: 5px;
  }

  .service-container.wood_overlay_6::before {
    content: '';
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    background-image: url("~/assets/content/images/wood_texture/wood_overlay_6.jpg");
    background-size: 100%;
    background-repeat: repeat;
    border-radius: 8px;
    z-index: 0;
  }

  /* ===== PAPER OVERLAY ===== */
  .service-container {
    position: relative;
    flex: 1;
    display: flex;
    flex-direction: column;
  }

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

  .service-container:nth-child(2n) .paperOverlayGrid {
    background-position: top left !important;
    transform: scaleX(-1) !important;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5) !important;
  }

  .service-container:nth-child(3n) .paperOverlayGrid {
    background-position: center right !important;
    transform: scaleY(-1) !important;
    background-size: 80% !important;
    box-shadow: 0 2px 10px 0 rgba(0, 0, 0, 0.5) !important;
  }

  .service-container:nth-child(4n) .paperOverlayGrid {
    background-position: bottom center !important;
    transform: rotate(180deg) !important;
    background-size: 90% !important;
    box-shadow: 0 2px 10px 0 rgba(0, 0, 0, 0.5) !important;
  }

  .service-container:nth-child(5n) .paperOverlayGrid {
    background-position: top center !important;
    transform: scaleX(-1) scaleY(-1) !important;
    box-shadow: 0 2px 10px 0 rgba(0, 0, 0, 0.5);
  }

  .service-container:nth-child(6n) .paperOverlayGrid {
    background-position: center left !important;
    transform: scaleY(-1) !important;
    background-size: 220% !important;
    box-shadow: 0 2px 10px 0 rgba(0, 0, 0, 0.5);
  }

  .service-container:nth-child(7n) .paperOverlayGrid {
    background-position: top right !important;
    transform: scaleX(-1) !important;
    box-shadow: 0 2px 10px 0 rgba(0, 0, 0, 0.5) !important;
  }

  .service-container:nth-child(8n) .paperOverlayGrid {
    background-position: left bottom !important;
    background-size: 220% !important;
    box-shadow: 0 2px 10px 0 rgba(0, 0, 0, 0.5) !important;
  }

  .service-container:nth-child(9n) .paperOverlayGrid {
    background-position: right center !important;
    background-size: 150% !important;
    box-shadow: 0 2px 10px 0 rgba(0, 0, 0, 0.5) !important;
  }

  .service-container:nth-child(10n) .paperOverlayGrid {
    background-position: right bottom !important;
    background-size: 80% !important;
    transform: scaleX(-1) !important;
    box-shadow: 0 2px 10px 0 rgba(0, 0, 0, 0.5) !important;
  }
  
  @media (max-width: 768px) {
    .container { 
      padding: 1rem; 
    }
    
    .portfolio-grid { 
      grid-template-columns: 1fr;
      gap: 1rem;
    }
    
    .portfolio-grid.is-filtered {
      grid-template-columns: 1fr;
      gap: 1rem;
    }

    /* Force all items to span full width on mobile */
    .portfolio-grid .grid-item { grid-column: 1 / -1; }
    
    /* First half mobile */
    .grid-item-01 { grid-column: 1 / 3; }
    .grid-item-03 { grid-column: 3 / 5; }
    .grid-item-05 { grid-column: 5 / 7; }
    .grid-item-06 { grid-column: 1 / 3; }
    .grid-item-09 { grid-column: 3 / 7; }
    .grid-item-11 { grid-column: 1 / 3; }
    .grid-item-13 { grid-column: 3 / 5; }
    .grid-item-17 { grid-column: 5 / 7; }
    .grid-item-20 { grid-column: 1 / 4; }
    
    /* Second half mobile - mirrored */
    .grid-item-21 { grid-column: 5 / 7; }   /* Mirror of 01 */
    .grid-item-23 { grid-column: 3 / 5; }   /* Mirror of 03 */
    .grid-item-25 { grid-column: 1 / 3; }   /* Mirror of 05 */
    .grid-item-26 { grid-column: 5 / 7; }   /* Mirror of 06 */
    .grid-item-29 { grid-column: 1 / 5; }   /* Mirror of 09 */
    .grid-item-31 { grid-column: 5 / 7; }   /* Mirror of 11 */
    .grid-item-33 { grid-column: 3 / 5; }   /* Mirror of 13 */
    .grid-item-37 { grid-column: 1 / 3; }   /* Mirror of 17 */
    .grid-item-40 { grid-column: 3 / 7; }   /* Mirror of 20 */
  
    .service-box {
      padding: 16px;
      border-radius: 10px;
    }
  
    .service-box:hover {
      transform: translateY(-4px) scale(1.005);
    }
  
    .service-icon {
      font-size: 2.2rem;
      margin: 10px 0 12px 0;
    }
  
    .service-description h3 {
      font-size: 12px;
      margin-bottom: 6px;
    }
  
    .service-description p {
      font-size: 9px;
      margin-bottom: 8px;
      line-height: 1.3;
    }
  
    .service-box .service-details {
      padding-top: 6px;
      gap: 3px;
    }
  
    .price-range {
      font-size: 11px;
    }
  
    .duration {
      font-size: 7px;
    }
  
    .service-title {
      font-size: 10px;
      margin-top: 10px;
      line-height: 1.2;
      height: auto;
    }

    /* Prevent overflow and clamp lines on small screens */
    .service-description h3,
    .service-description p,
    .service-title {
      hyphens: auto;
    }
    .service-description h3 {
      display: -webkit-box;
      line-clamp: 2;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .service-description p {
      display: -webkit-box;
      line-clamp: 3;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .service-title {
      display: -webkit-box;
      line-clamp: 1;
      -webkit-line-clamp: 1;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
  }

  @media (max-width: 1024px) {
    .portfolio-wrapper {
      padding-bottom: 10vh;
    }
    .category-filter {
      position: sticky;
      top: 0;
      left: 0;
      right: 0;
      margin: 0 0 1rem 0;
      padding: 0.75rem 1rem;
      background: #ffffff;
      z-index: 100;
      justify-content: flex-start;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      gap: 0.5rem;
    }
    .category-filter::-webkit-scrollbar { display: none; }
    .category-btn { flex: 0 0 auto; }
    .portfolio-grid { margin-top: 2rem; }
    .grid-item { margin-bottom: 8vh; min-height: auto; }
    .service-box { min-height: 280px; margin: 8px; }
  }

  @media (min-width: 769px) and (max-width: 1200px) {
    .portfolio-grid.is-filtered { grid-template-columns: repeat(3, 1fr); }
  }
  
  @media (max-width: 480px) {
    .portfolio-grid.is-filtered {
      grid-template-columns: 1fr;
      gap: 1rem;
    }

    .service-box {
      padding: 14px;
    }
  
    .service-icon {
      font-size: 2rem;
    }
  
    .service-description h3 {
      font-size: 11px;
    }
  
    .service-description p {
      font-size: 8px;
    }
  
    .price-range {
      font-size: 10px;
    }

    /* Reinforce clamping on extra-small screens */
    .service-title { line-clamp: 1; -webkit-line-clamp: 1; }
    .service-description h3 { line-clamp: 2; -webkit-line-clamp: 2; }
    .service-description p { line-clamp: 3; -webkit-line-clamp: 3; }
  }
  
  @media (prefers-reduced-motion: reduce) {
    .grid-item {
      opacity: 1;
      transform: none;
    }
    
    .service-box {
      transition: none;
    }
    
    .service-icon {
      will-change: auto;
    }
    
    .service-number,
    .service-description h3,
    .service-description p,
    .service-details,
    .service-title {
      opacity: 1;
      transform: none;
    }
  }
  </style>