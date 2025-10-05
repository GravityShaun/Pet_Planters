<template>
    <div class="ransomContainer">
      <div class="paperOverlayLanding"></div>
      <div class="noise"></div>
      <div class="randomBox" @mouseleave="stopGlitch()">
        <div id="ransomizer">
          <div v-for="(letter, index) in letters" :key="index" 
               class="letter-container" @mouseenter="startGlitch(index)" @mouseleave="stopGlitch()">
            
               <span class="letterBox">
            <span v-if="!letter.isSkull" :class="['rww', letter.rotateClass, letter.isStandard ? 'standard-style' : '']" 
                  :style="letter.style">
              {{ letter.char }}
            </span>
            <img v-else src="~/assets/content/images/logos/satori_logo.png" class="skull" :style="letter.skullStyle"/>
            </span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
 
  <script setup>

//   import skull from '~/assets/content/images/demos/fmk/skull.webp'
  
  
  const letters = ref([]);
  const glitchIntervals = ref([]);
  const isSkull = ref(false)
  const backgroundColor = ref('#1ebf74')
  
  const words = "SATORI";
  
  const fontFamilies = [
    "'Verdana', Geneva, sans-serif",
    "'Georgia', serif",
    "'Times New Roman', Times, serif",
    "'Trebuchet MS', Helvetica, sans-serif",
    "'Comic Sans MS', cursive",
    "'Courier', monospace",
    "'Impact', Charcoal, sans-serif",
    "'Arial', Helvetica, sans-serif",
    "'Tahoma', Geneva, sans-serif",
    "'Palatino Linotype', 'Book Antiqua', Palatino, serif"
  ];
  
  const colors = ['#03070a', '#000000', '#ffffff', '#fbffff', '#620d1a', '#030200', '#080207', '#ceffef'];
  const paddingColors = ['#92B9E0', '#ED8849', '#3836D6', '#FAD56E', '#DE91DB', '#FADADF', '#CE1126', '#0C8489', '#006847'];
