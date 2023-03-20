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

    return (
        <div className="App">
            <div className="ads-container">
                <div className="add">
                    <img src="amd.jpg" style={{ height: "auto", width: "162%" }}></img>
                </div>
                <div>
                    <div
                        style={{
                            paddingTop: "80px", // To accommodate the header's height when it's visible
                            paddingBottom: "3000px", // To create a long scrolling area
                            textAlign: "center",
                        }}
                    >
                        <h1>Your Website Content</h1>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
                            et pellentesque odio, vitae tincidunt ligula. Suspendisse gravida
                            bibendum purus, sit amet cursus velit sagittis et. Praesent nec
                            facilisis tortor, ac blandit justo. Etiam scelerisque eros vel
                            eleifend laoreet. Sed vel odio a sapien dictum tempus at nec arcu.
                            Duis bibendum consequat sapien eu laoreet. Curabitur porttitor,
                            urna et fringilla pellentesque, urna nisl venenatis lectus, vel
                            cursus odio urna vel velit. Nulla facilisi. Phasellus in eros
                            lacus. Vestibulum vehicula, lacus vel malesuada vestibulum, libero
                            lectus tincidunt dolor, eu faucibus lectus mi id ligula. Cras ac
                            vehicula sapien, ut volutpat augue.
                        </p>
                    </div>
                </div>
                <div className="add">
                    <img src="amd.jpg" style={{ height: "auto", width: "162%" }}></img>
                </div>
            </div>
        </div>
    );
};

export default App;
