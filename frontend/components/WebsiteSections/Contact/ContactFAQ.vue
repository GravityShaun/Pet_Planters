<template>
  <div class="faqSection" ref="faqSection">
    <div class="faqHeader">
      <div class="titleContainer" data-draw-line>
        <h2 class="sectionTitle">
          Frequently Asked <span class="accent-text">Questions</span>
        </h2>
        <div data-draw-line-box class="underline-box"></div>
      </div>
      <p class="sectionSubtitle">Everything you need to know about our services</p>
    </div>
    
    <div class="faqContainer">
      <div class="faqItem" 
           v-for="(faq, index) in faqs" 
           :key="index"
           :class="{ open: faq.isOpen }"
           @click="toggleFaq(index)">
        <div class="faqQuestion">
          <h3>{{ faq.question }}</h3>
          <div class="faqToggle">+</div>
        </div>
        <div class="faqAnswer" :ref="el => faqAnswers[index] = el">
          <p>{{ faq.answer }}</p>
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

gsap.registerPlugin(ScrollTrigger);

const { initUnderlineAnimation } = useUnderlineAnimation();

// Refs for animations
const faqSection = ref(null);
const faqAnswers = ref([]);

const faqs = ref([
  {
    question: 'How quickly can you start my project?',
    answer: 'For most projects, we can provide a quote within 2 hours and start work within 24-48 hours. Emergency repairs can often be addressed the same day.',
    isOpen: false
  },
  {
    question: 'Do you provide free estimates?',
    answer: 'Yes! We offer completely free, no-obligation estimates for all projects. We\'ll assess your needs and provide a detailed quote at no cost.',
    isOpen: false
  },
  {
    question: 'Are you licensed and insured?',
    answer: 'Absolutely. We are fully licensed, bonded, and insured. All our work comes with a satisfaction guarantee and warranty coverage.',
    isOpen: false
  },
  {
    question: 'What areas do you serve?',
    answer: 'We serve the greater metro area within a 30-mile radius. Primary service areas have free travel, while extended areas may have a small travel fee.',
    isOpen: false
  },
  {
    question: 'What payment methods do you accept?',
    answer: 'We accept cash, check, and all major credit cards. For larger projects, we can discuss payment plans and financing options.',
    isOpen: false
  }
]);

// Expose refs to parent if needed
defineExpose({
  faqSection
});

function toggleFaq(index) {
  const faq = faqs.value[index];
  const answer = faqAnswers.value[index];
  
  faq.isOpen = !faq.isOpen;
  
  if (faq.isOpen) {
    gsap.fromTo(answer, 
      { height: 0, opacity: 0 },
      { height: 'auto', opacity: 1, duration: 0.4, ease: 'power2.out' }
    );
  } else {
    gsap.to(answer, {
      height: 0,
      opacity: 0,
      duration: 0.3,
      ease: 'power2.in'
    });
  }
}

onMounted(async () => {
  await nextTick();
  
  // Initialize underline animations
  const titleContainers = faqSection.value?.querySelectorAll('[data-draw-line]');
  titleContainers?.forEach((container, index) => {
    // Create unique ID for each container to use as selector
    const uniqueId = `faq-draw-line-${index}`;
    container.setAttribute('id', uniqueId);
    
    initUnderlineAnimation(`#${uniqueId}`, {
      autoAnimate: false,
      duration: 1.2,
      ease: 'power2.inOut',
      delay: 0.5
    });
  });
  
  // FAQ Section Animation
  if (faqSection.value) {
    gsap.fromTo(faqSection.value.querySelectorAll('.faqItem'),
      { opacity: 0, x: -50 },
      {
        opacity: 1,
        x: 0,
        duration: 0.6,
        stagger: 0.1,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: faqSection.value,
          start: 'top 80%',
          toggleActions: 'play none none none'
        }
      }
    );
  }
  
  // Trigger underline animations on scroll
  if (faqSection.value) {
    ScrollTrigger.create({
      trigger: faqSection.value,
      start: 'top 80%',
      onEnter: () => {
        setTimeout(() => {
          titleContainers?.forEach(container => {
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
        }, 200);
      }
    });
  }
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

/* FAQ Section */
.faqSection {
  padding: 100px 20px;
  position: relative;
  z-index: 2;
}

.faqHeader {
  text-align: center;
  margin-bottom: 60px;
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
  max-width: 500px;
  margin: 0 auto;
  line-height: 1.6;
}

.faqContainer {
  max-width: 800px;
  margin: 0 auto;
}

.faqItem {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 15px;
  margin-bottom: 15px;
  border: 2px solid rgba(16, 108, 67, 0.1);
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
}

.faqItem:hover {
  border-color: rgba(200, 133, 98, 0.3);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
}

.faqQuestion {
  padding: 25px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.faqQuestion h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0;
  line-height: 1.4;
}

.faqToggle {
  width: 30px;
  height: 30px;
  background: #f8f9fa;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: 700;
  color: #293b2e;
  transition: all 0.3s ease;
  flex-shrink: 0;
  margin-left: 20px;
}

.faqItem.open .faqToggle {
  background: #293b2e;
  color: white;
  transform: rotate(45deg);
}

.faqAnswer {
  height: 0;
  overflow: hidden;
  opacity: 0;
}

.faqAnswer p {
  padding: 0 30px 25px;
  margin: 0;
  color: #666;
  line-height: 1.6;
  font-size: 1rem;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .sectionTitle {
    font-size: 2.5rem;
  }
}

@media (max-width: 768px) {
  .sectionTitle {
    font-size: 2rem;
  }
}

@media (max-width: 480px) {
  .faqQuestion {
    padding: 20px;
  }
  
  .faqQuestion h3 {
    font-size: 1rem;
  }
  
  .sectionTitle {
    font-size: 1.8rem;
  }
}
</style> 