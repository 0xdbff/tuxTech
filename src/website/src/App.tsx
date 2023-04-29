import React, { useEffect, useState } from "react";
import { useTheme } from "./themeContext";
import "./App.css";
import Registration from "./resgitration";
import Images from "./images";
import ImageModal from "./ImageModal";
// const backendUrl = process.env.REACT_APP_BACKEND_URL;

const App: React.FC = () => {
    const { lightMode } = useTheme();

    const imageSrc = "redhat2.png";

    useEffect(() => {
        if (lightMode) {
            document.body.classList.add("dark-mode");
            document.body.classList.remove("light-mode");
        } else {
            document.body.classList.add("light-mode");
            document.body.classList.remove("dark-mode");
        }
    }, [lightMode]);

    const applyBlurToImage = (
        image: HTMLImageElement,
        blurRadius: number,
        containerWidth: number,
        containerHeight: number
    ): string => {
        const canvas = document.createElement("canvas");
        const context = canvas.getContext("2d");
        canvas.width = containerWidth;
        canvas.height = containerHeight;

        if (context) {
            context.filter = `blur(${blurRadius}px)`;
            context.drawImage(image, 0, 0, containerWidth, containerHeight);
        }

        return canvas.toDataURL();
    };

    const handleContextMenu = (event: React.MouseEvent) => {
        event.preventDefault();
    };

    const [blurredImage, setBlurredImage] = useState<string | null>(null);

    useEffect(() => {
        const image = new Image();
        image.src = "redhat2.png";
        image.onload = () => {
            const banner = document.querySelector(".banner");
            if (banner) {
                const bannerRect = banner.getBoundingClientRect();
                setBlurredImage(
                    applyBlurToImage(image, 256, bannerRect.width, bannerRect.height)
                );
            }
        };
        image.onerror = () => {
            setBlurredImage(null);
        };
    }, []);
    return (
        <div className="Main">
            <div className="left-banner">
                <img src={`amd.jpg`} alt="Logo" onContextMenu={handleContextMenu} />
            </div>

            <div className="content">
                <h1>Something here</h1>
                <h1>Something here</h1>
                <div className="banner">
                    <div
                        className="non-blurred-background"
                        style={{
                            backgroundImage: `url(${imageSrc})`,
                        }}
                    ></div>
                    <div
                        className="blurred-background"
                        style={{
                            backgroundImage: blurredImage ? `url(${blurredImage})` : "",
                        }}
                    ></div>
                    <img src={imageSrc} alt="Your ad image" />
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
