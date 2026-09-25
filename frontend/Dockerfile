# Stage 1: Build React/Vite application
FROM node:22-alpine AS build

WORKDIR /app

# Install dependencies first for better Docker caching
COPY package*.json ./
RUN npm ci

# Copy frontend source code
COPY . .

# Create production build
RUN npm run build


# Stage 2: Serve React application using Nginx
FROM nginx:1.27-alpine

# Copy Vite production build
COPY --from=build /app/dist /usr/share/nginx/html

# Use our Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
