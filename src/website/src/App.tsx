// src/App.tsx
import React, { useEffect } from "react";
import { useTheme } from "./themeContext";
import "./App.css";

const App: React.FC = () => {
    const { lightMode } = useTheme();

    useEffect(() => {
        if (lightMode) {
            document.body.classList.add("light-mode");
            document.body.classList.remove("dark-mode");
        } else {
            document.body.classList.add("dark-mode");
            document.body.classList.remove("light-mode");
        }
    }, [lightMode]);

    return <div className="App">{}</div>;
};

export default App;
