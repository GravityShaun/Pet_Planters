<template>
  <div class="artistry-wrapper">

    <!-- Hero Section -->
    <section id="hero" class="hero">
      <div class="container">
        <div class="row row-svg">
          <div class="col-12">
            <BigText :text="heroText" />
          </div>
        </div>
        <div class="row row-content">
          <div class="col-5 hero-left">
            <div class="hero-image">
              <img  ref="heroImageRef" src="~/assets/content/images/homePage/joel_1.png" alt="Portrait">
              <!-- <div class="texture-overlay"></div> -->
            </div>
          </div>
          <div class="hero-right">
            <h1 class="about_title" data-draw-line="service-about-joel-title">
              About Joel
              <span data-draw-line-box></span>
            </h1>
            <p class="about-text" ref="aboutTextRef">
                With over 15 years as Charleston's trusted handyman, I'm Joel. I deliver quality home repairs and renovations, from small fixes to large remodels.
            My goal is a safer, more comfortable home for you. As a local, I'm here for my community with scheduled maintenance and emergency repairs.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section id="gallery" class="gallery">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="gallery-wrapper">
              <div
                v-for="(item, index) in galleryItems"
                :key="index"
                class="gallery-item"
                :ref="el => { if (el) galleryItemRefs[index] = el }"
              >
                <img :src="item.src" :alt="item.alt">
              </div>
            </div>
            <div class="gallery-caption">
              <p>Hey, I’m Joel—your go-to handyman here in Charleston, SC, and yes… I do know how to handle a good piece of wood. Whether something’s squeaking, sagging, or just needs a little extra attention, I come fully equipped to tighten, caulk, and screw things back into place. I’ve got the right tools and I’m not afraid to use them—gently or with a little force, depending on the job. I like to keep things level, well-lubricated, and properly secured. It’s all about precision… and a little pleasure in the process. So if your house needs a little love, I’m always ready to slide in and fix it up.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { CustomEase } from 'gsap/CustomEase';
import BigText from '~/components/FontFx/BigText.vue';
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';

import joel1 from '~/assets/content/images/about/joel_1.jpg';
import joel2 from '~/assets/content/images/about/joel_2.jpg';
import joel3 from '~/assets/content/images/about/joel_3.jpg';
import joel4 from '~/assets/content/images/about/joel_4.jpg';
import joel5 from '~/assets/content/images/about/joel_5.jpg';
import joel6 from '~/assets/content/images/about/joel_6.jpg';

const galleryItems = ref([
  { src: joel1, alt: 'Joel working on a project' },
  { src: joel2, alt: 'Another project by Joel' },
  { src: joel3, alt: 'Joel fixing something' },
  { src: joel4, alt: 'Joel and a happy client' },
  { src: joel5, alt: 'Finished work by Joel' },
  { src: joel6, alt: 'Joel on site' },
]);

// Refs for DOM elements
const heroImageRef = ref(null);
const aboutTextRef = ref(null);
const galleryItemRefs = ref([]);

const heroText = "HANDY JOEL";

const { initUnderlineAnimation } = useUnderlineAnimation();

onMounted(async () => {
  await nextTick();

  gsap.registerPlugin(ScrollTrigger, CustomEase);

  // Custom eases
  CustomEase.create("verticalEase", "0.4, 0, 0.2, 1");
  CustomEase.create("blurEase", "0.65, 0, 0.35, 1");
  if (!CustomEase.get("svgEase")) {
    CustomEase.create("svgEase", "0.25, 0.1, 0.25, 1");
  }


  // Set initial state for hero image
  if (heroImageRef.value) {
    gsap.set(heroImageRef.value, {
      scale: 0.8,
      opacity: 0,
      filter: "blur(4px)",
      y: 50
    });

    // Animate hero image on mount with 500ms delay
    gsap.to(heroImageRef.value, {
      scale: 1,
      opacity: 1,
      filter: "blur(0px)",
      y: 0,
      duration: 0.8,
      ease: "blurEase",
      delay: 0.8
    });
  }

  gsap.to(aboutTextRef.value, {
    scrollTrigger: {
      trigger: ".hero",
      start: "top bottom",
      end: "center center",
      scrub: true
    },
    y: 0,
    opacity: 1,
    filter: "blur(0px)",
    duration: 1,
    ease: "verticalEase"
  });

  // Gallery staggered animation
  const galleryImages = galleryItemRefs.value.map(item => item.querySelector('img')).filter(Boolean);

  gsap.set(galleryImages, { clipPath: "inset(100% 0 0 0)", opacity: 0, y: 40 });

  gsap.timeline({
    scrollTrigger: {
      trigger: ".gallery",
      start: "top 80%",
      end: "bottom top",
      toggleActions: "play none none reverse"
    }
  })
  .to(galleryImages, {
    clipPath: "inset(0% 0 0 0)",
    opacity: 1,
    y: 0,
    duration: 1.2,
    ease: "verticalEase",
    stagger: 0.15
  });

  // Initialize underline animation
  setTimeout(() => {
    if (typeof window !== 'undefined') {
      initUnderlineAnimation('[data-draw-line="service-about-joel-title"]', {
        autoAnimate: true,
        duration: 1,
        ease: "power2.inOut",
        delay: 0.25
      });

      // Force red color after animation initializes
      setTimeout(() => {
        const element = document.querySelector('[data-draw-line="service-about-joel-title"]');
        const svg = element?.querySelector('svg');
        const path = svg?.querySelector('path');
        if (path) {
          path.setAttribute('stroke', '#fd3d13');
          path.style.stroke = '#fd3d13';
          path.style.strokeWidth = '8px';
        }
      }, 100);
    }
  }, 100);

});

