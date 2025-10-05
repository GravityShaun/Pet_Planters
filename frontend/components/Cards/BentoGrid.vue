<template>
  <div class="bento_grid_container" ref="gridRef">
    <div
      v-for="(item, i) in items"
      :key="i"
      :ref="el => { if (el) itemRefs[i] = el }"
      :class="['bento_grid_item', getSpanClass(i)]"
      @mouseenter="handleMouseEnter"
      @mouseleave="handleMouseLeave"
    >
    <!-- <div class="bento_grid_item_content"> -->
      <div class="paperOverlayBento"></div>
      
      <!-- Unsplash Images Header -->
      <div :class="[i == 3 || i == 7 ? 'bento_item_header_double' : 'bento_item_header', getBackgroundClass(i)]">
        <img 
          :src="item.imageUrl" 
          :alt="item.title"
          class="unsplash_image"
        />
      </div>
      
      <!-- Content -->
      <div class="content_wrapper">
        <!-- Icon Placeholder -->
        <div class="bento_item_icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12.22 2h-4.44a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h8.88a2 2 0 0 0 2-2v-8.44L12.22 2z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
          </svg>
        </div>
        <!-- <div :class="['bento_item_title_wood', getBackgroundClass(i)]">
          {{ item.title }}
        </div> -->
        <div class="bento_item_title">
          <span class="text-draw" :data-draw-line="`bento-${i}`">
            {{ item.title }}
            <div class="text-draw__box" :data-draw-line-box="`bento-${i}`"></div>
          </span>
        </div>
        <div class="bento_item_description">
          {{ item.description }}
        </div>
      </div>
    </div>
  <!-- </div> -->
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';
import joel_1 from '@/assets/content/images/joel_ladder.webp';
import joel_2 from '@/assets/content/images/electric_joel.png';
import joel_3 from '@/assets/content/images/joel_hang.webp';
import joel_4 from '@/assets/content/images/joel_outside.png';
import joel_5 from '@/assets/content/images/joel_caulk.png';
import joel_6 from '@/assets/content/images/joel_shelf.png';
import joel_7 from '@/assets/content/images/joel_pipe.png';
import joel_8 from '@/assets/content/images/joel_assemble.png';
import joel_9 from '@/assets/content/images/joel_structure.png';

gsap.registerPlugin(ScrollTrigger);

// Reactive references
const gridRef = ref(null);
const itemRefs = ref([]);
const { initUnderlineAnimation } = useUnderlineAnimation();

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

// Grid items data
const items = ref([
  {
    title: "Upload Photos",
    description: "Share up to 5 photos of your dog from different angles for the best 3D model results.",
    imageUrl: joel_8
  },
  {
    title: "Custom 3D Design",
    description: "Our designers create a unique 3D model capturing your pet's personality and features.",
    imageUrl: joel_9
  },
  {
    title: "Precision Printing",
    description: "High-quality 3D printing brings your pet planter to life in durable, eco-friendly materials.",
    imageUrl: joel_3
  },
  {
    title: "Hand-Painted Finish",
    description: "Each planter is carefully hand-painted to match your pet's unique coloring and markings.",
    imageUrl: joel_2
  },
  {
    title: "Succulent Selection",
    description: "Choose from our curated collection of low-maintenance succulents for the perfect topper.",
    imageUrl: "https://images.unsplash.com/photo-1534398079543-7ae6d016b86a?w=400&h=300&fit=crop&crop=center"
  },
  {
    title: "Quality Assurance",
    description: "Every planter is inspected to ensure it meets our high standards before shipping.",
    imageUrl: joel_6
  },
  {
    title: "Eco-Friendly Materials",
    description: "We use sustainable, biodegradable materials that are safe for plants and the environment.",
    imageUrl: joel_5
  },
  {
    title: "Perfect Sizing",
    description: "Each planter is crafted to be 4-5 inches tall, perfect for desks, shelves, or windowsills.",
    imageUrl: joel_1
  },
  {
    title: "Care Instructions",
    description: "Receive detailed care guides for both your planter and succulent to ensure longevity.",
    imageUrl: joel_7
  },
  {
    title: "Gift Ready",
    description: "Each planter comes beautifully packaged, making it the perfect gift for pet lovers.",
    imageUrl: joel_4
  }
]);

