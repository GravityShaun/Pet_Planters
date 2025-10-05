<template>
  <div class="contactLandingContainer">
    <div class="paperOverlay"></div>
    

    <!-- Contact Methods and Form Section -->
    <div class="contactAndFormSection" ref="contactFormSection">
      <div class="sectionHeader">
        <div class="titleContainer" data-draw-line>
          <h2 class="sectionTitle" ref="titleElement">
            Get Started with Joel
          </h2>
          <div data-draw-line-box class="underline-box"></div>
        </div>
        <p class="sectionSubtitle">Choose how you'd like to connect or fill out our project form</p>
      </div>
      
      <div class="contactFormGrid">
        <!-- Left Column - Contact Cards -->
        <ContactMethods ref="contactMethodsRef" />

        <!-- Right Column - Contact Form -->
        <ContactForm ref="contactFormRef" />
      </div>
    </div>

        <!-- Hero Section -->
        <ContactHero />

    <!-- FAQ Section -->
    <ContactFAQ ref="contactFAQRef" />

  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';
import ContactHero from './ContactHero.vue';
import ContactMethods from './ContactMethods.vue';
import ContactForm from './ContactForm.vue';
import ContactFAQ from './ContactFAQ.vue';

gsap.registerPlugin(ScrollTrigger);

const { initUnderlineAnimation } = useUnderlineAnimation();

// Refs for child components and elements
const contactMethodsRef = ref(null);
const contactFormRef = ref(null);
const contactFAQRef = ref(null);
const contactFormSection = ref(null);
const titleElement = ref(null);

onMounted(async () => {
  await nextTick();
  
  // Initialize underline animation - same pattern as ContactHero
  const titleContainers = document.querySelectorAll('[data-draw-line]');
  titleContainers.forEach((container, index) => {
    // Create unique ID for each container to use as selector
    const uniqueId = `contact-landing-draw-line-${index}`;
    container.setAttribute('id', uniqueId);
    
    try {
      initUnderlineAnimation(`#${uniqueId}`, {
        autoAnimate: true,
        duration: 1.2,
        ease: 'power2.inOut',
        delay: 0.3
      });
    } catch (error) {
      console.error('Error initializing underline animation:', error);
    }
  });
  
  // Set initial states for section title
  if (titleElement.value) {
    gsap.set(titleElement.value, { opacity: 0, y: -30 });
    
    // Animate title in
    gsap.to(titleElement.value, {
      y: 0,
      opacity: 1,
      duration: 1,
      ease: 'power3.out',
      delay: 0.1
    });
  }
});
</script>

<style scoped>
.contactLandingContainer {
  width: 100%;
  background-color: #fff;
  position: relative;
  overflow-x: hidden;
  padding-top: 10vh;
}


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

/* Contact and Form Section */
.contactAndFormSection {
  padding: 100px 20px;
  position: relative;
  z-index: 2;
}

.sectionHeader {
  text-align: center;
  margin-bottom: 120px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.titleContainer {
  position: relative;
  display: inline-block;
}

.sectionTitle {
  font-size: 3rem;
  font-weight: 800;
  color: #293b2e;
  margin-bottom: 15px;
  position: relative;
  display: inline-block;
}

.sectionSubtitle {
  font-size: 1.1rem;
  color: #666;
  margin: 0 auto;
  line-height: 1.6;
}

.contactFormGrid {
  display: grid;
  grid-template-columns: 1fr 1.65fr;
  gap: 5vw;
  width: 90%;
  margin: 0 auto;
  align-items: start;
  margin-top:10%
}

/* Responsive Design */
@media (max-width: 1024px) {
  .sectionTitle {
    font-size: 2.5rem;
  }
  
  .contactFormGrid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}

@media (max-width: 768px) {
  .sectionTitle {
    font-size: 2rem;
  }
}

@media (max-width: 480px) {
  .sectionTitle {
    font-size: 1.8rem;
  }
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
  height: 100%;
  position: absolute;
  overflow: visible !important;
  color: #fd3d13;
}

.text-draw__box-svg path {
  stroke: #fd3d13;
}
</style>