const bgColors = [
'rgba(146, 185, 224, 0.2)',
  'rgba(175, 96, 214, 0.2)',
  'rgba(56, 54, 214, 0.2)',
  'rgba(250, 213, 110, 0.2)',
  'rgba(222, 145, 219, 0.2)',
  'rgba(250, 218, 223, 0.2)',
  'rgba(206, 17, 38, 0.2)',
  'rgba(12, 132, 137, 0.2)',
  'rgba(0, 104, 71, 0.2)'
];
  
  const bgImages = [
    // 'url(https://i.imgur.com/ruhP2kd.png)',
    // 'url(https://i.imgur.com/EXlM455.png)',
    // 'url(https://i.imgur.com/3EarthF.png)',
    // 'url(https://i.imgur.com/DCLz7wl.png)',
    // 'url(https://i.imgur.com/1wxqouY.png)',
    // 'url(https://i.imgur.com/nIRJZjA.png)',
    // 'url(https://i.imgur.com/pwrAKPo.png)',
    // 'url(https://i.imgur.com/IcV8Q3G.png)',
    // 'url(https://i.imgur.com/6ILZOkO.png)',
    // 'url(https://i.imgur.com/jbMv00O.png)'
  ];
  
  const bgPositions = [
    'left center', 'right bottom', 'center bottom', 'right center', 'left top',
    'center top', 'center center', 'right top', 'left bottom'
  ];


  const randomSkullStyle = () => {
  return {
    transform: `
      translateX(${(Math.random() - 0.5) * 60}px)
      translateY(${(Math.random() - 0.5) * 50}px)
      rotate(${(Math.random() - 0.5) * 60}deg)
      scale(${0.9 + Math.random() * 0.4})
    `,
    transition: 'all 0.1s ease',
  };
};



  
  const randomStyle = () => {
  const style = {
    fontFamily: fontFamilies[Math.floor(Math.random() * fontFamilies.length)],
    fontSize: `${80 + Math.floor(Math.random() * 50)}%`,
    fontWeight: ['lighter', 'normal', 'bold', 'bolder'][Math.floor(Math.random() * 4)],
    fontStyle: Math.random() > 0.5 ? 'italic' : 'normal',
    textTransform: Math.random() > 0.5 ? 'uppercase' : 'lowercase',
    textDecoration: Math.random() > 0.8 ? ['underline', 'line-through'][Math.floor(Math.random() * 2)] : 'none',
    color: colors[Math.floor(Math.random() * colors.length)],
    backgroundColor: paddingColors[Math.floor(Math.random() * paddingColors.length)],
    backgroundImage: bgImages[Math.floor(Math.random() * bgImages.length)],
    backgroundPosition: bgPositions[Math.floor(Math.random() * bgPositions.length)],
    boxShadow: `${Math.random() > 0.5 ? '-' : ''}1px ${Math.random() > 0.5 ? '-' : ''}1px 2px #333`,
    padding: '0.3em 0.25em',
    margin: '0.15em',
    verticalAlign: ['baseline', '1em', '0.25em'][Math.floor(Math.random() * 3)],
    lineHeight: ['0%', '50%', '100%'][Math.floor(Math.random() * 3)],
    display: 'inline-block',
    position: 'relative',
    transform: `
      translateX(${(Math.random() - 0.5) * 30}px)
      translateY(${(Math.random() - 0.5) * 30}px)
      rotate(${(Math.random() - 0.5) * 30}deg)
      scale(${0.8 + Math.random() * 0.4})
    `,
    zIndex: Math.floor(Math.random() * 10),
    transition: `
      font-family 0.1s ease,
      font-size 0.1s ease,
      font-weight 0.1s ease,
      font-style 0.1s ease,
      text-transform 0.1s ease,
      text-decoration 0.1s ease,
      color 0.1s ease,
      padding 0s ease,
      background-color 0s,
        background-color 0s,
        background-image 0.0s,
        background-position 0.0s,
      box-shadow 0,
      margin 0.1s ease,
      vertical-align 0.1s ease,
      line-height 0.1s ease,
      display 0.1s ease,
      position 0.1s ease,
      transform 0.1s ease,
      z-index 0.1s ease
    `
  };
  return style;
};



const randomStyleStandard = () => {
  const style = {
    transform: `
      translateX(${(Math.random() - 0.5) * 50}px)
      translateY(${(Math.random() - 0.5) * 50}px)
      rotate(${(Math.random() - 0.5) * 50}deg)
    `,
    zIndex: Math.floor(Math.random() * 10),
    transition: `
      font-family 0.1s ease,
      font-size 0.1s ease,
      font-weight 0.1s ease,
      font-style 0.1s ease,
      text-transform 0.1s ease,
      text-decoration 0.1s ease,
      color 0.1s ease,
      padding 0s ease,
      background-color 0s,
        background-color 0s,
        background-image 0.0s,
        background-position 0.0s,
      box-shadow 0,
      margin 0.1s ease,
      vertical-align 0.1s ease,
      line-height 0.1s ease,
      display 0.1s ease,
      position 0.1s ease,
      transform 0.1s ease,
      z-index 0.1s ease
    `
  };
  return style;
};



const startGlitch = (index) => {
  if (letters.value[index].char === ' ') return;

  stopAnimateAllLetters();


  backgroundColor.value = bgColors[index]
  
  if (!glitchIntervals.value[index]) {
    glitchIntervals.value[index] = setInterval(() => {
        stopAnimateAllLetters();
        letters.value[index].isSkull = Math.random() > 0.8;
    
    if (letters.value[index].isSkull) {
      letters.value[index].skullStyle = randomSkullStyle();
    } else {
      letters.value[index].style = randomStyle();
      letters.value[index].isStandard = false;
    }
    }, 150 + Math.random() * 50);
  }
};

