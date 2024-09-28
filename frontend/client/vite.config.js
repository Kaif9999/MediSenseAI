import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: 'Health-AI', // Replace 'your-repo-name' with your actual repository name
});
