<template>
  <div class="grid-background">
    <div class="grid-lines"></div>
  </div>
</template>

<script setup>
// No script needed for simple grid
</script>

<style scoped>
.grid-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 1;
  overflow: hidden;
}

.grid-lines {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  mix-blend-mode: multiply;
  background-image: 
    linear-gradient(rgba(0, 0, 0, 0.4) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 0, 0, 0.4) 1px, transparent 1px);
  background-size: 50px 50px;
  opacity: 0.2;
  mask: radial-gradient(ellipse at top left, black 0%, transparent 70%);
  -webkit-mask: radial-gradient(ellipse at top left, black 0%, transparent 70%);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .grid-lines {
    background-size: 30px 30px;
  }
}

@media (max-width: 480px) {
  .grid-lines {
    background-size: 20px 20px;
  }
}
</style> 