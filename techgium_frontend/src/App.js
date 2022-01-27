import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import Msg from './component/msg';

import './App.css';

function App() {
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const newSocket = io(`http://${window.location.hostname}:8080`);
    setSocket(newSocket);
    return () => newSocket.close();
  }, [setSocket]);

  return (
    <div className="App">
      <header className="app-header">
        React Chat
      </header>
      { socket ? (
        <div className="chat-container">
          <Msg socket = {socket}/>
        </div>
      ) : (
        <div>Not Connected</div>
      )}
    </div>
  );
}

export default App;