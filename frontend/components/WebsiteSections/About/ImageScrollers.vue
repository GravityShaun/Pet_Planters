<template>
    <div class="card-container" ref="containerRef">
      <p class="background-text">
        I'm just an honest handy guy,<br>let's share a drink
      </p>
      <div
        v-for="(item, index) in items"
        :key="index"
        :ref="el => { if (el) cardRefs[index] = el }"
        class="card"
        :style="item.style"
      >
        <div class="card-content">
          <img :src="item.image" :alt="item.title" class="card-image" />
          <h3 class="card-title">{{ item.title }}</h3>
          <div class="card-glare"></div>
        </div>
      </div>
    </div>
  </template>
  

  

  <script setup>
  import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue';
  import { gsap } from 'gsap';
  import { Draggable } from 'gsap/Draggable';
  import { InertiaPlugin } from 'gsap/InertiaPlugin';
  
  // Import images
  import joel1 from '~/assets/content/images/about/joel_1.jpg';
  import joel2 from '~/assets/content/images/about/joel_2.jpg';
  import joel3 from '~/assets/content/images/about/joel_3.jpg';
  import joel4 from '~/assets/content/images/about/joel_4.jpg';
  import joel5 from '~/assets/content/images/about/joel_5.jpg';
  import joel6 from '~/assets/content/images/about/joel_6.jpg';
  import joel7 from '~/assets/content/images/about/joel_7.jpg';
  import joel8 from '~/assets/content/images/about/joel_8.jpg';
  import joel9 from '~/assets/content/images/about/joel_9.jpg';
  
  // Register the GSAP Draggable and InertiaPlugin
  gsap.registerPlugin(Draggable, InertiaPlugin);
  
  const containerRef = ref(null);
  const cardRefs = ref([]);
  let draggables = []; // To store Draggable instances for cleanup
  
  const cardData = [
    { title: "Don't tempt me with a good time", image: joel1 },
    { title: "Christmas !", image: joel2 },
    { title: "Just a regular pool boy", image: joel3 },
    { title: "Orange you glad I am your handyman", image: joel4 },
    { title: "Post tune-up drinks", image: joel5 },
    { title: "Party Mountain !", image: joel6 },
    { title: "I am a man of the people", image: joel7 },
    { title: "idk, I'm just a regular handy guy", image: joel8 },
    { title: "My last name is not bond, its handyman", image: joel9 },
  ];

  const items = ref([]); // Initialize as an empty ref, will be populated on mount
  
  onMounted(async () => {
    // --- Position generation logic moved to onMounted to ensure window is defined ---
    
    // 1. Define container dimensions and constraints
    const containerHeight = window.innerHeight * 1.5;
    const cardHeight = 320;
    const maxTop = containerHeight - cardHeight - 20;
    const minTop = containerHeight * 0.15;
    const verticalRange = maxTop - minTop;
    const totalCards = cardData.length;
    
    // 2. Create evenly spaced vertical "slots" to ensure full height is covered
    const verticalSlots = Array.from({ length: totalCards }, (_, i) => {
      const segmentHeight = verticalRange / (totalCards - 1); 
      return minTop + (i * segmentHeight);
    });
  
    // 3. Shuffle the slots to ensure random vertical distribution
    for (let i = verticalSlots.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [verticalSlots[i], verticalSlots[j]] = [verticalSlots[j], verticalSlots[i]];
    }
  
    // 4. Create and shuffle horizontal slots to ensure full width spread
    const containerWidth = window.innerWidth;
    const cardWidth = 320;
    const minLeftPercent = 1;
    const maxLeftPixels = containerWidth - cardWidth - 20;
    const maxLeftPercent = (maxLeftPixels / containerWidth) * 100;
    
    const horizontalRange = maxLeftPercent - minLeftPercent;
    const horizontalSlots = Array.from({ length: totalCards }, (_, i) => {
      const segmentWidth = horizontalRange / (totalCards - 1);
      return minLeftPercent + (i * segmentWidth);
    });
  
    // Shuffle horizontal slots for randomness
    for (let i = horizontalSlots.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [horizontalSlots[i], horizontalSlots[j]] = [horizontalSlots[j], horizontalSlots[i]];
    }
    
    // 5. Populate the items ref with calculated positions
    items.value = cardData.map((card, index) => {
      const top = verticalSlots[index];
      const left = horizontalSlots[index];
      const rotation = (Math.random() - 0.5) * 35;
      
      const style = {
        top: `${top}px`,
        left: `${left}%`,
        transform: `rotate(${rotation}deg) scale(0.85)`,
      };
      
      return { ...card, style };
    });

    await nextTick(); // Wait for the DOM to update with cards
  
    cardRefs.value.forEach((cardEl) => {
      if (!cardEl) return;
  
      const contentEl = cardEl.querySelector('.card-content');
      const glareEl = cardEl.querySelector('.card-glare');
  
      // Initialize Draggable with basic configuration
      const d = Draggable.create(cardEl, {
        type: "x,y",
        bounds: containerRef.value,
        inertia: true, // Keep standard inertia for the x/y throw
        onDragStart: function() {
          gsap.to(this.target, { zIndex: 100 });
          document.body.style.cursor = 'grabbing';
          this.target._startTime = Date.now();
          this.target._startX = this.x;
          this.target._startY = this.y;
        },
        onDragEnd: function() {
          // This fires *after* the inertia animation is completely finished.
          // We only use it to reset the z-index.
          gsap.to(this.target, { zIndex: 1 });
        },
        onRelease: function() {
          document.body.style.cursor = 'grab';
          
          // Get velocity using InertiaPlugin.getVelocity()
          const velocityX = InertiaPlugin.getVelocity(this.target, "x") || 0;
          const velocityY = InertiaPlugin.getVelocity(this.target, "y") || 0;
          const velocity = Math.sqrt(velocityX * velocityX + velocityY * velocityY);
          const velocityThreshold = 1000;
          
          console.log('Release - VelocityX:', velocityX, 'VelocityY:', velocityY, 'Total Velocity:', velocity);
          
          // Only rotate if velocity exceeds threshold
          if (velocity > velocityThreshold) {
            const currentRotation = gsap.getProperty(this.target, "rotation");
            
            // Calculate rotation amount based on velocity (5-20 degrees)
            const minRotation = 5;
            const maxRotation = 10;
            const velocityFactor = Math.min(velocity / 300, 1);
            const rotationAmount = minRotation + (maxRotation - minRotation) * velocityFactor;
            
            // Random direction (positive or negative)
            const direction = Math.random() > 0.5 ? 1 : -1;
            
            console.log('Rotating by:', rotationAmount * direction, 'degrees');
            
            gsap.to(this.target, {
              rotation: currentRotation + (rotationAmount * direction),
              duration: 0.8,
              ease: "power2.out"
            });
          } else {
            console.log('Velocity too low, no rotation');
          }
        }
      });
      draggables.push(d[0]);
  
      // 3D tilt and opacity effects (unchanged)
      const rotX = gsap.quickTo(contentEl, "rotationX", { duration: 0.4, ease: "power2.out" });
      const rotY = gsap.quickTo(contentEl, "rotationY", { duration: 0.4, ease: "power2.out" });
  
      cardEl.addEventListener('mouseenter', () => {
        gsap.to(cardEl, { scale: 0.9, duration: 0.3 });
      });
  
      cardEl.addEventListener('mousemove', (e) => {
        const { left, top, width, height } = cardEl.getBoundingClientRect();
        const x = e.clientX - left;
        const y = e.clientY - top;
        const centerX = width / 2;
  
        const mappedRotateX = gsap.utils.mapRange(0, height, 15, -15, y);
        const mappedRotateY = gsap.utils.mapRange(0, width, -15, 15, x);
        const mappedGlareOpacity = gsap.utils.mapRange(0, centerX, 0, 0.2, Math.abs(x - centerX));
  
        rotX(mappedRotateX);
        rotY(mappedRotateY);
        gsap.set(glareEl, { opacity: mappedGlareOpacity });
      });
  
      cardEl.addEventListener('mouseleave', () => {
        gsap.to(cardEl, { scale: 0.85, duration: 0.5, ease: "power2.out" });
        gsap.to(contentEl, { rotationX: 0, rotationY: 0, duration: 0.7, ease: "elastic.out(1, 0.5)" });
        gsap.to(glareEl, { opacity: 0, duration: 0.5 });
      });
    });
  });
  
  // Clean up GSAP instances to prevent memory leaks
  onBeforeUnmount(() => {
    draggables.forEach(d => d.kill());
  });
  </script>
 
  
  <style>
  /* General body and container styles */
  .card-container {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-height: 150vh;
    overflow: clip;
    perspective: 3000px;
    color: #293b2e;
    margin-top:-10vh;
  }
  
  .background-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -75%);
    max-width: 50vw; /* 384px */
    text-align: center;
    font-size: 2.25rem; /* 36px */
    font-weight: 900;
    color: #293b2e;
    z-index: 0;
    line-height: 1.5;
  }
  
  /* Individual card wrapper styles */
  .card {
    position: absolute;
    width: 320px;
    cursor: grab;
    user-select: none;
    will-change: transform;
  }
  
  .card:active {
    cursor: grabbing;
  }
  
  /* Card content styles for tilting */
  .card-content {
    background-color: #fff;
    padding: 1.5rem; /* 24px */
    border-radius: 0.5rem; /* 8px */
    box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.4);
    transform-style: preserve-3d;
  }
  
  /* Card image styles */
  .card-image {
    pointer-events: none;
    position: relative;
    z-index: 10;
    height: 320px;
    width: 100%;
    object-fit: cover;
    border-radius: 0.375rem; /* 6px */
  }
  
  /* Card title styles */
  .card-title {
    margin-top: 1rem; /* 16px */
    text-align: center;
    font-size: 1.3rem; /* 24px */
    font-weight: 400;
    color: #333333;
  }
  
  /* Glare effect element */
  .card-glare {
    pointer-events: none;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 0.5rem; /* 8px */
    background-color: white;
    opacity: 0;
    mix-blend-mode: overlay; /* Creates a nice highlight effect */
    z-index: 20;
  }
  </style>