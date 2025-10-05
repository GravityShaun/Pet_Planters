<template>
  <div class="formSection" ref="formContainer">
    <div class="formWrapper">
      <div class="formHeader">
        <h3 class="formTitle">Tell Us About Your Project</h3>
        <p class="formSubtitle">Get a detailed quote in under 2 hours</p>
      </div>
  
      <div class="formCard">
        <div class="formBackground"></div>
        <form @submit.prevent="submitForm" class="contactForm">
          <!-- Step 1: Basic Info -->
          <div class="formStep" :class="{ active: currentStep === 1 }" ref="step1">
            <div class="stepHeader">
              <span class="stepNumber">01</span>
              <h3>Let's start with the basics</h3>
            </div>
            
            <div class="formGrid">
              <div class="formGroup">
                <label for="name">Full Name *</label>
                <input type="text" id="name" v-model="form.name" required>
              </div>
              
              <div class="formGroup">
                <label for="email">Email Address *</label>
                <input type="email" id="email" v-model="form.email" required>
              </div>
              
              <div class="formGroup">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" v-model="form.phone">
              </div>
              
              <div class="formGroup">
                <label for="address">Property Address</label>
                <input type="text" id="address" v-model="form.address" placeholder="Street, City, State">
              </div>
            </div>
          </div>
          
          <!-- Step 2: Project Details -->
          <div class="formStep" :class="{ active: currentStep === 2 }" ref="step2">
            <div class="stepHeader">
              <span class="stepNumber">02</span>
              <h3>What can we help you with?</h3>
            </div>
            
            <div class="serviceSelection">
              <div class="serviceGrid">
                <div class="serviceCard" 
                     v-for="service in services" 
                     :key="service.id"
                     :class="{ selected: selectedServices.includes(service.id) }"
                     @click="toggleService(service.id)">
                  <div class="serviceIcon">{{ service.icon }}</div>
                  <span class="serviceName">{{ service.name }}</span>
                </div>
              </div>
              
              <div class="formGroup fullWidth">
                <label for="urgency">How urgent is this project?</label>
                <select id="urgency" v-model="form.urgency">
                  <option value="">Select timeline</option>
                  <option value="emergency">Emergency - ASAP</option>
                  <option value="urgent">Urgent - This week</option>
                  <option value="soon">Soon - Within 2 weeks</option>
                  <option value="planning">Planning - Within a month</option>
                  <option value="flexible">Flexible - No rush</option>
                </select>
              </div>
            </div>
          </div>
          
          <!-- Step 3: Project Description -->
          <div class="formStep" :class="{ active: currentStep === 3 }" ref="step3">
            <div class="stepHeader">
              <span class="stepNumber">03</span>
              <h3>Tell us more about your project</h3>
            </div>
            
            <div class="formGroup fullWidth">
              <label for="message">Project Description *</label>
              <textarea id="message" 
                       v-model="form.message" 
                       rows="6" 
                       required 
                       placeholder="Describe your project in detail. Include dimensions, materials, current issues, desired outcome, budget range, etc."></textarea>
            </div>
            
            <div class="formGroup fullWidth">
              <label for="budget">Estimated Budget Range</label>
              <select id="budget" v-model="form.budget">
                <option value="">Select budget range</option>
                <option value="under-500">Under $500</option>
                <option value="500-1500">$500 - $1,500</option>
                <option value="1500-5000">$1,500 - $5,000</option>
                <option value="5000-15000">$5,000 - $15,000</option>
                <option value="over-15000">Over $15,000</option>
              </select>
            </div>
          </div>
          
          <!-- Form Navigation -->
          <div class="formNavigation">
            <button type="button" 
                    class="navBtn prevBtn" 
                    @click="previousStep" 
                    v-if="currentStep > 1">
              ← Previous
            </button>
            
            <button type="button" 
                    class="navBtn nextBtn" 
                    @click="nextStep" 
                    v-if="currentStep < 3">
              Next →
            </button>
            
            <button type="submit" 
                    class="submitBtn" 
                    v-if="currentStep === 3"
                    :disabled="!isFormValid">
              <span>Send My Request</span>
              <div class="btnIcon">✓</div>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, nextTick } from 'vue';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// Refs for animations
