const fs = require('fs');
const path = require('path');

// Danh sách các file bản dịch được nhúng trực tiếp vào app
// Do Vercel không có quyền truy cập filesystem local,
// nội dung file sẽ được người dùng paste hoặc load từ URL public

module.exports = (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.status(200).json({ message: 'Library API - content is embedded in the frontend' });
};
