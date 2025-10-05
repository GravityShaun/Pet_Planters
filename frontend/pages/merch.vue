<template>
<div>

<WebsiteSectionsHeaderBar/>
    <NuxtLayout :name="layout">

<div class="background">
   <div class="paperOverlay"></div>

   <WebsiteSectionsMerchInteractiveGridDots />

   <WebsiteSectionsMerchProducts />

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
  title: 'Gallery - PetPlanters',
  meta: [
    { name: 'description', content: 'See our collection of custom 3D printed pet planters. Each one is unique and crafted with love.' }
  ]
})

</script>

<style scoped>
.background {
  background-color: #f7fdf6;
  min-height: 100vh;
  width: 100vw;
  position: relative;
  color: #274534;
  border-bottom: 1px solid #466151;
}
</style>
