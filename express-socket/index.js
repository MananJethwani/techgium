const rosnodejs = require('rosnodejs');
const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

var allowCrossDomain = function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE");
    res.header("Access-Control-Allow-Headers", "*");
    next();
};

app.use(express.json());
app.use(allowCrossDomain);
rosnodejs.initNode('/my_node').then(() => {
    const nh = rosnodejs.nh;
    nh.subscribe('/express', 'std_msgs/String', (msg) => {
        io.emit('data', msg);
    });
}).catch(err => console.log(err))

function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}

app.post('/', async (req, res) => {
    const length = req.body.length;
    const breadth = req.body.breadth;
    const nh = rosnodejs.nh;
    const pub = nh.advertise('/ros_start', 'std_msgs/String');
    await sleep(5000)
    const dt = JSON.stringify({ flag: 1, length, breadth });
    pub.publish({ data: dt });
    res.status(200).send();
});

app.get('/stop', async (req, res) => {
    await sleep(5000);
    const pub = nh.advertise('/flag_stop', 'std_msgs/String');
    const dt = JSON.stringify({ flag: 0 });
    pub.publish({ data: dt });
    res.status(200).send();
});

server.listen(3000, () => {
    console.log('listening on *:3000');
});

