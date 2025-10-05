<template>
   <div id="footer">

    <div class="mobile_footer_container">


        <div class="mobile_content_container">
          <!-- <MoveText/> -->

      <div class="footer_title_container">
    
        <img class="mobile_logo" src="~/assets/content/images/petplanters_logo_1.png">
        <p class="place_holder">Transform your beloved pet into a beautiful, living planter. Each piece is custom 3D printed and topped with a succulent.</p>
        </div>

<div class="grid_1_mobile">
                            <div class="">
                            <div class="info_title">Email</div>
                            <div class="info_content">hello@petplanters.com</div>
                            </div>
                            <div class="info_item">
                            <div class="info_title">Phone</div>
                            <div class="info_content">(555) 738-7526</div>
                            </div>
                            <div class="info_item">
                            <div class="info_title">Social</div>
                            <div class="social_links">
                              <a href="#" class="social_link">Facebook</a>
                              <a href="#" class="social_link">Instagram</a>
                              <a href="#" class="social_link">Twitter</a>
                            </div>
                            </div>

                    </div>


</div>

    </div>




    <div class="desktop_footer_container"  style="background-color: var(--background_color_two)">
     <div class="desktop_footer">
      
         
            
      <img class="logo" src="~/assets/content/images/petplanters_logo_1.png">

      <div class="first_job_free_title">
        <h2 class="marker">Turn Your Pet Into Art</h2>
      </div>

      <div class="footer_content_container">

        <div class="footer_content_item">
          <div class="contact_info">
            <h3 class="contact_title">Contact Us</h3>
            <div class="contact_item">
              <div class="info_title">Email</div>
              <div class="info_content">hello@petplanters.com</div>
            </div>
            <div class="contact_item">
              <div class="info_title">Phone</div>
              <div class="info_content">(555) 738-7526</div>
            </div>
            <div class="contact_item">
              <div class="info_title">Social</div>
              <div class="social_links">
                <a href="#" class="social_link">Facebook</a>
                <a href="#" class="social_link">Instagram</a>
                <a href="#" class="social_link">Twitter</a>
              </div>
            </div>
          </div>
        </div>

      </div>







 
        
     </div>
   </div>
   <div class="made_by">
    Made By GravityLabs
   </div>
   </div>
 </template>
 
 <script setup>
 import { onMounted } from 'vue';
 import gsap from 'gsap';
 import { ScrollTrigger } from 'gsap/ScrollTrigger';


onMounted(() => {
  setTimeout(() => {
  gsap.fromTo(".made_by", 
    { y: 100 }, // Starting state: y is 30px
    {
      y: 0, // Ending state: Move up by 30px
      duration: .8, // Animation duration in seconds
      delay: 4, // Delay before the animation starts in seconds
      scrollTrigger: {
        trigger: "footer",
        start: "center bottom", // Start the animation when the center of the footer is at the bottom of the viewport
        toggleActions: "restart none none reset" // Restart on enter, do nothing on leave, and reset when the trigger isn't in the viewport
      }
    }
  );



     // Footer ScrollTrigger
     ScrollTrigger.create({
      trigger: ".desktop_footer_container",
      start: "bottom bottom",
      pin: ".desktop_footer_container",
      pinSpacing: true,
    });

     // Initialize hand-drawn circle animation
     initHandDrawnCircle();

}, 100);
});

// Hand-drawn circle animation functions
const initHandDrawnCircle = () => {
  const marker = document.querySelector('.marker');
  if (!marker) return;

  const width = marker.offsetWidth;
  const height = 2 * marker.offsetHeight;
  const ns = "http://www.w3.org/2000/svg";

  // Create SVG element
  const svg = document.createElementNS(ns, "svg");
  svg.style.cssText = `
    position: absolute;
    left: 0;
    top: -50%;
    right: 0;
    margin-left: auto;
    margin-right: auto;
    pointer-events: none;
    width: ${width}px;
    height: ${height}px;
    transform: scale(${(2 * width) / height}, 1);
  `;
  svg.setAttribute('width', width);
  svg.setAttribute('height', height);
  svg.setAttribute('viewBox', '-1 -1 2 2');

  // Create path element
  const path = document.createElementNS(ns, "path");
  path.setAttribute('pathLength', '100');
  path.setAttribute('vector-effect', 'non-scaling-stroke');
  path.style.cssText = `
    transition: stroke-dashoffset 1.5s ease-in-out;
    stroke-width: 4;
    stroke: #56badb;
    fill: none;
    stroke-linecap: round;
    visibility: hidden;
  `;

  svg.appendChild(path);
  marker.appendChild(svg);

  // Generate circle path
  const circlePath = generateCirclePath();
  const pathLength = path.getTotalLength();
  
  path.setAttribute('d', circlePath);
  path.style.strokeDasharray = pathLength;
  path.style.strokeDashoffset = pathLength;

  // Show animation when element is visible
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          path.style.visibility = 'visible';
          path.style.strokeDashoffset = '0';
        }, 500);
      } else {
        path.style.visibility = 'hidden';
        path.style.strokeDashoffset = pathLength;
      }
    });
  }, { threshold: 0.5 });

  observer.observe(marker);
};

