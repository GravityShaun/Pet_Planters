<template>
    <div class="slider_main_container">
          <h1 class="slider_title">{{ title }}</h1>
    <div class="slider-container" ref="sliderContainerImage">
        <div class="image_card" v-for="(testimonial, index) in testimonials" :key="index" :class="`wood-${testimonial.woodType}`">
          <div class="slider_container_outer">
                          <div class="paperOverlayTestamonial" :style="getPaperOverlayStyle(index)"></div>
          <div class="image_container">
            <div class="image_background"></div>
            <div class="image_container_inner">
            <img :src="testimonial.image" :alt="testimonial.name" class="logo">
            </div>
            </div>
            <div class="info_container">
                <h1 class="info_title">
                  <span v-for="star in 5" :key="star" class="star" :class="{ 'filled': star <= testimonial.rating }">★</span>
                </h1>
                <h1 class="info_subtitle" :data-draw-line="`subtitle-${componentId}-${index}`">
                  {{ testimonial.name }}
                  <span data-draw-line-box></span>
                </h1>
                <p class="info_text">{{ testimonial.testimonial }}</p>
            </div>
        </div>
      </div>
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue';
import gsap from 'gsap';
import { Draggable } from 'gsap/Draggable';
import { InertiaPlugin } from 'gsap/InertiaPlugin';
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';

gsap.registerPlugin(Draggable, InertiaPlugin);

const props = defineProps(['direction', 'title']);

