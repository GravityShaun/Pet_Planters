<template>
  <div>
    <WebsiteSectionsHeaderBar />
    <NuxtLayout :name="layout">
 

      <div class="background">
        <div class="paperOverlay"></div>
        <GridBackground />
        
        <!-- Hero Section -->
        <ServiceItemsServiceHero 
          :service="service" 
          @scroll-to-details="scrollToDetails"
        />

        <!-- Service Details Section -->
        <ServiceItemsServiceDetails 
          :service="service" 
          ref="detailsRef"
        />

        <!-- CTA Section -->
        <ServiceItemsServiceCTA :service="service" />

        <!-- Related Services -->
        <ServiceItemsRelatedServices 
          :service="service" 
          :related-services="relatedServices"
        />
      </div>
      <WebsiteSectionsFooter/>
    </NuxtLayout>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const route = useRoute()
const layout = "public"

// Ref for scroll functionality
const detailsRef = ref(null)

// Service data (matching the ItemsGrid component)
const portfolioItems = [
  { 
    id: '01', 
    class: 'grid-item-01', 
    bgColor: '#a15e3c',
    icon: '🔧', 
    title: 'Drywall Repair & Patching', 
    description: 'Professional drywall installation, hole repair, texture matching, and patching for water damage or wear. Includes priming and paint touch-ups.',
    priceRange: '$80-250',
    duration: '2-4 hours',
    category: 'REPAIRS',
    visible: true
  },
  { 
    id: '03', 
    class: 'grid-item-03', 
    bgColor: '#04251b',
    icon: '🪚', 
    title: 'Trim & Molding Installation', 
    description: 'Crown molding, baseboards, door casings, and window trim installation. Custom cuts, precision fitting, and professional finishing.',
    priceRange: '$150-400',
    duration: '3-6 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '05', 
    class: 'grid-item-05', 
    bgColor: '#c88562',
    icon: '💡', 
    title: 'Light Fixture Installation', 
    description: 'Ceiling fans, chandeliers, recessed lighting, and switch replacements. Includes electrical safety checks and proper mounting.',
    priceRange: '$100-300',
    duration: '1-3 hours',
    category: 'ELECTRICAL',
    visible: true
  },
  { 
    id: '06', 
    class: 'grid-item-06', 
    bgColor: '#e7c6b3',
    icon: '🚿', 
    title: 'Faucet & Fixture Repair', 
    description: 'Leaky faucet repairs, toilet fixes, showerhead installation, and basic plumbing maintenance. Quick diagnosis and reliable solutions.',
    priceRange: '$75-200',
    duration: '1-2 hours',
    category: 'PLUMBING',
    visible: true
  },
  { 
    id: '09', 
    class: 'grid-item-09', 
    bgColor: '#04251b',
    icon: '🎨', 
    title: 'Interior Painting', 
    description: 'Room painting, accent walls, cabinet refinishing, and touch-up work. Quality prep work, premium paints, and clean finish.',
    priceRange: '$150-400/room',
    duration: '1-2 days',
    category: 'PAINTING',
    visible: true
  },
  { 
    id: '11', 
    class: 'grid-item-11', 
    bgColor: '#a15e3c',
    icon: '🚪', 
    title: 'Door & Window Services', 
    description: 'Door hanging, window caulking, weatherstripping, lock installation, and hardware replacement. Improved security and energy efficiency.',
    priceRange: '$100-350',
    duration: '2-4 hours',
    category: 'REPAIRS',
    visible: true
  },
  { 
    id: '13', 
    class: 'grid-item-13', 
    bgColor: '#c88562',
    icon: '📦', 
    title: 'Furniture Assembly', 
    description: 'IKEA, Wayfair, and custom furniture assembly. Bed frames, desks, shelving units, and complex multi-piece installations.',
    priceRange: '$60-150',
    duration: '1-3 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '17', 
    class: 'grid-item-17', 
    bgColor: '#e7c6b3',
    icon: '🏠', 
    title: 'Deck & Fence Repairs', 
    description: 'Deck board replacement, railing repairs, fence post stabilization, and staining. Extends outdoor structure lifespan.',
    priceRange: '$120-450',
    duration: '2-6 hours',
    category: 'OUTDOOR',
    visible: true
  },
  { 
    id: '20', 
    class: 'grid-item-20', 
    bgColor: '#04251b',
    icon: '⚡', 
    title: 'Home Maintenance Package', 
    description: 'Seasonal maintenance including gutter cleaning, caulk renewal, HVAC filter changes, and preventive repairs. Keep your home in top condition.',
    priceRange: '$200-500',
    duration: '3-5 hours',
    category: 'MAINTENANCE',
    visible: true
  },
  { 
    id: '21', 
    class: 'grid-item-21', 
    bgColor: '#c88562',
    icon: '🔨', 
    title: 'Kitchen Cabinet Hardware', 
    description: 'Cabinet handle and knob installation, drawer slide replacement, soft-close hinges, and cabinet door adjustments.',
    priceRange: '$90-280',
    duration: '2-4 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '23', 
    class: 'grid-item-23', 
    bgColor: '#e7c6b3',
    icon: '🪟', 
    title: 'Window Blind Installation', 
    description: 'Custom blind mounting, cordless options, motorized systems, and window treatment hardware. Perfect fit guaranteed.',
    priceRange: '$80-200/window',
    duration: '1-2 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '25', 
    class: 'grid-item-25', 
    bgColor: '#04251b',
    icon: '🧰', 
    title: 'Garage Organization', 
    description: 'Wall-mounted storage systems, pegboard installation, overhead racks, and tool organization solutions.',
    priceRange: '$180-450',
    duration: '3-6 hours',
    category: 'ORGANIZATION',
    visible: true
  },
  { 
    id: '26', 
    class: 'grid-item-26', 
    bgColor: '#a15e3c',
    icon: '🌡️', 
    title: 'Thermostat Installation', 
    description: 'Smart thermostat setup, programmable controls, WiFi connectivity, and HVAC system compatibility checks.',
    priceRange: '$120-250',
    duration: '1-2 hours',
    category: 'ELECTRICAL',
    visible: true
  },
  { 
    id: '29', 
    class: 'grid-item-29', 
    bgColor: '#e7c6b3',
    icon: '🔒', 
    title: 'Home Security Upgrades', 
    description: 'Deadbolt installation, security camera mounting, motion sensor lights, and smart doorbell setup.',
    priceRange: '$100-350',
    duration: '2-4 hours',
    category: 'ELECTRICAL',
    visible: true
  },
  { 
    id: '31', 
    class: 'grid-item-31', 
    bgColor: '#c88562',
    icon: '🛠️', 
    title: 'Closet Organization', 
    description: 'Custom shelving systems, closet rod installation, shoe racks, and storage optimization solutions.',
    priceRange: '$150-400',
    duration: '3-5 hours',
    category: 'ORGANIZATION',
    visible: true
  },
  { 
    id: '33', 
    class: 'grid-item-33', 
    bgColor: '#04251b',
    icon: '🏡', 
    title: 'Bathroom Accessories', 
    description: 'Towel bars, toilet paper holders, shower caddies, and medicine cabinet installation. Complete bathroom setup.',
    priceRange: '$75-180',
    duration: '1-3 hours',
    category: 'ASSEMBLY',
    visible: true
  },
  { 
    id: '37', 
    class: 'grid-item-37', 
    bgColor: '#a15e3c',
    icon: '🌿', 
    title: 'Outdoor Project Assembly', 
    description: 'Patio furniture, grills, planters, and outdoor storage shed assembly. Weather-resistant installation.',
    priceRange: '$100-300',
    duration: '2-5 hours',
    category: 'OUTDOOR',
    visible: true
  },
  { 
    id: '40', 
    class: 'grid-item-40', 
    bgColor: '#e7c6b3',
    icon: '📺', 
    title: 'TV & Electronics Mounting', 
    description: 'Wall-mounted TVs, soundbar installation, cable management, and entertainment center setup. Clean, professional finish.',
    priceRange: '$120-280',
    duration: '2-3 hours',
    category: 'ELECTRICAL',
    visible: true
  },
]

