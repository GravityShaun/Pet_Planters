<template>
  <div ref="landingPageRef" class="landing-page">
    
    <!-- Main Landing Section -->
    <section class="landing-section">
      <div class="text-content">
        <h1 class="landing-title">
          3D Print Your Pet into<br>
          <span class="text-draw" data-draw-line>a custom planter
            <div class="text-draw__box" data-draw-line-box></div>
          </span> 
        </h1>
        <p class="landing-subtitle">Upload up to 5 photos of your beloved dog and we'll create a custom 3D printed planter topped with a beautiful succulent. Each piece is handcrafted to capture your pet's unique personality.</p>
        <NuxtLink to="/contact" class="cta-button">Start Creating</NuxtLink>
      </div>
      <div class="image-container">
        <div ref="colorCircle" class="color-circle">
          <div class="paperOverlayImageBackground"></div>
        </div>
        <div class="landing_image_container" ref="landingImage" >
          <!-- <div class="paperOverlayImageOverlay"></div> -->
          <img class="landing-image" src="~/assets/content/images/homePage/home_1.png" />
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { gsap } from 'gsap';
import { useElementVisibility } from '@vueuse/core';
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';


const colorCircle = ref(null);
const landingImage = ref(null);


// Mouse tracking variables
let mouseX = 0;
let mouseY = 0;
let circleX = 0;
let circleY = 0;
let circleRotX = 0;
let circleRotY = 0;
let imageX = 0;
let imageY = 0;
let imageRotX = 0;
let imageRotY = 0;

const landingPageRef = ref(null);

// Use VueUse element visibility to track when component is visible
const isVisible = useElementVisibility(landingPageRef);

const handleMouseMove = (event) => {
  if (!landingPageRef.value) return;
  
  const rect = landingPageRef.value.getBoundingClientRect();
  
  // Calculate component center
  const componentCenterX = rect.left + rect.width / 2;
  const componentCenterY = rect.top + rect.height / 2;
  
  // Get mouse position relative to component center
  const deltaX = event.clientX - componentCenterX;
  const deltaY = event.clientY - componentCenterY;
  
  // Normalize to -1 to 1 range based on component size
  mouseX = deltaX / (rect.width * 0.5);
  mouseY = deltaY / (rect.height * 0.5);
  
  // No clamping - let it move freely for extended tracking
};

// Watch visibility and manage event listener
watch(isVisible, (visible) => {
  if (visible) {
    window.addEventListener('mousemove', handleMouseMove);
  } else {
    window.removeEventListener('mousemove', handleMouseMove);
  }
});

const animateMouseFollow = () => {
  // Smooth easing constants for different elements
  const circleEase = 0.12;
  const imageEase = 0.15;
  const rotationEase = 0.08;
  
  // Circle follows mouse with smaller offset and subtle tilt
  const targetCircleX = mouseX * 20;
  const targetCircleY = mouseY * 20;
  const targetCircleRotX = mouseY * -6;
  const targetCircleRotY = mouseX * 6;
  
  circleX += (targetCircleX - circleX) * circleEase;
  circleY += (targetCircleY - circleY) * circleEase;
  circleRotX += (targetCircleRotX - circleRotX) * rotationEase;
  circleRotY += (targetCircleRotY - circleRotY) * rotationEase;
  
  // Image follows mouse with larger offset and more pronounced tilt
  const targetImageX = mouseX * 15;
  const targetImageY = mouseY * 15;
  const targetImageRotX = mouseY * -4;
  const targetImageRotY = mouseX * 4;
  
  imageX += (targetImageX - imageX) * imageEase;
  imageY += (targetImageY - imageY) * imageEase;
  imageRotX += (targetImageRotX - imageRotX) * rotationEase;
  imageRotY += (targetImageRotY - imageRotY) * rotationEase;
  
  if (colorCircle.value) {
    gsap.set(colorCircle.value, {
      x: circleX,
      y: circleY,
      rotationX: circleRotX,
      rotationY: circleRotY,
      transformPerspective: 1200,
      force3D: true,
    });
  }
  
  if (landingImage.value) {
    gsap.set(landingImage.value, {
      x: imageX,
      y: imageY,
      rotationX: imageRotX,
      rotationY: imageRotY,
      transformPerspective: 1000,
      force3D: true,
    });
  }
  
  requestAnimationFrame(animateMouseFollow);
};

const { initUnderlineAnimation } = useUnderlineAnimation();

