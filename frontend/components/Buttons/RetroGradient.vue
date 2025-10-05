<template>
    <button class="buttonBox">
      <span class="buttonText">{{ text }}</span>
    </button>
  </template>
  
  <script setup>
  const props = defineProps(['text'])
  </script>
  
  <style scoped>
  .buttonBox {
    position: relative;
    width: 200px;
    height: 60px;
    /* background-color: #ece0c8; */
    background: linear-gradient(45deg, #202020, #202020, #202020, #202020);
    border: none;
    border-radius: 8px;
    font-size: 18px;
    font-weight: bold;
    overflow: hidden;
    transition: transform 0.3s ease, background 0.3s ease;
    /* Add padding to accommodate the border */
    padding: 2px;
    /* Use background-origin to keep the background within the border */
    background-origin: border-box;
    /* Create the gradient border */
    background-image: linear-gradient(45deg, rgba(106, 210, 196, 08), rgba(156, 103, 189, 0.8), rgba(235, 113, 156, 0.8), rgba(255, 181, 98, 0.8));
  }
  
  .buttonBox::before {
    content: '';
    position: absolute;
    top: 2px;
    left: 2px;
    right: 2px;
    bottom: 2px;
    /* background-color: #ece0c8; */
    background: linear-gradient(45deg, #202020, #202020, #202020, #202020);
    border-radius: 6px;
    z-index: 0;
  }
  
  .buttonText {
    position: relative;
    z-index: 1;
    background: linear-gradient(45deg, rgba(106, 210, 196, 0.8), rgba(156, 103, 189, 0.8), rgba(235, 113, 156, 0.8), rgba(255, 181, 98, 0.8));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    text-fill-color: transparent;
    transition: background 0.3s ease, -webkit-text-fill-color 0.3s ease, text-fill-color 0.3s ease;
  }
  
  .buttonBox:hover {
    transform: scale(1.05);
  }
  
  .buttonBox:hover::before {
    background: linear-gradient(45deg, rgba(106, 210, 196, 0.8), rgba(156, 103, 189, 0.8), rgba(235, 113, 156, 0.8), rgba(255, 181, 98, 0.8));
  }
  
  .buttonBox:hover .buttonText {
    -webkit-text-fill-color: white;
    text-fill-color: white;
  }
  
  .buttonBox::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('https://i.gyazo.com/a26366e538851a5c569ff648e99b7fd4.png');
    opacity: 0.6;
    mix-blend-mode: overlay;
    pointer-events: none;
    transition: opacity 0.3s ease;
    z-index: 2;
  }
  
  .buttonBox:hover::after {
    opacity: 0.3;
  }
  </style>