// Testimonials data with Unsplash images
const testimonials = ref([
  {
    name: "Sarah Johnson",
    workType: "Cat Planter",
    testimonial: "These 3D printed planters are absolutely adorable! The quality is outstanding and my succulents look perfect in them. Highly recommend!",
    image: "https://images.unsplash.com/photo-1754264546091-fcbad3feafbe?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHx0b3BpYy1mZWVkfDR8dG93SlpGc2twR2d8fGVufDB8fHx8fA%3D%3D",
    woodType: 1,
    rating: 5
  },
  {
    name: "Michael Chen",
    workType: "Dog Planter",
    testimonial: "The print quality on these planters is exceptional. Love the unique pet designs - they add so much personality to my office space!",
    image: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=face",
    woodType: 2,
    rating: 5
  },
  {
    name: "Emma Rodriguez",
    workType: "Bunny Planter",
    testimonial: "Great quality 3D print with smooth finish. The drainage holes work perfectly. My herbs are thriving in these cute planters!",
    image: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop&crop=face",
    woodType: 3,
    rating: 4
  },
  {
    name: "David Thompson",
    workType: "Elephant Planter",
    testimonial: "Sturdy and well-made 3D printed planters. The elephant design is charming and the size is perfect for small plants. Very satisfied!",
    image: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop&crop=face",
    woodType: 4,
    rating: 5
  },
  {
    name: "Lisa Park",
    workType: "Owl Planter",
    testimonial: "These pet planters are the cutest thing ever! The 3D print quality exceeded my expectations. Makes a great gift too!",
    image: "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=400&h=400&fit=crop&crop=face",
    woodType: 5,
    rating: 5
  },
  {
    name: "Robert Martinez",
    workType: "Bear Planter",
    testimonial: "Nice planter but the print lines are slightly visible up close. Still looks great from normal viewing distance and holds plants well.",
    image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face",
    woodType: 6,
    rating: 4
  },
  {
    name: "Jennifer Wilson",
    workType: "Fox Planter",
    testimonial: "Absolutely in love with these 3D printed pet planters! The detail is incredible and they're the perfect conversation starter. Ordering more!",
    image: "https://images.unsplash.com/photo-1445053023192-8d45cb66099d?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    woodType: 1,
    rating: 5
  },
  {
    name: "James Anderson",
    workType: "Turtle Planter",
    testimonial: "Decent planter but smaller than I expected. The print quality is good though and it works fine for tiny succulents.",
    image: "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=400&h=400&fit=crop&crop=face",
    woodType: 2,
    rating: 3
  },
  {
    name: "Maria Garcia",
    workType: "Penguin Planter",
    testimonial: "The penguin planter is so cute! High-quality 3D print with vibrant colors. My desk plants have never looked better. Five stars!",
    image: "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&h=400&fit=crop&crop=face",
    woodType: 3,
    rating: 5
  },
  {
    name: "Kevin Brown",
    workType: "Dinosaur Planter",
    testimonial: "My kids love the dinosaur planter! Well-crafted and durable. Great way to get them interested in caring for plants. Would buy again.",
    image: "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400&h=400&fit=crop&crop=face",
    woodType: 4,
    rating: 4
  },
  {
    name: "Amanda Taylor",
    workType: "Hedgehog Planter",
    testimonial: "Beautiful 3D printed planter with amazing attention to detail. The hedgehog design is adorable and the quality is top-notch. Worth every penny!",
    image: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=400&fit=crop&crop=face",
    woodType: 5,
    rating: 5
  },
  {
    name: "Ryan Davis",
    workType: "Sloth Planter",
    testimonial: "The sloth planter is perfect for my workspace! Excellent print quality and the design makes me smile every day. Shipping was fast too!",
    image: "https://images.unsplash.com/photo-1589571894960-20bbe2828d0a?q=80&w=686&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    woodType: 6,
    rating: 5
  },
  {
    name: "Nicole White",
    workType: "Llama Planter",
    testimonial: "These llama planters are fantastic! The 3D printing is flawless and they're so unique. Bought several as gifts and everyone loved them!",
    image: "https://plus.unsplash.com/premium_photo-1690587673708-d6ba8a1579a5?q=80&w=679&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    woodType: 1,
    rating: 5
  },
  {
    name: "Christopher Lee",
    workType: "Frog Planter",
    testimonial: "The planter arrived with some rough edges and the color wasn't quite what I expected. It works but quality could be better.",
    image: "https://images.unsplash.com/photo-1507591064344-4c6ce005b128?w=400&h=400&fit=crop&crop=face",
    woodType: 2,
    rating: 2
  },
  {
    name: "Stephanie Clark",
    workType: "Panda Planter",
    testimonial: "Really cute panda design and good quality print. Only minor imperfections but overall very happy with the purchase. Great for air plants!",
    image: "https://images.unsplash.com/photo-1557296387-5358ad7997bb?w=400&h=400&fit=crop&crop=face",
    woodType: 3,
    rating: 4
  },
  {
    name: "Daniel Miller",
    workType: "Giraffe Planter",
    testimonial: "Not impressed with the quality. The print is rough and the planter feels flimsy. Doesn't match the photos shown online.",
    image: "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=400&h=400&fit=crop&crop=face",
    woodType: 4,
    rating: 1
  }
]);

// const rando = ref(randomFromInterval(.025, .2))
const rando = ref(.05)

const sliderContainerImage = ref(null);
// let draggableInstance = null;
let loopAnimation = null;
let activeElement;

// Add mouse over effect for cards
let isHovered = false;
let mouseX = 0;
let mouseY = 0;
let cardX = 0; 
let cardY = 0;

const setupHorizontalLoop = () => {
  const items = sliderContainerImage.value.children;
  loopAnimation = horizontalLoop(items, {
    speed: rando.value, // 100 pixels per second
    draggable: true,
    repeat: -1,
    snap: 0, // Snapping to nearest 0.1% for smooth transitions
    reversed: true,
    paused: false, 
    center:false,
    paddingRight: '0px'
  });
  if (direction_move.value === 1) {
    loopAnimation.reverse();
      } else {
        loopAnimation.play();
      }
};

const direction_move = ref(null)
const { initUnderlineAnimation } = useUnderlineAnimation();

// Generate unique component instance ID
const componentId = ref(`slider-${Math.random().toString(36).substr(2, 9)}`);

