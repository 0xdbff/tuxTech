import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
    return (
        <div className="App">
            <div className="ads-container">
                <div>
                    <img src="amd.jpg"></img>
                </div>
                <div>
                    TEXT IN THE MIDDLE
                </div>
                <div>
                    <img src="amd.jpg"></img>
                </div>
            </div>
        </div>
    );
}

// <header className="App-header">
//     <img src={logo} className="App-logo" alt="logo" />
//     <p>
//         Edit <code>src/App.tsx</code> and save to reload.
//     </p>
//     <a
//         className="App-link"
//         href="https://reactjs.org"
//         target="_blank"
//         rel="noopener noreferrer"
//     >
//         Learn React
//     </a>
// </header>
export default App;
