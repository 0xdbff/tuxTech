# First stage: "builder"
FROM node:latest as builder

WORKDIR /app

COPY tuxTech/src/website/package*.json ./
RUN npm install
COPY tuxTech/src/website/ ./
RUN npm run build

# Second stage: "production"
FROM nginx:latest

COPY --from=builder /app/build /var/www/TuxTech/
COPY reverse-proxy.nginx /etc/nginx/conf.d/default.conf
COPY options-ssl-nginx.conf /etc/letsencrypt/options-ssl-nginx.conf
COPY tuxTech/static /var/www/TuxTech/static
COPY tuxTech/media /var/www/TuxTech/media