onMounted(() => {
    direction_move.value = props.direction
    setTimeout(() => {
        setupHorizontalLoop();
        
        // Initialize underline animations for all subtitles
        testimonials.value.forEach((_, index) => {
          const selector = `[data-draw-line="subtitle-${componentId.value}-${index}"]`;
          initUnderlineAnimation(selector, {
            autoAnimate: true,
            duration: 1,
            ease: "power2.inOut",
            delay: 0.25 + (index * 0.1) // Stagger the animations slightly
          });
          
          // Force red color after animation initializes
          setTimeout(() => {
            const element = document.querySelector(selector);
            const svg = element?.querySelector('svg');
            const path = svg?.querySelector('path');
            if (path) {
              path.setAttribute('stroke', '#56badb');
              path.style.stroke = '#56badb';
              path.style.strokeWidth = '6px';
            }
          }, 100);
        });
    }, 200);

    const cards = document.querySelectorAll('.image_card');

    cards.forEach((card) => {
      card.addEventListener('mouseenter', () => {
        isHovered = true;
        const rect = card.getBoundingClientRect();
        cardX = rect.left;
        cardY = rect.top;
      });

      card.addEventListener('mouseleave', () => {
        isHovered = false;
        gsap.to(card, {
          x: 0,
          y: 0,
          duration: 2,
          ease: 'elastic.out(1, 0.3)'
        });
      });

      card.addEventListener('mousemove', (e) => {
        if (!isHovered) return;

        mouseX = e.clientX;
        mouseY = e.clientY;

        const moveX = (mouseX - cardX - card.offsetWidth / 2) * 0.15;
        const moveY = (mouseY - cardY - card.offsetHeight / 2) * 0.15;

        gsap.to(card, {
          x: moveX,
          y: moveY,
          duration: 0.3,
          ease: 'power2.out'
        });
      });
    });
});

onUnmounted(() => {
  if (loopAnimation) loopAnimation.kill();
});

function randomFromInterval(min, max) { // min and max included 
  return Math.random() * (max - min) + min;
}

function getPaperOverlayStyle(index) {
  // Use index as seed for consistent randomization per item
  const seed = index * 137.5; // Using a prime-like number for better distribution
  const pseudoRandom1 = (Math.sin(seed) + 1) / 2;
  const pseudoRandom2 = (Math.sin(seed * 1.3) + 1) / 2;
  const pseudoRandom5 = (Math.sin(seed * 2.7) + 1) / 2;
  
  const rotation = (pseudoRandom2 - 0.5) * 5; // -5deg to 5deg
  
  // Calculate minimum size needed to cover container when rotated
  // For a rectangle with rotation, we need size = diagonal * sqrt(2) to ensure full coverage
  // With max rotation of 5deg, we need approximately 155% to cover corners
  // Adding extra buffer for safety and variation
  const minSize = 180; // Base minimum to handle rotation
  const backgroundSize = minSize + pseudoRandom1 * 150; // 160% to 260%
  
  // Random position
  const positions = ['top left', 'top center', 'top right', 'center left', 'center center', 'center right', 'bottom left', 'bottom center', 'bottom right'];
  const positionIndex = Math.floor(pseudoRandom5 * positions.length);
  const position = positions[positionIndex];
  
  //flip horizontal or vertical or both or none
  const flip = ['horizontal', 'vertical', 'both', 'none'];
  const flipIndex = Math.floor(pseudoRandom5 * flip.length);
  const flipDirection = flip[flipIndex];
  
  return {
    backgroundSize: `${backgroundSize}%`,
    backgroundPosition: position,
    transform: `rotate(${rotation}deg) ${flipDirection}`
  };
}

function random_width() {
  const widthPercentage = randomFromInterval(40, 60);
  return `${widthPercentage}vw`;
}

