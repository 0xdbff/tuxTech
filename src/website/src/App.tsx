import React, { useEffect, useRef } from "react";
import { useTheme } from "./themeContext";
import "./App.css";

const App: React.FC = () => {
    const { lightMode } = useTheme();

    useEffect(() => {
        if (lightMode) {
            document.body.classList.add("dark-mode");
            document.body.classList.remove("light-mode");
        } else {
            document.body.classList.add("light-mode");
            document.body.classList.remove("dark-mode");
        }
    }, [lightMode]);

    return (
        <div className="App">
            <div className="content">
                <div className="ads-container">
                    <div className="add">
                        <img
                            src="amd.jpg"
                            alt="ad"
                            style={{ height: "100%", width: "100%" }}
                        />
                    </div>
                    <div
                        style={{
                            paddingTop: "80px", // To accommodate the header's height when it's visible
                            textAlign: "center",
                            paddingBottom: "3000px", // To create a long scrolling area
                        }}
                    >
                        <h1>Your Website Content</h1>
                        <p>...</p>
                    </div>
                    <div className="add">
                        <img
                            src="amd.jpg"
                            alt="ad"
                            style={{
                                height: "100%",
                                width: "100%",
                                transform: "rotate(180deg)",
                            }}
                        />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default App;
