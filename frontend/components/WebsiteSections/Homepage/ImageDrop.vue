<template>
  <div class="image-drop-section">
    <div class="section-header">
      <h2 class="section-title eikoFont"><i>Start Your Custom Order</i></h2>
      <p class="section-subtitle">Upload photos of your pet and we'll create a beautiful 3D planter just for them</p>
    </div>

    <div class="content-wrapper">
      <!-- Main Upload Column -->
      <div class="upload-column">
        <!-- Upload Card -->
        <div class="upload-card">
          <div class="card-inner">
            <div class="upload-section">
              <h3 class="upload-title">Upload Your Pet Photos</h3>
              <p class="upload-subtitle">Share 3-4 high-quality photos of your beloved pet from different angles</p>
              
              <div 
                class="drop-zone"
                :class="{ 'drag-over': isDragOver, 'has-images': uploadedImages.length > 0 }"
                @drop="handleDrop"
                @dragover.prevent="isDragOver = true"
                @dragleave="isDragOver = false"
                @dragenter.prevent
              >
                <div v-if="uploadedImages.length === 0" class="drop-zone-content">
                  <div class="upload-icon">📸</div>
                  <p class="drop-text">Drag & drop your pet photos here</p>
                  <p class="or-text">or</p>
                  <button class="browse-button" @click="triggerFileInput">Browse Files</button>
                </div>
                
                <div v-else class="image-preview-grid">
                  <div 
                    v-for="(image, index) in uploadedImages" 
                    :key="index"
                    class="image-preview-item"
                  >
                    <img :src="image.url" :alt="`Pet photo ${index + 1}`" class="preview-image">
                    <button class="remove-image" @click="removeImage(index)">×</button>
                  </div>
                  
                  <div 
                    v-if="uploadedImages.length < 4"
                    class="add-more-slot"
                    @click="triggerFileInput"
                  >
                    <div class="add-icon">+</div>
                    <p class="add-text">Add More</p>
                  </div>
                </div>
              </div>
              
              <input 
                ref="fileInput"
                type="file"
                multiple
                accept="image/*"
                @change="handleFileSelect"
                style="display: none"
              >
              
              <div class="upload-info">
                <p class="info-text">{{ uploadedImages.length }}/4 photos uploaded</p>
                <p class="format-text">Supported formats: JPG, PNG, WEBP (Max 10MB each)</p>
              </div>
              
              <button 
                v-if="uploadedImages.length > 0"
                class="upload-button"
                @click="handleUpload"
                :disabled="uploadedImages.length === 0 || isUploading"
              >
                {{ isUploading ? 'Uploading...' : 'Create My Pet Planter' }}
              </button>
            </div>
          </div>
        </div>


        <div class="example-images-card">
          <h3 class="examples-title">Example Photos</h3>
          <div class="example-grid">
            <div class="example-item">
              <div class="example-image-placeholder">
                <span class="placeholder-icon">🐕</span>
                <span class="placeholder-label">Front View</span>
              </div>
            </div>
            <div class="example-item">
              <div class="example-image-placeholder">
                <span class="placeholder-icon">🐕</span>
                <span class="placeholder-label">Side View</span>
              </div>
            </div>
            <div class="example-item">
              <div class="example-image-placeholder">
                <span class="placeholder-icon">🐕</span>
                <span class="placeholder-label">3/4 View</span>
              </div>
            </div>
            <div class="example-item">
              <div class="example-image-placeholder">
                <span class="placeholder-icon">🐕</span>
                <span class="placeholder-label">Close-up</span>
              </div>
            </div>
          </div>
        </div>

      
      </div>

      <!-- Examples Sidebar -->
      <div class="examples-sidebar">
        <div class="examples-card">
          <h3 class="examples-title">📷 Photo Tips</h3>
          <p class="examples-subtitle">Best results come from great photos</p>
          
          <div class="tips-list">
            <div class="tip-item">
              <div class="tip-icon">✓</div>
              <div class="tip-content">
                <h4>Clear Front View</h4>
                <p>Capture your pet facing the camera directly</p>
              </div>
            </div>
            
            <div class="tip-item">
              <div class="tip-icon">✓</div>
              <div class="tip-content">
                <h4>Side Profile</h4>
                <p>Include a side view to capture unique features</p>
              </div>
            </div>
            
            <div class="tip-item">
              <div class="tip-icon">✓</div>
              <div class="tip-content">
                <h4>Good Lighting</h4>
                <p>Natural lighting works best, avoid shadows</p>
              </div>
            </div>
            
            <div class="tip-item">
              <div class="tip-icon">✓</div>
              <div class="tip-content">
                <h4>High Resolution</h4>
                <p>The clearer the photo, the better the result</p>
              </div>
            </div>
          </div>
        </div>

  
          <!-- What Happens Next Card -->
          <div class="process-card">
          <h3 class="examples-title">What Happens Next?</h3>
          <div class="process-steps">
            <div class="process-step">
              <div class="step-number">1</div>
              <p>We review your photos</p>
            </div>
            <div class="process-step">
              <div class="step-number">2</div>
              <p>Create 3D model</p>
            </div>
            <div class="process-step">
              <div class="step-number">3</div>
              <p>Print & assemble</p>
            </div>
            <div class="process-step">
              <div class="step-number">4</div>
              <p>Ship to you!</p>
            </div>
          </div>
        </div>


      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isDragOver = ref(false)
