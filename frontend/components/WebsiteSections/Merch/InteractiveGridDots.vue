<template>
  <section class="section-resource">
    <div class="paperOverlay"></div>
    <div class="dots-wrap">
      <div ref="dotsContainer" class="dots-container">
        <!-- Dots will be dynamically generated -->
      </div>
    </div>
  <div class="logo">
    <img src="~/assets/content/images/joel_logo_2.png" alt="Logo" />
  </div>
  </section>

</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'

const { $gsap: gsap } = useNuxtApp()

const dotsContainer = ref(null)
let dots = []
let dotCenters = []
let lastTime = 0
let lastX = 0
let lastY = 0

// Configuration
const colors = { base: "#08342a", active: "#ff0000" }
const threshold = 150
const speedThreshold = 100
const shockRadius = 250
const shockPower = 5
const maxSpeed = 5000
const centerHole = true

function buildGrid() {
  if (!dotsContainer.value) {
    console.log('Dots container not found')
    return
  }
  
  console.log('Building grid...')
  dotsContainer.value.innerHTML = ""
  dots = []
  dotCenters = []

  // Use a fixed dot size instead of relying on font-size
  const dotPx = 15 // Fixed dot size in pixels
  const gapPx = 40 // Fixed gap size in pixels
  const contW = dotsContainer.value.clientWidth
  const contH = dotsContainer.value.clientHeight

  console.log('Container dimensions:', contW, contH)

  const cols = Math.floor((contW + gapPx) / (dotPx + gapPx))
  const rows = Math.floor((contH + gapPx) / (dotPx + gapPx))
  const total = cols * rows

  console.log('Grid dimensions:', cols, rows, total)

  const holeCols = centerHole ? (cols % 2 === 0 ? 8 : 9) : 0
  const holeRows = centerHole ? (rows % 2 === 0 ? 8 : 9) : 0
  const startCol = (cols - holeCols) / 2
  const startRow = (rows - holeRows) / 2

  for (let i = 0; i < total; i++) {
    const row = Math.floor(i / cols)
    const col = i % cols
    const isHole = centerHole &&
      row >= startRow && row < startRow + holeRows &&
      col >= startCol && col < startCol + holeCols

    const d = document.createElement("div")
    d.classList.add("dot")

    if (isHole) {
      d.style.visibility = "hidden"
      d._isHole = true
    } else {
      // Set initial styles directly on the element
      d.style.width = `${dotPx}px`
      d.style.height = `${dotPx}px`
      d.style.borderRadius = '50%'
      d.style.backgroundColor = colors.base
      d.style.position = 'absolute'
      d.style.left = `${col * (dotPx + gapPx)}px`
      d.style.top = `${row * (dotPx + gapPx)}px`
      d._inertiaApplied = false
    }

    dotsContainer.value.appendChild(d)
    dots.push(d)
  }

  console.log('Created dots:', dots.length)

  requestAnimationFrame(() => {
    dotCenters = dots
      .filter(d => !d._isHole)
      .map(d => {
        const r = d.getBoundingClientRect()
        return {
          el: d,
          x: r.left + window.scrollX + r.width / 2,
          y: r.top + window.scrollY + r.height / 2
        }
      })
    console.log('Dot centers:', dotCenters.length)
  })
}

function handleMouseMove(e) {
  const now = performance.now()
  const dt = now - lastTime || 16
  let dx = e.pageX - lastX
  let dy = e.pageY - lastY
  let vx = dx / dt * 1000
  let vy = dy / dt * 1000
  let speed = Math.hypot(vx, vy)

  if (speed > maxSpeed) {
    const scale = maxSpeed / speed
    vx *= scale
    vy *= scale
    speed = maxSpeed
  }

  lastTime = now
  lastX = e.pageX
  lastY = e.pageY

  requestAnimationFrame(() => {
    dotCenters.forEach(({ el, x, y }) => {
      const dist = Math.hypot(x - e.pageX, y - e.pageY)
      const t = Math.max(0, 1 - dist / threshold)
      const col = gsap.utils.interpolate(colors.base, colors.active, t)
      gsap.set(el, { backgroundColor: col })

      if (speed > speedThreshold && dist < threshold && !el._inertiaApplied) {
        el._inertiaApplied = true
        const pushX = (x - e.pageX) + vx * 0.005
        const pushY = (y - e.pageY) + vy * 0.005

        gsap.to(el, {
          inertia: { x: pushX, y: pushY, resistance: 750 },
          onComplete() {
            gsap.to(el, {
              x: 0,
              y: 0,
              duration: 1.5,
              ease: "elastic.out(1,0.75)"
            })
            el._inertiaApplied = false
          }
        })
      }
    })
  })
}

