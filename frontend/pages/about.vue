<template>
<div>

<WebsiteSectionsHeaderBar/>
    <NuxtLayout :name="layout">

<div class="background">
  <GridBackground />
   <div class="paperOverlay"></div>

   <!-- <WebsiteSectionsAboutMainAbout /> -->
    <WebsiteSectionsServicesLanding />

   <WebsiteSectionsAboutImageScrollers />
<!--       
   <WebsiteSectionsAboutWorkWithMeContent /> -->

  </div>
    <WebsiteSectionsFooter/>

</NuxtLayout>
</div>

</template>

<script setup>

const layout = "public";

// Set page title and meta
useHead({
  title: 'Our Story - PetPlanters',
  meta: [
    { name: 'description', content: 'Transform your beloved pet into a beautiful, living planter. Custom 3D printed with care.' }
  ]
})

</script>

<style scoped>
.background {
  background-color: #f7fdf6;
  min-height: 100vh;
  width: 100vw;
  position: relative;
  color: #274534; /* Base content color */
  border-bottom: 1px solid #466151;
}
</style>
