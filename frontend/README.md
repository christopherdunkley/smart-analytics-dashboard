### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Install Tailwind css and its dependencies
npm install -D tailwindcss@3.3.3 postcss@8.4.27 autoprefixer@10.4.14

# Initialise Tailwind
npx tailwindcss init -p

# Create or edit .vscode/settings.json and add:
{
  "files.associations": {
    "*.css": "tailwindcss"
  }
}

# Start the development server
npm run dev

# View Smart Analytics Dashboard Frontend
Follow the link provided after running the above command, as below:

    Local:   http://localhost:5173/

# React + Vite
This template provides minimal setup to get React working in Vite with HMR, and some ESLint rules.

Currently, there are 2 official plugins available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
