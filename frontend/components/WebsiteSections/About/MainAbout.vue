<template>
    <div class="about_container">
    <div class="about_grid">
        <div class="about_content">
        <h1 class="about_title" data-draw-line="main-about-joel-title">
            Get Serviced By Joel
            <span data-draw-line-box></span>
        </h1>
        <div class="about_text">
            <p>Hiring a service should be easy. Here's what you can expect when you hire me for your handyman needs. For more details on specific services, check out the sections below.</p>
            <ul class="how-it-works-list">
                <li>
                    <strong class="animated-underline">Scheduling & Quotes:</strong> Simply send me a message with your project details. I'll provide a clear, no-obligation quote and we'll schedule the work for a time that suits you.
                </li>
                <li>
                    <strong class="animated-underline">The Work:</strong> I arrive on time and ready to work. I treat your home with respect, work efficiently, and am fully insured for your peace of mind. Your property is in safe hands.
                </li>
                <li>
                    <strong class="animated-underline">Clear Pricing:</strong> The price we agree on is the price you pay. No hidden fees, no surprises. Payment is due upon satisfactory completion of the job.
                </li>
                <li>
                    <strong class="animated-underline">My Guarantee:</strong> Your satisfaction is my promise. I stand by the quality of my work, and if you're not happy, I'll make it right.
                </li>
            </ul>
        </div>
        <NuxtLink to="/contact" class="contact-button">
            <span class="contact-button-text">Get Your Free Quote</span>
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
                <img class="image" src="~/assets/content/images/services/service_1.png" alt="Joel at work">
            </div>
            <div class="image_container_2" data-speed="1.05">
                <img class="image" src="~/assets/content/images/services/service_2.png" alt="Joel's handiwork">
            </div>
            <div class="image_1_background"></div>
            <!-- <div class="image_2_background"></div> -->
    </div>
    </div>
  
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useUnderlineAnimation } from '~/composables/useUnderlineAnimation';
import gsap from 'gsap';

const { initUnderlineAnimation } = useUnderlineAnimation();

