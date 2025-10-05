<template>
  <div class="contactGrid" ref="contactGrid">
    <div class="gridHeader">
      <h3 class="gridTitle">Multiple Ways to Connect</h3>
      <p class="gridSubtitle">Choose the method that works best for you</p>
    </div>
    
    <div class="contactCards">
      <div class="contactCard" @mouseenter="animateCard" ref="phoneCard">
        <div class="cardBackground"></div>
        <div class="cardIcon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="cardContent">
          <h4 class="cardContentTitle">Call Direct</h4>
          <p class="cardPhone">(555) 123-JOEL</p>
          <span class="cardSubtext">Instant response • 7AM-7PM</span>
        </div>
        <div class="cardAction">Call Now</div>
      </div>
      
      <div class="contactCard" @mouseenter="animateCard" ref="textCard">
        <div class="cardBackground"></div>
        <div class="cardIcon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="cardContent">
          <h4 class="cardContentTitle">Text Message</h4>
          <p class="cardPhone">(555) 123-JOEL</p>
          <span class="cardSubtext">Quick questions • Photos welcome</span>
        </div>
        <div class="cardAction">Send Text</div>
      </div>
      
      <div class="contactCard" @mouseenter="animateCard" ref="emailCard">
        <div class="cardBackground"></div>
        <div class="cardIcon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="2"/>
            <polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <div class="cardContent">
          <h4 class="cardContentTitle">Email Us</h4>
          <p class="cardEmail">hello@<br></br>joelshandys.com</p>
          <span class="cardSubtext">Detailed quotes • Project planning</span>
        </div>
        <div class="cardAction">Send Email</div>
      </div>
      
      <div class="contactCard" @mouseenter="animateCard" ref="scheduleCard">
        <div class="cardBackground"></div>
        <div class="cardIcon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <rect x="3" y="4" width="18" height="18" rx="2" ry="2" stroke="currentColor" stroke-width="2"/>
            <line x1="16" y1="2" x2="16" y2="6" stroke="currentColor" stroke-width="2"/>
            <line x1="8" y1="2" x2="8" y2="6" stroke="currentColor" stroke-width="2"/>
            <line x1="3" y1="10" x2="21" y2="10" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <div class="cardContent">
          <h4 class="cardContentTitle">Schedule Online</h4>
          <p class="cardSchedule">Book your consultation</p>
          <span class="cardSubtext">Free estimates • Same day available</span>
        </div>
        <div class="cardAction">Book Now</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// Refs for animations
const contactGrid = ref(null);
const phoneCard = ref(null);
const textCard = ref(null);
const emailCard = ref(null);
const scheduleCard = ref(null);

// Expose ref to parent if needed
defineExpose({
  contactGrid
});

function animateCard(event) {
  const card = event.currentTarget;
  gsap.to(card, {
    scale: 1.05,
    duration: 0.3,
    ease: 'power2.out'
  });
  
  card.addEventListener('mouseleave', () => {
    gsap.to(card, {
      scale: 1,
      duration: 0.3,
      ease: 'power2.out'
    });
  }, { once: true });
}

onMounted(async () => {
  await nextTick();
  
  // Set initial states
  if (contactGrid.value) {
    gsap.set(contactGrid.value.querySelectorAll('.contactCard'), { opacity: 0, y: 50 });
  }
  
  // ScrollTrigger animations
  if (contactGrid.value) {
    gsap.to(contactGrid.value.querySelectorAll('.contactCard'), {
      y: 0,
      opacity: 1,
      duration: 0.8,
      stagger: 0.15,
      ease: 'power2.out',
      scrollTrigger: {
        trigger: contactGrid.value,
        start: 'top 80%',
        toggleActions: 'play none none none'
      }
    });
  }
});
</script>

<style scoped>
/* Contact Grid */
.contactGrid {
  position: relative;
  z-index: 2;
}

.gridHeader {
  text-align: left;
  margin-bottom: 40px;
}

.gridTitle {
  font-size: 2rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 10px;
}

.gridSubtitle {
  font-size: 1rem;
  color: #666;
  line-height: 1.6;
}

.contactCards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  margin-bottom: 10vh;
  z-index: 10;
  position: relative;
}

.contactCard {
  background: rgb(255, 255, 255);
  border-radius: 20px;
  padding: 30px 20px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid rgba(44, 63, 54, 0.5);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  z-index: 10;
  position: relative;
}

.contactCard.priority {
  border: 2px solid #fd3d13;
  background: linear-gradient(135deg, rgba(200, 133, 98, 0.05), rgba(255, 255, 255, 0.95));
}

.contactCard:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.cardBackground {
  position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    opacity:0.4;
    background-size: 800%;
    background-repeat: repeat;
    background-image: url("~/assets/content/images/paper_overlay_5.jpg");
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 1;
    background-color: #ffffff;
}

.cardIcon {
  width: 40px;
  height: 40px;
  background: #293b2e;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  color: white;
  border: 1px solid #fd3d13;
}

.cardContentTitle {
  font-size: 0.8rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 8px;
}

.cardPhone, .cardEmail, .cardSchedule {
  font-size: 1.3rem;
  font-weight: 600;
  color: #293b2e;
  margin-bottom: 15px;
  margin-top: 10px;
}

.cardSubtext {
  font-size: 0.9rem;
  color: #666;
  line-height: 1.4;
}

.cardAction {
  position: absolute;
  top: 30px;
  right: 20px;
  background: #fd3d13;
  color: white;
  padding: 8px 15px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  opacity: 0;
  transform: translateY(-10px);
  transition: all 0.3s ease;
}

.contactCard:hover .cardAction {
  opacity: 1;
  transform: translateY(0);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .gridHeader {
    text-align: center;
  }
}

@media (max-width: 768px) {
  .contactCards {
    gap: 15px;
  }
  
  .contactCard {
    padding: 25px;
  }
}

@media (max-width: 480px) {
  .contactCard {
    padding: 20px;
  }
}
</style> 