<template>
    <div class="about_container">
        <div class="paperOverlay"></div>
    <div class="about_grid">
        <div class="about_content">
        <h1 class="about_title" data-draw-line="about-joel-title">
            About Joel
            <span data-draw-line-box></span>
        </h1>
        <p class="about_text">
            With over 15 years of experience in the trades, I've built a reputation for quality work and reliable service. 
            <br><br>
            I'm not just a handyman; I'm a craftsman dedicated to improving your home. I take pride in every project, big or small.
            <br><br>
            Your satisfaction is my top priority. I'm not happy until you're happy.
        </p>
        <NuxtLink to="/contact" class="contact-button">
            <span class="contact-button-text">Contact Us</span>
            <span class="contact-button-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14"></path>
                    <path d="M12 5l7 7-7 7"></path>
                </svg>
            </span>
        </NuxtLink>
    </div>
    <div class="aboutImages">
            <div class="image_container_1" data-speed="0.95">
                <div class="image_placeholder">👨‍🔧</div>
            </div>
            <div class="image_container_2" data-speed="1.05">
                <div class="image_placeholder">工具</div>
            </div>
    </div>
    </div>
    <h1 class="about_quote">"The job is not done until it's done right."</h1>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';

const { initUnderlineAnimation } = useUnderlineAnimation();

onMounted(() => {
  setTimeout(() => {
    if (process.client) {
      // Initialize underline animation
      initUnderlineAnimation('[data-draw-line="about-joel-title"]', {
        autoAnimate: true,
        duration: 1,
        ease: "power2.inOut",
        delay: 0.25
      });

      // Force red color after animation initializes
      setTimeout(() => {
        const element = document.querySelector('[data-draw-line="about-joel-title"]');
        const svg = element?.querySelector('svg');
        const path = svg?.querySelector('path');
        if (path) {
          path.setAttribute('stroke', '#fd3d13');
          path.style.stroke = '#fd3d13';
          path.style.strokeWidth = '3px';
        }
      }, 100);
    }
  }, 100);
});
</script>

<style scoped>

.about_container{
    position: relative;
    min-height: 80vw;
    padding: 15vh 0;
}

.about_grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    width: 90%;
    margin: 0 auto;
}

.aboutImages{
    display:grid;
    grid-template-columns: 1fr 1fr;

}

.image_container_1{
    width: 100%;
    height: auto;
    border-radius: 10px;
    overflow: hidden;
    position: relative;
    z-index: 1;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
}

.image_container_2{
    width: 70%;
    height: auto;
    border-radius: 10px;
    overflow: hidden;
    position: relative;
    margin-top: 30%;
    z-index: 2;
    margin-left: -10%;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.3);
}

.about_title{
    margin-top: 25%;
    position: relative;
    overflow: visible;
}

.about_title [data-draw-line-box] {
    display: block;
    width: 100%;
    height: 1px !important;
    margin-top: -24px;
}

.about_title [data-draw-line-box] svg {
    width: 100% !important;
    height: 0px !important;
    display: block !important;
}

.about_title [data-draw-line-box] svg path {
    stroke: #fd3d13 !important;
    stroke-width: 3px !important;
    fill: none !important;
}

.about_text{
    margin-top: 3%;
    width:80%;
    line-height: 1.5;
}

.image_placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4rem;
    background: linear-gradient(135deg, var(--primary_color), var(--secondary_color));
    color: white;
    opacity: 0.9;
}

.about_quote{
    font-size: 3rem;
    font-weight: 600;
    color: #1d1d1dd5;
    text-align: center;
    margin-top: 10%;
    width: 80%;
    margin-left: 10%;
    line-height: 1.5;
}

/* Contact Button Styling */
.contact-button {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 12px 28px;
    background: linear-gradient(45deg, #107a32, #0e7269);
    color: #fff;
    text-decoration: none;
    border-radius: 50px;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1px;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.2, 0.6, 0.4, 1);
    box-shadow: 0 8px 15px rgba(30, 184, 84, 0.15), 0 0 0 2px rgba(30, 184, 84, 0.1);
    z-index: 1;
    margin-top: 35px;
    display: inline-flex;
}

.contact-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, #0e7c73, #0e7a33);
    opacity: 0;
    z-index: -1;
    transition: opacity 0.4s ease;
}

.contact-button-text {
    position: relative;
    z-index: 2;
    transition: transform 0.4s cubic-bezier(0.2, 0.6, 0.4, 1);
}

.contact-button-icon {
    position: relative;
    width: 24px;
    height: 24px;
    margin-left: 12px;
    opacity: 0;
    transform: translateX(-10px);
    transition: all 0.4s cubic-bezier(0.2, 0.6, 0.4, 1);
    z-index: 2;
}

.contact-button-icon svg {
    width: 100%;
    height: 100%;
}

.contact-button:hover {
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 12px 25px rgba(30, 184, 84, 0.25), 0 0 0 3px rgba(30, 184, 84, 0.15);
}

.contact-button:hover::before {
    opacity: 1;
}

.contact-button:hover .contact-button-text {
    transform: translateX(-10px);
}

.contact-button:hover .contact-button-icon {
    opacity: 1;
    transform: translateX(0);
}

.contact-button:active {
    transform: translateY(-2px) scale(0.98);
    box-shadow: 0 6px 12px rgba(30, 184, 84, 0.2), 0 0 0 2px rgba(30, 184, 84, 0.1);
}
</style>