// Utility functions
const getBackgroundClass = (index) => {
  return backgroundAssignments.value[index] || '';
};

const initializeBackgrounds = () => {
  backgroundAssignments.value = items.value.map(() => {
    const randomIndex = Math.floor(Math.random() * backgroundClasses.length);
    return backgroundClasses[randomIndex];
  });
};

const getSpanClass = (index) => {
  const spanPattern = [
    '', // 0 - Item 1: Top-left square (1x1)
    '', // 1 - Item 2: Top-middle square (1x1)
    'md_col_span_2', // 2 - Item 3: Top-right wide (2x1)
    'md_col_span_2 md_row_span_2', // 3 - Item 4: Large square bottom-left (2x2)
    '', // 4 - Item 5: Top-middle-right square (1x1)
    '', // 5 - Item 6: normal (1x1)
    '', // 6 - Item 7: Middle-right square (1x1)
    'md_row_span_2', // 7 - Item 8: long rectangle (1x2)
    '', // 8 - Item 9: Bottom-right square (1x1)
    'md_col_span_2', // 9 - Item 10: Bottom-middle wide (2x1)
  ];
  
  return spanPattern[index] || '';
};

// Animation variables
let scrollTriggerInstance;

// Event handlers
const handleMouseEnter = (e) => {
  const target = e.currentTarget;
  const content = target.querySelector('.content_wrapper');
  
  gsap.to(target, {
    duration: 0.3,
    scale: 1.02,
    boxShadow: "0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)",
    ease: "power2.out"
  });
  
  gsap.to(content, {
    duration: 0.3,
    x: 8,
    ease: "power2.out"
  });
};

const handleMouseLeave = (e) => {
  const target = e.currentTarget;
  const content = target.querySelector('.content_wrapper');
  
  gsap.to(target, {
    duration: 0.3,
    scale: 1,
    boxShadow: '0px 2px 3px -1px rgba(0,0,0,0.1), 0px 1px 0px 0px rgba(25,28,33,0.02), 0px 0px 0px 1px rgba(25,28,33,0.08)',
    ease: "power2.out"
  });
  
  gsap.to(content, {
    duration: 0.3,
    x: 0,
    ease: "power2.out"
  });
};

// Lifecycle hooks
onMounted(() => {
  setTimeout(() => {
    initializeBackgrounds();
    
    if (itemRefs.value.length > 0) {
      // Set initial animation state
      gsap.set(itemRefs.value, { 
        autoAlpha: 0, 
        y: 100,
        scale: 0.8,
        rotation: 5
      });

      // Initialize underline animations without auto-animation
      items.value.forEach((_, index) => {
        initUnderlineAnimation(`[data-draw-line="bento-${index}"]`, {
          autoAnimate: false
        });
      });

      // Create individual ScrollTriggers for each item
      itemRefs.value.forEach((item, index) => {
        if (item) {
          ScrollTrigger.create({
            trigger: item,
            start: "top bottom",
            end: "bottom top",
            toggleActions: "play none none none",
            onEnter: () => {

                  // Reset underline
                  const underlinePath = item.querySelector('[data-draw-line-box] svg path');
              if (underlinePath) {
                gsap.set(underlinePath, {
                  strokeDashoffset: 0,
                  opacity: 0
                });
              }
              // Animate item immediately
              gsap.to(item, {
                duration: 0.8,
                autoAlpha: 1,
                y: 0,
                scale: 1,
                rotation: 0,
                ease: "back.out(1.7)",
                onComplete: () => {
                  // Animate underline for this specific item with index-based delay
                  const underlinePath = item.querySelector('[data-draw-line-box] svg path');
                  if (underlinePath) {
                    gsap.set(underlinePath, {
                  opacity: 1,
                  delay: index > 6 
                              ? index * 0.3 - 2.25 
                              : index > 4 
                                ? index * 0.3 - 1.25 
                                : index * 0.3 - 0.25
                });
                    gsap.fromTo(underlinePath, 
                      {
                        strokeDashoffset: underlinePath.getTotalLength()
                      },
                      {
                        strokeDashoffset: 0,
                        duration: 1.2,
                        ease: "power2.inOut",
                        delay: index > 6 
                              ? index * 0.3 - 2.25 
                              : index > 4 
                                ? index * 0.3 - 1.25 
                                : index * 0.3 - 0.25
                      }
                    );
                  }
                }
              });
            },
          });
        }
      });
    }
  }, 300);
});