const uploadedImages = ref([])
const fileInput = ref(null)
const isUploading = ref(false)
const uploadError = ref(null)
const uploadSuccess = ref(false)

const triggerFileInput = () => {
  fileInput.value.click()
}

const handleFileSelect = (event) => {
  const files = Array.from(event.target.files)
  processFiles(files)
}

const handleDrop = (event) => {
  event.preventDefault()
  isDragOver.value = false
  const files = Array.from(event.dataTransfer.files)
  processFiles(files)
}

const processFiles = (files) => {
  const imageFiles = files.filter(file => file.type.startsWith('image/'))
  const remainingSlots = 4 - uploadedImages.value.length
  const filesToProcess = imageFiles.slice(0, remainingSlots)
  
  filesToProcess.forEach(file => {
    if (file.size > 10 * 1024 * 1024) { // 10MB limit
      alert('File size must be less than 10MB')
      return
    }
    
    const reader = new FileReader()
    reader.onload = (e) => {
      uploadedImages.value.push({
        file: file,
        url: e.target.result,
        name: file.name
      })
    }
    reader.readAsDataURL(file)
  })
}

const removeImage = (index) => {
  uploadedImages.value.splice(index, 1)
}

const handleUpload = async () => {
  if (uploadedImages.value.length === 0) {
    alert('Please upload at least one image')
    return
  }

  isUploading.value = true
  uploadError.value = null
  uploadSuccess.value = false

  try {
    // Create FormData object
    const formData = new FormData()
    
    // Add all image files to FormData
    uploadedImages.value.forEach((image) => {
      formData.append('files', image.file)
    })
    
    // Add optional metadata
    formData.append('pet_name', 'My Pet') // TODO: Add input field for this
    formData.append('pet_type', 'dog') // TODO: Add input field for this
    formData.append('notes', 'Custom pet planter order') // TODO: Add input field for this

    // Send request to backend (no authentication required for now)
    const response = await fetch('http://localhost:8007/api/images/upload', {
      method: 'POST',
      body: formData
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.detail || 'Upload failed')
    }

    // Success!
    uploadSuccess.value = true
    alert(`Success! Your order has been created.\nOrder ID: ${data.order_id}\n\nWe'll start working on your custom planter!`)
    
    // Clear uploaded images after success
    uploadedImages.value = []

  } catch (error) {
    console.error('Upload error:', error)
    uploadError.value = error.message
    alert(`Upload failed: ${error.message}`)
  } finally {
    isUploading.value = false
  }
}
</script>

<style scoped>
.image-drop-section {
  max-width: 1500px;
  margin: 0 auto;
  padding: 100px 40px 120px;
  min-height: 100vh;
}

.section-header {
  text-align: center;
  margin-bottom: 80px;
}

.section-title {
  font-size: 3.5rem;
  color: #243e2e;
  margin-bottom: 15px;
  text-decoration: underline;
  text-decoration-color: #56badb;
  text-decoration-thickness: 4px;
  text-underline-offset: 10px;
}

