import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react({
      include: ['**/*.js',
                '**/*.jsx',
                '**/*.css',
                '**/*.html'],
    })
  ],
  server: {
    watch: {
      usePolling: true
    },
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: false,
        secure: false,      
        rewrite: (path) => path.replace(/^\/api/, ''),
       }
    }
  }
})
