// /* eslint-disable react-hooks/rules-of-hooks */
//
// import React, { useEffect } from "react";
// import { useTheme } from "./themeContext";
// import "./App.css";
// import Registration from "./resgitration"; // !TODO CHANGE
// import Images from "./images";
//
// const App: React.FC = () => {
//     const { lightMode } = useTheme();
//
//     useEffect(() => {
//         if (lightMode) {
//             document.body.classList.add("dark-mode");
//             document.body.classList.remove("light-mode");
//         } else {
//             document.body.classList.add("light-mode");
//             document.body.classList.remove("dark-mode");
//         }
//     }, [lightMode]);
//
//     return (
//         <div className="App">
//             <div className="ad-left">
//                 <img src="amd.jpg" alt=" " />
//             </div>
//             <div className="content">
//                 <div
//                     style={{
//                         paddingTop: "80px",
//                         textAlign: "center",
//                         paddingBottom: "3000px",
//                     }}
//                 >
//                     <Images></Images>
//                     <h1>Website Content</h1>
//                     <p>...</p>
//                     <p>Contains bugs ATM, release expected 31/05!</p>
//                     <Registration></Registration>
//                 </div>
//             </div>
//             <div className="ad-right">
//                 <img src="amd.jpg" alt=" " />
//             </div>
//         </div>
//     );
// };
//
// export default App;

// App.tsx
import React, { useEffect } from "react";
import { useTheme } from "./themeContext";
import "./App.css";
import Registration from "./resgitration";
import Images from "./images";
import ImageModal from "./ImageModal";

// const backendUrl = process.env.REACT_APP_BACKEND_URL;

const App: React.FC = () => {
    const { lightMode } = useTheme();

    const imageSrc = "./p047671_1_.jpg";

    useEffect(() => {
        if (lightMode) {
            document.body.classList.add("dark-mode");
            document.body.classList.remove("light-mode");
        } else {
            document.body.classList.add("light-mode");
            document.body.classList.remove("dark-mode");
        }
    }, [lightMode]);

    const handleContextMenu = (event: React.MouseEvent) => {
        event.preventDefault();
    };

    return (
        <div className="Main">
            <div className="left-banner">
                <img src={`amd.jpg`} alt="Logo" onContextMenu={handleContextMenu} />
            </div>
            <div className="content">
                <h1>Website Content</h1>
                <p>...</p>
                <p>Contains bugs ATM, release expected 31/05!</p>
                <div className="horizontal-ad">
                    <img src={`amd.jpg`} alt="Logo" onContextMenu={handleContextMenu} />
                </div>
                <Images></Images>
                <Registration></Registration>
                <Registration></Registration>
                <Registration></Registration>
            </div>
            <div className="right-banner">
                <img src={`amd.jpg`} alt="Logo" onContextMenu={handleContextMenu} />
            </div>
        </div>
    );
};
// <ImageModal src={imageSrc} alt="Your image description" />

export default App;
