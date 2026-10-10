const https = require('https');

module.exports = (req, res) => {
    const q = req.query.q;
    const tl = req.query.tl || 'vi';
    
    if (!q) {
        return res.status(400).send('Missing query parameter q');
    }

    const googleTtsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&q=${encodeURIComponent(q)}&tl=${tl}&client=tw-ob`;
    
    https.get(googleTtsUrl, (googleRes) => {
        res.setHeader('Content-Type', 'audio/mpeg');
        res.setHeader('Access-Control-Allow-Origin', '*');
        googleRes.pipe(res);
    }).on('error', (e) => {
        res.status(500).send('Error fetching from Google TTS');
    });
};
