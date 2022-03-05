import React, { useState } from "react";
import Initializer from "./component/Inititalizer";
import rosnodejs from "rosnodejs"

import "./App.css";
import "./fontawesome.min.css"

function App() {
  const [ros, setRos] = useState(null);

  const startRos = async (length, breadth) => {
    await rosnodejs.initNode('my_node');
    const pub = rosnodejs.nh.advertise('/backend', 'std_msgs/string');
    pub.publish({ data: JSON.stringify({ length, breadth })});
    setRos(rosnodejs);
  }

  return (
    <div className="App">
      <div className="chat-container">
        <Initializer ros={ros} startRos={startRos}/>
      </div>
    </div>
  );
}

export default App;