onBeforeUnmount(() => {
  if (scrollTriggerInstance) {
    scrollTriggerInstance.kill();
  }
  itemRefs.value.forEach(item => gsap.killTweensOf(item));
});
</script>

<style>
/* ===== GRID LAYOUT ===== */
.bento_grid_container {
  width: 85%;
  margin-left: auto;
  margin-right: auto;
  display: grid;
  grid-template-columns: repeat(1, minmax(0, 1fr));
  gap: 1.5rem;
  margin-top: 22vh;
  margin-bottom: 20vh;
}

@media (min-width: 768px) {
  .bento_grid_container {
    grid-auto-rows: minmax(25vh, auto);
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

.bento_grid_item_content{
  background-color: rgb(255, 255, 255);
  border-radius: 0.75rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 1rem;
  background-color: rgb(255, 255, 255);
  border: 0px solid rgba(41, 59, 46, 0.629);
  height: 100%;
  overflow: hidden;
}

/* ===== GRID ITEMS ===== */
.bento_grid_item {
  box-shadow: 0px 2px 3px -1px rgba(0,0,0,0.2), 0px 1px 0px 0px rgba(25,28,33,0.05), 0px 0px 0px 1px rgba(25,28,33,0.1);
  grid-row: span 1 / span 1;
  border-radius: 0.75rem;
  background-color: rgba(255, 255, 255, 0.873);
  border: 1px solid rgba(41, 59, 46, 0.459);
  min-height: 15vh;
  overflow: hidden;
  padding: 1rem;
  padding-top: 0;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/* ===== WOOD BORDERS ===== */
.bento_grid_item.wood_overlay_1 {
  position: relative;
  border: 10px solid transparent;
  background: 
    linear-gradient(rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.3)) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_1.jpg") border-box;
  background-size: auto, 100px;
}

.bento_grid_item.wood_overlay_2 {
  position: relative;
  border: 10px solid transparent;
  background: 
    linear-gradient(rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.3)) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_2.jpg") border-box;
  background-size: auto, 120px;
}

.bento_grid_item.wood_overlay_3 {
  position: relative;
  border: 10px solid transparent;
  background: 
    linear-gradient(rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.3)) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_3.jpg") border-box;
  background-size: auto, 120px;
}

.bento_grid_item.wood_overlay_4 {
  position: relative;
  border: 10px solid transparent;
  background: 
    linear-gradient(rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.3)) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_4.jpg") border-box;
  background-size: auto, 80px;
}

.bento_grid_item.wood_overlay_5 {
  position: relative;
  border: 10px solid transparent;
  background: 
    linear-gradient(rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.3)) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_5.jpg") border-box;
  background-size: auto, 110px;
}

.bento_grid_item.wood_overlay_6 {
  position: relative;
  border: 10px solid transparent;
  background: 
    linear-gradient(rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.3)) padding-box,
    url("~/assets/content/images/wood_texture/wood_overlay_6.jpg") border-box;
  background-size: auto, 80px;
}

.bento_grid_item > :not([hidden]) ~ :not([hidden]) {
  margin-top: 1rem;
}

/* ===== GRID SPANS ===== */
@media (min-width: 768px) {
  .bento_grid_item.md_col_span_2 {
    grid-column: span 2 / span 2;
  }
  
  .bento_grid_item.md_row_span_2 {
    grid-row: span 2 / span 2;
  }
  
  .bento_grid_item.md_col_span_2.md_row_span_2 {
    grid-column: span 2 / span 2;
    grid-row: span 2 / span 2;
  }
}

