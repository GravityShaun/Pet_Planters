<template>
  <div class="our_process_section">
    <div class="our_process_container">
      <div class="our_process_header">
        <h2 class="our_process_title">Our Process</h2>
        <p class="our_process_subtitle">We make it easy to get your home improvement projects done right.</p>
      </div>
      <div class="our_process_grid">
        <div class="our_process_item">
          <img src="https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Contact Us" class="our_process_icon">
          <h3 class="our_process_item_title">Contact Us</h3>
          <p class="our_process_item_text">Get in touch with us to discuss your project and get a free estimate.</p>
        </div>
        <div class="our_process_item">
          <img src="https://images.unsplash.com/photo-1529400971008-f566de0e6df1?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="We Get to Work" class="our_process_icon">
          <h3 class="our_process_item_title">We Get to Work</h3>
          <p class="our_process_item_text">We'll schedule a time to complete the work to your satisfaction.</p>
        </div>
        <div class="our_process_item">
          <img src="https://images.unsplash.com/photo-1579621970795-87f54d5921ba?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Project Complete" class="our_process_icon">
          <h3 class="our_process_item_title">Project Complete</h3>
          <p class="our_process_item_text">Enjoy your newly improved home. It's that simple!</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

onMounted(() => {
  gsap.utils.toArray('.our_process_item').forEach((item, i) => {
    gsap.from(item, {
      opacity: 0,
      y: 50,
      duration: 0.5,
      delay: i * 0.1,
      scrollTrigger: {
        trigger: item,
        start: 'top 80%',
        toggleActions: 'play none none none'
      }
    });
  });
});
</script>

<style scoped>
.our_process_section {
  background: var(--background_color_two);
  padding: 80px 0;
}

.our_process_container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.our_process_header {
  text-align: center;
  margin-bottom: 60px;
}

.our_process_title {
  font-size: 2.5rem;
  color: var(--primary_color);
  margin-bottom: 20px;
  font-weight: 700;
}

.our_process_subtitle {
  font-size: 1.2rem;
  color: var(--text_color);
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.our_process_grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.our_process_item {
  background: var(--background_color);
  padding: 30px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(44, 85, 48, 0.1);
  transition: transform 0.3s ease;
}

.our_process_item:hover {
  transform: translateY(-5px);
}

.our_process_icon {
  font-size: 3rem;
  margin-bottom: 20px;
  color: var(--accent_color);
  font-weight: 700;
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px;
}

.our_process_item_title {
  font-size: 1.4rem;
  color: var(--primary_color);
  margin-bottom: 15px;
  font-weight: 600;
}

.our_process_item_text {
  color: var(--text_color);
  line-height: 1.6;
}
</style>
