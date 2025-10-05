<template>
  <div class="hero-big-text-container" ref="textContainerRef">
    <h1 class="hero-big-text">
      <span v-for="(char, i) in textArray" :key="i" class="hero-letter" :ref="el => { if (el) letterRefs[i] = el }">{{ char === ' ' ? '&nbsp;' : char }}</span>
    </h1>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick, computed } from 'vue';
import { useIntersectionObserver } from '@vueuse/core';
import { gsap } from 'gsap';
import { CustomEase } from 'gsap/CustomEase';

const props = defineProps({
  text: {
    type: String,
    required: true
  }
});

const textContainerRef = ref(null);
const letterRefs = ref([]);
const textArray = computed(() => props.text.split(""));

const isMounted = ref(false);
const isIntersectingVar = ref(false);

const { stop: stopObserver } = useIntersectionObserver(
  textContainerRef,
  ([{ isIntersecting }]) => {
    isIntersectingVar.value = isIntersecting;
    if (isIntersecting) {
      if (!isMounted.value) {
        setTimeout(() => {
          animateHeroText();
          isMounted.value = true;
        }, 600);
      } else {
        animateHeroText();
      }
    } else {
      gsap.set(letterRefs.value, { opacity: 0, y: 60 });
    }
  },
  { threshold: 0.1 }
);

function animateHeroText() {
  gsap.set(letterRefs.value, { opacity: 0, y: 60 });
  gsap.to(letterRefs.value, {
    opacity: 1,
    y: 0,
    duration: 1,
    ease: "svgEase",
    stagger: 0.07,
    onUpdate: () => {
      if (!isIntersectingVar.value) {
        gsap.set(letterRefs.value, { opacity: 0, y: 60 });
      }
    }
  });
}

onMounted(async () => {
  await nextTick();
  gsap.registerPlugin(CustomEase);
  if (!CustomEase.get("svgEase")) {
    CustomEase.create("svgEase", "0.25, 0.1, 0.25, 1");
  }

  gsap.set(letterRefs.value, { opacity: 0, y: 60 });

  setTimeout(() => {
    if (isIntersectingVar.value) {
      animateHeroText();
    }
  }, 1000);
});

onBeforeUnmount(() => {
  stopObserver();
});
</script>

<style>
.hero-big-text-container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.hero-big-text {
  font-size: 14vw;
  font-weight: 900;
  letter-spacing: 0em;
  color: #293b2e;
  text-transform: uppercase;
  line-height: 1;
  text-align: center;
  position: relative;
  z-index: 1;
}

.hero-letter {
  display: inline-block;
  will-change: transform, opacity;
}
</style> 