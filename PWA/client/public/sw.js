const staticCacheName ='s-app-v1'
const dynamicCacheName ='d-app-v1'
const assetUrls = [
    '/client/public/index.html',
    '/client/public/offline.html',
    '/client/src/App.css',
    '/client/src/App.js',
    '/client/src/index.js'
    // '/client/src/mutations/auto.js',
    // '/client/src/query/auto.js'
]



self.addEventListener('install',async event =>{
    console.log('[SW]: install')
    const cache = await caches.open(staticCacheName)
    await cache.addAll(assetUrls)
})
// self.addEventListener('install',event =>{
//     console.log('[SW]: install')
//     event.waitUntil(
//         caches.open(staticCacheName).then(cache => cache.addAll(assetUrls))
//     )
// })
self.addEventListener('activate',async event => {
    console.log('[SW]: activate')
    const cacheNames = await caches.keys()
    await Promise.all(
        cacheNames
            .filter(name => name !== staticCacheName)

            .map(name => caches.delete(name))
    )

})
//.filter(name => name !== dynamicCacheName)
self.addEventListener('fetch', event => {
    console.log('Fetch',event.request.url)
    event.respondWith(cacheFirst(event.request))
})
// self.addEventListener('fetch', event => {
//     const {request} = event
//     const url = new URL(request.url)
//     if (url.origin === location.origin) {
//         event.respondWith(cacheFirst(request))
//     } else {
//         event.respondWith(networkFirst(request))
//     }
//
// })
async function cacheFirst(request) {
    const cached = await caches.match(request)
    return cached ?? await fetch(request)
}
//
// async function networkFirst(request) {
//     const cache = await caches.open(dynamicCacheName)
//     try {
//         const response = await fetch(request)
//         await cache.put(request, response.clone())
//         return response
//     }
//     catch (e) {
//         const cached = await cache.match(request)
//         return cached ?? await caches.match('/offline.html')
//     }
// }