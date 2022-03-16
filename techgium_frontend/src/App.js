import React, { useState } from "react";
import io from "socket.io-client";
import Initializer from "./component/Inititalizer";
import $ from "jquery";

import "./App.css";
import "./fontawesome.min.css"

function App() {
  const [socket, setSocket] = useState(null);

  const createNewSocket = (length, breadth) => {
    const newSocket = io(`http://${window.location.hostname}:5000`);
    newSocket.emit("start", JSON.stringify([length, breadth]));
    setSocket(newSocket);
  };

  const deleteSocket = () => {
    setSocket(null);
  };
  $("input").on("focusin", function () {
    $(this).parent().find("label").addClass("active");
  });

  $("input").on("focusout", function () {
    if (!this.value) {
      $(this).parent().find("label").removeClass("active");
    }
  });

  return (

    <div className="App">
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
