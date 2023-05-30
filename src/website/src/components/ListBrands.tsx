import React, { useEffect, useState } from "react";
import { useInterval } from "react-use";
import axios from "axios";
import { getWebsiteUrl } from "../utils/path";

export interface Brand {
    name: string;
    logoHash: string;
    logoType: string;
    logo: string;
    dateAdded: Date;
}

const BrandList: React.FC = () => {
    const [brands, setBrands] = useState<Brand[]>([]);
    const [scrollPosition, setScrollPosition] = useState(0);
    const [isHovered, setIsHovered] = useState(false);

    const fetchBrands = async () => {
        try {
            const response = await axios.get(getWebsiteUrl() + "products/api/brands");
            setBrands(response.data);
        } catch (error) {
            console.log(error);
            return;
        }
    };

    useEffect(() => {
        fetchBrands();
    }, []);

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
            if (scrollPosition > (128 + 12) * brands.length) {
                setScrollPosition(0);
            } else {
                container.scrollLeft = scrollPosition;
            }
        }
    }, [scrollPosition]);

    return (
        <div
            className="brandContainer"
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave}
        >
            {Array(2)
                .fill(0)
                .map((_, i) =>
                    brands.map((brand, j) => (
                        <img key={`logo-${i}-${j}`} src={brand.logo} />
                    ))
                )}
        </div>
    );
};

export default BrandList;