const generateCirclePath = () => {
  const c = 0.551915024494;
  const β = Math.atan(c);
  const d = Math.sqrt(c * c + 1 * 1);
  let r = 0.75;
  let θ = ((150 + Math.random() * (190 - 150)) * Math.PI) / 180;
  let path = "M";

  path += [r * Math.sin(θ), r * Math.cos(θ)];
  path += " C" + [d * r * Math.sin(θ + β), d * r * Math.cos(θ + β)];

  for (let i = 0; i < 4; i++) {
    θ += (Math.PI / 2) * (1 + 0.05 + Math.random() * (0.3 - 0.05));
    r *= 1 + (-0.15) + Math.random() * (0.05 - (-0.15));
    path +=
      " " +
      (i ? "S" : "") +
      [d * r * Math.sin(θ - β), d * r * Math.cos(θ - β)];
    path += " " + [r * Math.sin(θ), r * Math.cos(θ)];
  }
  return path;
};

 </script>
 
 <style scoped>
.made_by {
  position: fixed;
  color: #fff;
  background-color: #000;
  font-size: 8px;
  padding: 8px;
  z-index: 0;
  width: 100vw;
  bottom: 0;
  font-weight: 400;
}

.desktop_footer_container {
  z-index: -5;
  bottom: 0;
  margin-top: calc(-1 * (100vh - 501px));
}

.desktop_footer {
  background-color: #fff;
  height: 500px;
  width: 100%;
  border-top: 2px solid #293b2e45;
  position: fixed;
  bottom: 0px;
  margin-top: -100vh;
  z-index: -5;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10%;
}

.desktop_footer::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("~/assets/content/images/paper_overlay_4.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0.3;
  z-index: -1;
}

.footer_title_container {
  width: 55%;
  border-right: #1d1d1dd5 solid 1px;
  padding: 10px 0;
}

.place_holder {
  color: #1d1d1dd5;
  width: 80%;
  line-height: 1.25;
}

.info_title {
  color: #1d1d1dd5;
  font-size: 80%;
}

.info_content {
  color: #1d1d1dd5;
  margin-top: 10px;
  font-size: 120%;
}

.logo {
  width: 45%;
  margin-bottom: 20px;
  margin-left: 5%;
}

.first_job_free_title {
  text-align: center;
  margin: 0 10px;
  margin-left: -7%;
}

.first_job_free_title h2 {
  font-size: 3.5rem;
  line-height: 1.5;
  font-weight: 700;
  color: #1d1d1d;
  margin: 0;
  letter-spacing: 2px;
  text-transform: uppercase;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  color: #243e2e;
}

/* Marker styling for hand-drawn circle */
.marker {
  position: relative;
  display: inline-block;
}

.footer_content_container {
  display: flex;
  justify-content: flex-start;
  width: 40%;
  margin-right: 5%;
}

.footer_content_item {
  margin-right: 40px;
}

.contact_info {
  color: #1d1d1dd5;
}

.contact_title {
  font-size: 200%;
  margin-bottom: 40px;
  font-weight: 400;
  letter-spacing: 1px;
  text-decoration: underline;
  text-underline-offset: 8px;
  text-decoration-color: #1ebf74;
  text-decoration-thickness: 2px;
}

.contact_item {
  margin-bottom: 35px;
}

.social_links {
  display: flex;
  gap: 15px;
  margin-top: 10px;
}

.social_link {
  color: #1d1d1dd5;
  text-decoration: none;
  transition: color 0.3s ease;
}

.social_link:hover {
  color: #cd9a0d;
}

/* Mobile Styles */
@media only screen and (min-width: 0px) and (max-width: 576px) {
  .desktop_footer_container {
    display: none;
  }
  
  .mobile_footer_container {
    background-color: #49161b;
    width: 100%;
    height: 100%;
    padding-bottom: 20vh;
  }

  .mobile_content_container {
    width: 80%;
    margin-left: 10%;
  }

  .footer_title_container {
    width: 80%;
    border-right: none;
    border-bottom: #1d1d1dd5 solid 1px;
    padding-bottom: 40px;
    margin-left: 10%;
    padding-top: 20%;
  }

  .mobile_title {
    font-size: 6vw;
    color: #1d1d1dd5;
  }
  
  .place_holder {
    width: 100%;
    margin-top: 10%;
  }

  .grid_1_mobile {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(4, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 40px;
    margin-left: 10%;
    margin-top: 20%;
  }
}

/* Tablet Styles */
@media only screen and (min-width: 576px) and (max-width: 769px) {
  .desktop_footer_container {
    display: none;
  }
  
  .mobile_footer_container {
    background-color: #49161b;
    width: 100%;
    height: 100%;
    padding-bottom: 20vh;
  }

  .mobile_content_container {
    width: 80%;
    margin-left: 10%;
  }

  .footer_title_container {
    width: 80%;
    border-right: none;
    border-bottom: #1d1d1dd5 solid 1px;
    padding-bottom: 40px;
    margin-left: 10%;
    padding-top: 20%;
  }

  .mobile_title {
    font-size: 6vw;
    color: #1d1d1dd5;
  }
  
  .place_holder {
    width: 100%;
    margin-top: 10%;
  }

  .grid_1_mobile {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(4, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 40px;
    margin-left: 10%;
    margin-top: 20%;
  }
}

/* Desktop Styles */
@media only screen and (min-width: 769px) {
  .mobile_footer_container {
    display: none;
  }
}
</style>