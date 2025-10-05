import { gsap } from 'gsap'
import { InertiaPlugin } from 'gsap/InertiaPlugin'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

export default defineNuxtPlugin(() => {
  // Register plugins for interactive animations
  gsap.registerPlugin(InertiaPlugin, ScrollTrigger)

  if (process.client) {
    // Some plugins need to be registered only on the client
    // gsap.registerPlugin(SplitText, ...)
  }

  return {
    provide: {
      gsap
    }
  }
})