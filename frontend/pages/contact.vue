<template>
    <div>
        <WebsiteSectionsHeaderBar/>
        <NuxtLayout :name="layout">
            <div class="background">
                <GridBackground />
                <div class="paperOverlay"></div>
                <WebsiteSectionsContactLanding/>
            </div>
            <WebsiteSectionsFooter/>
        </NuxtLayout>
    </div>
</template>

<script setup>
const layout = "public";
</script>

<style scoped>
.background {
    background-color: #f7fdf6;
    position: relative;
    min-height: 100vh;
    border-bottom: 1px solid #466151;
}
</style>