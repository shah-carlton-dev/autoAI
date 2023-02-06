import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react({
      include: ['**/*.js',
                '**/*.jsx',
                '**/*.css'],
    })
  ],
  server: {
    watch: {
      usePolling: true
    }
  }
})
