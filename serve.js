const http = require('http');
const fs = require('fs');
const path = require('path');
// const { handleMusicAPI } = require('./music-backend');

const PORT = 8080;

const MIME_TYPES = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.wav': 'audio/wav',
    '.mp3': 'audio/mpeg',
    '.mp4': 'video/mp4',
    '.woff': 'application/font-woff',
    '.ttf': 'application/font-ttf',
    '.eot': 'application/vnd.ms-fontobject',
    '.otf': 'application/font-otf',
    '.wasm': 'application/wasm'
};

http.createServer((req, res) => {
    // Intercept music API requests
    if (req.url.startsWith('/api/music')) {
        // handleMusicAPI(req, res);
        res.writeHead(404);
        res.end('Not Found');
        return;
    }

    // Endpoint Proxy cho Google TTS để tránh bị chặn và lỗi CORS
    if (req.url.startsWith('/tts')) {
        const urlParams = new URL(req.url, `http://${req.headers.host}`).searchParams;
        const q = urlParams.get('q');
        const tl = urlParams.get('tl') || 'vi';
        
        if (!q) {
            res.writeHead(400);
            res.end('Missing query parameter q');
            return;
        }

        const googleTtsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&q=${encodeURIComponent(q)}&tl=${tl}&client=tw-ob`;
        
        const https = require('https');
        https.get(googleTtsUrl, (googleRes) => {
            res.writeHead(200, {
                'Content-Type': 'audio/mpeg',
                'Access-Control-Allow-Origin': '*'
            });
            googleRes.pipe(res);
        }).on('error', (e) => {
            res.writeHead(500);
            res.end('Error fetching from Google TTS');
        });
        return;
    }

    let rawPath = req.url.split('?')[0];
    if (rawPath === '/music' || rawPath === '/music-player') {
        rawPath = '/music-player.html';
    }

    let filePath = '.' + rawPath;
    if (filePath === './' || filePath === '.') filePath = './index.html';

    const extname = String(path.extname(filePath)).toLowerCase();
    const contentType = MIME_TYPES[extname] || 'application/octet-stream';

    fs.readFile(filePath, (error, content) => {
        if (error) {
            if(error.code == 'ENOENT') {
                res.writeHead(404);
                res.end('File not found');
            } else {
                res.writeHead(500);
                res.end('Sorry, check with the site admin for error: '+error.code+' ..\n');
            }
        } else {
            res.writeHead(200, { 'Content-Type': contentType });
            res.end(content, 'utf-8');
        }
    });

}).listen(PORT);

console.log(`Server running at http://localhost:${PORT}/`);
console.log(`Nhấn Ctrl+C để dừng server.`);
