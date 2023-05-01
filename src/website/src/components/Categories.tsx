import React, { useEffect, useState, useRef } from "react";
import "../assets/css/categories.css";
import axios from "axios";
import ScrollableContainer from "./utils/ScrollableContainer";

interface Category {
    name: string;
    description: string;
    image: string;
}

const Categories: React.FC = () => {
    const [categories, setCategories] = useState<Category[]>([]);
    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await axios.get<Category[]>(
                    "http://localhost:8000/products/api/categories/"
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
        <div className="categoriesContainer">
            <ScrollableContainer renderContent={renderCategories} scrollStep={106}>
                {categories.map((category) => (
                    <>
                        {Array(16)
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
