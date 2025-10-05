<template>
  <div>
    <WebsiteSectionsHeaderBar />
    <NuxtLayout :name="layout">
 

      <div class="background">
        <GridBackground />
        <div class="paperOverlay"></div>

        <MerchItemsMerchDetails
          :product="product"
          ref="detailsRef"
        />
        
      
        <!-- Product Details Section -->
        <MerchItemsProductGallery 
          :product="product" 
          ref="detailsRef"
        />


        <!-- Related Products -->
        <MerchItemsRelatedMerch 
          :product="product" 
          :related-products="relatedProducts"
        />
      </div>
      <WebsiteSectionsFooter/>
    </NuxtLayout>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import merch_1 from '~/assets/content/images/merch/merch_1.png'
import merch_10 from '~/assets/content/images/merch/merch_10.png'
import merch_4 from '~/assets/content/images/merch/merch_4.png'
import merch_6 from '~/assets/content/images/merch/merch_6.png'
import merch_7 from '~/assets/content/images/merch/merch_7.png'
import merch_8 from '~/assets/content/images/merch/merch_8.png'
import merch_9 from '~/assets/content/images/merch/merch_9.png'

const route = useRoute()
const layout = "public"

// Ref for scroll functionality
const detailsRef = ref(null)

// Merchandise data
const merchItems = [
  {
    id: '01',
    class: 'grid-item-01',
    bgColor: '#a15e3c',
    icon: '👕',
    title: 'Long Sleeve',
    description: 'Look cool and formal whether you are at church or drinking with the boys under the bridge. Always be prepared.',
    price: '$34.99',
    sizes: ['S', 'M', 'L', 'XL', 'XXL'],
    colors: ['Navy', 'Forest Green', 'Charcoal'],
    category: 'APPAREL',
    inStock: true,
    images: [merch_1, merch_1]
  },
  {
    id: '02',
    class: 'grid-item-02',
    bgColor: '#04251b',
    icon: '🧢',
    title: 'Hats & Beanies',
    description: 'For when you need to hide that "I just rolled out of bed to fix the sink" hair. Warning: May make you look surprisingly competent.',
    price: '$24.99',
    sizes: ['One Size'],
    colors: ['Navy', 'Black', 'Khaki'],
    category: 'APPAREL',
    inStock: true,
    images: [merch_4, merch_4]
  },
  {
    id: '03',
    class: 'grid-item-03',
    bgColor: '#c88562',
    icon: '🎵',
    title: 'Mix Tapes',
    description: 'Joel\'s greatest hits featuring "Hammer Time" and "Another Nail in the Wall." Side B includes his emotional ballad "I Left My Wrench at Your Place."',
    price: '$19.99',
    sizes: ['Standard'],
    colors: ['Classic Black'],
    category: 'ACCESSORIES',
    inStock: true,
    images: [merch_10, merch_10]
  },
  {
    id: '04',
    class: 'grid-item-04',
    bgColor: '#e7c6b3',
    icon: '🛼',
    title: 'Roller Blades',
    description: 'Get to job sites 47% faster while looking absolutely ridiculous. Perfect for the handyman who values efficiency over dignity.',
    price: '$89.99',
    sizes: ['7', '8', '9', '10', '11', '12'],
    colors: ['Classic White'],
    category: 'ACCESSORIES',
    inStock: true,
    images: [merch_6, merch_6]
  },
  {
    id: '05',
    class: 'grid-item-05',
    bgColor: '#04251b',
    icon: '👕',
    title: 'T-Shirts',
    description: 'Comes pre-stained with paint, caulk, and regret. Machine washable, but why would you? It adds character.',
    price: '$29.99',
    sizes: ['S', 'M', 'L', 'XL', 'XXL'],
    colors: ['White', 'Navy', 'Forest Green'],
    category: 'APPAREL',
    inStock: true,
    images: [merch_7, merch_7]
  },
  {
    id: '06',
    class: 'grid-item-06',
    bgColor: '#a15e3c',
    icon: '🏓',
    title: 'Pickle Ball Paddles',
    description: 'For when fixing houses doesn\'t provide enough mid-life crisis energy. Also doubles as a flyswatter in emergencies.',
    price: '$44.99',
    sizes: ['Standard'],
    colors: ['Classic Wood'],
    category: 'ACCESSORIES',
    inStock: true,
    images: [merch_8, merch_8]
  },
  {
    id: '07',
    class: 'grid-item-07',
    bgColor: '#c88562',
    icon: '☂️',
    title: 'Umbrella',
    description: 'It can get wet when joel is not around so make sure you dont slip and buy an umbrella!',
    price: '$39.99',
    sizes: ['One Size'],
    colors: ['Navy', 'Black'],
    category: 'ACCESSORIES',
    inStock: true,
    images: [merch_9, merch_9]
  }
]

// Find current product
const product = computed(() => {
  return merchItems.find(item => item.id === route.params.id)
})

// Related products (same category first, then others, excluding current)
const relatedProducts = computed(() => {
  if (!product.value) return []
  
  // First get products from same category
  const sameCategory = merchItems
    .filter(item => item.category === product.value.category && item.id !== product.value.id)
  
  // If we need more products, get from other categories
  const otherCategories = merchItems
    .filter(item => item.category !== product.value.category && item.id !== product.value.id)
  
  // Combine them and take first 3
  const allRelated = [...sameCategory, ...otherCategories]
  
  return allRelated.slice(0, 3)
})

// SEO
useHead(() => ({
  title: product.value ? `${product.value.title} - Joel's Handys Merchandise` : 'Product Not Found',
  meta: [
    { name: 'description', content: product.value?.description || 'Official Joel\'s Handys merchandise and branded items' }
  ]
}))

// 404 redirect if product not found
if (!product.value) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Product Not Found'
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
  z-index: 1;
  border-bottom: 1px solid #293b2e;
}
</style>