<template>
  <div class="cta-section" ref="ctaRef">
    <div class="cta-content">
      <div class="cta-visual">
        <div class="cta-icon">{{ service?.icon }}</div>
        <div class="cta-decoration"></div>
      </div>
      <div class="cta-text">
        <h2>Ready to Get Started?</h2>
        <p>Contact us today to schedule your <strong>{{ service?.title?.toLowerCase() }}</strong> service and experience professional craftsmanship.</p>
        
        <div class="cta-features">
          <div class="feature-item">
            <span class="feature-icon">📞</span>
            <span>Free Consultation</span>
          </div>
          <div class="feature-item">
            <span class="feature-icon">⚡</span>
            <span>Quick Response</span>
          </div>
          <div class="feature-item">
            <span class="feature-icon">💯</span>
            <span>100% Satisfaction</span>
          </div>
        </div>
        
        <div class="cta-buttons">
          <NuxtLink to="/contact" class="cta-button primary">
            <span class="button-icon">📧</span>
            Get Free Quote
          </NuxtLink>
          <NuxtLink to="/services" class="cta-button secondary">
            <span class="button-icon">🔍</span>
            View All Services
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const props = defineProps({
  service: {
    type: Object,
    required: true
  }
})

const ctaRef = ref(null)

onMounted(() => {
  setTimeout(() => {
    initializeAnimations()
  }, 100)
})

function initializeAnimations() {
  // CTA section animation
  if (ctaRef.value) {
    // Animate icon and decoration
    gsap.from('.cta-icon', {
      scale: 0,
      rotation: -180,
      opacity: 0,
      duration: 0.8,
      ease: "back.out(1.7)",
      scrollTrigger: {
        trigger: ctaRef.value,
        start: "top 80%",
        toggleActions: "play none none reverse"
      }
    })

    gsap.from('.cta-decoration', {
      scale: 0,
      opacity: 0,
      duration: 0.8,
      delay: 0.2,
      ease: "power2.out",
      scrollTrigger: {
        trigger: ctaRef.value,
        start: "top 80%",
        toggleActions: "play none none reverse"
      }
    })

    // Animate heading
    gsap.from('.cta-text h2', {
      y: 40,
      opacity: 0,
      duration: 0.6,
      delay: 0.3,
      ease: "power2.out",
      scrollTrigger: {
        trigger: ctaRef.value,
        start: "top 80%",
        toggleActions: "play none none reverse"
      }
    })

    // Animate paragraph
    gsap.from('.cta-text p', {
      y: 40,
      opacity: 0,
      duration: 0.6,
      delay: 0.4,
      ease: "power2.out",
      scrollTrigger: {
        trigger: ctaRef.value,
        start: "top 80%",
        toggleActions: "play none none reverse"
      }
    })

    // Animate feature items with stagger (scoped to this component)
    gsap.from(ctaRef.value.querySelectorAll('.feature-item'), {
      y: 30,
      opacity: 0,
      duration: 0.5,
      stagger: 0.15,
      delay: 0.5,
      ease: "power2.out",
      scrollTrigger: {
        trigger: ctaRef.value,
        start: "top 80%",
        toggleActions: "play none none reverse"
      }
    })

  }
}
</script>

<style scoped>
.cta-section {
  padding: 5rem 2rem;
  background: linear-gradient(135deg, #293b2e 0%, #1a2621 100%);
  color: white;
  position: relative;
  overflow: hidden;
}

.cta-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="dots" width="40" height="40" patternUnits="userSpaceOnUse"><circle cx="20" cy="20" r="2" fill="%23ffffff" opacity="0.1"/></pattern></defs><rect width="100%" height="100%" fill="url(%23dots)" /></svg>') repeat;
  pointer-events: none;
}

.cta-content {
  max-width: 1000px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 8rem;
  align-items: center;
  position: relative;
  z-index: 1;
}

.cta-visual {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.cta-icon {
  font-size: 6rem;
  filter: drop-shadow(0 10px 30px rgba(0, 0, 0, 0.3));
  animation: ctaFloat 8s ease-in-out infinite;
}

@keyframes ctaFloat {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  25% { transform: translateY(-10px) rotate(2deg); }
  75% { transform: translateY(5px) rotate(-1deg); }
}

.cta-decoration {
  position: absolute;
  width: 120px;
  height: 120px;
  border: 3px solid rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  animation: rotate 20s linear infinite;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.cta-text {
  text-align: left;
}

.cta-text h2 {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  letter-spacing: 0.5px;
  background: linear-gradient(135deg, #ffffff 0%, rgba(255, 255, 255, 0.8) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-transform: uppercase;
}

.cta-text p {
  font-size: 18px;
  line-height: 1.6;
  margin-bottom: 5rem;
  opacity: 0.9;
  text-transform: none;
  font-family: system-ui, -apple-system, sans-serif;
  font-weight: 400;
  max-width: 500px;
}

.cta-features {
  display: flex;
  gap: 2rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 12px;
  font-weight: 500;
  opacity: 0.8;
  text-transform: uppercase;
  letter-spacing: 0.8px;
}

.feature-icon {
  font-size: 14px;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  align-items: center;
  opacity: 1;
}

.cta-button {
  padding: 1.2rem 2.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  letter-spacing: 0.8px;
  transition: all 0.3s ease;
  font-size: 14px;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  border: 2px solid transparent;
  text-transform: uppercase;
  opacity: 1;
}

.button-icon {
  font-size: 16px;
}

.cta-button.primary {
  background: linear-gradient(135deg, #a15e3c 0%, #b36e4f 100%);
  color: white;
  box-shadow: 0 6px 20px rgba(161, 94, 60, 0.3);
}

.cta-button.primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(161, 94, 60, 0.4);
}

.cta-button.secondary {
  background: transparent;
  color: white;
  border-color: rgba(255, 255, 255, 0.3);
}

.cta-button.secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: white;
  transform: translateY(-3px);
}

@media (max-width: 768px) {
  .cta-section {
    padding: 3rem 1rem;
  }

  .cta-content {
    grid-template-columns: 1fr;
    gap: 2rem;
    text-align: center;
  }

  .cta-text {
    text-align: center;
  }

  .cta-text h2 {
    font-size: 2.2rem;
  }

  .cta-features {
    justify-content: center;
  }

  .cta-buttons {
    flex-direction: column;
    width: 100%;
  }

  .cta-button {
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .cta-features {
    flex-direction: column;
    gap: 1rem;
  }

  .cta-text h2 {
    font-size: 1.8rem;
  }
}
</style>