.section-subtitle {
  font-size: 1.3rem;
  color: #466151;
  line-height: 1.6;
  max-width: 700px;
  margin: 0 auto;
}

.content-wrapper {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 50px;
  align-items: start;
}

/* Upload Column Styles */
.upload-column {
  display: flex;
  flex-direction: column;
  gap: 35px;
}

/* Upload Card Styles */
.upload-card {
  background: white;
  border-radius: 24px;
  box-shadow: 
    0 20px 60px rgba(36, 62, 46, 0.08),
    0 0 0 1px rgba(70, 97, 81, 0.1);
  overflow: hidden;
  transition: all 0.4s ease;
}

.upload-card:hover {
  box-shadow: 
    0 30px 80px rgba(36, 62, 46, 0.12),
    0 0 0 1px rgba(86, 186, 219, 0.2);
  transform: translateY(-2px);
}

.card-inner {
  padding: 60px;
}

.upload-section {
  text-align: center;
}

.upload-title {
  font-size: 2rem;
  color: #243e2e;
  margin-bottom: 10px;
  font-weight: 600;
}

.upload-subtitle {
  font-size: 1rem;
  color: #466151;
  margin-bottom: 30px;
  line-height: 1.5;
}

.drop-zone {
  border: 3px dashed rgba(86, 186, 219, 0.4);
  border-radius: 16px;
  padding: 40px 20px;
  background: linear-gradient(135deg, rgba(70, 97, 81, 0.05) 0%, rgba(39, 69, 52, 0.05) 100%);
  transition: all 0.3s ease;
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.drop-zone.drag-over {
  border-color: #56badb;
  background: linear-gradient(135deg, rgba(86, 186, 219, 0.1) 0%, rgba(70, 97, 81, 0.1) 100%);
  transform: scale(1.02);
}

.drop-zone.has-images {
  padding: 20px;
  min-height: auto;
}

.drop-zone-content {
  text-align: center;
}

.upload-icon {
  font-size: 3rem;
  margin-bottom: 20px;
}

.drop-text {
  font-size: 1.2rem;
  color: #243e2e;
  margin-bottom: 10px;
  font-weight: 500;
}

.or-text {
  color: #466151;
  margin: 15px 0;
  font-size: 1rem;
}

.browse-button {
  background: linear-gradient(135deg, #56badb 0%, #3f7c49 100%);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.browse-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(86, 186, 219, 0.3);
}

.image-preview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 15px;
  width: 100%;
}

.image-preview-item {
  position: relative;
  aspect-ratio: 1;
  border-radius: 10px;
  overflow: hidden;
  border: 2px solid rgba(86, 186, 219, 0.3);
  transition: all 0.3s ease;
}

.image-preview-item:hover {
  border-color: rgba(86, 186, 219, 0.6);
  transform: scale(1.05);
}

.preview-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.remove-image {
  position: absolute;
  top: 5px;
  right: 5px;
  background: rgba(255, 0, 0, 0.8);
  color: white;
  border: none;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  cursor: pointer;
  font-size: 16px;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.remove-image:hover {
  background: rgba(255, 0, 0, 1);
}

.add-more-slot {
  aspect-ratio: 1;
  border: 2px dashed rgba(86, 186, 219, 0.4);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background: rgba(86, 186, 219, 0.05);
}

.add-more-slot:hover {
  border-color: #56badb;
  background: rgba(86, 186, 219, 0.1);
}

.add-icon {
  font-size: 2rem;
  color: #56badb;
  margin-bottom: 5px;
}

.add-text {
  color: #466151;
  font-size: 0.9rem;
  font-weight: 500;
}

.upload-info {
  margin: 20px 0;
}

.info-text {
  color: #243e2e;
  font-weight: 500;
  margin-bottom: 5px;
}

.format-text {
  color: #466151;
  font-size: 0.9rem;
}

.upload-button {
  background: linear-gradient(135deg, #56badb 0%, #3f7c49 100%);
  color: white;
  border: none;
  padding: 15px 30px;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 20px;
  box-shadow: 0 4px 12px rgba(86, 186, 219, 0.2);
}

.upload-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(86, 186, 219, 0.3);
}

.upload-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Examples Sidebar Styles */
.examples-sidebar {
  display: flex;
  flex-direction: column;
  gap: 35px;
}

.examples-card,
.process-card {
  background: white;
  border-radius: 24px;
  padding: 40px;
  box-shadow: 
    0 15px 40px rgba(36, 62, 46, 0.08),
    0 0 0 1px rgba(70, 97, 81, 0.1);
  transition: all 0.3s ease;
}

.example-images-card {
  background: white;
  border-radius: 20px;
  padding: 25px;
  box-shadow: 
    0 15px 40px rgba(36, 62, 46, 0.08),
    0 0 0 1px rgba(70, 97, 81, 0.1);
  transition: all 0.3s ease;
}

.examples-card:hover,
.example-images-card:hover,
.process-card:hover {
  box-shadow: 
    0 15px 40px rgba(36, 62, 46, 0.1),
    0 0 0 1px rgba(86, 186, 219, 0.15);
  transform: translateY(-2px);
}

.examples-title {
  font-size: 1.7rem;
  color: #243e2e;
  margin-bottom: 24px;
  font-weight: 600;
}

.example-images-card .examples-title {
  font-size: 1.2rem;
  margin-bottom: 15px;
}

.examples-subtitle {
  font-size: 1.05rem;
  color: #466151;
  margin-bottom: 30px;
}

/* Tips List */
.tips-list {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.tip-item {
  display: flex;
  gap: 18px;
  align-items: flex-start;
}

.tip-icon {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #56badb 0%, #3f7c49 100%);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  flex-shrink: 0;
  font-size: 1rem;
}

.tip-content h4 {
  font-size: 1.1rem;
  color: #243e2e;
  margin-bottom: 6px;
  font-weight: 600;
}

.tip-content p {
  font-size: 1rem;
  color: #466151;
  line-height: 1.5;
}

/* Example Images Grid */
.example-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}

.example-item {
  aspect-ratio: 1;
  border-radius: 10px;
  overflow: hidden;
}

.example-image-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(86, 186, 219, 0.1) 0%, rgba(70, 97, 81, 0.1) 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  border: 2px dashed rgba(86, 186, 219, 0.3);
  transition: all 0.3s ease;
}

.example-image-placeholder:hover {
  background: linear-gradient(135deg, rgba(86, 186, 219, 0.15) 0%, rgba(70, 97, 81, 0.15) 100%);
  border-color: rgba(86, 186, 219, 0.5);
}

.placeholder-icon {
  font-size: 1.4rem;
}

.placeholder-label {
  font-size: 0.7rem;
  color: #466151;
  font-weight: 500;
}

/* Process Steps */
.process-steps {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 5px;
}

.process-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 12px;
}

