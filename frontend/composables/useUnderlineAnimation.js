import { gsap } from 'gsap';

export function useUnderlineAnimation() {
  // Ensure DOM APIs exist (client-only)
  const isBrowser = typeof window !== 'undefined' && typeof document !== 'undefined';

  async function waitForFontsReady() {
    try {
      if (isBrowser && document.fonts && document.fonts.ready) {
        await document.fonts.ready;
      }
    } catch (_) {
      // Ignore font readiness errors; fall back to proceeding
    }
  }

  function waitForLayoutStable(element, maxFrames = 60) {
    return new Promise((resolve) => {
      if (!isBrowser) return resolve();
      let tries = 0;
      function check() {
        tries += 1;
        const width = element?.offsetWidth || 0;
        if (width > 0 || tries >= maxFrames) {
          resolve();
        } else {
          requestAnimationFrame(check);
        }
      }
      requestAnimationFrame(check);
    });
  }
  // Add noise/jitter to path coordinates for hand-drawn effect
  function addNoiseToPath(pathData, intensity = 0.8) {
    return pathData.replace(/([0-9]+\.?[0-9]*)/g, (match) => {
      const num = parseFloat(match);
      const noise = (Math.random() - 0.5) * intensity;
      return (num + noise).toFixed(3);
    });
  }

  // Generate random stroke-width variation
  function getRandomStrokeWidth(baseWidth = 10) {
    const variation = (Math.random() - 0.5) * 2; // ±1 variation
    return Math.max(8, Math.min(12, baseWidth + variation));
  }

  const svgVariants = [
    `<svg width="310" height="40" viewBox="0 0 310 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5 20.9999C26.7762 16.2245 49.5532 11.5572 71.7979 14.6666C84.9553 16.5057 97.0392 21.8432 109.987 24.3888C116.413 25.6523 123.012 25.5143 129.042 22.6388C135.981 19.3303 142.586 15.1422 150.092 13.3333C156.799 11.7168 161.702 14.6225 167.887 16.8333C181.562 21.7212 194.975 22.6234 209.252 21.3888C224.678 20.0548 239.912 17.991 255.42 18.3055C272.027 18.6422 288.409 18.867 305 17.9999" stroke="currentColor" stroke-width="10" stroke-linecap="round"/></svg>`,
    `<svg width="310" height="40" viewBox="0 0 310 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5 24.2592C26.233 20.2879 47.7083 16.9968 69.135 13.8421C98.0469 9.5853 128.407 4.02322 158.059 5.14674C172.583 5.69708 187.686 8.66104 201.598 11.9696C207.232 13.3093 215.437 14.9471 220.137 18.3619C224.401 21.4596 220.737 25.6575 217.184 27.6168C208.309 32.5097 197.199 34.281 186.698 34.8486C183.159 35.0399 147.197 36.2657 155.105 26.5837C158.11 22.9053 162.993 20.6229 167.764 18.7924C178.386 14.7164 190.115 12.1115 201.624 10.3984C218.367 7.90626 235.528 7.06127 252.521 7.49276C258.455 7.64343 264.389 7.92791 270.295 8.41825C280.321 9.25056 296 10.8932 305 13.0242" stroke="#E55050" stroke-width="10" stroke-linecap="round"/></svg>`,
    `<svg width="310" height="40" viewBox="0 0 310 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5 29.5014C9.61174 24.4515 12.9521 17.9873 20.9532 17.5292C23.7742 17.3676 27.0987 17.7897 29.6575 19.0014C33.2644 20.7093 35.6481 24.0004 39.4178 25.5014C48.3911 29.0744 55.7503 25.7731 63.3048 21.0292C67.9902 18.0869 73.7668 16.1366 79.3721 17.8903C85.1682 19.7036 88.2173 26.2464 94.4121 27.2514C102.584 28.5771 107.023 25.5064 113.276 20.6125C119.927 15.4067 128.83 12.3333 137.249 15.0014C141.418 16.3225 143.116 18.7528 146.581 21.0014C149.621 22.9736 152.78 23.6197 156.284 24.2514C165.142 25.8479 172.315 17.5185 179.144 13.5014C184.459 10.3746 191.785 8.74853 195.868 14.5292C199.252 19.3205 205.597 22.9057 211.621 22.5014C215.553 22.2374 220.183 17.8356 222.979 15.5569C225.4 13.5845 227.457 11.1105 230.742 10.5292C232.718 10.1794 234.784 12.9691 236.164 14.0014C238.543 15.7801 240.717 18.4775 243.356 19.8903C249.488 23.1729 255.706 21.2551 261.079 18.0014C266.571 14.6754 270.439 11.5202 277.146 13.6125C280.725 14.7289 283.221 17.209 286.393 19.0014C292.321 22.3517 298.255 22.5014 305 22.5014" stroke="#E55050" stroke-width="10" stroke-linecap="round"/></svg>`,
    `<svg width="310" height="40" viewBox="0 0 310 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M17.0039 32.6826C32.2307 32.8412 47.4552 32.8277 62.676 32.8118C67.3044 32.807 96.546 33.0555 104.728 32.0775C113.615 31.0152 104.516 28.3028 102.022 27.2826C89.9573 22.3465 77.3751 19.0254 65.0451 15.0552C57.8987 12.7542 37.2813 8.49399 44.2314 6.10216C50.9667 3.78422 64.2873 5.81914 70.4249 5.96641C105.866 6.81677 141.306 7.58809 176.75 8.59886C217.874 9.77162 258.906 11.0553 300 14.4892" stroke="#E55050" stroke-width="10" stroke-linecap="round"/></svg>`,
    `<svg width="310" height="40" viewBox="0 0 310 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.99805 20.9998C65.6267 17.4649 126.268 13.845 187.208 12.8887C226.483 12.2723 265.751 13.2796 304.998 13.9998" stroke="currentColor" stroke-width="10" stroke-linecap="round"/></svg>`,
    `<svg width="310" height="40" viewBox="0 0 310 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5 29.8857C52.3147 26.9322 99.4329 21.6611 146.503 17.1765C151.753 16.6763 157.115 15.9505 162.415 15.6551C163.28 15.6069 165.074 15.4123 164.383 16.4275C161.704 20.3627 157.134 23.7551 153.95 27.4983C153.209 28.3702 148.194 33.4751 150.669 34.6605C153.638 36.0819 163.621 32.6063 165.039 32.2029C178.55 28.3608 191.49 23.5968 204.869 19.5404C231.903 11.3436 259.347 5.83254 288.793 5.12258C294.094 4.99476 299.722 4.82265 305 5.45025" stroke="#E55050" stroke-width="10" stroke-linecap="round"/></svg>`
  ];

  function decorateSVG(svgEl) {
    svgEl.setAttribute("class", "text-draw__box-svg");
    svgEl.setAttribute("preserveAspectRatio", "none");
    svgEl.querySelectorAll("path").forEach((path) => {
      path.setAttribute("stroke", "currentColor");
    });
  }

  function getLastLineWidth(element) {
    const text = element.textContent.trim();
    const words = text.split(/\s+/).filter(word => word.length > 0);

    if (words.length === 0) return 100;

    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');

    // Get computed styles to match font
    const computedStyle = window.getComputedStyle(element);
    context.font = `${computedStyle.fontWeight} ${computedStyle.fontSize} ${computedStyle.fontFamily}`;

    const maxWidth = element.offsetWidth;
    let lines = [];
    let currentLine = '';

    console.log('Text:', text);
    console.log('Max width:', maxWidth);
    console.log('Font:', context.font);

    // Simulate text wrapping to find where lines break
    // Add small buffer to account for rendering differences
    const wrapThreshold = maxWidth - 5;

    for (let i = 0; i < words.length; i++) {
      const testLine = currentLine + (currentLine ? ' ' : '') + words[i];
      const testWidth = context.measureText(testLine).width;

      console.log(`Testing: "${testLine}" - width: ${testWidth}`);

      if (testWidth > wrapThreshold && currentLine) {
        lines.push(currentLine);
        console.log(`Line break - added line: "${currentLine}"`);
        currentLine = words[i];
      } else {
        currentLine = testLine;
      }
    }

    if (currentLine) {
      lines.push(currentLine);
    }

    console.log('All lines:', lines);

    // Get the last line text
    const lastLine = lines[lines.length - 1] || text;

    const lastLineWidth = context.measureText(lastLine).width;

    console.log('Last line:', lastLine);
    console.log('Last line width:', lastLineWidth);

    // Return width of last line as percentage of container width, ensuring it doesn't exceed 100%
    // Add 5% buffer to account for font rendering differences
    const percentage = Math.min(100, Math.max(20, (lastLineWidth / maxWidth) * 100 + 5));

    console.log('Percentage:', percentage);

    return percentage;
  }

  async function initUnderlineAnimation(containerSelectorOrEl = "[data-draw-line]", options = {}) {
    const {
      autoAnimate = true,
      duration = 1.2,
      ease = "power2.inOut",
      delay = 0.85,
      strokeColor = '#56badb'
    } = options;

    if (!isBrowser) return;

    const container = typeof containerSelectorOrEl === 'string'
      ? document.querySelector(containerSelectorOrEl)
      : containerSelectorOrEl;
    const box = container?.querySelector("[data-draw-line-box]");
    
    if (!container) {
      console.error('Underline animation: Container not found for:', containerSelectorOrEl);
      return;
    }
    
    if (!box) {
      console.error('Underline animation: Box element [data-draw-line-box] not found in container');
      return;
    }
    
    // Skip if we've already initialized this container
    if (container.dataset.drawInitialized === '1') {
      return;
    }

    // Wait for fonts and layout to be ready so measurements are accurate on full reload
    await waitForFontsReady();
    await waitForLayoutStable(container);
    
    // Calculate the width of the last line
    const lastLineWidthPercent = getLastLineWidth(container);
    
    const randomIndex = Math.floor(Math.random() * svgVariants.length);
    
    // Apply noise to the selected SVG variant for hand-drawn effect
    let selectedSvg = svgVariants[randomIndex];
    const pathMatch = selectedSvg.match(/d="([^"]+)"/);
    if (pathMatch) {
      const originalPath = pathMatch[1];
      const noisyPath = addNoiseToPath(originalPath);
      selectedSvg = selectedSvg.replace(pathMatch[1], noisyPath);
    }
    
    // Apply random stroke width variation
    const randomStrokeWidth = getRandomStrokeWidth();
    selectedSvg = selectedSvg.replace(/stroke-width="[^"]*"/, `stroke-width="${randomStrokeWidth}"`);
    
    // Reset any existing content to avoid duplication on re-init
    box.innerHTML = '';
    box.innerHTML = selectedSvg;
    const svg = box.querySelector("svg");
    
    if (svg) {
      decorateSVG(svg);
      // Ensure it renders even if component-scoped CSS tries to zero out size
      svg.style.setProperty('display', 'block', 'important');
      svg.style.setProperty('height', '100%', 'important');
      svg.style.setProperty('overflow', 'visible', 'important');
      // Set desired stroke color context
      svg.style.setProperty('color', strokeColor, 'important');
      
      // Set the SVG width to match the last line width with !important to override CSS
      svg.style.setProperty('width', `${lastLineWidthPercent}%`, 'important');
      
      // Get the SVG's viewBox height to calculate proper margin
      const viewBox = svg.getAttribute('viewBox');
      const svgHeight = viewBox ? parseInt(viewBox.split(' ')[3]) : 40; // Default to 40 if no viewBox
      
      // Adjust the container's margin-bottom based on SVG height
      // Normalize to a scale where 40px height = -0.095em margin
      const normalizedMargin = 0.055 * (svgHeight / 40);
      box.style.marginBottom = `${normalizedMargin}em`;
      
      console.log(`SVG height: ${svgHeight}, Adjusted margin: ${normalizedMargin}em`);
      
      const path = svg.querySelector("path");
      
      if (path) {
        const pathLength = path.getTotalLength();
        // Enforce stroke visibility over any !important CSS
        path.style.setProperty('stroke', strokeColor, 'important');
        path.style.setProperty('fill', 'none', 'important');
        // Ensure stroke-width wins over component CSS rules
        const sw = svg.getAttribute('stroke-width') || svg.querySelector('path')?.getAttribute('stroke-width');
        const strokeWidth = sw ? parseFloat(sw) : 10;
        path.style.setProperty('stroke-width', `${strokeWidth}`, 'important');
        
        // Always set initial state
        gsap.set(path, { 
          strokeDasharray: pathLength,
          strokeDashoffset: pathLength,
          opacity: 1,
          mixBlendMode: 'multiply'
        });
        
        // Only animate if autoAnimate is true
        if (autoAnimate) {
          gsap.to(path, {
            duration,
            strokeDashoffset: 0,
            ease,
            delay
          });
        }
        // Mark as initialized to avoid duplicate injections
        container.dataset.drawInitialized = '1';
      } else {
        console.error('Underline animation: Path element not found in SVG');
      }
    }
  }

  return {
    initUnderlineAnimation,
    svgVariants
  };
}