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
      '/': {
        target: 'https://localhost:44305',
        changeOrigin: true,
        secure: false,      
        ws: true,
       }
    }
  }
})
