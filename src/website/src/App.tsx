import React, { useEffect } from "react";
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
            <div className="ad-left ad">
            </div>
            <div className="content">
                <div
                    style={{
                        paddingTop: "80px",
                        textAlign: "center",
                        paddingBottom: "3000px",
                    }}
                >
                    <h1>Website Content</h1>
                    <p>...</p>
                    <p>Contains bugs ATM, release expected 31/05!</p>
                </div>
            </div>
            <div className="ad-right ad">
            </div>
        </div>
    );
};

export default App;