/* ===== ITEM HEADERS ===== */
.bento_item_header {
  display: flex;
  flex: 1 1 0%;
  width: 100%;
  height: 100%;
  overflow: hidden;
  max-height: 30vh;
  min-height: 12vh;
  border-radius: 0.75rem;
  box-shadow: inset 0 0 3px 0 rgba(0, 0, 0, 0.75);
  padding: 15px;
  position: relative;
  z-index: 2;
}

.bento_item_header_double {
  display: flex;
  flex: 1 1 0%;
  width: 100%;
  height: 100%;
  overflow: hidden;
  min-height: 12vh;
  border-radius: 0.75rem;
  box-shadow: inset 0 0 3px 0 rgba(0, 0, 0, 0.95);
  padding: 15px;
  position: relative;
  z-index: 2;
}

/* ===== WOOD OVERLAY BACKGROUNDS ===== */
.bento_item_header.wood_overlay_1,
.bento_item_header_double.wood_overlay_1 {
  background-image: linear-gradient(to bottom right, rgba(229, 231, 235, 0.8), rgba(243, 244, 246, 0.8)), url("~/assets/content/images/wood_texture/wood_overlay_1.jpg");
  background-size: cover, 100%;
  background-repeat: no-repeat, repeat;
  background-blend-mode: multiply;
}

.bento_item_header.wood_overlay_2,
.bento_item_header_double.wood_overlay_2 {
  background-image: linear-gradient(to bottom right, rgba(229, 231, 235, 0.8), rgba(243, 244, 246, 0.8)), url("~/assets/content/images/wood_texture/wood_overlay_2.jpg");
  background-size: cover, 180%;
  background-repeat: no-repeat, repeat;
  background-blend-mode: multiply;
}

.bento_item_header.wood_overlay_3,
.bento_item_header_double.wood_overlay_3 {
  background-image: linear-gradient(to bottom right, rgba(229, 231, 235, 0.8), rgba(243, 244, 246, 0.8)), url("~/assets/content/images/wood_texture/wood_overlay_3.jpg");
  background-size: cover, 180%;
  background-repeat: no-repeat, repeat;
  background-blend-mode: multiply;
}

.bento_item_header.wood_overlay_4,
.bento_item_header_double.wood_overlay_4 {
  background-image: linear-gradient(to bottom right, rgba(229, 231, 235, 0.8), rgba(243, 244, 246, 0.8)), url("~/assets/content/images/wood_texture/wood_overlay_4.jpg");
  background-size: cover, 80%;
  background-repeat: no-repeat, repeat;
  background-blend-mode: multiply;
}

.bento_item_header.wood_overlay_5,
.bento_item_header_double.wood_overlay_5 {
  background-image: linear-gradient(to bottom right, rgba(229, 231, 235, 0.8), rgba(243, 244, 246, 0.8)), url("~/assets/content/images/wood_texture/wood_overlay_5.jpg");
  background-size: cover, 150%;
  background-repeat: no-repeat, repeat;
  background-blend-mode: multiply;
}

.bento_item_header.wood_overlay_6,
.bento_item_header_double.wood_overlay_6 {
  background-image: linear-gradient(to bottom right, rgba(229, 231, 235, 0.8), rgba(243, 244, 246, 0.8)), url("~/assets/content/images/wood_texture/wood_overlay_6.jpg");
  background-size: cover, 80%;
  background-repeat: no-repeat, repeat;
  background-blend-mode: multiply;
}

/* ===== CONTENT ELEMENTS ===== */
.content_wrapper {
  flex-shrink: 0;
}

.bento_item_icon {
  height: 1rem;
  width: 1rem;
  color: #737373;
  margin-bottom: 0.5rem;
}

.bento_item_icon svg {
  height: 1rem;
  width: 1rem;
  color: #737373;
}

.bento_item_title {
  font-weight: 600;
  color: #293b2e;
  margin-bottom: 0.8rem;
  margin-top: 0.5rem;
  font-size: 2rem;
  line-height: 1.2;
}

.bento_item_title_wood {
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-weight: 900;
  color: #ffffff;
  margin-bottom: 0.8rem;
  margin-top: 0.5rem;
  font-size: 2.25rem;
  text-shadow: 0 1px 1px rgba(0, 0, 0, 0.65);
  line-height: 1.2;
}

