<template>
  <section class="app-screens-section">
    <div class="container">
      <div class="phone-screens">
        <div class="phone-screen">
          <img src="~/assets/content/images/homePage/haven_1.png" alt="Haven App Screen 1" class="app-screen">
        </div>
        <div class="phone-screen" style="margin-top:5%">
          <img src="~/assets/content/images/homePage/haven_3.png" alt="Haven App Screen 3" class="app-screen">
        </div>
        <div class="phone-screen" data-speed="1.2" style="margin-top:6%">
          <img src="~/assets/content/images/homePage/haven_2.png" alt="Haven App Screen 2" class="app-screen">
        </div>
        <div class="phone-screen" style="margin-top:5%">
          <img src="~/assets/content/images/homePage/haven_4.png" alt="Haven App Screen 4" class="app-screen">
        </div>
        <div class="phone-screen">
          <img src="~/assets/content/images/homePage/haven_5.png" alt="Haven App Screen 5" class="app-screen">
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

onMounted(() => {
    setTimeout(() => {
  gsap.registerPlugin(ScrollTrigger)
  

  
  // Animate phone screens with staggered effect
  gsap.from('.phone-screen', {
    opacity: 0,
    stagger: 0.2,
    duration: 0.5,
    scrollTrigger: {
      trigger: '.phone-screens',
      start: 'top 65%',
      toggleActions: 'play none none none'
    }
  })
}, 1000)
})
</script>

<style scoped>
.app-screens-section {
  padding: 80px 0;
  position: relative;
  overflow: hidden;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 1;
}

.main-screen {
  margin-bottom: 60px;
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
}

.ipad-screen {
  width: 80%;
  max-width: 800px;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.2);
  transition: transform 0.5s ease;
}

.ipad-screen:hover {
  transform: translateY(-15px) scale(1.02);
}

.phone-screens {
  display: flex;
  justify-content: center;
  gap: 30px;
  flex-wrap: wrap;
  width: 100%;
}

.phone-screen {
  position: relative;
  transition: transform 0.3s ease;
}

.phone-screen:hover {
  transform: translateY(-15px);
}

.app-screen {
  width: 150px;
  height: auto;
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.15);
}

@media (max-width: 768px) {
  .phone-screens {
    gap: 15px;
  }
  
  .app-screen {
    width: 120px;
  }
}
</style> 