.process-step:nth-child(3),
.process-step:nth-child(4) {
  margin-top: 34px;
}

.step-number {
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, #56badb 0%, #3f7c49 100%);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.4rem;
  box-shadow: 0 6px 20px rgba(86, 186, 219, 0.3);
}

.process-step p {
  font-size: 1rem;
  color: #466151;
  font-weight: 500;
}

@media (max-width: 1200px) {
  .content-wrapper {
    grid-template-columns: 1fr;
    gap: 50px;
  }
  
  .examples-sidebar {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 35px;
  }
  
  .section-title {
    font-size: 2.8rem;
  }
  
  .image-drop-section {
    padding: 80px 30px 100px;
  }
}

@media (max-width: 768px) {
  .image-drop-section {
    padding: 60px 20px 80px;
  }
  
  .section-title {
    font-size: 2.2rem;
  }
  
  .section-subtitle {
    font-size: 1.1rem;
  }
  
  .card-inner {
    padding: 30px 20px;
  }
  
  .upload-title {
    font-size: 1.6rem;
  }
  
  .image-preview-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .drop-zone {
    padding: 30px 15px;
  }
  
  .examples-sidebar {
    grid-template-columns: 1fr;
  }
  
  .examples-card,
  .example-images-card,
  .process-card {
    padding: 25px 20px;
  }
  
  .process-steps {
    grid-template-columns: 1fr;
    gap: 15px;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 1.8rem;
  }
  
  .section-header {
    margin-bottom: 40px;
  }
  
  .example-grid {
    grid-template-columns: 1fr;
  }
}
</style>