// Find current service
const service = computed(() => {
  return portfolioItems.find(item => item.id === route.params.id)
})

// Related services (same category first, then others, excluding current)
const relatedServices = computed(() => {
  if (!service.value) return []
  
  // First get services from same category
  const sameCategory = portfolioItems
    .filter(item => item.category === service.value.category && item.id !== service.value.id)
  
  // If we need more services, get from other categories
  const otherCategories = portfolioItems
    .filter(item => item.category !== service.value.category && item.id !== service.value.id)
  
  // Combine them and take first 3
  const allRelated = [...sameCategory, ...otherCategories]
  
  return allRelated.slice(0, 3)
})

// SEO
useHead(() => ({
  title: service.value ? `${service.value.title} - Joel's Handy Services` : 'Service Not Found',
  meta: [
    { name: 'description', content: service.value?.description || 'Professional handyman services' }
  ]
}))

// 404 redirect if service not found
if (!service.value) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Service Not Found'
  })
}

// Smooth scroll to details section
function scrollToDetails() {
  if (detailsRef.value) {
    detailsRef.value.$el.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  }
}
</script>

<style scoped>
.background {
  background-color: #fff;
  min-height: 100vh;
  width: 100vw;
  position: relative;
  z-index: 0;
  border-bottom: 1px solid #293b2e;
}
</style>