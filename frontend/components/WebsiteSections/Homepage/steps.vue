<template>
    <div class="stackContainer" ref="stackContainer">



        <div class="content_container">
      <div
        v-for="(content, index) in contentElements"
        :key="index"
        class="content__sticky"
        ref="contentRefs"
      >
      <div class="paperOverlayTestamonial"></div>
      <div v-if="index === contentElements.length - 1" class="end_trigger"></div>
        <!-- <img class="content__img content__img--small" :src="content.imgSrc" /> -->
        <h2 class="content__title eikoFont"><i> {{ content.title }}</i></h2>
        <div class="center_it">
        <div v-if="content.type == 'bullets'" class="bulletBox">
          <div v-for="(bullet, bulletIndex) in content.bullets" :key="bulletIndex" class="flex_it">
              <div class="bullet">•</div>
              <div class="bulletItem">{{ bullet }}</div>
            </div>
        </div>
        <div v-else>
            <p class="content__text text-meta md_primer">{{ content.description }}</p>
        </div>
        <div class="imageBox">
            <div class="paperOverlayTestamonial"></div>
          <img class="image" :src="content.imgSrc" :alt="content.title">
        </div>
      </div>
      </div>
    </div>


    <div class="threeOuterContianer">

        <div class="sectionScrollContainer">
        <h1 class="sectionTitle">From Photo to Planter</h1>
        <p class="sectionSubtitle">Transform your favorite photos into a one-of-a-kind living planter. Our AI-powered process makes it easy to create a lasting tribute to your furry friend.</p>
        </div>

        <div class="sectionScrollContainer">
        <h1 class="sectionTitle">Powered by AI Technology</h1>
        <p class="sectionSubtitle">Advanced artificial intelligence carefully analyzes your pet's unique features and creates a detailed 3D model that captures their personality and charm.</p>
        </div>

        <div class="sectionScrollContainer">
        <h1 class="sectionTitle">Handcrafted Quality</h1>
        <p class="sectionSubtitle">Each planter is 3D printed with precision and care, using premium materials to ensure your pet's likeness is beautifully preserved for years to come.</p>
        </div>

        <div class="sectionScrollContainer">
        <h1 class="sectionTitle">Perfect Gift for Pet Lovers</h1>
        <p class="sectionSubtitle">Whether for yourself or a loved one, these custom planters make a thoughtful and unique gift that celebrates the special bond we share with our pets.</p>
        </div>

    </div>

    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted, nextTick } from 'vue';
  import { gsap } from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger'
  import pet_1 from '~/assets/content/images/homePage/home_1.png'
  import pet_2 from  '~/assets/content/images/homePage/home_2_wide.png'
  import pet_3 from  '~/assets/content/images/homePage/home_3_wide.png'
  import pet_4 from  '~/assets/content/images/homePage/home_4.png'
  
  gsap.registerPlugin(ScrollTrigger);
  
  const contentRefs = ref([]);
  
  const contentElements = [
    {
      imgSrc: pet_1,
      title: 'Upload Your Pet Photos',
      type: 'bullets',
      description: "",
      bullets: [
        'Share 3-5 high-quality photos of your beloved pet from different angles',
        'Our AI analyzes each unique feature to create an accurate 3D model'
      ]
    },
    {
        imgSrc: pet_2,
      title: 'AI Creates Your Planter',
      type: 'bullets',
      description: '',
      bullets: [
        "Advanced AI transforms your photos into a custom 3D planter design",
        "Get up to 3 free regenerations to perfect every detail of your pet"
      ]
    },
    {
        imgSrc: pet_3,
      title: 'Customize & Approve',
      type: 'bullets',
      description: '',
      bullets: [
        "Choose your size, color, drainage options, and add a live succulent",
        "Review and approve your design before we 3D print it to perfection"
      ]
    },
    {
        imgSrc: pet_4,
      title: 'Delivered with Love',
      type: 'bullets',
      description: '',
      bullets: [
        'Handcrafted 3D printed planter arrives ready to display and enjoy',
        'Complete with care instructions and optional succulent starter kit'
      ]
    }
  ];
  
  const stackContainer = ref(null);

  const scroll = () => {
  contentRefs.value.forEach((el, index) => {
    const isLastIndex = index === contentRefs.value.length - 1;
    gsap
      .timeline({
        scrollTrigger: {
          trigger: el,
          start: 'top 17.5%',
          endTrigger: ".end_trigger",
          scrub: true,
          pin: true,
          pinSpacing: false,
          markers: false,
        },
      })
      .to(el, {
        scale: isLastIndex ? 1 : 0.9 + index / 100,
        yPercent: isLastIndex ? -20 + index * 4 : -20 + index * 2,
        zIndex: -10,
        filter: isLastIndex ? 'none' : 'blur(1px)',
      });
  });
};




const isMobile = ref(false);

