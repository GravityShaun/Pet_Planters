<template>
  <div class="heroSection">
    <div class="heroContent">
      <div class="titleContainer" data-draw-line>
        <h1 class="mainTitle" ref="titleElement">
          People Love Joel
        </h1>
        <div data-draw-line-box class="underline-box"></div>
      </div>
      <p class="heroSubtitle" ref="subtitleElement">
        Professional handyman services you can trust. From quick fixes to major renovations,
        we're here to bring your vision to life with quality craftsmanship.
      </p>
      <div class="heroStats" ref="statsElement">
        <div class="stat">
          <span class="statNumber" ref="statNumber1" data-target="500">0<span class="statAccent">+</span></span>
          <span class="statLabel">Projects Completed</span>
        </div>
        <div class="stat">
          <span class="statNumber" ref="statNumber2" data-target="100">0<span class="statAccent">%</span></span>
          <span class="statLabel">Satisfaction Rate</span>
        </div>
        <div class="stat">
          <span class="statNumber" ref="statNumber3" data-target="2500">0<span class="statAccent">+</span></span>
          <span class="statLabel">Drinks Shared</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';

const { initUnderlineAnimation } = useUnderlineAnimation();

// Refs for animations
const titleElement = ref(null);
const subtitleElement = ref(null);
const statsElement = ref(null);
const statNumber1 = ref(null);
const statNumber2 = ref(null);
const statNumber3 = ref(null);

// Counter animation function
const animateCounter = (element, target, suffix = '') => {
  const obj = { value: 0 };
  
  gsap.to(obj, {
    value: target,
    duration: 2,
    ease: 'power2.out',
    onUpdate: () => {
      const currentValue = Math.floor(obj.value);
      element.innerHTML = `${currentValue.toLocaleString()}<span class="statAccent">${suffix}</span>`;
      
      // Force red color on accent using GSAP
      const accentElement = element.querySelector('.statAccent');
      if (accentElement) {
        gsap.set(accentElement, { color: '#fd3d13', fontSize: '3vw' });
      }
    }
  });
};

// Expose refs to parent if needed
defineExpose({
  titleElement,
  subtitleElement,
  statsElement
});

onMounted(async () => {
  await nextTick();
  
  // Initialize underline animations
  const titleContainers = document.querySelectorAll('[data-draw-line]');
  titleContainers.forEach((container, index) => {
    // Create unique ID for each container to use as selector
    const uniqueId = `hero-draw-line-${index}`;
    container.setAttribute('id', uniqueId);
    
    initUnderlineAnimation(`#${uniqueId}`, {
      autoAnimate: false,
      duration: 1.2,
      ease: 'power2.inOut',
      delay: 0.5
    });
  });
  
  // Set initial states
  if (titleElement.value) {
    gsap.set(titleElement.value, { opacity: 0, y: -50 });
  }
  if (subtitleElement.value) {
    gsap.set(subtitleElement.value, { opacity: 0, y: -30 });
  }
  if (statsElement.value) {
    gsap.set(statsElement.value.children, { opacity: 0, y: 30 });
  }
  
  // Hero section animations
  if (titleElement.value && subtitleElement.value && statsElement.value) {
    const heroTl = gsap.timeline({ delay: 0.2 });
    
    heroTl
      .to(titleElement.value, {
        y: 0,
        opacity: 1,
        duration: 1.2,
        ease: 'power3.out'
      })
      .to(subtitleElement.value, {
        y: 0,
        opacity: 1,
        duration: 1,
        ease: 'power3.out'
      }, '-=0.8')
      .to(statsElement.value.children, {
        y: 0,
        opacity: 1,
        duration: 0.8,
        stagger: 0.1,
        ease: 'power2.out'
      }, '-=0.5');
  }
  
  // Setup counter animations with ScrollTrigger
  if (statNumber1.value && statNumber2.value && statNumber3.value) {
    ScrollTrigger.create({
      trigger: statsElement.value,
      start: 'top 80%',
      once: true,
      onEnter: () => {
        animateCounter(statNumber1.value, 500, '+');
        animateCounter(statNumber2.value, 100, '%');
        animateCounter(statNumber3.value, 2500, '+');
      }
    });
  }
  
  // Trigger underline animations after hero
  setTimeout(() => {
    titleContainers.forEach(container => {
      const underlineBox = container.querySelector('[data-draw-line-box]');
      const path = underlineBox?.querySelector('path');
      if (path) {
        gsap.to(path, {
          strokeDashoffset: 0,
          duration: 1.2,
          ease: 'power2.inOut'
        });
      }
    });
  }, 1500);
});
</script>

<style scoped>
/* Underline Animation Styles */
.underline-box {
  position: relative;
  margin-top: -0.2em;
  z-index: 1;
}

.accent-text {
  color: #fd3d13;
  position: relative;
}

/* Hero Section */
.heroSection {
  padding: 140px 0 100px;
  text-align: center;
  position: relative;
  z-index: 2;
  padding-bottom: 20vh;
}

.heroContent {
  margin: 0 auto;
  padding: 0 20px;
  width: 80%;
  margin: 0 auto;
}

.titleContainer {
  position: relative;
  display: inline-block;
  margin-bottom: 30px;
}

.mainTitle {
  font-size: 4rem;
  font-weight: 900;
  color: #293b2e;
  line-height: 1.1;
  position: relative;
  z-index: 3;
  margin: 0;
}

.heroSubtitle {
  font-size: 1.3rem;
  color: #2a2a2a;
  line-height: 1.7;
  max-width: 60vw;
  margin: 0 auto 40px;
  font-weight: 500;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
  position: relative;
  z-index: 3;
}

.heroStats {
  display: flex;
  justify-content: center;
  gap: 12vw;
  margin-top: 10vh;
}

.stat {
  text-align: center;
}

.statNumber {
  display: block;
  font-size: 8vw;
  font-weight: 900;
  color: #293b2e;
  line-height: 1;
  margin-bottom: 8px;
}

.statAccent {
  color: #fd3d13;
  font-size: 3vw;
}

.statLabel {
  font-size: 0.9rem;
  color: #555;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .mainTitle {
    font-size: 3.5rem;
  }
  
  .heroStats {
    gap: 30px;
  }
  
  .statNumber {
    font-size: 2rem;
  }
}

@media (max-width: 768px) {
  .heroSection {
    padding: 120px 0 80px;
  }
  
  .mainTitle {
    font-size: 2.8rem;
  }
  
  .heroSubtitle {
    font-size: 1.1rem;
  }
  
  .heroStats {
    flex-direction: column;
    gap: 20px;
  }
}

@media (max-width: 480px) {
  .heroSection {
    padding: 100px 0 60px;
  }
  
  .mainTitle {
    font-size: 2.2rem;
  }
}
</style> 