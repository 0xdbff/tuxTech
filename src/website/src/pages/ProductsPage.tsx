import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import getAuthHeaders from "../utils/getAuthHeaders";
import getAccessToken from "../utils/tokenManager";
import { getWebsiteUrl } from "../utils/path";
import "../assets/css/products.css";

interface Product {
    // define your product properties here
}

const ProductsPage: React.FC = () => {
    const [products, setProducts] = useState<Product[]>([]);
    const { categories } = useParams<{ categories: string }>();

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const token = getAccessToken();
                if (!token) {
                    console.error("Unauthorized!");
                    return;
                }
                const authHeaders = getAuthHeaders();

                let url = getWebsiteUrl() + "products/api/products/";
                if (categories) {
                    url += `?categories=${categories}`;
                }

                const response = await axios.get<Product[]>(url, {
                    headers: authHeaders,
                });
                setProducts(response.data);
            } catch (error) {
                console.error("Error fetching products:", error);
            }
        };

        fetchProducts();
    }, [categories]);

    return (
        <div className="products">
        <h1>Products</h1>
        
            {products.map((product, index) => (
                <div key={index}>{/* Render your product data here */}</div>
            ))}
        </div>
    );
};

export default ProductsPage;
