<template>
    <div class="wrapper" @mouseenter="noCursor()" @mouseleave="clearCursor()">
      <div class="hero hero--primary">
        <div class="paperOverlayLanding"></div>
              <!-- <div class="noise"></div> -->
        <!-- <h1 class="hero__heading glitch vhsFont" data-text="F-CK MARRY KILL">F-CK MARRY KILL</h1> -->
  
  <div v-if="isGlitch" class="glitch hero__heading vhsFont">
    <div class="line">JOEL'S HANDYS</div>
    <div class="line">JOEL'S HANDYS</div>
    <div class="line">JOEL'S HANDYS</div>
    <div class="line">JOEL'S HANDYS</div>
    <div class="line">JOEL'S HANDYS</div>
    <div class="line">JOEL'S HANDYS</div>
    <div class="line">JOEL'S HANDYS</div>
    <div class="line">JOEL'S HANDYS</div>
    <div class="line">JOEL'S HANDYS</div>
  </div>
      <h1 v-else class="hero__heading vhsFont">JOEL'S HANDYS</h1>
        <h1 class="hero__heading_subtitle top_subtitle">Quality Work, Guaranteed</h1>
      </div>
      <div class="hero hero--secondary" aria-hidden="true" ref="heroRef">
        <h1 class="hero__heading vhsFont">JOEL'S HANDYS</h1>
        <h1 class="hero__heading_subtitle">Your trusted handyman</h1>
      </div>
    </div>
  </template>
  
  
  <script setup>
  import { gsap } from 'gsap';
  import { useMouse, useWindowScroll } from '@vueuse/core';
  const { setCursor, clearCursor, noCursor } = useCursor()
  
  const heroRef = ref(null);
  const { x, y } = useMouse();
  const { y: scrollY } = useWindowScroll();
  const isGlitch = ref(false);
  
  onMounted(() => {
    const tl = gsap.timeline();
    tl.to(heroRef.value, {
      '--maskSize1': '11%',
      duration: 0.5,
      ease: 'back.out(2)',
    }).to(heroRef.value, {
      '--maskSize2': '15%',
      '--maskSize3': 'calc(15% + 0.1rem)',
      duration: 0.5,
      delay: 0.5,
      ease: 'back.out(2)',
    });
  
    const updateMousePosition = () => {
      if (!heroRef.value) return;
  
      const rect = heroRef.value.getBoundingClientRect();
      const xPercentage = ((x.value - rect.left) / rect.width) * 100;
      const yPercentage = ((y.value - scrollY.value - rect.top) / rect.height) * 100;
  
      gsap.to(heroRef.value, {
        '--x': `${xPercentage}%`,
        '--y': `${yPercentage}%`,
        duration: 0.3,
        ease: 'sine.out',
        overwrite: 'auto',
      });
    };
  
    watch([x, y, scrollY], updateMousePosition, { immediate: true });
  
  
    isGlitch.value = true;
    setTimeout(() => {
      isGlitch.value = false;
    }, 4000);
  
  
  });
  
  
  
  
  // Toggle the glitch animation every 65 seconds
  setInterval(() => {
    isGlitch.value = true;
    setTimeout(() => {
      isGlitch.value = false;
    }, 3500); // 3 seconds
  }, 20000); // 25 seconds
  
  
  </script>
  
  
  
  
  
  
  <style>
  @import url("https://fonts.googleapis.com/css?family=Montserrat:700");
  
  :root {
    --bg: var(--primary_color);
    --gradientBg: linear-gradient(45deg, var(--primary_color), var(--secondary_color), var(--accent_color), #e55a2b);
  }
  
  .wrapper {
    position: relative;
    height: 100vh;
    z-index: 2;
  }
  
  .hero {
    min-height: 100vh;
    padding: clamp(1rem, 2vw, 5rem);
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    flex-direction: column;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    overflow: hidden;
  }
  
  .hero--primary {
    background-color: var(--bg);
    color: #ffffff;
    z-index: 1;
    background-image: url('~/assets/content/images/noise.webp');
    mix-blend-mode: overlay;
  }
  
  .hero--secondary {
    --mask: radial-gradient(
      circle at var(--x, 50%) var(--y, 50%),
      black var(--maskSize1, 0), 
      transparent 0, 
      transparent var(--maskSize2, 0),
      black var(--maskSize2, 0), 
      black var(--maskSize3, 0), 
      transparent 0
    );
    background: var(--gradientBg);
    color: var(--bg);
    -webkit-mask-image: var(--mask);
    mask-image: var(--mask);
    z-index: 2;
    position: relative;
  }
  
  .hero--secondary::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('http://assets.iceable.com/img/noise-transparent.png');
    opacity: 1;
    mix-blend-mode: overlay;
    pointer-events: none;
  }
  
  .hero__heading {
    font-size: 10rem;
    text-transform: uppercase;
    margin: 0;
    text-align: center;
    letter-spacing: 0px;
    font-weight: 600;
  }
  
  .hero__heading_subtitle {
    font-size: 130%;
    text-transform: uppercase;
    margin: 0;
    text-align: center;
    margin-top: 10%;
    color: #fff;
  }

  .top_subtitle{
    color: #244300;
  }
  
  
  
  .noise {
    position: absolute;
    top: -100%;
    left: -50%;
    right: -50%;
    bottom: -50%;
    width: 200%;
    height: 300vh;
    background: transparent url('http://assets.iceable.com/img/noise-transparent.png') repeat 0 0;
    background-repeat: repeat;
    background-size: 30%;
    animation: bg-animation .2s infinite;
    opacity: 0.8;
    visibility: visible;
    z-index:0
  }
  
  
  
  
  @keyframes bg-animation {
      0% { transform: translate(0,0) }
      10% { transform: translate(-5%,-5%) }
      20% { transform: translate(-10%,5%) }
      30% { transform: translate(5%,-10%) }
      40% { transform: translate(-5%,15%) }
      50% { transform: translate(-10%,5%) }
      60% { transform: translate(15%,0) }
      70% { transform: translate(0,10%) }
      80% { transform: translate(-15%,0) }
      90% { transform: translate(10%,5%) }
      100% { transform: translate(5%,0) }
  }
  
  
  
  
  
  
  
  .glitch {
    position: relative;
  }
  
  
  
  .line:not(:first-child) {
    position: absolute;
    top: 0;
    left: 0;
  }
  .line:nth-child(1) {
    -webkit-animation: clip 3000ms -300ms linear infinite, glitch1 500ms -832ms linear infinite;
            animation: clip 3000ms -300ms linear infinite, glitch1 500ms -832ms linear infinite;
  }
  @-webkit-keyframes glitch1 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(4px);
      color: #4E9A26;
    }
    90% {
      transform: translateX(0px);
      color: #AC1212;
    }
    95% {
      transform: translateX(2px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch1 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(4px);
      color: #1ebf74;
    }
    90% {
      transform: translateX(0px);
      color: #9253b3;
    }
    95% {
      transform: translateX(2px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  .line:nth-child(2) {
    -webkit-animation: clip 3000ms -600ms linear infinite, glitch2 500ms -889ms linear infinite;
            animation: clip 3000ms -600ms linear infinite, glitch2 500ms -889ms linear infinite;
  }
  @-webkit-keyframes glitch2 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(1px);
      color: #1068da;
    }
    90% {
      transform: translateX(-4px);
      color: #AC1212;
    }
    95% {
      transform: translateX(4px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch2 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(1px);
      color: #177caf;
    }
    90% {
      transform: translateX(-4px);
      color: #5ac9bd;
    }
    95% {
      transform: translateX(4px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  .line:nth-child(3) {
    -webkit-animation: clip 3000ms -900ms linear infinite, glitch3 500ms -454ms linear infinite;
            animation: clip 3000ms -900ms linear infinite, glitch3 500ms -454ms linear infinite;
  }
  @-webkit-keyframes glitch3 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(3px);
      color: #0c417e;
    }
    90% {
      transform: translateX(3px);
      color: #c111c7;
    }
    95% {
      transform: translateX(5px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch3 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(3px);
      color: #d0e500;
    }
    90% {
      transform: translateX(3px);
      color: #1ebf74;
    }
    95% {
      transform: translateX(5px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  .line:nth-child(4) {
    -webkit-animation: clip 3000ms -1200ms linear infinite, glitch4 500ms -35ms linear infinite;
            animation: clip 3000ms -1200ms linear infinite, glitch4 500ms -35ms linear infinite;
  }
  @-webkit-keyframes glitch4 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(2px);
      color: #12487d;
    }
    90% {
      transform: translateX(0px);
      color: #AC1212;
    }
    95% {
      transform: translateX(1px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch4 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(2px);
      color: #9253b3;
    }
    90% {
      transform: translateX(0px);
      color: #177caf;
    }
    95% {
      transform: translateX(1px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  .line:nth-child(5) {
    -webkit-animation: clip 3000ms -1500ms linear infinite, glitch5 500ms -788ms linear infinite;
            animation: clip 3000ms -1500ms linear infinite, glitch5 500ms -788ms linear infinite;
  }
  @-webkit-keyframes glitch5 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(3px);
      color: #4d269a;
    }
    90% {
      transform: translateX(3px);
      color: #AC1212;
    }
    95% {
      transform: translateX(5px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch5 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(3px);
      color: #5ac9bd;
    }
    90% {
      transform: translateX(3px);
      color: #d0e500;
    }
    95% {
      transform: translateX(5px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  .line:nth-child(6) {
    -webkit-animation: clip 3000ms -1800ms linear infinite, glitch6 500ms -340ms linear infinite;
            animation: clip 3000ms -1800ms linear infinite, glitch6 500ms -340ms linear infinite;
  }
  @-webkit-keyframes glitch6 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(-1px);
      color: #5a269a;
    }
    90% {
      transform: translateX(0px);
      color: #cc15b1;
    }
    95% {
      transform: translateX(5px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch6 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(-1px);
      color: #1ebf74;
    }
    90% {
      transform: translateX(0px);
      color: #9253b3;
    }
    95% {
      transform: translateX(5px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  .line:nth-child(7) {
    -webkit-animation: clip 3000ms -2100ms linear infinite, glitch7 500ms -800ms linear infinite;
            animation: clip 3000ms -2100ms linear infinite, glitch7 500ms -800ms linear infinite;
  }
  @-webkit-keyframes glitch7 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(0px);
      color: #113ac3;
    }
    90% {
      transform: translateX(-4px);
      color: #AC1212;
    }
    95% {
      transform: translateX(1px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch7 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(0px);
      color: #177caf;
    }
    90% {
      transform: translateX(-4px);
      color: #5ac9bd;
    }
    95% {
      transform: translateX(1px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  .line:nth-child(8) {
    -webkit-animation: clip 3000ms -2400ms linear infinite, glitch8 500ms -863ms linear infinite;
            animation: clip 3000ms -2400ms linear infinite, glitch8 500ms -863ms linear infinite;
  }
  @-webkit-keyframes glitch8 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(2px);
      color: #6138b8;
    }
    90% {
      transform: translateX(-1px);
      color: #a24ba2;
    }
    95% {
      transform: translateX(1px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch8 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(2px);
      color: #d0e500;
    }
    90% {
      transform: translateX(-1px);
      color: #1ebf74;
    }
    95% {
      transform: translateX(1px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  .line:nth-child(9) {
    -webkit-animation: clip 3000ms -2700ms linear infinite, glitch9 500ms -105ms linear infinite;
            animation: clip 3000ms -2700ms linear infinite, glitch9 500ms -105ms linear infinite;
  }
  @-webkit-keyframes glitch9 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(5px);
      color: #1e81b3;
    }
    90% {
      transform: translateX(4px);
      color: #ac128d;
    }
    95% {
      transform: translateX(1px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch9 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(5px);
      color: #9253b3;
    }
    90% {
      transform: translateX(4px);
      color: #177caf;
    }
    95% {
      transform: translateX(1px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  .line:nth-child(10) {
    -webkit-animation: clip 3000ms -3000ms linear infinite, glitch10 500ms -321ms linear infinite;
            animation: clip 3000ms -3000ms linear infinite, glitch10 500ms -321ms linear infinite;
  }
  @-webkit-keyframes glitch10 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(0px);
      color: #4E9A26;
    }
    90% {
      transform: translateX(1px);
      color: #e19264;
    }
    95% {
      transform: translateX(-4px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  @keyframes glitch10 {
    0% {
      transform: translateX(0);
    }
    80% {
      transform: translateX(0);
      color: #fff;
    }
    85% {
      transform: translateX(0px);
      color: #5ac9bd;
    }
    90% {
      transform: translateX(1px);
      color: #d0e500;
    }
    95% {
      transform: translateX(-4px);
      color: #fff;
    }
    100% {
      transform: translateX(0);
    }
  }
  
  @-webkit-keyframes clip {
    0% {
      -webkit-clip-path: polygon(0 100%, 100% 100%, 100% 120%, 0 120%);
              clip-path: polygon(0 100%, 100% 100%, 100% 120%, 0 120%);
    }
    100% {
      -webkit-clip-path: polygon(0 -20%, 100% -20%, 100% 0%, 0 0);
              clip-path: polygon(0 -20%, 100% -20%, 100% 0%, 0 0);
    }
  }
  
  @keyframes clip {
    0% {
      -webkit-clip-path: polygon(0 100%, 100% 100%, 100% 120%, 0 120%);
              clip-path: polygon(0 100%, 100% 100%, 100% 120%, 0 120%);
    }
    100% {
      -webkit-clip-path: polygon(0 -20%, 100% -20%, 100% 0%, 0 0);
              clip-path: polygon(0 -20%, 100% -20%, 100% 0%, 0 0);
    }
  }
  
  
  
  
  
  
  @media only screen and (min-width: 0px) and (max-width: 376px) {
  
    .hero__heading {
    font-size: 8.5rem;
    line-height: 0.5;
  }
  
  .hero__heading_subtitle {
    font-size: 90%;
    margin-top: 40%;
  }
  
  
  }
    
  @media only screen and (min-width: 376px) and (max-width: 576px) {
  
    .hero__heading {
    font-size: 10rem;
    line-height: 0.55;
    width:60%
  }
  
  .hero__heading_subtitle {
    font-size: 100%;
    margin-top: 30%;
  }
  
  }
  
  @media only screen and (min-width: 576px) and (max-width: 768px) {
  
    .hero__heading {
    font-size: 12rem;
    line-height: 0.55;
    width:60%
  }
  
  .hero__heading_subtitle {
    font-size: 100%;
    margin-top: 20%;
  }
  
  
  }
  
  @media only screen and (min-width: 768px) and (max-width: 992px) {
    .hero__heading {
    font-size: 9rem;
    line-height: 0.55;
  }
  
  .hero__heading_subtitle {
    font-size: 90%;
    margin-top: 10%;
  }
  
  
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