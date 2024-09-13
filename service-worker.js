const CACHE_NAME = 'juego-ruta-v1';
const urlsToCache = [
    '/',
    '/static/styles.css',
    '/static/logo/audi.png',
    '/static/logo/volkswagen.png',
    '/static/logo/ducati.png',
    '/static/logo/taller.png',
    '/static/logo/preguntas.png',
    '/routes/routes.json',
    '/preguntas/preguntas.json',
    '/icons/favicon.png',           // Favicon pequeño
    '/icons/icon-192x192.png',      // Ícono para instalación PWA
    '/icons/icon-512x512.png'       // Ícono para instalación PWA
];

// Instalar el service worker y cachear recursos
self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

// Interceptar peticiones de la red
self.addEventListener('fetch', function (event) {
    event.respondWith(
        caches.match(event.request)
            .then(function (response) {
                return response || fetch(event.request);
            })
    );
});

// Actualizar el service worker
self.addEventListener('activate', function (event) {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then(function (cacheNames) {
            return Promise.all(
                cacheNames.map(function (cacheName) {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

