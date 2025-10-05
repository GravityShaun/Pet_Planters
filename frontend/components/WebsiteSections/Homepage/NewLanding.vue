<template>
  <section class="landing-section">
    <div class="container">
      <div class="text-content" data-speed="1.2">
        <h1 class="tagline">Work With Me</h1>
        <p class="sub-tagline">I'm here to help you.</p>
        <button class="cta-button">Get Started</button>
      </div>
      <div class="image-content">
        <img src="https://images.unsplash.com/photo-1727654758597-a6ec6da5a7ba?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTg3fHxmb3JyZXN0fGVufDB8MHwwfHx8MA%3D%3D" alt="Placeholder image" />
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.landing-section {
  padding: 80px 0;
  background-color: #f4f4f4;
  padding-top:20vh
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.text-content {
  max-width: 50%;
}

.tagline {
  font-size: 3rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 20px;
}

.sub-tagline {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 30px;
}

.cta-button {
  padding: 15px 30px;
  background-color: #1eb854;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.cta-button:hover {
  background-color: #189a46;
}
    
.image-content img {
  width: 50vw;
  border-radius: 10px;
}

@media (max-width: 768px) {
  .container {
    flex-direction: column;
    text-align: center;
  }

  .text-content {
    max-width: 100%;
    margin-bottom: 40px;
  }
}
</style> 