const checkMobile = () => {
  isMobile.value = window.innerWidth <= 767;
};

  
onMounted(() => {
  checkMobile();
  window.addEventListener('resize', checkMobile);
  setTimeout(() => {
    scroll();
  }, 100);

  // Clean up the event listener when the component is unmounted
  onUnmounted(() => {
    window.removeEventListener('resize', checkMobile);
  });
});




  </script>
  
  <style scoped>

 .stackContainer{
    display: flex;
    gap:7.5%;
    padding-top:10vh;
    position: relative;
    padding-bottom: 10vh;
    padding-left: 2.5%;
    padding-right: 2.5%;
 }
 
 .stackContainer::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at 30% 50%, rgba(86, 186, 219, 0.05) 0%, transparent 50%),
              radial-gradient(circle at 70% 50%, rgba(63, 124, 73, 0.05) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
 }

.threeOuterContianer{
  position: relative;
  width:45%;
  z-index: 1;
  order: 1;
 }

.content_container {
  position: relative;
  z-index: 2;
  width: 45%;
  order: 2;
  margin-top:5vh
}

  .content__sticky {
    margin-bottom: 20vh;
    position: relative;
    transform: translateY(0);
    text-align: center;
    padding: 30px 20px;
    z-index: 1;
    background: linear-gradient(135deg, rgba(70, 97, 81, 0.95) 0%, rgba(39, 69, 52, 0.95) 100%);
    backdrop-filter: blur(10px);
    width:100%;
    height:70vh;
    margin-left:0%;
    border-radius:16px;
    border:3px solid rgba(86, 186, 219, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2),
                0 0 0 1px rgba(86, 186, 219, 0.1);
    overflow: hidden;
    transition: all 0s ease;
  }
  
  .content__sticky:hover {
    border-color: rgba(86, 186, 219, 0.5);
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.3),
                0 0 0 1px rgba(86, 186, 219, 0.2);
  }
  
  .content__img--small {
    max-width: 200px;
    margin-bottom: 20px;
  }
  
  .content__title {
    font-size: 200%;
    margin-bottom: 10px;
    color:#f7fdf6;
    text-decoration: underline;
    text-decoration-color: #56badb;
    text-decoration-thickness: 3px;
    text-underline-offset: 4px;
    margin-top:3%;
    font-weight: 500;
  }
  
  .content__text {
    font-size: 120%;
    color:#e8f5e6;
    width:80%;
    font-weight:400;
    margin-left:10%;
    text-align: justify;
    margin-top:10%;
    line-height:1.5
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

      
  .threeContainer{
    width:100%;
    height:100vh
}

.flex_it{
  display:flex;
  gap:1%;
  margin-bottom: 25px;
}

 .bullet{
  color: #56badb;
  font-size: 30px;
  line-height: 1;
 }
 
 .bulletItem{
  font-size: 125%;
    color:#f7fdf6;
    width:80%;
    font-weight:400;
    text-align: left;
    line-height:1.5;
    margin-left:12px
 }

.bulletBox{
  margin-top:8%;
  margin-left:5%
}



.image{
  width:100%;
  height: auto;
  object-fit: cover;
}

 .imageBox {
  height:25vh;
  width: 80%;
  margin-left: 10%;
  border-radius: 10px;
  overflow: hidden; 
  margin-top: 20px; 
  border: 2px solid rgba(86, 186, 219, 0.6);
  box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.5),
              0 4px 12px rgba(86, 186, 219, 0.2);
  position: relative;
  bottom:5vh;
  transition: all 0.3s ease;
 }
 
 .imageBox:hover {
  border-color: rgba(86, 186, 219, 0.9);
  box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.6),
              0 6px 20px rgba(86, 186, 219, 0.4);
  transform: scale(1.02);
 }

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}