const formContainer = ref(null);
const step1 = ref(null);
const step2 = ref(null);
const step3 = ref(null);

// Form state
const currentStep = ref(1);
const selectedServices = ref([]);

const form = ref({
  name: '',
  email: '',
  phone: '',
  address: '',
  urgency: '',
  message: '',
  budget: ''
});

const services = ref([
  { id: 'plumbing', name: 'Plumbing', icon: '🔧' },
  { id: 'electrical', name: 'Electrical', icon: '⚡' },
  { id: 'carpentry', name: 'Carpentry', icon: '🪚' },
  { id: 'painting', name: 'Painting', icon: '🎨' },
  { id: 'repairs', name: 'General Repairs', icon: '🔨' },
  { id: 'installation', name: 'Installation', icon: '🛠️' },
  { id: 'maintenance', name: 'Maintenance', icon: '⚙️' },
  { id: 'renovation', name: 'Renovation', icon: '🏗️' }
]);

const isFormValid = computed(() => {
  return form.value.name && form.value.email && form.value.message && selectedServices.value.length > 0;
});

// Expose refs to parent if needed
defineExpose({
  formContainer
});

// Methods
function toggleService(serviceId) {
  const index = selectedServices.value.indexOf(serviceId);
  if (index > -1) {
    selectedServices.value.splice(index, 1);
  } else {
    selectedServices.value.push(serviceId);
  }
}

function nextStep() {
  if (currentStep.value < 3) {
    animateStepTransition(currentStep.value + 1);
    currentStep.value++;
  }
}

function previousStep() {
  if (currentStep.value > 1) {
    animateStepTransition(currentStep.value - 1);
    currentStep.value--;
  }
}

function animateStepTransition(targetStep) {
  if (!formContainer.value) return;
  
  const currentStepEl = formContainer.value.querySelector('.formStep.active');
  const targetStepEl = formContainer.value.querySelector(`.formStep:nth-child(${targetStep})`);
  
  if (currentStepEl && targetStepEl) {
    gsap.to(currentStepEl, {
      opacity: 0,
      x: -50,
      duration: 0.3,
      onComplete: () => {
        gsap.fromTo(targetStepEl, 
          { opacity: 0, x: 50 },
          { opacity: 1, x: 0, duration: 0.3 }
        );
      }
    });
  }
}

function submitForm() {
  const formData = {
    ...form.value,
    services: selectedServices.value
  };
  
  console.log('Form submitted:', formData);
  alert('Thank you for your detailed request! We\'ll get back to you within 2 hours with a comprehensive quote.');
  
  // Reset form
  form.value = {
    name: '',
    email: '',
    phone: '',
    address: '',
    urgency: '',
    message: '',
    budget: ''
  };
  selectedServices.value = [];
  currentStep.value = 1;
}

onMounted(async () => {
  await nextTick();
  
  // Set initial states
  if (formContainer.value) {
    gsap.set(formContainer.value, { opacity: 0, scale: 0.95 });
  }
  
  // ScrollTrigger animations
  if (formContainer.value) {
    gsap.to(formContainer.value, {
      scale: 1,
      opacity: 1,
      duration: 1,
      ease: 'power2.out',
      scrollTrigger: {
        trigger: formContainer.value,
        start: 'top 80%',
        toggleActions: 'play none none none'
      }
    });
  }
});
</script>

<style scoped>
/* Form Section */
.formSection {
  position: relative;
  z-index: 2;
}

.formWrapper {
  width: 100%;
}

.formHeader {
  text-align: left;
  margin-bottom: 30px;
}

