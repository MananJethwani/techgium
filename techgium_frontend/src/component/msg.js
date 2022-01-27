import React, { useEffect, useState } from "react";

function Msg({ socket }) {
  const [length, setLength] = useState("");
  const [breadth, setBreadth] = useState("");

  useEffect(() => {
    const messageListener = (message) => {
      console.log(message);
    };

    socket.on("message", messageListener);
    console.log("gonna emit message");
    socket.emit("message", "send message");

    return () => {
      socket.off("message", messageListener);
    };
  }, [socket]);

  const handleSubmit = (event) => {
    event.preventDefault();
  };

  return (
    <div className="message-list">
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
    </div>
  );
}

export default Msg;
