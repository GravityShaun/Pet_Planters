<template>
    <div class="scrollContainer">
        <div class="paperOverlay"></div>
      <div class="tiles_oneline" ref="grid2">
        <div class="tiles_wrap">
          <div class="tiles_row">
            <div v-for="(img, index) in grid2Images" :key="index" class="image_box">
              <div class="image" :style="getFilteredStyle(img)">
                <div class="cameraText calcFont">HAVEN</div>
              </div>
            </div>
          </div>
        </div>
        <h2 class="tiles_title vhsFont">HAVEN</h2>
      </div>
  
      <div class="tiles_oneline" ref="grid3">
        <div class="tiles_wrap">
          <div class="tiles_row">
            <div v-for="(img, index) in grid3Images" :key="index" class="image_box">
              <div class="image" :style="getFilteredStyle(img)">
                <div class="cameraText calcFont">COACHING</div>
              </div>
            </div>
          </div>
        </div>
        <h2 class="tiles_title vhsFont">COACHING</h2>
      </div>
  
      <div class="tiles_oneline" ref="grid4">
        <div class="tiles_wrap">
          <div class="tiles_row">
            <div v-for="(img, index) in grid4Images" :key="index" class="image_box">
              <div class="image" :style="getFilteredStyle(img)">
                <div class="cameraText calcFont">CHSMoves</div>
              </div>
            </div>
          </div>
        </div>
        <h2 class="tiles_title vhsFont">CHSMoves</h2>
      </div>
    </div>
  </template>
  
  
  
  
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { gsap } from 'gsap'
  import { ScrollTrigger } from 'gsap/ScrollTrigger'
  
  import haven_1 from '~/assets/content/images/homePage/haven_2.png'
  import haven_2 from '~/assets/content/images/homePage/haven_3.png'
  import haven_3 from '~/assets/content/images/homePage/haven_4.png'
  import haven_4 from '~/assets/content/images/homePage/haven_5.png'

  
  gsap.registerPlugin(ScrollTrigger)
  
  const grid2 = ref(null)
  const grid3 = ref(null)
  const grid4 = ref(null)
  
  const grid2Images = [
    haven_1,
    haven_2,
    haven_3,
    haven_4
  ]
  
  const grid3Images = [
        'https://images.unsplash.com/photo-1519834785169-98be25ec3f84?q=80&w=764&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1507537362848-9c7e70b7b5c1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGNvYWNoaW5nfGVufDB8fDB8fHwy',
    'https://images.unsplash.com/photo-1493612276216-ee3925520721?q=80&w=764&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1557425529-b1ae9c141e7d?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
  ]
  
  const grid4Images = [
    'https://images.unsplash.com/photo-1601422407692-ec4eeec1d9b3?q=80&w=1325&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1485727749690-d091e8284ef3?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1616279969856-759f316a5ac1?q=80&w=765&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1590556409324-aa1d726e5c3c?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
  ]
  
  const getFilteredStyle = (image) => {
    return {
      backgroundImage: `
        url(https://i.ibb.co/vJt5HSh/noisy-texture-100x100-o10-d10-c-a82851-t1.png),
        url(${image})`
    }
  }
  
  onMounted(() => {
    setTimeout(() => {
      gsap.to(grid2.value.querySelector('.tiles_row'), {
        xPercent: -25,
        ease: 'none',
        scrollTrigger: {
          trigger: grid2.value,
          start: 'top bottom',
          end: 'bottom top',
          scrub: true
        }
      })
  
      gsap.to(grid3.value.querySelector('.tiles_row'), {
        xPercent: -50,
        ease: 'none',
        scrollTrigger: {
          trigger: grid3.value,
          start: 'top bottom',
          end: 'bottom top',
          scrub: true
        }
      })
  
      gsap.to(grid4.value.querySelector('.tiles_row'), {
        xPercent: -25,
        ease: 'none',
        scrollTrigger: {
          trigger: grid4.value,
          start: 'top bottom',
          end: 'bottom top',
          scrub: true
        }
      })
  
      const titles = document.querySelectorAll('.tiles_title')
      titles.forEach(title => {
        gsap.to(title, {
          y: -200,
          ease: 'none',
          scrollTrigger: {
            trigger: title,
            start: 'top bottom',
            end: 'bottom top',
            scrub: true
          }
        })
      })
    }, 100) // 100ms timeout
  })
  </script>
  
  
  
  
  
  
  
  <style scoped>
  .scrollContainer {
    padding: 15vh 0;
    background-color: #e2f8ff;
    position: relative;
  }
  
  .tiles_oneline {
    position: relative;
    margin: 5% 0;
  }
  
  .tiles_wrap {
    white-space: nowrap;
  }
  
  .tiles_row {
    display: inline-flex;
    gap: 2%;
  }
  
  .image_box {
    width: 35vw;
    height: 45vw;
    border-radius: 10px;
    overflow: hidden;
  }
  
  .image {
    width: 100%;
    height: 100%;
    background-size: auto, auto, auto, cover;
    background-position: center;
    background-repeat: repeat, repeat, repeat, no-repeat;
  }
  
  .disposable_camera_effect {
    filter: blur(0.05em) saturate(0.7) contrast(1.5) brightness(1.35);
    box-shadow: 0 0 5px rgba(255, 255, 255, 0.05);
    border:1px solid rgba(255, 255, 255, 0.05);
    border-radius:5px
  }
  
  .tiles_title {
    font-weight: bold;
    color: #fff;
    position: absolute;
    font-size: 10rem;
    z-index: 10;
    margin-top: -35%;
    right: 10%;
    letter-spacing:0;
    text-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: #000;
  }
  
  
  
  .cameraText {
      position: absolute;
      font-size: 80%;
      color: rgba(255, 166, 0, 0.5);
      z-index: 2;
      letter-spacing: -0.25rem;
      writing-mode: vertical-rl;
      text-orientation: upright;
      left: 1.5%;
      bottom: 1%;
      font-weight: 500;
      text-shadow: 
          -1px -1px 0 rgba(255, 166, 0, 0.2),
          1px 1px 0 rgba(255, 166, 0, 0.2);
      transform: rotate(0.5deg);
      filter: blur(0.5px);
      line-height: -10.8em;
  }
  
  
  
  
  @media only screen and (min-width: 0px) and (max-width: 376px) {
  
    .tiles_title{
    font-size: 5rem;
    margin-top: -17%;
    }
  
    .scrollContainer {
    padding: 8vh 0;
  }
  }
    
  @media only screen and (min-width: 376px) and (max-width: 576px) {
    .tiles_title{
    font-size: 8rem;
    margin-top: -14%;
    }
  
    .scrollContainer {
    padding: 8vh 0;
  }
  }
  
  @media only screen and (min-width: 576px) and (max-width: 768px) {
    .tiles_title{
    font-size: 10rem;
    margin-top: -14%;
    }
  
    .scrollContainer {
    padding: 8vh 0;
  }
  }
  
  @media only screen and (min-width: 768px) and (max-width: 992px) {
  }
  
  @media only screen and (min-width: 992px) and (max-width: 1200px) {
  }
  
  @media only screen and (min-width: 1200px) and (max-width: 1400px) {
  }
  
  @media only screen and (min-width: 1400px) and (max-width: 1600px) {
  }
  
  
  @media only screen and (min-width: 1600px) and (max-width: 2000px) {
  }
  
  @media only screen and (min-width: 2000px) and (max-width: 2500px) {
  }
  
  @media only screen and (min-width: 2500px) and (max-width: 5600px) {
  }
  
  
  </style>