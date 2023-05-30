import React, { useEffect, useState, useRef } from "react";
import axios from "axios";
import ScrollableContainer from "./utils/ScrollableContainer";
import getAuthHeaders from "../utils/getAuthHeaders";
import getAccessToken from "../utils/tokenManager";
import { getWebsiteUrl, getMediaPath } from "../utils/path";
import { useNavigate } from "react-router-dom";
import "../assets/css/categories.css";

interface Category {
    name: string;
    description: string;
    image: string;
}

const Categories: React.FC = () => {
    const [categories, setCategories] = useState<Category[]>([]);
    const containerRef = useRef<HTMLDivElement>(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const token = getAccessToken();
                if (!token) {
                    console.error("Unauthorized!");
                    return;
                }
                const authHeaders = getAuthHeaders();

                const response = await axios.get<Category[]>(
                    getWebsiteUrl() + "products/api/categories/",
                    { headers: authHeaders }
                );
                if (response && response.data && Array.isArray(response.data)) {
                    setCategories(response.data);
                } else {
                    console.error("No categories returned from backend.");
                }
            } catch (error) {
                console.error("Error fetching categories:", error);
            }
        };

        fetchCategories();
    }, []);

    const renderCategories = (
        content: React.ReactNode,
        ref: React.Ref<HTMLDivElement>
    ) => (
        <div className="scrollable-container__content" ref={ref}>
            {content}
        </div>
    );

    return (
        <div className="categoriesContainer" ref={containerRef}>
            <ScrollableContainer renderContent={renderCategories}>
                {categories &&
                    categories.map((category, index) => (
                        <div
                            className="categoryContainer"
                            key={`${category.name}-${index}`}
                            onClick={() => navigate(`/products/categories=${category.name}`)}
                        >
                            <img src={getMediaPath(category.image)} alt={" "} />
                            {category.name}
                        </div>
                    ))}
            </ScrollableContainer>
        </div>
    );
};

export default Categories;
