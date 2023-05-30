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
import withAuth from "../utils/getAuthHeaders";

import { useInterval } from "react-use";

import "../assets/css/brands.css"; //!TODO remove

import axios from "axios";

const HomeContent: React.FC = () => {
    const bannerSrc = "images/amd3.jpg";
    const banner2Src = "images/a.jpg";

    const handleContextMenu = (event: React.MouseEvent) => {
        event.preventDefault();
    };
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

    const logoT1 = "images/nvidia.png"; //!TODO remove
    const logoT2 = "images/amdl.png"; //!TODO remove
    const logoT3 = "images/supermicro.png"; //!TODO remove
    const logoT4 = "images/micron.png"; //!TODO remove
    const logoT5 = "images/cisco.png"; //!TODO remove
    const logoT6 = "images/apple.png"; //!TODO remove
    const logoT7 = "images/asus.png"; //!TODO remove
    const logoT8 = "images/dell.png"; //!TODO remove
    const logoT9 = "images/lenovo.png"; //!TODO remove
    const logoT10 = "images/intel.png"; //!TODO remove
    const logoT11 = "images/lg.png"; //!TODO remove
    const logoT12 = "images/samsung.png"; //!TODO remove
    const logoT13 = "images/sony.png"; //!TODO remove
    const logoT14 = "images/synology.png"; //!TODO remove
    const logoT15 = "images/ubiquiti.png"; //!TODO remove
    const logoT16 = "images/tp-link.png"; //!TODO remove
    const logoT17 = "images/wd.png"; //!TODO remove
    const logoT18 = "images/xiaomi.png"; //!TODO remove

    return (
        <div className="Main">
            <div className="content">
                <h1> - </h1>
                <Categories />

                <div className="banner">
                    <div
                        className="non-blurred-background"
                        style={{
                            backgroundImage: `url(${bannerSrc})`,
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
                        {Array.isArray(baseInfos) &&
                            baseInfos.map((info, index) => (
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
                    <img src={banner2Src} alt="Your ad image" />
                </div>
                <div className="subtitle-container">
                    <h2>|Top vendas</h2>
                    <h3>Ver mais+</h3>
                </div>
                <div>
                    <div className="base-info-display">
                        {Array.isArray(baseInfos) &&
                            baseInfos.map((info, index) => (
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
    {Array.isArray(baseInfos) && baseInfos.map((info, index) => (
        <BaseInfoDisplay key={index} info={info} />
    ))}
</div>
                </div>
            </div>
        </div>
    );
};
// <ImageModal src={imageSrc} alt="Your image description" />

const Home: React.FC = () => {
    return (
        <div>
            <StoreHeader logoUrl=" " />
            <HomeContent />
            <Footer />
        </div>
    );
};

export default Home;