.center_it{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: space-between;
  position: relative;
  height:62.5vh;
}


 .sectionScrollContainer{
    width:95%;
    height:95vh;
    margin-left:5%;
    margin-top:-5vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 40px 20px;
 }
 
 .sectionScrollContainer:nth-child(1){
    margin-top:-15vh
 }

 .sectionTitle{
    font-size: 300%;
    color:#243e2e;
    text-decoration: underline;
    text-decoration-color: #56badb;
    text-decoration-thickness: 4px;
    text-underline-offset: 8px;
    margin-top:3%;
    line-height:1.25;
    font-weight: 500;
 }
 
 .sectionSubtitle{
    font-size: 125%;
    color:#466151;
    line-height:1.6;
    margin-top:5%;
    font-weight: 300;
 }





 @media only screen and (min-width: 0px) and (max-width: 376px) {
  .stackContainer{
    display: flex;
    flex-direction: column;
    padding-top:10vh;
    padding-left: 0;
    padding-right: 0;
 }

 .threeOuterContianer {
    width: 100%;
    order: 1;
  }

 .content_container {
    width: 100%;
    order: 2;
  }

  .sectionScrollContainer {
    height: auto;
    min-height: 50vh;
    margin-top: 0;
    margin-left: 0;
    width: 100%;
  }
 
 .content__sticky {
    position: relative;
    margin-top:5vh;
    margin-bottom: 5vh;
    width:90vw;
    margin-left:5vw;
    height: auto;
    min-height: 60vh;
  }


  
.bulletItem{
  font-size: 80%;
  width:95%
 }
 
 .center_it{
  display: flex;
  flex-direction: column;
  position: relative;
  height: auto;
  min-height: 40vh;
 }

.content__title {
    font-size: 150%;
    line-height:1.5
  }

   .bullet{
   color: #56badb;
  font-size: 80px;
  line-height: 0.5;
}

.content__text {
    width:95%;
    margin-left:2.5%;
  }

  .bulletBox{
  margin-left:-5%
}

.imageBox{
  display: none;
}


}
  
 @media only screen and (min-width: 376px) and (max-width: 576px) {
 
  .stackContainer{
    display: flex;
    flex-direction: column;
    padding-top:10vh;
    padding-left: 0;
    padding-right: 0;
 }

  .threeOuterContianer {
    width: 100%;
    order: 1;
  }

 .content_container {
    width: 100%;
    order: 2;
  }

  .sectionScrollContainer {
    height: auto;
    min-height: 50vh;
    margin-top: 0;
    margin-left: 0;
    width: 100%;
  }
 
 .content__sticky {
    position: relative;
    margin-top:5vh;
    margin-bottom: 5vh;
    width:90vw;
    margin-left:5vw;
    height: auto;
    min-height: 60vh;
  }


  
.bulletItem{
  font-size: 80%;
  width:95%
}

.center_it{
  display: flex;
  flex-direction: column;
  position: relative;
  height:50vw;
}

.content__title {
    font-size: 150%;
    line-height:1.5
  }

   .bullet{
   color: #56badb;
  font-size: 80px;
  line-height: 0.5;
}

.content__text {
    width:90%;
    margin-left:5%;
  }

  .bulletBox{
  margin-left:-2.5%
}

.imageBox{
  display: none;
}



}

 @media only screen and (min-width: 576px) and (max-width: 768px) {
 
  .stackContainer{
    display: flex;
    flex-direction: column;
    padding-top:10vh;
    padding-left: 0;
    padding-right: 0;
 }

  .threeOuterContianer {
    width: 100%;
    order: 1;
  }

 .content_container {
    width: 100%;
    order: 2;
  }

  .sectionScrollContainer {
    height: auto;
    min-height: 50vh;
    margin-top: 0;
    margin-left: 0;
    width: 100%;
  }
 
 .content__sticky {
    position: relative;
    margin-top:5vh;
    margin-bottom: 5vh;
    width:90vw;
    margin-left:5vw;
    height: auto;
    min-height: 65vh;
  }


  
.bulletItem{
  font-size: 100%;
  width:95%
}

.center_it{
  display: flex;
  flex-direction: column;
  position: relative;
  height:50vw;
}

.content__title {
    font-size: 150%;
    line-height:1.5
  }

   .bullet{
   color: #56badb;
  font-size: 80px;
  line-height: 0.5;
}

.content__text {
    width:90%;
    margin-left:5%;
  }

  .bulletBox{
  margin-left:-2.5%
}

.imageBox{
  display: none;
}



}

 @media only screen and (min-width: 768px) and (max-width: 992px) {
 
  .stackContainer{
    display: flex;
    flex-direction: column;
    padding-top:10vh;
    padding-left: 0;
    padding-right: 0;
 }

  .threeOuterContianer {
    width: 100%;
    order: 1;
  }

 .content_container {
    width: 100%;
    order: 2;
  }

  .sectionScrollContainer {
    height: auto;
    min-height: 50vh;
    margin-top: 0;
    margin-left: 0;
    width: 100%;
  }
 
 .content__sticky {
    position: relative;
    margin-top:5vh;
    margin-bottom: 5vh;
    width:90vw;
    margin-left:5vw;
    height: auto;
    min-height: 65vh;
  }


  
.bulletItem{
  font-size: 100%;
  width:95%
}

.center_it{
  display: flex;
  flex-direction: column;
  position: relative;
  height:50vw;
}

.content__title {
    font-size: 150%;
    line-height:1.5
  }

   .bullet{
   color: #56badb;
  font-size: 80px;
  line-height: 0.5;
}

.content__text {
    width:80%;
    margin-left:10%;
  }

  .bulletBox{
  margin-left:0%
}

.imageBox{
  display: none;
}


}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
  .bulletItem{
  font-size: 100%;
  width:95%
}

.imageBox{
  display: none;
}


}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
  .bulletItem{
  font-size: 100%;
}
}


@media only screen and (min-width: 1600px) and (max-width: 2000px) {
  .bulletItem{
  font-size: 100%;
}
}

@media only screen and (min-width: 2000px) and (max-width: 2500px) {
  .bulletItem{
  font-size: 100%;
}
}

@media only screen and (min-width: 2500px) and (max-width: 5600px) {
  .bulletItem{
  font-size: 100%;
}
}





  </style>
  