onMounted(() => {
  setTimeout(() => {
    if (typeof window !== 'undefined') {
      // Initialize underline animation
      initUnderlineAnimation('[data-draw-line="main-about-joel-title"]', {
        autoAnimate: true,
        duration: 1,
        ease: "power2.inOut",
        delay: 0.25
      });

      // Force red color after animation initializes
      setTimeout(() => {
        const element = document.querySelector('[data-draw-line="main-about-joel-title"]');
        const svg = element?.querySelector('svg');
        const path = svg?.querySelector('path');
        if (path) {
          path.setAttribute('stroke', '#fd3d13');
          path.style.stroke = '#fd3d13';
          path.style.strokeWidth = '8px';
        }
      }, 100);

      // Animate arrows with GSAP
      const listItems = document.querySelectorAll('.how-it-works-list li');
      const underlines = document.querySelectorAll('.animated-underline');

      listItems.forEach((item, index) => {
        const arrowDelay = 2 + (index * 0.2);
        const underlineDelay = arrowDelay + 0.215; // Start underline after arrow finishes

        // Animate arrow
        gsap.fromTo(item,
          {
            '--arrow-opacity': 0,
            '--arrow-x': '-25px'
          },
          {
            '--arrow-opacity': 1,
            '--arrow-x': '0px',
            duration: 0.5,
            delay: arrowDelay,
            ease: 'power2.out'
          }
        );

        // Animate underline
        gsap.fromTo(underlines[index],
          {
            '--underline-width': '0%'
          },
          {
            '--underline-width': '100%',
            duration: 0.55,
            delay: underlineDelay,
            ease: 'power2.out'
          }
        );
      });
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
    gap: 1.5rem;
    width: 85%;
    margin: 0 auto;
}

.aboutImages{
    position: relative;
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin-top: 5%;
}

.image_container_1{
    width: 65%;
    height: 50vh;
    border-radius: 10px;
    overflow: hidden;
    position: absolute;
    z-index: 1;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
    margin-top: 10%;
}

.image_1_background{
    width: 65%;
    height: 50vh;
  background-color: #243e2e;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: visible;
  position: absolute;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    border: 2px solid #fd3d13;
    top: 11%;
    margin-left: 5%;
}

.image_container_2{
    width: 90%;
    height: auto;
    border-radius: 10px;
    overflow: hidden;
    position: absolute;
    margin-top:65%;
    z-index: 2;
    margin-left: 15%;
    box-shadow: 0 0 10px 0 rgba(33, 27, 27, 0.3);
    background-color: #243e2e;
    border: 1px solid #fd3d13;
    padding: 1%;
}

.image_2_background{
    width: 90%;
    height: 40vh;
  background-color: #243e2e;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: visible;
  position: absolute;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    border: 2px solid #fd3d13;
    top: 40%;
    margin-left: 20%;
}

.about_title{
    margin-top: 12%;
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
    margin-left: -48% !important;
}

.about_title [data-draw-line-box] svg {
    width: 100% !important;
    height: 0px !important;
    display: block !important;
}

.about_title [data-draw-line-box] svg path {
    stroke: #fd3d13 !important;
    stroke-width: 8px !important;
    fill: none !important;
}

.about_text{
    margin-top: 10%;
    width: 90%;
    line-height: 1.8;
    font-size: 1.1rem;
    color: #293b2e;
    font-weight: 400;
    text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
}

.how-it-works-list {
    list-style: none;
    padding: 0;
    margin-top: 2rem;
}

.how-it-works-list li {
    position: relative;
    padding-left: 25px;
    margin-bottom: 1rem;
    line-height: 1.5;
    font-size: 120%;
    --arrow-opacity: 0;
    --arrow-x: -10px;
}

.how-it-works-list li::before {
    content: "→";
    position: absolute;
    left: 0;
    top: 0;
    color: #fd3d13;
    font-weight: bold;
    opacity: var(--arrow-opacity);
    transform: translateX(var(--arrow-x));
}

.animated-underline {
    position: relative;
    display: inline-block;
    --underline-width: 0%;
}

.animated-underline::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: 0px;
    width: var(--underline-width);
    height: 2px;
    background-color: #293b2e;
}

.image{
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.about_quote{
    font-size: 2.5rem;
    font-weight: 600;
    color: #293b2e;
    text-align: center;
    margin-top: 10%;
    width: 80%;
    margin-left: 10%;
    line-height: 1.4;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    font-style: italic;
}

/* Contact Button Styling */
.contact-button {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 15px 32px;
    background: linear-gradient(45deg, #293b2e, #1a2b1f);
    color: #fff;
    text-decoration: none;
    border-radius: 50px;
    font-weight: 700;
    font-size: 1rem;
    letter-spacing: 1px;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.2, 0.6, 0.4, 1);
    box-shadow: 0 8px 15px rgba(41, 59, 46, 0.3), 0 0 0 2px rgba(41, 59, 46, 0.1);
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
    background: linear-gradient(45deg, #1a2b1f, #293b2e);
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
    box-shadow: 0 12px 25px rgba(41, 59, 46, 0.4), 0 0 0 3px rgba(41, 59, 46, 0.2);
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
    box-shadow: 0 6px 12px rgba(41, 59, 46, 0.3), 0 0 0 2px rgba(41, 59, 46, 0.1);
}

/* Responsive Design */

/* Tablets and medium screens */
@media (max-width: 1024px) {
    .about_grid {
        gap: 2rem;
        width: 90%;
    }

    .about_title {
        font-size: 3rem;
    }

    .about_text {
        width: 95%;
        font-size: 1rem;
    }

    .aboutImages {
        margin-top: 8%;
    }

    .image_container_1 {
        width: 70%;
        height: 45vh;
    }

    .image_1_background {
        width: 70%;
        height: 45vh;
    }

    .image_container_2 {
        width: 95%;
        margin-top: 60%;
        margin-left: 12%;
    }
}

/* Small tablets */
@media (max-width: 768px) {
    .about_container {
        min-height: auto;
        padding: 10vh 0;
    }

    .about_grid {
        grid-template-columns: 1fr;
        gap: 0;
        width: 90%;
    }

    .about_content {
        order: 2;
    }

    .about_title {
        font-size: 2.25rem;
        margin-top: 8%;
        margin-bottom: 1.5rem;
    }

    .about_title [data-draw-line-box] {
        margin-left: -30% !important;
    }

    .about_text {
        width: 100%;
        font-size: 0.95rem;
        margin-top: 6%;
    }

    .how-it-works-list li {
        font-size: 105%;
        margin-bottom: 1.5rem;
        padding-left: 24px;
    }

    .about_quote {
        font-size: 1.8rem;
        width: 95%;
        margin-left: 2.5%;
    }

    .contact-button {
        width: 100%;
        max-width: 100%;
        padding: 15px 30px;
        font-size: 0.95rem;
        margin-top: 30px;
    }

    .aboutImages {
        order: 1;
        min-height: 500px;
        margin-bottom: 3rem;
        margin-top: 0;
    }

    .image_container_1 {
        width: 72%;
        height: 36vh;
        margin-top: 5%;
    }

    .image_1_background {
        width: 72%;
        height: 36vh;
        top: 8%;
        margin-left: 3%;
    }

    .image_container_2 {
        width: 88%;
        margin-top: 48%;
        margin-left: 12%;
    }
}

/* Mobile phones */
@media (max-width: 480px) {
    .about_container {
        padding: 6vh 0;
    }

    .about_grid {
        width: 92%;
    }

    .about_title {
        font-size: 1.85rem;
        margin-top: 5%;
    }

    .about_title [data-draw-line-box] {
        margin-left: -25% !important;
    }

    .about_text {
        font-size: 0.9rem;
        margin-top: 5%;
    }

    .how-it-works-list li {
        font-size: 100%;
        margin-bottom: 1.3rem;
        padding-left: 22px;
    }

    .contact-button {
        padding: 14px 26px;
        font-size: 0.9rem;
        margin-top: 25px;
    }

    .aboutImages {
        min-height: 420px;
        margin-bottom: 2.5rem;
    }

    .image_container_1 {
        width: 78%;
        height: 32vh;
        margin-top: 3%;
    }

    .image_1_background {
        width: 78%;
        height: 32vh;
        top: 6%;
        margin-left: 2%;
    }

    .image_container_2 {
        width: 92%;
        margin-top: 46%;
        margin-left: 8%;
    }
}

/* Very small phones */
@media (max-width: 375px) {
    .about_title {
        font-size: 1.65rem;
    }

    .about_text {
        font-size: 0.85rem;
    }

    .how-it-works-list li {
        font-size: 95%;
    }

    .aboutImages {
        min-height: 380px;
    }

    .image_container_1 {
        width: 82%;
        height: 28vh;
    }

    .image_1_background {
        width: 82%;
        height: 28vh;
    }

    .image_container_2 {
        width: 95%;
        margin-left: 5%;
    }
}
</style>