import React, { useState } from "react";
import io from "socket.io-client";
import Initializer from "./component/Inititalizer";

import "./App.css";

function App() {
  const [socket, setSocket] = useState(null);

  const createNewSocket = (length, breadth) => {
    const newSocket = io(`http://${window.location.hostname}:8080`);
    newSocket.emit("start", JSON.stringify([length, breadth]));
    setSocket(newSocket);
  };

  const deleteSocket = () => {
    socket.close();
    setSocket(null);
  };

  return (
    <div className="App">
      <header className="app-header">React Chat</header>
      <div className="chat-container">
        <Initializer
          socket={socket}
          createNewSocket={createNewSocket}
          deleteSocket={deleteSocket}
        />
      </div>
    </div>
  );
}

export default App;
