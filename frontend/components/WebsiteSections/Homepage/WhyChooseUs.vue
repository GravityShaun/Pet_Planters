<template>
  <div class="why_choose_us_section">
    <div class="why_choose_us_container">
      <div class="why_choose_us_header">
        <h2 class="why_choose_us_title">Why Choose Us?</h2>
        <p class="why_choose_us_subtitle">We are committed to providing the best handyman services in the area.</p>
      </div>
      <div class="why_choose_us_grid">
        <div class="why_choose_us_item">
          <img src="https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Quality Workmanship" class="why_choose_us_icon">
          <h3 class="why_choose_us_item_title">Quality Workmanship</h3>
          <p class="why_choose_us_item_text">We take pride in our work and ensure that every job is done to the highest standards.</p>
        </div>
        <div class="why_choose_us_item">
          <img src="https://images.unsplash.com/photo-1529400971008-f566de0e6df1?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Reliable Service" class="why_choose_us_icon">
          <h3 class="why_choose_us_item_title">Reliable Service</h3>
          <p class="why_choose_us_item_text">We are punctual, professional, and respectful of your home and your time.</p>
        </div>
        <div class="why_choose_us_item">
          <img src="https://images.unsplash.com/photo-1579621970795-87f54d5921ba?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Fair Pricing" class="why_choose_us_icon">
          <h3 class="why_choose_us_item_title">Fair Pricing</h3>
          <p class="why_choose_us_item_text">We offer competitive pricing without compromising on quality.</p>
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
  gsap.utils.toArray('.why_choose_us_item').forEach((item, i) => {
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
.why_choose_us_section {
  background: var(--background_color);
  padding: 80px 0;
}

.why_choose_us_container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.why_choose_us_header {
  text-align: center;
  margin-bottom: 60px;
}

.why_choose_us_title {
  font-size: 2.5rem;
  color: var(--primary_color);
  margin-bottom: 20px;
  font-weight: 700;
}

.why_choose_us_subtitle {
  font-size: 1.2rem;
  color: var(--text_color);
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.why_choose_us_grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.why_choose_us_item {
  background: var(--background_color_two);
  padding: 30px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(44, 85, 48, 0.1);
  transition: transform 0.3s ease;
}

.why_choose_us_item:hover {
  transform: translateY(-5px);
}

.why_choose_us_icon {
  font-size: 3rem;
  margin-bottom: 20px;
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px;
}

.why_choose_us_item_title {
  font-size: 1.4rem;
  color: var(--primary_color);
  margin-bottom: 15px;
  font-weight: 600;
}

.why_choose_us_item_text {
  color: var(--text_color);
  line-height: 1.6;
}
</style>
