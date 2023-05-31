import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { getWebsiteUrl } from "../utils/path";
import getAuthHeaders from "../utils/getAuthHeaders";

import { BaseInfo, DefaultVariant, Media } from "../components/BaseInfoDisplay"; // adjust this import according to your project structure

const ProductInfoPage: React.FC = () => {
    const { sku } = useParams<{ sku?: string }>();
    const [productInfo, setProductInfo] = useState<BaseInfo | null>(null);
    const [error, setError] = useState<string | null>(null);

    const fetchData = async (sku: string) => {
        if (!sku) return; // do nothing if sku is undefined

        try {
            const response = await axios.get(
                `${getWebsiteUrl()}/products/api/${sku}/`, // adjust this URL to match your API
                { headers: getAuthHeaders() } // assuming getAuthHeaders is a function that returns necessary headers
            );
            console.log(response);
            setProductInfo(response.data);
        } catch (error) {
            console.error("Error fetching data:", error);
            setError(`Error fetching data: ${error}`);
            setProductInfo(null);
        }
    };

    useEffect(() => {
        if (sku) fetchData(sku);
    }, [sku]);

    if (error) {
        return <div>{error}</div>;
    }

    // if (!productInfo) {
    //     return <div>Loading...</div>;
    // }
    if (productInfo) {
        // Check if the thumbnail and default variant exists before trying to use them
        const thumbnailUrl = productInfo.thumbnail?.image
            ? getWebsiteUrl() + productInfo.thumbnail.image
            : "";
        const price = productInfo.default_variant?.price;

        return (
            <div>
                <h1>{productInfo.name}</h1>
                {thumbnailUrl && <img src={thumbnailUrl} alt={productInfo.name} />}
                <p>{productInfo.description}</p>
                {price && <p>Price: {price}€</p>}
                {/* Display other product information as needed */}
            </div>
        );
    }
        return <div>Loading...</div>;
};

export default ProductInfoPage;