const stopGlitch = () => {
  letters.value.forEach((letter, index) => {
    if (glitchIntervals.value[index]) {
      clearInterval(glitchIntervals.value[index]);
      glitchIntervals.value[index] = null;
    }
    letter.style = {};
    letter.isStandard = true;
    letter.isSkull = false;
  });
  
  backgroundColor.value = "#1ebf74";
  stopAnimateAllLetters();
  animateAllLetters();
};


const animationTimeout = ref(null);
const standardAnimationTimeout = ref(null);

const animateAllLetters = () => {

  
  
  const nonSpaceIndices = letters.value
    .map((letter, index) => letter.char !== ' ' ? index : -1)
    .filter(index => index !== -1);

  const animateRandomLetter = () => {
    if (nonSpaceIndices.length === 0) return;

    const availableIndices = nonSpaceIndices.filter(index => !glitchIntervals.value[index]);
    if (availableIndices.length === 0) return;

    const randomIndex = Math.floor(Math.random() * availableIndices.length);
    const letterIndex = availableIndices[randomIndex];

    letters.value[letterIndex].isSkull = Math.random() > 0.8;
    
    if (letters.value[letterIndex].isSkull) {
      letters.value[letterIndex].skullStyle = randomSkullStyle();
      letters.value[letterIndex].isStandard = false;
    } else {
      letters.value[letterIndex].style = randomStyle();
      letters.value[letterIndex].isStandard = false;
    }

    // Return to standard style after 500ms
    setTimeout(() => {
        letters.value[letterIndex].style = {};
        letters.value[letterIndex].isStandard = true;
        letters.value[letterIndex].isSkull = false;
    }, 450  + Math.random() * 200);

    animationTimeout.value = setTimeout(animateRandomLetter, 600 + Math.random() * 200);
  };

  const animateStandardLetter = () => {
    const availableIndices = nonSpaceIndices.filter(index => 
      !letters.value[index].isSkull && 
      !glitchIntervals.value[index] && 
      letters.value[index].isStandard
    );

    if (availableIndices.length > 0) {
      const randomIndex = Math.floor(Math.random() * availableIndices.length);
      const letterIndex = availableIndices[randomIndex];

      letters.value[letterIndex].style = randomStyleStandard();
      letters.value[letterIndex].isStandard = true;

      // Return to default standard style after 500ms
      setTimeout(() => {
        if (!glitchIntervals.value[letterIndex]) {
          letters.value[letterIndex].style = {};
          letters.value[letterIndex].isStandard = true;
        }
      }, 1000);
    }

    standardAnimationTimeout.value = setTimeout(animateStandardLetter, 800 + Math.random() * 300);
  };

  animateRandomLetter();
  animateStandardLetter();
};


const stopAnimateAllLetters = () => {
  clearTimeout(animationTimeout.value);
  clearTimeout(standardAnimationTimeout.value);
  animationTimeout.value = null;
  standardAnimationTimeout.value = null;
};

  
onMounted(() => {
  letters.value = words.split('').map(char => ({
    char,
    rotateClass: Math.random() > 0.5 ? 'rr' : 'rl',
    style: {},
    isStandard: true,
    isSkull: false
  }));
  glitchIntervals.value = new Array(letters.value.length).fill(null);

  animateAllLetters();
});
  </script>



  
  <style scoped>

  .ransomContainer{
    padding:20vh 0;
    position: relative;
    overflow:hidden;
    background-color: v-bind(backgroundColor);
    height:80vh;
    display:flex;
    justify-content: center;
    transition: all 0.35s ease;
  }

  .randomBox{
    width:100%;
    height:30vh;
  }

  .noise {
  position: absolute;
  top: -100%;
  left: -50%;
  right: -50%;
  bottom: -50%;
  width: 200%;
  height: 300vh;
  background: transparent url('http://assets.iceable.com/img/noise-transparent.png') repeat 0 0;
  background-repeat: repeat;
  background-size: 30%;
  animation: bg-animation .2s infinite;
  opacity: 0.25;
  visibility: visible;
  z-index:0
}

