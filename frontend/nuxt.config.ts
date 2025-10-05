import wasm from 'vite-plugin-wasm';
import topLevelAwait from 'vite-plugin-top-level-await';

export default defineNuxtConfig({
  devtools: { enabled: false },
  ssr: true,

  app: {
    buildAssetsDir: '/_nuxt/',
    head: {
      htmlAttrs: {
        lang: 'en',
      },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      ]
    }
  },

  css: [
    '~/assets/css/main.css',
  ],

  modules: [
    '@vueuse/nuxt',
    '@vueuse/motion/nuxt',
    ['nuxt-mail', {
      message: {
        from: 'shaun@gravitylabs.lol', // Ensure this field is set
        to: ['shaun@gravitylabs.lol'],
      },
      smtp: {
        host: "mail.spacemail.com",
        port: 465,
        auth: {
          user: 'shaun@gravitylabs.lol',
          pass: 'F9D7DEb3-51B0-4f36-994e-f8c157159f1D',
        },
      },
    }],
  ],

  build: {
    transpile: ['gsap', 'swiper'],
  },

  nitro: {
    preset: 'digital-ocean',
  },

  runtimeConfig: {
    public: {
      flask_url: process.env.FLASK_URL
    }
  },

  plugins: [
    '~/plugins/smoothScroller.js',
    '~/plugins/underline.client.js'
  ],

  devServer: {
    port: 3000,
    host: '127.0.0.1',
  },



  vite: {
    plugins: [
      wasm(),
      topLevelAwait()
    ],
    worker: {
      format: 'es', // Switch to the es format
      plugins: () => [wasm(), topLevelAwait()],
    },
    build: {
      chunkSizeWarningLimit: 1000,
      target: 'esnext',
      rollupOptions: {
        output: {
          format: 'es', // Ensure using the "es" module format
        },
      },
    },
    server: {
      fs: {
        strict: false // prevents this error ------>> The request url "index.mjs" is outside of Vite serving allow list.
      },
    },
    optimizeDeps: {
      exclude: [
        'three', // to prevent Vite's code chunking which causes an error
      ],
      esbuildOptions: {
        target: 'esnext', // Three.js uses top-level await
      },
    },
  },

  compatibilityDate: '2024-08-09',


});
