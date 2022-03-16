const rosnodejs = require("rosnodejs");
rosnodejs.initNode("/my_node").then(() => {
    console.log("success");
}).catch((err) => {
    console.log(err);
});
