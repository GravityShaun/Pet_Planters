<template>
    <div>
      <WebsiteSectionsHeaderBar />
      <NuxtLayout :name="layout">
        <GridBackground />
        <div class="paperOverlay" style="z-index: -10;"></div>
        <div class="background">
          <div class="paperOverlay"></div>
          <WebsiteSectionsAboutMainAbout />

          <WebsiteSectionsServicesItemsGrid />
          
        </div>
        <WebsiteSectionsFooter />
      </NuxtLayout>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import { gsap } from 'gsap'
  import { ScrollTrigger } from 'gsap/ScrollTrigger'
  
  const layout = "public";
  

  </script>
  
  <style scoped>
  .background {
    min-height: 100vh;
    width: 100vw;
    position: relative;
    overflow: hidden;
    background-color: #f7fdf6;
    border-bottom: 1px solid #466151;
  }
  
  </style>
