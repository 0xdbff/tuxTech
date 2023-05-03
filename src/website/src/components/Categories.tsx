import React, { useEffect, useState, useRef } from "react";
import "../assets/css/categories.css";
import axios from "axios";
import ScrollableContainer from "./utils/ScrollableContainer";
import getAuthHeaders from "../utils/getAuthHeaders";
import getAccessToken from "../utils/tokenManager";

interface Category {
    name: string;
    description: string;
    image: string;
}

const Categories: React.FC = () => {
    const [categories, setCategories] = useState<Category[]>([]);
    const containerRef = useRef<HTMLDivElement>(null);

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
                    "http://localhost:8000/products/api/categories/",
                    { headers: authHeaders }
                );
                setCategories(response.data);
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
                {categories.map((category) => (
                    <>
                        {Array(6)
                            .fill(null)
                            .map((_, index) => (
                                <div
                                    className="categoryContainer"
                                    key={`${category.name}-${index}`}
                                >
                                    <img src={category.image} alt={category.name} />
                                    {category.name}
                                </div>
                            ))}
                    </>
                ))}
            </ScrollableContainer>
        </div>
    );
};

export default Categories;