.bento_item_description {
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-weight: 600;
  font-size: 0.85rem;
  line-height: 1.5;
  color: #293b2e;
}

/* ===== WOOD TEXTURE TITLES ===== */
.bento_item_title_wood.wood_overlay_1 {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_1.jpg");
  background-size: 100%;
  background-repeat: repeat;
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: none;
  filter: drop-shadow(2px 2px 1px rgba(0, 0, 0, 0.5));
}

.bento_item_title_wood.wood_overlay_2 {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_2.jpg");
  background-size: 100%;
  background-repeat: repeat;
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: none;
  filter: drop-shadow(2px 2px 1px rgba(0, 0, 0, 0.5));
}

.bento_item_title_wood.wood_overlay_3 {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_3.jpg");
  background-size: 100%;
  background-repeat: repeat;
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: none;
  filter: drop-shadow(2px 2px 1px rgba(0, 0, 0, 0.5));
}

.bento_item_title_wood.wood_overlay_4 {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_4.jpg");
  background-size: 100%;
  background-repeat: repeat;
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: none;
  filter: drop-shadow(2px 2px 1px rgba(0, 0, 0, 0.5));
}

.bento_item_title_wood.wood_overlay_5 {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_5.jpg");
  background-size: 100%;
  background-repeat: repeat;
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: none;
  filter: drop-shadow(2px 2px 1px rgba(0, 0, 0, 0.5));
}

.bento_item_title_wood.wood_overlay_6 {
  background-image: url("~/assets/content/images/wood_texture/wood_overlay_6.jpg");
  background-size: 200%;
  background-repeat: repeat;
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: none;
  filter: drop-shadow(2px 2px 1px rgba(0, 0, 0, 0.5));
}

/* ===== IMAGES ===== */
.unsplash_image {
  width: 100%;
  object-fit: cover;
  border-radius: 0.75rem;
  box-shadow: 0px 0px 5px 1px rgba(51, 0, 0, 0.4);
}

/* ===== UNDERLINE ANIMATION ===== */
.text-draw {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

.text-draw__box {
  color: #fd3d13;
  width: 100%;
  height: 0.4em;
  position: relative;
  margin-top: -0.095em;
}

.text-draw__box-svg {
  width: 0%;
  height: 100%;
  position: absolute;
  overflow: visible !important;
}

.paperOverlayBento {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    opacity:.6;
    background-size: 150%;
    background-repeat: repeat;
    background-image: url("~/assets/content/images/paper_overlay_7.jpg");
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 0;
    background-position: bottom right;
  }



.bento_grid_item:nth-child(2n) .paperOverlayBento {
    background-position: top left !important;
    transform: scaleX(-1) !important;
  }

  .bento_grid_item:nth-child(3n) .paperOverlayBento {
    background-position: center right !important;
    transform: scaleY(-1) !important;
    background-size: 80% !important;
  }

  .bento_grid_item:nth-child(4n) .paperOverlayBento {
    background-position: bottom center !important;
    transform: rotate(180deg) !important;
    background-size: 90% !important;
  }

  .bento_grid_item:nth-child(5n) .paperOverlayBento {
    background-position: top center !important;
    transform: scaleX(-1) scaleY(-1) !important;
  }

  .bento_grid_item:nth-child(6n) .paperOverlayBento {
    background-position: center left !important;
    transform: scaleY(-1) !important;
    background-size: 220% !important;
  }

  .bento_grid_item:nth-child(7n) .paperOverlayBento {
    background-position: top right !important;
    transform: scaleX(-1) !important;
  }

  .bento_grid_item:nth-child(8n) .paperOverlayBento {
    background-position: left bottom !important;
    background-size: 220% !important;
  }

  .bento_grid_item:nth-child(9n) .paperOverlayBento {
    background-position: right center !important;
    background-size: 150% !important;
  }

  .bento_grid_item:nth-child(10n) .paperOverlayBento {
    background-position: right bottom !important;
    background-size: 80% !important;
    transform: scaleX(-1) !important;
  }


</style>