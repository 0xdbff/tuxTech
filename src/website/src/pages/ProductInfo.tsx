import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { getWebsiteUrl } from "../utils/path";
import getAuthHeaders from "../utils/getAuthHeaders";
import Footer from "../components/Footer";
import StoreHeader from "../components/Header";

import { BaseInfo, DefaultVariant, Media } from "../components/BaseInfoDisplay"; // adjust this import according to your project structure

const ProductInfo: React.FC = () => {
    const { uuid } = useParams<{ uuid?: string }>();

    console.log(uuid);
    const [productInfo, setProductInfo] = useState<BaseInfo | null>(null);

    const fetchData = async (sku: string) => {
        if (!sku) return; // do nothing if sku is undefined

        try {
            const response = await axios.get(
                `${getWebsiteUrl()}products/api/${sku}/`, // adjust this URL to match your API
                { headers: getAuthHeaders() } // assuming getAuthHeaders is a function that returns necessary headers
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
    // Check if the thumbnail and default variant exists before trying to use them
    const thumbnailUrl = productInfo.thumbnail?.image
        ? getWebsiteUrl() + productInfo.thumbnail.image
        : "";
    const price = productInfo.default_variant?.price;

            const detailsArray = productInfo.details.split('.');
        const detailsElements = detailsArray.map((detail, index) => {
            const wordsArray = detail.split(' ');
            const firstWord = wordsArray[0];
            const restOfWords = wordsArray.slice(1).join(' ');
            return (
                <div key={index}>
                    <h3>{firstWord}</h3>
                    <p>{restOfWords}</p>
                </div>
            );
        });

        return (
            <div>
                <div style={{ height: "50px" }}></div>
                <h1>{productInfo.name}</h1>
                {thumbnailUrl && <img src={thumbnailUrl} alt={productInfo.name} />}
                <p>{productInfo.description}</p>
                {price && <p>Price: {price}€</p>}
                {detailsElements}
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
