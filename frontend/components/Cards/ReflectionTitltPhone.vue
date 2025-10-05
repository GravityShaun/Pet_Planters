<template>
    <div class="card_container">
      <div class="scene">
        <div class="card" ref="card">
          <div class="phoneImage" :style="{ backgroundImage: `url(${imgUrl})` }">
            <div class="overlay" ref="overlay"></div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>

  
  import havenImage from "~/assets/content/images/homePage/haven_1.png";
  
  const imgUrl = havenImage;
  const card = ref(null);
  const overlay = ref(null);
  
  function updateReflection(degree, percentage) {
    if (overlay.value) {
      overlay.value.style.background = `linear-gradient(${degree}deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.3) ${percentage}%, rgba(255,255,255,0) 100%)`;
    }
  }
  
  function handleMouseMove(event) {
    const mouseX = event.clientX;
    const mouseY = event.clientY;
    const halfWidth = window.innerWidth / 2;
    const halfHeight = window.innerHeight / 2;
    const xdeg = (mouseX - halfWidth) / halfWidth;
    const ydeg = (mouseY - halfHeight) / halfHeight;
    updateReflection(ydeg * 180, xdeg * 100);
    if (card.value) {
      card.value.style.transform = `rotateX(${ydeg * 15}deg) rotateY(${xdeg * 15}deg)`;
    }
  }
  
  function handleDeviceMotion(event) {
    const accelerationX = event.accelerationIncludingGravity.x;
    const accelerationY = event.accelerationIncludingGravity.y;
    const xdeg = accelerationX / 10;
    const ydeg = accelerationY / 10;
    updateReflection(ydeg * 280, xdeg * 100);
    if (card.value) {
      card.value.style.transform = `rotateX(-${ydeg * 20}deg) rotateY(${xdeg * 20}deg)`;
    }
  }
  
  onMounted(() => {
    updateReflection(100, 0);
    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('devicemotion', handleDeviceMotion);
  });
  </script>
  


  
  <style scoped>
  .card_container {
    margin-left: 0%;
    width: 80%;
    padding:0vh 0;
  }
  
  .card {
    height: auto;
    width: 100%;
    border-radius: 15px;
    display: flex;
    justify-content: center;
    align-items: center;

  }
  
  .scene {
    perspective: 40em;
  }
  

  .overlay {
  position: absolute;
  top: 1%;
  left:4%;
  right: 4%;
  bottom:1%;
  z-index: 5;
  border-radius: 50px;
}
  
  .phoneImage {
  position: relative;
  z-index: 1;
  width: 100%;
  padding-top: 201.5%; /* Adjust this value based on your image's aspect ratio */
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius:50px;
  overflow: hidden;
  background-position: center center;
  background-repeat: no-repeat;
  background-size: contain;
}



@media only screen and (min-width: 0px) and (max-width: 376px) {

  .overlay {
  border-radius: 15px;
}
  
  .phoneImage {
  border-radius:10px;
}

.card_container {
    margin-left: 10%;
    margin-bottom:20%
  }

    
}
  
@media only screen and (min-width: 376px) and (max-width: 576px) {
  .overlay {
  border-radius: 15px;
}
  
  .phoneImage {
  border-radius:10px;
}

.card_container {
    margin-left: 20%;
    width:60%
  }

}

@media only screen and (min-width: 576px) and (max-width: 768px) {
  .overlay {
  border-radius: 15px;
}
  
  .phoneImage {
  border-radius:10px;
}

.card_container {
  margin-left: 30%;
  width:40%
  }

}

@media only screen and (min-width: 768px) and (max-width: 992px) {
  .overlay {
  border-radius: 15px;
}
  
  .phoneImage {
  border-radius:10px;
}

.card_container {
  margin-left: 30%;
  width:40%
  }

}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
  .card_container {
    margin-left: 0%;
    width: 100%;
    padding:0vh 0;
  }
  
}

@media only screen and (min-width: 1200px) and (max-width: 1300px) {
    .card_container {
    width: 70%;
  }
}

@media only screen and (min-width: 1300px) and (max-width: 1400px) {
    .card_container {
    width: 60%;
  }
}

@media only screen and (min-width: 1400px) and (max-width: 1500px) {
    .card_container {
    width: 70%;
    margin-left:5%;
    margin-top:-10%
  }
}

@media only screen and (min-width: 1500px) and (max-width: 1600px) {
    .card_container {
    width: 50%;
    margin-left:15%
  }
}


@media only screen and (min-width: 1600px) and (max-width: 2000px) {
    .card_container {
    width: 60%;
    margin-left:10%;
    margin-top:-10%
  }
}

@media only screen and (min-width: 2000px) and (max-width: 2500px) {
}

@media only screen and (min-width: 2500px) and (max-width: 5600px) {
}




  </style>