@keyframes bg-animation {
    0% { transform: translate(0,0) }
    10% { transform: translate(-5%,-5%) }
    20% { transform: translate(-10%,5%) }
    30% { transform: translate(5%,-10%) }
    40% { transform: translate(-5%,15%) }
    50% { transform: translate(-10%,5%) }
    60% { transform: translate(15%,0) }
    70% { transform: translate(0,10%) }
    80% { transform: translate(-15%,0) }
    90% { transform: translate(10%,5%) }
    100% { transform: translate(5%,0) }
}

#ransomizer {
    font-size: 3em;
    line-height: normal;
    position: absolute;
    height: 20vh;
    text-align: center;
    width:100vw;
  }

  .letter-container {
    display: inline-block;
    width: 1.95em;
    height: 0em;
    position: relative;
    z-index:1;
  }

  #ransomizer .rww {
    display: block;
    white-space: pre;
  }

  .letterBox{
    padding: .55em 0;
    z-index:10;
  }



  .standard-style {
    font-size: 4rem;
    font-weight: normal;
    font-style: normal;
    text-transform: none;
    text-decoration: none;
    color: #fff;
    background-color:transparent;
    box-shadow: none;
    padding: 1.75em 0;
    line-height: 0rem;
    vertical-align: baseline;
    letter-spacing:0;
    display: inline-block;
    position: relative;
    transform: none;
    z-index: 1;
    transition:
    font-family 0.1s ease,
    font-size 0.1s ease,
    font-weight 0.1s ease,
    font-style 0.1s ease,
    text-transform 0.1s ease,
    text-decoration 0.1s ease,
    color 0.1s ease,
    background-color 0s,
    background-image 0.0s,
    background-position 0.0s,
    box-shadow 0 ease,
    margin 0.1s ease,
    padding 0s,
    vertical-align 0.1s ease,
    line-height 0.1s ease,
    display 0.1s ease,
    position 0.1s ease,
    transform 0.1s ease,
    z-index 0.1s ease;
}

  .skull {
  width: 1.25em;
  height: 1.25em;
  vertical-align: middle;
  display: inline-block;
}





@media only screen and (min-width: 0px) and (max-width: 376px) {

  .standard-style {
    font-size: 3rem;
}

.letter-container {
    width: 2.2em;
  }
  .skull {
  width: 1em;
  height: 1em;
}

#ransomizer {
    font-size: 0.8em;
  }

  .ransomContainer{
    margin-top:10vh;
    height:50vh;
  }


}
  
@media only screen and (min-width: 376px) and (max-width: 576px) {
  .standard-style {
    font-size: 3.35rem;
}

.letter-container {
    width: 2.55em;
  }
  .skull {
  width: 1.5em;
  height: 1.5em;
}

#ransomizer {
    font-size: 1em;
  }

  .ransomContainer{
    margin-top:10vh;
    height:50vh;
  }

}

@media only screen and (min-width: 576px) and (max-width: 768px) {
  .standard-style {
    font-size: 4rem;
}

.letter-container {
    width: 2.35em;
  }
  .skull {
  width: 2em;
  height: 2em;
}

#ransomizer {
    font-size: 1.5em;
  }

  .ransomContainer{
    margin-top:10vh;
    height:50vh;
  }

}

@media only screen and (min-width: 768px) and (max-width: 992px) {
  .standard-style {
    font-size: 5.6rem;
}

.letter-container {
    width: 2.35em;
  }
  .skull {
  width: 2em;
  height: 2em;
}

#ransomizer {
    font-size: 1.75em;
  }

  .ransomContainer{
    margin-top:20vh;
    height:50vh;
  }

}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}


@media only screen and (min-width: 1600px) and (max-width: 2000px) {
}

@media only screen and (min-width: 2000px) and (max-width: 2500px) {
}

@media only screen and (min-width: 2500px) and (max-width: 5600px) {
}





  </style>