function handleClick(e) {
  dotCenters.forEach(({ el, x, y }) => {
    const dist = Math.hypot(x - e.pageX, y - e.pageY)
    if (dist < shockRadius && !el._inertiaApplied) {
      el._inertiaApplied = true
      const falloff = Math.max(0, 1 - dist / shockRadius)
      const pushX = (x - e.pageX) * shockPower * falloff
      const pushY = (y - e.pageY) * shockPower * falloff

      gsap.to(el, {
        inertia: { x: pushX, y: pushY, resistance: 750 },
        onComplete() {
          gsap.to(el, {
            x: 0,
            y: 0,
            duration: 1.5,
            ease: "elastic.out(1,0.75)"
          })
          el._inertiaApplied = false
        }
      })
    }
  })
}

onMounted(async () => {
  await nextTick()
  buildGrid()
  window.addEventListener("resize", buildGrid)
  window.addEventListener("mousemove", handleMouseMove)
  window.addEventListener("click", handleClick)
})

onUnmounted(() => {
  window.removeEventListener("resize", buildGrid)
  window.removeEventListener("mousemove", handleMouseMove)
  window.removeEventListener("click", handleClick)
})
</script>

<style scoped>
/* ------- Osmo [https://osmo.supply/] ------- */
/* Osmo UI: https://slater.app/10324/23333.css */

.section-resource {
  padding: 4em;
  justify-content: center;
  align-items: center;
  height: 100svh;
  display: flex;
  position: relative;
  background-color: #fff;
  color: #08342a;
  font-size: 1vw;
  margin: 0;
  padding: 0;
  overscroll-behavior: none;
  min-height: 100%;
}

.osmo-icon__link {
  color: currentColor;
  text-decoration: none;
  position: absolute;
  cursor: pointer;
}

.logo {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -55%);
  width: 30%;
  height: 30%;
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.osmo-icon-svg {
  width: 10em;
}

.dots-wrap {
  width: 100%;
  height: 100%;
  position: relative;
}

.dots-container {
  pointer-events: none;
  position: absolute;
  inset: 0em;
  width: 100%;
  height: 100%;
  /* Temporary border for debugging */
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.dot {
  will-change: transform, background-color;
  transform-origin: center;
  background-color: #245e51;
  border-radius: 50%;
  position: absolute;
  transform: translate(0);
  display: block;
}

.osmo-credits {
  z-index: 999;
  pointer-events: none;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 4em;
  padding: 1em;
  display: flex;
  position: fixed;
  bottom: 0;
  left: 0;
}

.osmo-credits__p {
  pointer-events: auto;
  color: #efeeec80;
  text-align: center;
  margin: 0;
  font-family: "PP Neue Montreal", Arial, sans-serif;
  font-size: 1.125em;
  font-weight: 500;
  line-height: 1.3;
}

.osmo-credits__p-a {
  color: #efeeec;
  text-decoration: none;
}

.osmo-credits__p-a:hover {
  text-decoration: underline;
}

@font-face {
  font-family: "PP Neue Montreal";
  src: url("https://cdn.prod.website-files.com/6819ed8312518f61b84824df/6819ed8312518f61b84825ba_PPNeueMontreal-Medium.woff2")
    format("woff2");
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}

/* Custom cursor styles */
.section-resource {
  cursor: url("https://cdn.prod.website-files.com/6708f85ff3d3cba6aff436fb/671251b239d7aeb290a31ac5_cursor-default%402x.svg") 2 0, auto;
}

.osmo-icon__link {
  cursor: url("https://cdn.prod.website-files.com/6708f85ff3d3cba6aff436fb/671251b212e6b71494aa67ff_cursor-pointer%402x.svg") 12 0, pointer;
}
</style>
