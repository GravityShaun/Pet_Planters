<template>
  <section class="sideways-accordion" @mousemove="handleMouseMove">
    <div class="text-content">
      <h1 class="fluid">Featured Planters</h1>
      <p class="text-content-description">
        See what other pet parents have created with PetPlanters!
      </p>
    </div>
    
    <ul ref="listRef" class="accordion-list">
      <li 
        v-for="(item, index) in items" 
        :key="index"
        :data-active="activeIndex === index"
        @click="setActiveIndex(index)"
        @pointermove="setActiveIndex(index)"
        @focus="setActiveIndex(index)"
        class="accordion-item"
      >
        <article class="accordion-content">
          <h3>{{ item.title }}</h3>
          <p class="accordion-content-description">{{ item.description }}</p>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            v-html="item.icon"
            class="item-icon"
          ></svg>
          <a href="#" class="watch-link">
            <span>Create Yours</span>
          </a>
          <div class="image-wrapper">
            <img :src="item.image" :alt="item.title" class="item-image" />
          </div>
        </article>
      </li>
    </ul>
  </section>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { gsap } from 'gsap'
import merch_1 from '~/assets/content/images/merch/merch_1.png'
import merch_10 from '~/assets/content/images/merch/merch_10.png'
import merch_4 from '~/assets/content/images/merch/merch_4.png'
import merch_6 from '~/assets/content/images/merch/merch_6.png'
import merch_7 from '~/assets/content/images/merch/merch_7.png'
import merch_8 from '~/assets/content/images/merch/merch_8.png'
import merch_9 from '~/assets/content/images/merch/merch_9.png'

const listRef = ref(null)
const activeIndex = ref(0)

// Mouse tracking variables
let mouseX = 0
let mouseY = 0

const items = ref([
  {
    title: 'Golden Retriever',
    description: 'Meet Buddy! This happy golden retriever planter brings sunshine to any space with its warm smile and a succulent crown.',
    icon: '<path d="M15 2v2a3 3 0 0 1-3 3H9l-3 3v4a3 3 0 0 0 3 3h6a3 3 0 0 0 3-3v-4l-3-3h-3a3 3 0 0 1-3-3V2Z" /><path d="M9 12h6" />',
    image: merch_1
  },
  {
    title: 'French Bulldog',
    description: 'This adorable Frenchie planter captures those iconic bat ears and wrinkly face. Perfect for succulent lovers!',
    icon: '<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />',
    image: merch_4
  },
  {
    title: 'Corgi Cutie',
    description: 'Short legs, big personality! This corgi planter is ideal for small spaces and brings endless charm to your desk.',
    icon: '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z" />',
    image: merch_10
  },
  {
    title: 'German Shepherd',
    description: 'Noble and loyal, this German Shepherd planter stands proud with its signature alert expression and pointed ears.',
    icon: '<path d="M18 6 7 17l-5-5" /><path d="m22 10-7.5 7.5L13 16" />',
    image: merch_6
  },
  {
    title: 'Pug Life',
    description: 'Those adorable wrinkles and big eyes make this pug planter absolutely irresistible. A conversation starter for sure!',
    icon: '<rect width="18" height="18" x="3" y="3" rx="2" /><path d="M7 3v18" /><path d="M3 7.5h4" /><path d="M3 12h18" /><path d="M3 16.5h4" /><path d="M17 3v18" /><path d="M17 7.5h4" /><path d="M17 16.5h4" />',
    image: merch_7
  },
  {
    title: 'Husky Hero',
    description: 'Piercing blue eyes and majestic markings - this husky planter is perfect for those who love adventure and the outdoors.',
    icon: '<path d="M3 6h18" /><path d="M7 12h10" /><path d="M10 18h4" />',
    image: merch_8
  },
  {
    title: 'Beagle Buddy',
    description: 'Floppy ears and an inquisitive expression make this beagle planter a delightful addition to any plant collection.',
    icon: '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z" />',
    image: merch_9
  }
])

