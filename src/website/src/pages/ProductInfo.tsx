import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { getWebsiteUrl } from "../utils/path";
import getAuthHeaders from "../utils/getAuthHeaders";
import { useNavigate } from "react-router-dom";
import Footer from "../components/Footer";
import StoreHeader from "../components/Header";
import "../assets/css/productInfo.css";

import { BaseInfo, DefaultVariant, Media } from "../components/BaseInfoDisplay";

const ProductInfo: React.FC = () => {
    const navigate = useNavigate();
    const { uuid } = useParams<{ uuid?: string }>();

    const [productInfo, setProductInfo] = useState<BaseInfo | null>(null);

    const fetchData = async (sku: string) => {
        if (!sku) return;

        try {
            const response = await axios.get(
                `${getWebsiteUrl()}products/api/${sku}/`,
                { headers: await getAuthHeaders() }
            );
            console.log(response);
            setProductInfo(response.data);
        } catch (error) {
            console.error("Error fetching data:", error);
            setProductInfo(null);
        }
    };

    useEffect(() => {
        if (uuid) fetchData(uuid);
    }, [uuid]);

    if (!productInfo) {
        return <div></div>;
    }
    const thumbnailUrl = productInfo.thumbnail?.image
        ? getWebsiteUrl() + productInfo.thumbnail.image
        : "";
    const price = productInfo.default_variant?.price;

    const processDetails = (details: string): React.ReactNode[] => {
        const lines = details.split("\n").filter(Boolean);
        return lines.map((line: string, index: number) => {
            if (line === line.toUpperCase()) {
                return <div className="s2-2">{line}</div>;
            } else {
                return <div style={{ lineHeight: "1.2" }}>{line.trim()}</div>;
            }
        });
    };

    return (
        <div className="productInfoContainer">
            <div className="productInfoContent">
                <div className="productHeaderLinkBar">
                    <a
                        className="linkP"
                        onClick={() => {
                            navigate("/");
                        }}
                    >
                        home
                    </a>
                    <a
                        className="linkP"
                        onClick={() => {
                            navigate("/");
                        }}
                    >
                        {" > " + productInfo.category}
                    </a>
                    <a
                        className="linkP"
                        onClick={() => {
                            navigate("/");
                        }}
                    >
                        {" > " + productInfo.subCategory}
                    </a>
                    <a
                        className="linkP"
                        onClick={() => {
                            navigate("/");
                        }}
                    >
                        {" > " + productInfo.ptype}
                    </a>
                </div>
                <div className="productInfoHeader">Header</div>
                <div className="productInfoInnerContainer">
                    <div className="productInfoDescription">
                        <div className="s1">{productInfo.name}</div>
                        {thumbnailUrl && <img src={thumbnailUrl} alt={productInfo.name} />}
                        <p>{productInfo.description}</p>
                        {price && <p>Price: {price}€</p>}
                        {processDetails(productInfo.details)}
                    </div>
                    <div className="productInfoBuy">hi</div>
                </div>
            </div>
        </div>
    );
};

const ProductInfoPage: React.FC = () => {
    return (
        <div>
            <StoreHeader logoUrl=" " />
            <ProductInfo />
            <Footer />
        </div>
    );
};

export default ProductInfoPage;