onMounted(() => {
  // Set initial states for the animation
  gsap.set(colorCircle.value, { scale: 0, transformOrigin: 'center center' });
  gsap.set(landingImage.value, { scale: 0, opacity: 0, transformOrigin: 'center center' });

  // Animate the colored circle scaling in
  gsap.to(colorCircle.value, {
    scale: 1,
    duration: 2.5,
    delay: 0.5,
    ease: 'elastic.out(1, 0.5)',
  });

  // Animate the image inside the circle, staggered by 1 second
  gsap.to(landingImage.value, {
    scale: 1,
    opacity: 1,
    duration: 1.2,
    delay: 0.7, // 3s for circle + 1s stagger
    ease: 'power3.out',
  });

  // Start mouse follow animation
  animateMouseFollow();
  
  // Initialize draw underline effect
  initUnderlineAnimation();
});

onUnmounted(() => {
  // Clean up event listener if it exists
  window.removeEventListener('mousemove', handleMouseMove);
});
</script>

<style scoped>
.landing-page {
  width: 100%;
  min-height: 100vh;
}


.landing-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  justify-items: center;
  min-height: calc(100vh - 80px); /* Adjust based on actual header height */
  padding: 2rem 5vw;
  gap: 2rem;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
}

.text-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  max-width: 550px;
  z-index: 1;
}

.landing-title {
  font-size: 3.25rem;
  font-weight: 700;
  color: #04602c;
  line-height: 1.2;
  margin-bottom: 1rem;
}

/* Draw underline styles */
.text-draw {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

.text-draw__box {
  color: #3f7c49;
  width: 100%;
  height: 0.625em;
  position: relative;
  margin-top: -0.15em;
}

.text-draw__box-svg {
  width: 100%;
  height: 100%;
  position: absolute;
  overflow: visible !important;
}

.landing-subtitle {
  font-size: 1.2rem;
  color: #466151;
  margin-bottom: 2rem;
  line-height: 1.6;
  margin-top: 8%
}

.cta-button {
  font-weight: 500;
  font-size: 1rem;
  text-transform: uppercase;
  cursor: pointer;
  display: inline-block;
  padding: 1rem 2rem;
  border-radius: 50px;
  transition: all .3s ease;
  background-color: #3f7c49;
  color: #f7fdf6;
  text-decoration: none;
  box-shadow: 0 4px 15px rgba(63, 124, 73, 0.2);
  border: 2px solid #466151;
}

.cta-button:hover {
  background-color: #274534;
  color: #f7fdf6;
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(39, 69, 52, 0.3);
}

.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  position: relative;
  z-index: 1;
  margin-top: 80px;
}

.color-circle {
  width: 400px;
  height: 600px;
  background: linear-gradient(135deg, #466151 0%, #3f7c49 100%);
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: visible;
  position: relative;
  box-shadow: 0 10px 30px rgba(70, 97, 81, 0.3);
  border: 3px solid #274534;
}

.landing_image_container {
  width: 400px;
  height: 600px;
  object-fit: cover;
  border-radius: 20px;
  position: absolute;
  margin-top: -50px;
  margin-left: -50px;
  box-shadow: 0 15px 40px rgba(39, 69, 52, 0.25);
  overflow: hidden;
  z-index: 1;
  border: 2px solid #f7fdf6;
}

.landing-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: relative;
  z-index: 0;
}

/* Responsive Design */
@media (max-width: 992px) {
  .landing-section {
    grid-template-columns: 1fr;
    text-align: center;
    padding: 4rem 5vw;
    gap: 3rem;
    min-height: auto;
  }

  .text-content {
    align-items: center;
    order: 2; /* Text comes after image on mobile */
  }

  .image-container {
    order: 1;
  }

  .landing-title {
    font-size: 2.5rem;
  }

  .landing-subtitle {
    font-size: 1.1rem;
  }

  .color-circle {
    width: 350px;
    height: 350px;
  }

  .landing-image {
    width: 310px;
    height: 310px;
    top: -20px;
    left: 20px;
  }
}

@media (max-width: 576px) {
  .landing-title {
    font-size: 2rem;
  }

  .landing-subtitle {
    font-size: 1rem;
  }

  .color-circle {
    width: 300px;
    height: 300px;
  }

  .landing-image {
    width: 265px;
    height: 265px;
    top: -17px;
    left: 17px;
  }

  .cta-button {
    padding: 0.8rem 1.6rem;
    font-size: 0.9rem;
  }
}



.paperOverlayImageBackground {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    opacity:1;
    background-size: 1000%;
    background-repeat: repeat;
    background-image: url("~/assets/content/images/paper_overlay_5.jpg");
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 1;
  }

  .paperOverlayImageOverlay{
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    opacity:0.75;
    background-size: 300%;
    background-repeat: repeat;
    background-image: url("~/assets/content/images/paper_overlay_5.jpg");
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 1;
  }
</style>