function horizontalLoop(items, config) {
  let timeline;
  items = gsap.utils.toArray(items);
  config = config || {};
  gsap.context(() => { // use a context so that if this is called from within another context or a gsap.matchMedia(), we can perform proper cleanup like the "resize" event handler on the window
    let onChange = config.onChange,
      lastIndex = 0,
      tl = gsap.timeline({repeat: config.repeat, onUpdate: onChange && function() {
          let i = tl.closestIndex();
          if (lastIndex !== i) {
            lastIndex = i;
            onChange(items[i], i);
          }
        }, paused: config.paused, defaults: {ease: "none"}, onReverseComplete: () => tl.totalTime(tl.rawTime() + tl.duration() * 100)}),
      length = items.length,
      startX = items[0].offsetLeft,
      times = [],
      widths = [],
      spaceBefore = [],
      xPercents = [],
      curIndex = 0,
      indexIsDirty = false,
      center = config.center,
      pixelsPerSecond = (config.speed || 1) * 1000,
      snap = config.snap === false ? v => v : gsap.utils.snap(config.snap || 1), // some browsers shift by a pixel to accommodate flex layouts, so for example if width is 20% the first element's width might be 242px, and the next 243px, alternating back and forth. So we snap to 5 percentage points to make things look more natural
      timeOffset = 0,
      container = center === true ? items[0].parentNode : gsap.utils.toArray(center)[0] || items[0].parentNode,
      totalWidth,
      getTotalWidth = () => items[length-1].offsetLeft + xPercents[length-1] / 100 * widths[length-1] - startX + spaceBefore[0] + items[length-1].offsetWidth * gsap.getProperty(items[length-1], "scaleX") + (parseFloat(config.paddingRight) || 0),
      populateWidths = () => {
        let b1 = container.getBoundingClientRect(), b2;
        items.forEach((el, i) => {
          widths[i] = parseFloat(gsap.getProperty(el, "width", "px"));
          xPercents[i] = snap(parseFloat(gsap.getProperty(el, "x", "px")) / widths[i] * 100 + gsap.getProperty(el, "xPercent"));
          b2 = el.getBoundingClientRect();
          spaceBefore[i] = b2.left - (i ? b1.right : b1.left);
          b1 = b2;
        });
        gsap.set(items, { // convert "x" to "xPercent" to make things responsive, and populate the widths/xPercents Arrays to make lookups faster.
          xPercent: i => xPercents[i]
        });
        totalWidth = getTotalWidth();
      },
      timeWrap,
      populateOffsets = () => {
        timeOffset = center ? tl.duration() * (container.offsetWidth / 2) / totalWidth : 0;
        center && times.forEach((t, i) => {
          times[i] = timeWrap(tl.labels["label" + i] + tl.duration() * widths[i] / 2 / totalWidth - timeOffset);
        });
      },
      getClosest = (values, value, wrap) => {
        let i = values.length,
          closest = 1e10,
          index = 0, d;
        while (i--) {
          d = Math.abs(values[i] - value);
          if (d > wrap / 2) {
            d = wrap - d;
          }
          if (d < closest) {
            closest = d;
            index = i;
          }
        }
        return index;
      },
      populateTimeline = () => {
        let i, item, curX, distanceToStart, distanceToLoop;
        tl.clear();
        for (i = 0; i < length; i++) {
          item = items[i];
          curX = xPercents[i] / 100 * widths[i];
          distanceToStart = item.offsetLeft + curX - startX + spaceBefore[0];
          distanceToLoop = distanceToStart + widths[i] * gsap.getProperty(item, "scaleX");
          tl.to(item, {xPercent: snap((curX - distanceToLoop) / widths[i] * 100), duration: distanceToLoop / pixelsPerSecond}, 0)
            .fromTo(item, {xPercent: snap((curX - distanceToLoop + totalWidth) / widths[i] * 100)}, {xPercent: xPercents[i], duration: (curX - distanceToLoop + totalWidth - curX) / pixelsPerSecond, immediateRender: false}, distanceToLoop / pixelsPerSecond)
            .add("label" + i, distanceToStart / pixelsPerSecond);
          times[i] = distanceToStart / pixelsPerSecond;
        }
        timeWrap = gsap.utils.wrap(0, tl.duration());
      },
      refresh = (deep) => {
        let progress = tl.progress();
        tl.progress(0, true);
        populateWidths();
        deep && populateTimeline();
        populateOffsets();
        deep && tl.draggable ? tl.time(times[curIndex], true) : tl.progress(progress, true);
      },
      onResize = () => refresh(true),
      proxy;
    gsap.set(items, {x: 0});
    populateWidths();
    populateTimeline();
    populateOffsets();
    window.addEventListener("resize", onResize);
    function toIndex(index, vars) {
      vars = vars || {};
      (Math.abs(index - curIndex) > length / 2) && (index += index > curIndex ? -length : length); // always go in the shortest direction
      let newIndex = gsap.utils.wrap(0, length, index),
        time = times[newIndex];
      if (time > tl.time() !== index > curIndex && index !== curIndex) { // if we're wrapping the timeline's playhead, make the proper adjustments
        time += tl.duration() * (index > curIndex ? 1 : -1);
      }
      if (time < 0 || time > tl.duration()) {
        vars.modifiers = {time: timeWrap};
      }
      curIndex = newIndex;
      vars.overwrite = true;
      gsap.killTweensOf(proxy);    
      return vars.duration === 0 ? tl.time(timeWrap(time)) : tl.tweenTo(time, vars);
    }
    tl.toIndex = (index, vars) => toIndex(index, vars);
    tl.closestIndex = setCurrent => {
      let index = getClosest(times, tl.time(), tl.duration());
      if (setCurrent) {
        curIndex = index;
        indexIsDirty = false;
      }
      return index;
    };
    tl.current = () => indexIsDirty ? tl.closestIndex(true) : curIndex;
    tl.next = vars => toIndex(tl.current()+1, vars);
    tl.previous = vars => toIndex(tl.current()-1, vars);
    tl.times = times;
    tl.progress(1, true).progress(0, true); // pre-render for performance
    if (config.reversed) {
      tl.vars.onReverseComplete();
      tl.reverse();
    }
    if (config.draggable && typeof(Draggable) === "function") {
      proxy = document.createElement("div")
      let wrap = gsap.utils.wrap(0, 1),
        ratio, startProgress, draggable, dragSnap, lastSnap, initChangeX, wasPlaying,
        align = () => tl.progress(wrap(startProgress + (draggable.startX - draggable.x) * ratio)),
        syncIndex = () => tl.closestIndex(true);
      typeof(InertiaPlugin) === "undefined" && console.warn("InertiaPlugin required for momentum-based scrolling and snapping. https://greensock.com/club");
      draggable = Draggable.create(proxy, {
        trigger: items[0].parentNode,
        type: "x",
        onPressInit() {
          let x = this.x;
          gsap.killTweensOf(tl);
          wasPlaying = !tl.paused();
          tl.pause();
          startProgress = tl.progress();
          refresh();
          ratio = 1 / totalWidth;
          initChangeX = (startProgress / -ratio) - x;
          gsap.set(proxy, {x: startProgress / -ratio});
        },
        onDrag: align,
        onThrowUpdate: align,
        overshootTolerance: 0,
        inertia: true,
        snap(value) {
          //note: if the user presses and releases in the middle of a throw, due to the sudden correction of proxy.x in the onPressInit(), the velocity could be very large, throwing off the snap. So sense that condition and adjust for it. We also need to set overshootTolerance to 0 to prevent the inertia from causing it to shoot past and come back
          if (Math.abs(startProgress / -ratio - this.x) < 10) {
            return lastSnap + initChangeX
          }
          let time = -(value * ratio) * tl.duration(),
            wrappedTime = timeWrap(time),
            snapTime = times[getClosest(times, wrappedTime, tl.duration())],
            dif = snapTime - wrappedTime;
          Math.abs(dif) > tl.duration() / 2 && (dif += dif < 0 ? tl.duration() : -tl.duration());
          lastSnap = (time + dif) / tl.duration() / -ratio;
          return lastSnap;
        },
        onRelease() {
          syncIndex();
          draggable.isThrowing && (indexIsDirty = true);
        },
        onThrowComplete: () => {
          syncIndex();
          wasPlaying && tl.play();
          const direction = draggable.getDirection("end") === "left" ? 'next' : 'previous';
            direction_move.value = direction === 'next' ? 1 : -1;
            rando.value = randomFromInterval(.3, .8)
            if (direction === 'next') {
                loopAnimation.play();
            } else {
                loopAnimation.reverse();
            }
        }
      })[0];
      tl.draggable = draggable;
    }
    tl.closestIndex(true);
    lastIndex = curIndex;
    onChange && onChange(items[curIndex], curIndex);
    timeline = tl;
    return () => window.removeEventListener("resize", onResize); // cleanup
  });
  return timeline;
}

