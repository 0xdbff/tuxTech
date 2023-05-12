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
import { getWebsiteUrl } from "../utils/path";
import getAuthHeaders from "../utils/getAuthHeaders";

import { useInterval } from "react-use";

import "../assets/css/brands.css"; //!TODO remove

import axios from "axios";

// const backendUrl = process.env.REACT_APP_BACKEND_URL;

const HomeContent: React.FC = () => {
    const { lightMode } = useTheme();

    // const bannerSrc = getStaticPath("nvidiaA1002.png");
    const bannerSrc = getStaticPath("redhat2.png");
    const banner2Src = getStaticPath("nvidiaA1002.png");
    const verticalAdSrc = getStaticPath("nvidiaA100.png");
    // const verticalAdSrc = getStaticPath("amd.png");
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
    const [blurredImage2, setBlurredImage2] = useState<string | null>(null);

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

    useEffect(() => {
        setTimeout(() => {
            const image = new Image();
            image.src = banner2Src;
            image.onload = () => {
                const banner = document.querySelector(".banner");
                if (banner) {
                    const bannerRect = banner.getBoundingClientRect();
                    setBlurredImage2(
                        applyBlurToImage(image, 256, bannerRect.width, bannerRect.height)
                    );
                }
            };
            image.onerror = () => {
                setBlurredImage2(null);
            };
        }, 30);
    }, []);

    const [baseInfos, setBaseInfos] = useState<BaseInfo[] | null>(null);

    const fetchData = async () => {
        try {
            const response = await axios.get(
                getWebsiteUrl() + "products/api/base_info/",
                                    { headers: getAuthHeaders() }

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

    const [scrollPosition, setScrollPosition] = useState(0);
    const [isHovered, setIsHovered] = useState(false);
    const logoWidth = 128 + 12; // Width of a logo
    const numLogos = 18; // Total number of logos

    useInterval(() => {
        if (!isHovered) {
            setScrollPosition((prevScrollPosition) => prevScrollPosition + 1);
        }
    }, 32);

    const handleMouseEnter = () => {
        setIsHovered(true);
    };

    const handleMouseLeave = () => {
        setIsHovered(false);
    };

    useEffect(() => {
        const container = document.querySelector(".brandContainer");
        if (container) {
            if (scrollPosition > logoWidth * numLogos) {
                // Reset the scroll position to the start when it reaches the halfway point
                setScrollPosition(0);
            } else {
                container.scrollLeft = scrollPosition;
            }
        }
    }, [scrollPosition]);

    if (!baseInfos) {
        return <div>Loading...</div>;
    }

    const logoT1 = getStaticPath("nvidia.png"); //!TODO remove
    const logoT2 = getStaticPath("amdl.png"); //!TODO remove
    const logoT3 = getStaticPath("supermicro.png"); //!TODO remove
    const logoT4 = getStaticPath("micron.png"); //!TODO remove
    const logoT5 = getStaticPath("cisco.png"); //!TODO remove
    const logoT6 = getStaticPath("apple.png"); //!TODO remove
    const logoT7 = getStaticPath("asus.png"); //!TODO remove
    const logoT8 = getStaticPath("dell.png"); //!TODO remove
    const logoT9 = getStaticPath("lenovo.png"); //!TODO remove
    const logoT10 = getStaticPath("intel.png"); //!TODO remove
    const logoT11 = getStaticPath("lg.png"); //!TODO remove
    const logoT12 = getStaticPath("samsung.png"); //!TODO remove
    const logoT13 = getStaticPath("sony.png"); //!TODO remove
    const logoT14 = getStaticPath("synology.png"); //!TODO remove
    const logoT15 = getStaticPath("ubiquiti.png"); //!TODO remove
    const logoT16 = getStaticPath("tp-link.png"); //!TODO remove
    const logoT17 = getStaticPath("wd.png"); //!TODO remove
    const logoT18 = getStaticPath("xiaomi.png"); //!TODO remove

    return (
        <div className="Main">
            <div className="left-banner">
                <img src={verticalAdSrc} alt=" " onContextMenu={handleContextMenu} />
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
                <div className="subtitle-container">
                    <h2>|Marcas</h2>
                </div>
                <div
                    className="brandContainer"
                    onMouseEnter={handleMouseEnter}
                    onMouseLeave={handleMouseLeave}
                >
                    {Array(2)
                        .fill(0)
                        .map((_, i) =>
                            [
                                logoT1,
                                logoT2,
                                logoT3,
                                logoT4,
                                logoT5,
                                logoT6,
                                logoT7,
                                logoT8,
                                logoT9,
                                logoT10,
                                logoT11,
                                logoT12,
                                logoT13,
                                logoT14,
                                logoT15,
                                logoT16,
                                logoT17,
                                logoT18,
                            ].map((logoSrc, j) => (
                                <img key={`logo-${i}-${j}`} src={logoSrc} />
                            ))
                        )}
                </div>
                <div className="subtitle-container">
                    <h2>|Promocoes</h2>
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
                <div className="subtitle-container">
                    <h2> </h2>
                </div>
                <div className="banner">
                    <div
                        className="non-blurred-background"
                        style={{
                            backgroundImage: `url(${banner2Src})`,
                        }}
                    ></div>
                    <div
                        className="blurred-background"
                        style={{
                            backgroundImage: blurredImage2 ? `url(${blurredImage2})` : "",
                        }}
                    ></div>
                    <img src={banner2Src} alt="Your ad image" />
                </div>
                <div className="subtitle-container">
                    <h2>|Top vendas</h2>
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
                <div className="subtitle-container">
                    <h2>|Novidades</h2>
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
            </div>

            <div className="right-banner">
                <img src={verticalAdSrc} alt=" " onContextMenu={handleContextMenu} />
            </div>
        </div>
    );
};
// <ImageModal src={imageSrc} alt="Your image description" />

const Home: React.FC = () => {
    return (
        <ThemeProvider>
            <StoreHeader logoUrl=" " />
            <HomeContent />
            <Footer />
        </ThemeProvider>
    );
};

export default Home;