.formTitle {
  font-size: 2rem;
  font-weight: 700;
  color: #293b2e;
  margin-bottom: 10px;
}

.formSubtitle {
  font-size: 1.1rem;
  color: #666;
  line-height: 1.6;
}

.formCard {
  background: rgb(255, 255, 255);
  border-radius: 25px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  border: 1px solid #293b2e7a;
  position: relative;
  z-index: 10;
  transition: all 0.3s ease;
}

.formCard:hover {
  box-shadow: 0 7px 12px rgba(0, 0, 0, 0.25);
  transform: translateY(-2px);
}

.formBackground {
  position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    opacity:0.4;
    background-size: 250%;
    background-repeat: repeat;
    background-image: url("~/assets/content/images/paper_overlay_5.jpg");
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 1;
    background-color: #ffffff;
}

.contactForm {
  padding: 40px;
}

.formStep {
  display: none;
}

.formStep.active {
  display: block;
}

.stepHeader {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
}

.stepNumber {
  width: 40px;
  height: 40px;
  background:#293b2e;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.1rem;
  border: 1px solid #fd3d13;
}

.stepHeader h3 {
  font-size: 1.4rem;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0;
}

.formGrid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.formGroup {
  margin-bottom: 20px;
}

.formGroup.fullWidth {
  grid-column: 1 / -1;
}

.serviceSelection {
  margin-bottom: 30px;
}

.serviceGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 15px;
  margin-bottom: 25px;
}

.serviceCard {
  background: #f8f9fa;
  border: 2px solid #e9ecef;
  border-radius: 15px;
  padding: 20px 10px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.serviceCard:hover {
  border-color: #fd3d13;
  background: rgba(200, 133, 98, 0.05);
}

.serviceCard.selected {
  border-color: #293b2e;
  background: rgba(16, 108, 67, 0.1);
  transform: translateY(-2px);
}

.serviceIcon {
  font-size: 1.8rem;
  margin-bottom: 8px;
}

.serviceName {
  font-size: 0.9rem;
  font-weight: 600;
  color: #333;
}

label {
  display: block;
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 8px;
  color: #333;
}

input, select, textarea {
  width: 100%;
  padding: 15px 18px;
  border: 2px solid #e8e8e8;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: #fafafa;
  font-family: inherit;
  z-index: 10;
  position: relative;
}

input:focus, select:focus, textarea:focus {
  outline: none;
  border-color: #293b2e;
  background: white;
  box-shadow: 0 0 0 3px rgba(16, 108, 67, 0.1);
}

.formNavigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 30px;
  padding-top: 25px;
  border-top: 2px solid #f0f0f0;
}

.navBtn {
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  color: #495057;
  padding: 12px 25px;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 10;
  position: relative;
}

.navBtn:hover {
  background: #e9ecef;
  border-color: #adb5bd;
}

.submitBtn {
  background: #293b2e;
  color: white;
  border: none;
  padding: 15px 30px;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 10px;
  position: relative;
  overflow: hidden;
  border: 1px solid #fd3d13;
  z-index: 10;
  position: relative;
}

.submitBtn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(16, 108, 67, 0.3);
}

.submitBtn:disabled {
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
  z-index: 10;
  position: relative;
  color: #a18181;
}

.btnIcon {
  font-size: 1.2rem;
  transition: transform 0.3s ease;
}

.submitBtn:hover .btnIcon {
  transform: translateX(5px);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .formHeader {
    text-align: center;
  }
  
  .formGrid {
    grid-template-columns: 1fr;
  }
  
  .serviceGrid {
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  }
}

@media (max-width: 768px) {
  .contactForm {
    padding: 30px 20px;
  }
}

@media (max-width: 480px) {
  .serviceGrid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .formNavigation {
    flex-direction: column;
    gap: 15px;
  }
  
  .navBtn, .submitBtn {
    width: 100%;
    justify-content: center;
  }
}
</style> 