const handleMouseMove = (event) => {
  const rect = event.currentTarget.getBoundingClientRect()
  mouseX = (event.clientX - rect.left - rect.width / 2) / rect.width
  mouseY = (event.clientY - rect.top - rect.height / 2) / rect.height
}

const setActiveIndex = (index) => {
  if (activeIndex.value === index) return
  
  activeIndex.value = index
  updateGridTemplate()
  animateActiveItem()
}

const updateGridTemplate = () => {
  if (!listRef.value) return
  
  const cols = new Array(items.value.length)
    .fill()
    .map((_, i) => activeIndex.value === i ? '10fr' : '1fr')
    .join(' ')
  
  gsap.to(listRef.value, {
    duration: 0.4,
    ease: 'power2.inOut',
    onUpdate: function() {
      listRef.value.style.setProperty('grid-template-columns', cols)
    }
  })
}

const animateActiveItem = () => {
  const items = listRef.value?.children
  if (!items) return

  // Animate all items
  gsap.to(items, {
    duration: 0.3,
    ease: 'power2.inOut',
    scale: 0.95,
    opacity: 1
  })

  // Animate active item
  if (items[activeIndex.value]) {
    gsap.to(items[activeIndex.value], {
      duration: 0.4,
      ease: 'power2.out',
      scale: 1,
      opacity: 1,
      delay: 0.05
    })
  }
}

const resync = () => {
  if (!listRef.value) return
  
  const items = listRef.value.children
  const w = Math.max(...[...items].map(i => i.offsetWidth))
  listRef.value.style.setProperty('--article-width', w)
}

const initAnimations = () => {
  // Initial setup
  gsap.set('.accordion-item', { 
    scale: 0.8, 
    opacity: 0,
    y: 50
  })
  
  gsap.set('.accordion-content', { 
    opacity: 0,
    y: 20
  })
  
  // Stagger animation for items
  gsap.to('.accordion-item', {
    duration: 0.6,
    scale: 1,
    opacity: 1,
    y: 0,
    stagger: 0.05,
    ease: 'power2.out',
    delay: 0.3
  })
  
  // Animate content
  gsap.to('.accordion-content', {
    duration: 0.4,
    opacity: 1,
    y: 0,
    stagger: 0.05,
    ease: 'power2.out',
    delay: 0.5
  })
  
  // Set first item as active
  setTimeout(() => {
    setActiveIndex(0)
  }, 800)
}

onMounted(async () => {
  await nextTick()
  resync()
  initAnimations()
  
  window.addEventListener('resize', resync)
})
</script>

<style scoped>
.sideways-accordion {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 2rem;
  padding: 4rem 2rem;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  z-index: 1;
  padding-bottom: 30vh;
}

.sideways-accordion::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  
  pointer-events: none;
  z-index: 0;
}

.text-content {
  text-align: center;
  max-width: 55%;
  z-index: 1;
  position: relative;
  margin-bottom:3vh
}

.fluid {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 700;
  color: #243e2e;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.text-content p {
  font-size: 1.2rem;
  color: #243e2e;
  line-height: 1.6;
  opacity: 0.8;
  margin: 0;
  font-family: 'SF Pro Text', 'Helvetica Neue', Arial, sans-serif;
}

.accordion-list {
  display: grid;
  grid-template-columns: 10fr 1fr 1fr 1fr 1fr 1fr 1fr;
  gap: 1rem;
  list-style: none;
  padding: 0;
  margin: 0;
  height: 500px;
  width: 100%;
  max-width: 1200px;
  transition: grid-template-columns 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  z-index: 1;
  position: relative;
}

.accordion-item {
  background: #f3e6d47a;
  border-radius: 12px;
  border: 3px solid #243e2e;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.accordion-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
}

.accordion-item[data-active="true"] {
  border-color: #243e2e;
  box-shadow: 0 20px 40px rgba(36, 62, 46, 0.2);
}