</script>


  
  <style scoped>

  .slider_main_container{
    width: 105%;
    margin-left: -5%;
    position: relative;
    padding: 2vh;
  }
  .slider-container {
    display: flex;
    width: max-content;
  }
  .image_container {
    width: 9vw;
    height: 10vw;
    border-radius: 10px;
    position: relative;
    z-index: 1;
  }

  .slider_container_outer{
    position: relative;
    z-index: 1;
    overflow: visible;
    margin: 5px 5px;
    padding: 5px;
    width: 100%;
    height: calc(100% - 10px);
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #ffffff;
    border: 2px solid #243e2e;
    gap: 10%;
    box-shadow: 0 1px 4px 0 rgba(0, 0, 0, 0.4);
    border-radius: 3px;
  }


  .image_container_inner{
    width: 8vw;
    height: 10vw;
    overflow: hidden;
    border-radius: 10px;
    position: relative;
    z-index: 1;
    box-shadow: 1px 1px 3px 0 rgba(0, 0, 0, 0.5);
  }
  .image_card {
    display: flex;
    margin-right: 50px;
    overflow: hidden;
    border-radius: 5px;
    width: 40vw;
    height: 15vw;
    background-color: #0e92411e;
    border: 1px solid #243e2e;
    gap: 10%;
    align-items: center;
    justify-content: center;
    position: relative;
    mix-blend-mode: multiply;
    pointer-events: none;
    box-shadow: 0 1px 8px 0 rgba(0, 0, 0, 0.25);
  }

  

  .logo {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .slider_title{
    font-size: 100%;
    font-weight: 200;
    color: #243e2e;
    margin-left: 5%;
  }

  .info_container{
    width: 50%;
  }

  .info_title{
    font-size: 300%;
    font-weight: 200;
    color: #ffffff;
    margin-bottom: 5px;
  }

  .star {
    color: #ddd;
    font-size: 100%;
    transition: color 0.2s;
  }

  .star.filled {
    color: gold;
  }

  .info_subtitle{
    font-size: 75%;
    font-weight: 200;
    color: #243e2e;
    margin-bottom: 8%;
    position: relative;
    overflow: visible;
  }

  .info_subtitle [data-draw-line-box] {
    display: block;
    width: 100%;
    height: 1px !important;
    margin-top: -2px;
  }

  .info_subtitle [data-draw-line-box] svg {
    width: 100% !important;
    height: 0px !important;
    display: block !important;
  }

  .info_subtitle [data-draw-line-box] svg path {
    stroke: #56badb !important;
    stroke-width: 6px !important;
    fill: none !important;
  }

  .info_text{
    font-size: 85%;
    font-weight: 200;
    color: #243e2e;
    line-height: 1.5;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
  }



.paperOverlayTestamonial {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    opacity: .6;
    background-repeat: repeat;
    background-image: url("~/assets/content/images/paper_overlay_8.jpg");
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 0;
    transform-origin: center;
    transform: rotate(0deg);
  }

  .image_background{
    position: absolute;
    width: 8vw;
    height: 10.25vw;
    overflow: hidden;
    border-radius: 5px;
    border: 2px solid #56badb;
    z-index: 1;
    background-color: #293b2e;
    top: 8px;
    left: 15px;
    right: 0;
    bottom: 0;
  }




  .paperOverlayTestamonial {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    opacity: .55;
    background-size: 100%;
    background-repeat: repeat;
    background-image: url("~/assets/content/images/paper_overlay_3.webp");
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 0;
  }


  </style>
  