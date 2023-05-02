import React, { useEffect, useState } from "react";
import { useTheme } from "../contexts/themeContext";
import "../assets/css/App.css"; // !TODO CHANGE
import Registration from "../components/Registration";
import Images from "../components/Images";
import ImageModal from "../components/ImageModal";
import { getStaticPath } from "../utils/staticPathUtil";
import StoreHeader from "../components/Header";
import Footer from "../components/Footer";
import { ThemeProvider } from "../contexts/themeContext";
import Categories from "../components/Categories";
import BaseInfoDisplay, { BaseInfo } from "../components/BaseInfoDisplay";

import "../assets/css/brands.css"; //!TODO remove

import axios from "axios";

// const backendUrl = process.env.REACT_APP_BACKEND_URL;

const HomeContent: React.FC = () => {
    const { lightMode } = useTheme();

    // const bannerSrc = getStaticPath("nvidiaA1002.png");
    const bannerSrc = getStaticPath("redhat2.png");
    // const verticalAdSrc = getStaticPath("nvidiaA100.png");
    const verticalAdSrc = getStaticPath("amd.png");
    console.log(verticalAdSrc);
    console.log(bannerSrc);

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
        setTimeout(() => {
            const image = new Image();
            image.src = bannerSrc;
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
        }, 30);
    }, []);

    const [baseInfos, setBaseInfos] = useState<BaseInfo[] | null>(null);

    const fetchData = async () => {
        try {
            const response = await axios.get(
                "http://localhost:8000/products/api/base_info/"
            );
            setBaseInfos(response.data);
        } catch (error) {
            console.error("Error fetching data:", error);
            setBaseInfos([]);
        }
    };

    useEffect(() => {
        fetchData();
    }, []);

    if (!baseInfos) {
        return <div>Loading...</div>;
    }

    const logoT1 = getStaticPath("nvidia.png"); //!TODO remove
    const logoT2 = getStaticPath("amdl.png"); //!TODO remove
    const logoT3 = getStaticPath("supermicro.png"); //!TODO remove
    const logoT4 = getStaticPath("micron.png"); //!TODO remove
    const logoT5 = getStaticPath("nvidia.png"); //!TODO remove
    const logoT6 = getStaticPath("nvidia.png"); //!TODO remove
    const logoT7 = getStaticPath("nvidia.png"); //!TODO remove
    const logoT8 = getStaticPath("nvidia.png"); //!TODO remove
    const logoT9 = getStaticPath("nvidia.png"); //!TODO remove
    const logoT10 = getStaticPath("nvidia.png"); //!TODO remove
    const logoT11 = getStaticPath("nvidia.png"); //!TODO remove

    return (
        <div className="Main">
            <div className="left-banner">
                <img src={verticalAdSrc} alt="Logo" onContextMenu={handleContextMenu} />
            </div>

            <div className="content">
                <h1>Something here</h1>
                <Categories />

                <div className="banner">
                    <div
                        className="non-blurred-background"
                        style={{
                            backgroundImage: `url(${bannerSrc})`,
                        }}
                    ></div>
                    <div
                        className="blurred-background"
                        style={{
                            backgroundImage: blurredImage ? `url(${blurredImage})` : "",
                        }}
                    ></div>
                    <img src={bannerSrc} alt="Your ad image" />
                </div>
                <div className="subtitle-container">
                    <h2>|Destaques</h2>
                    <h3>Ver mais+</h3>
                </div>
                <div>
                    <div className="base-info-display">
                        {baseInfos.map((info, index) => (
                            <BaseInfoDisplay key={index} info={info} />
                        ))}
                        {baseInfos.map((info, index) => (
                            <BaseInfoDisplay key={index} info={info} />
                        ))}
                        {baseInfos.map((info, index) => (
                            <BaseInfoDisplay key={index} info={info} />
                        ))}
                        {baseInfos.map((info, index) => (
                            <BaseInfoDisplay key={index} info={info} />
                        ))}
                        {baseInfos.map((info, index) => (
                            <BaseInfoDisplay key={index} info={info} />
                        ))}
                        {baseInfos.map((info, index) => (
                            <BaseInfoDisplay key={index} info={info} />
                        ))}
                        {baseInfos.map((info, index) => (
                            <BaseInfoDisplay key={index} info={info} />
                        ))}
                        {baseInfos.map((info, index) => (
                            <BaseInfoDisplay key={index} info={info} />
                        ))}
                        {baseInfos.map((info, index) => (
                            <BaseInfoDisplay key={index} info={info} />
                        ))}
                    </div>
                </div>
                <h2>|Marcas</h2>
                <div className="brandContainer">
                    <img src={logoT1} />
                    <img src={logoT2} />
                    <img src={logoT3} />
                    <img src={logoT4} />
                    <img src={logoT5} />
                    <img src={logoT6} />
                    <img src={logoT7} />
                    <img src={logoT8} />
                    <img src={logoT9} />
                    <img src={logoT10} />
                    <img src={logoT11} />
                </div>
            </div>

            <div className="right-banner">
                <img src={verticalAdSrc} alt="Logo" onContextMenu={handleContextMenu} />
            </div>
        </div>
    );
};
// <ImageModal src={imageSrc} alt="Your image description" />

const logoUrl = "https://example.com/logo.png";

const Home: React.FC = () => {
    return (
        <ThemeProvider>
            <StoreHeader logoUrl={logoUrl} />
            <HomeContent />
            <Footer />
        </ThemeProvider>
    );
};

export default Home;
