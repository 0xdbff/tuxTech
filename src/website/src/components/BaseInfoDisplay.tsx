import React from "react";
import { useState, useEffect } from "react";
import "../assets/css/baseInfoDisplay.css";
import { getWebsiteUrl } from "../utils/path";

import { AiFillCheckCircle } from "react-icons/ai";
export interface Media {
    id: number;
    name: string;
    media_type: string;
    image: string;
}

export interface DefaultVariant {
    sku: string;
    ean: string;
    is_default: boolean;
    name: string;
    price: number;
    medias: { media: Media; pos: number }[];
}

export interface BaseInfo {
    name: string;
    ref: string;
    description: string;
    category: number;
    subCategory: number;
    ptype: number;
    brand: number;
    date_added: string;
    price_min: number;
    price_max: number;
    default_variant: DefaultVariant | null;
    thumbnail: Media | null;
}

interface BaseInfoDisplayProps {
    info: BaseInfo | null;
}

const BaseInfoDisplay: React.FC<BaseInfoDisplayProps> = ({ info }) => {
    const [deliveryDate, setDeliveryDate] = useState("");

    useEffect(() => {
        const today = new Date();
        const tomorrow = new Date(today);
        tomorrow.setDate(tomorrow.getDate() + 1);

        const day = String(tomorrow.getDate()).padStart(2, "0");
        const monthNames = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro",
        ];
        const month = monthNames[tomorrow.getMonth()];

        setDeliveryDate(`${day} ${month}`);
    }, []);

    if (!info) {
        return <div>No information available.</div>;
    }

    var briefDescription = info.description;
    var briefName = info.name;
    var briefsku = info.default_variant?.sku;

    if (briefDescription.length > 102) {
        var briefDescription = info.description.substring(0, 101) + "...";
    }
    if (info.name.length > 57) {
        briefName = info.name.substring(0, 56) + "...";
    }

    if (briefsku && briefsku?.length > 16) {
        briefsku = info.default_variant?.sku.substring(0, 15);
    }

    return (
        <div className="base-info-container">
            <div className="base-info-item">
                {info.thumbnail && (
                    <div className="base-info-item">
                        <img src={getWebsiteUrl() + info.thumbnail.image} alt={info.name} />
                    </div>
                )}
                <div className="s2">{briefName}</div>
                <div className="s4">{briefDescription}</div>
                <div className="s4">{briefsku}</div>
                <div className="s3-1">
                    <AiFillCheckCircle />
                    Em stock
                </div>
                <div className="s3">Entrega prevista dia {deliveryDate}!</div>
                <div className="s1">
                    {info.default_variant?.price}
                    {"€"}
                </div>
            </div>
        </div>
    );
};

export default BaseInfoDisplay;
