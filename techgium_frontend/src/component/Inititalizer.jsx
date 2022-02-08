import React, { useEffect, useState } from "react";

function Initializer({ socket, createNewSocket, deleteSocket }) {
  const [length, setLength] = useState("");
  const [breadth, setBreadth] = useState("");
  const [value1, setValue1] = useState(0);


  useEffect(() => {
    const messageListener = (message) => {
      console.log(message);
      const key_val = JSON.parse(message);
      setValue1(key_val['data']);
    };
    if (socket != null) {
      socket.on("data", messageListener);
    }
  }, [socket]);

  const handleSubmit = (event) => {
    event.preventDefault();
    createNewSocket(Number(length), Number(breadth));
  };

  const stop = (event) => {
    event.preventDefault();
    socket.emit("stop", "stopping");
  }

  // {socket == null ?
  //   (<form onSubmit={handleSubmit}>
  //     <label>
  //       Enter Length:
  //       <input
  //         type="text"
  //         value={length}
  //         onChange={(e) => setLength(e.target.value)}
  //       />
  //     </label>
  //     <label>
  //       Enter breadth:
  //       <input
  //         type="text"
  //         value={breadth}
  //         onChange={(e) => setBreadth(e.target.value)}
  //       />
  //     </label>
  //     <input type="submit" />
  //   </form>)
  //   : (<div>Under devlopment<div/>)
  // }
  return (
    <div className="message-list">
      {socket == null ? (
        <form onSubmit={handleSubmit}>
          <label>
            Enter Length:
            <input
              type="text"
              value={length}
              onChange={(e) => setLength(e.target.value)}
            />
          </label>
          <label>
            Enter breadth:
            <input
              type="text"
              value={breadth}
              onChange={(e) => setBreadth(e.target.value)}
            />
          </label>
          <input type="submit" />
        </form>
      ) : (
        // edit
        <div>
          value1 - {value1}
          <button onClick={stop}>Stop</button>
        </div>
      )}
    </div>
  );
}

export default Initializer;
