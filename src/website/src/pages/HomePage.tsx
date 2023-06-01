import React, { useEffect, useState } from "react";
import { useTheme } from "../contexts/themeContext";
import "../assets/css/App.css"; // !TODO CHANGE
import Registration from "../components/Registration";
import Images from "../components/Images";
import ImageModal from "../components/ImageModal";
import { getStaticPath } from "../utils/staticPathUtil";
import StoreHeader from "../components/Header";
import Footer from "../components/Footer";
import Categories from "../components/Categories";
import BaseInfoDisplay, { BaseInfo } from "../components/BaseInfoDisplay";
import { getWebsiteUrl } from "../utils/path";
import getAuthHeaders from "../utils/getAuthHeaders";
import BrandList from "../components/ListBrands";
import Advertisements from "../components/Advertisements";

import "../assets/css/brands.css";

import axios from "axios";

const HomeContent: React.FC = () => {
    const handleContextMenu = (event: React.MouseEvent) => {
        event.preventDefault();
    };
    const [baseInfos, setBaseInfos] = useState<BaseInfo[] | null>(null);

    const fetchData = async () => {
        try {
            const response = await axios.get(
                getWebsiteUrl() + "products/api/base_info/",
                { headers: await getAuthHeaders() }
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

    return (
        <div className="Main">
            <div className="content">
                <div style={{ height: "80px" }}></div>
                <Categories />

                <div className="banner">
                    <Advertisements startingIndex={0} />
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
                <BrandList />
                <div className="subtitle-container">
                    <h2>|Promocoes</h2>
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
                <div style={{ height: "20px" }}></div>
                <div className="banner">
                    <Advertisements startingIndex={1} />
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
                        {Array.isArray(baseInfos) &&
                            baseInfos.map((info, index) => (
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