onBeforeUnmount(() => {
  // Kill all ScrollTriggers to prevent memory leaks
  ScrollTrigger.getAll().forEach(trigger => trigger.kill());
});
</script>

<style>
:root {
  --accent-color: #ffd700;
  --offwhite: #f5f5f0;
}

.artistry-wrapper {
  font-weight: 700;
  font-size: 1.8rem;
  letter-spacing: -0.02em;
  overflow-x: hidden;
  position: relative;
}



/* Grid System */
.container {
  width: 100%;
  max-width: 100%;
  margin: 0 auto;
  padding: 0 3vw;
  height: 100%;
}

.row {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1rem;
  width: 90%;
  margin-left: 5%;
}

.row-svg {
  margin-top: 10vh;
  margin-bottom: 12vh;
}

.row-content {
  height: calc(100% - 14rem);
  align-items: end;
  margin-bottom: 2rem;
}

.col-1 { grid-column: span 1; }
.col-2 { grid-column: span 2; }
.col-3 { grid-column: span 3; }
.col-4 { grid-column: span 4; }
.col-5 { grid-column: span 5; }
.col-6 { grid-column: span 6; }
.col-7 { grid-column: span 7; }
.col-8 { grid-column: span 8; }
.col-9 { grid-column: span 9; }
.col-10 { grid-column: span 10; }
.col-11 { grid-column: span 11; }
.col-12 { grid-column: span 12; }




/* Hero Section */
.hero {
  min-height: 100vh;
  display: flex;
}

.hero-left {
  position: relative;
}

.hero-image {
  width: 90%;
  overflow: hidden;
  position: relative;
}

.hero-image img {
  width: 100%;
  height: auto;
  object-fit: cover;
  position: relative;
  z-index: 1;
  display: block;
}



.hero-right {
  grid-column: 8 / -1;
  text-align: right;
  overflow: hidden;
}

.about-text {
  font-size: 80%;
  line-height: 1.6;
  text-transform: none;
  opacity: 0;
  transform: translateY(5rem);
  filter: blur(5px);
  color: #293b2e;
  margin-top: 12%
}

/* Gallery Section */
.gallery {
  min-height: 80vh;
  display: flex;
  overflow: hidden;
}

.gallery-wrapper {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 10vh;
  margin-top:5vh;
  overflow: visible;
}

.gallery-item {
  flex: 0 0 25rem;
  height: 35rem;
  overflow: hidden;
  position: relative;
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}



.gallery-caption {
  max-width: 80rem;
  margin: 0 auto;
  padding: 2rem;
  font-size: 1.4rem;
  line-height: 1.6;
  text-transform: none;
  opacity: 1;
  transform: translateY(-2rem);
  color: #293b2e;
}

    .about_title{
    margin-top: 25%;
    font-size: 3.5rem;
    font-weight: 700;
    color: #293b2e;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
    position: relative;
    overflow: visible;
}

.about_title [data-draw-line-box] {
    display: block;
    width: 100%;
    height: 1px !important;
    margin-top: -15px;
}

.about_title [data-draw-line-box] svg {
    width: 100% !important;
    height: 0px !important;
    display: block !important;
    margin-left: 48%;
}

.about_title [data-draw-line-box] svg path {
    stroke: #fd3d13 !important;
    stroke-width: 8px !important;
    fill: none !important;
}
    
</style>
