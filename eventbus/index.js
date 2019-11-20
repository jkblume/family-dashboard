const app = require('http').createServer(handler)
const io = require('socket.io')(app);
const fs = require('fs');
const redis = require("redis");
const redisClient = redis.createClient(process.env.REDIS_URL || "redis://127.0.0.1:6379/1");

app.listen(8080);

const CHANNEL_PATTERN = process.env.CHANNEL_PATTERN || "notifications_*"

function handler (req, res) {
    fs.readFile(__dirname + '/index.html',
    function (err, data) {
      if (err) {
        res.writeHead(500);
        return res.end('Error loading index.html');
      }
  
      res.writeHead(200);
      res.end(data);
    });
  }

io.on('connection', function (socket) {
    redisClient.on("pmessage", (pattern, channel, message) => {
        console.log(channel, message);
        socket.emit(channel, message);        
    });

    redisClient.psubscribe(CHANNEL_PATTERN);

    socket.on('disconnect', () => {
        console.log("Client disconnected and unsubscribe from redis channel.")
        redisClient.punsubscribe(CHANNEL_PATTERN);
    });
    console.log("Client connected and subscribed to redis channel.")
});