.accordion-content {
  position: absolute;
  inset: 0;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  color: #243e2e;
  font-family: 'SF Pro Text', 'Helvetica Neue', Arial, sans-serif;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.accordion-content h3 {
  position: absolute;
  top: 1.5rem;
  left: 1.5rem;
  font-size: 1.1rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
  opacity: 0.8;
  transition: opacity 0.3s ease;
  transform-origin: 0 50%;
  rotate: 90deg;
  white-space: nowrap;
  color: #1a1a1a;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
}

.accordion-content p {
  font-size: 0.9rem;
  line-height: 1.4;
  margin: 0 0 1rem 0;
  opacity: 0;
  transition: opacity 0.3s ease;
  max-width: 200px;
}

.accordion-item[data-active="true"] .accordion-content p {
  opacity: 1;
}

.item-icon {
  position: absolute;
  bottom: 1.5rem;
  right: 1.5rem;
  width: 20px;
  height: 20px;
  opacity: 0.6;
  transition: opacity 0.3s ease;
}

.text-content-description{
    font-size: 100%;
    font-weight: 400;
    color: #243e2e;
    line-height: 1.4;
    margin: 20px;
}

.accordion-item[data-active="true"] .accordion-content h3 {
  opacity: 1;
  color: white;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.8);
}

.accordion-item[data-active="true"] .item-icon {
  opacity: 1;
}

.accordion-item:not([data-active="true"]) .accordion-content h3 {
  opacity: 0.8;
}

.accordion-item:not([data-active="true"]) .item-icon {
  opacity: 0.6;
}

.watch-link {
  position: absolute;
  bottom: 1.5rem;
  left: 1.5rem;
  color: #fd3d13;
  text-decoration: none;
  font-weight: 500;
  font-size: 100%;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  opacity: 0;
  transition: opacity 0.3s ease;
  background-color: rgba(255, 255, 255, 0.5);
  color: #fd3d13;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.accordion-item[data-active="true"] .watch-link {
  opacity: 1;
}

.watch-link:hover {
  text-decoration: underline;
  text-underline-offset: 4px;
}

.accordion-content-description{
    font-size: 100%;
    font-weight: 400;
    color: #1a1a1a;
    line-height: 1.4;
    margin: 0;
    text-align: left;
    position: absolute;
    bottom: 120px;
    left: 1.5rem;
    text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    background-color: rgba(255, 255, 255, 0.5);
    padding: 10px;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 0, 0, 0.523);
}

.image-wrapper {
  position: absolute;
  inset: 0;
  overflow: hidden;
  border-radius: 10px;
  z-index: -1;
}

.item-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: grayscale(1) brightness(0.8);
  transition: all 0.3s ease;
  transform: scale(1.1);
  opacity: 0;
}

.accordion-item[data-active="true"] .item-image {
  filter: grayscale(0) brightness(1);
  transform: scale(1);
  opacity: 1;
}

/* Responsive Design */
@media (max-width: 768px) {
  .sideways-accordion {
    padding: 2rem 1rem;
  }
  
  .accordion-list {
    grid-template-columns: 1fr;
    height: auto;
    gap: 1rem;
  }
  
  .accordion-item {
    height: 200px;
  }
  
  .accordion-content {
    padding: 1.5rem;
  }
  
  .accordion-content h3 {
    top: 1rem;
    left: 1rem;
    font-size: 1rem;
    rotate: 90deg;
    transform-origin: 0 50%;
  }
  
  .accordion-content p {
    font-size: 0.8rem;
    max-width: none;
  }
  
  .item-icon {
    top: 1rem;
    right: 1rem;
    width: 18px;
    height: 18px;
  }
  
  .watch-link {
    bottom: 1rem;
    left: 1rem;
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .fluid {
    font-size: 2rem;
  }
  
  .text-content p {
    font-size: 1rem;
  }
  
  .accordion-item {
    height: 180px;
  }
}
</style>
