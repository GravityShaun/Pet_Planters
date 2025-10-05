<template>
<div>

<WebsiteSectionsHeaderBar/>
    <NuxtLayout :name="layout">



<div class="background">
  <GridBackground />
  <div class="paperOverlay"></div>



      <WebsiteSectionsHomepageLanding/>
      <div class="testimonial_slider_container">
        <WebsiteSectionsHomepageTestamonialSlider  :direction="1" :images="images_1" :title="''"/>
        <!-- <WebsiteSectionsHomepageTestamonialSlider  :direction="-1" :images="images_2" :title="''"/> -->
      </div>
     
         <WebsiteSectionsHomepageSteps/>

         <WebsiteSectionsHomepageImageDrop/>


         <!-- <WebsiteSectionsHomepageMap/> -->

         <!-- <WebsiteSectionsHomepageSidewaysAccordian/> -->


  </div>
    <WebsiteSectionsFooter/>





</NuxtLayout>
</div>

</template>

<script setup>
 import image_1 from '~/assets/content/images/homepage/joel_1.png'


const layout = "public";

const images_1 = [image_1, image_1, image_1, image_1, image_1, image_1, image_1, image_1, image_1];
const images_2 = [image_1, image_1, image_1, image_1, image_1, image_1, image_1, image_1, image_1];

// Set page title and meta
useHead({
  title: 'PetPlanters - Custom 3D Pet Planters with Succulents',
  meta: [
    { name: 'description', content: 'Transform your beloved dog into a beautiful, living planter. Upload photos and get a custom 3D printed planter with a succulent on top. 4-5 inches tall, handcrafted with care.' }
  ]
})
</script>

<style scoped>

.background {
  background-color: #fdfffd;
  min-height: 100vh;
  width: 100vw;
  z-index: 0;
  position: relative;
  border-bottom: 1px solid #466151;
}

.testimonial_slider_container {
  margin-top: 5vh;
  position: relative;
  z-index: 10;
  padding-bottom:10vh
}
</style>