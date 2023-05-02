import React from "react";
import "../assets/css/baseInfoDisplay.css";

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
    if (!info) {
        return <div>No information available.</div>;
    }

    console.log(info.thumbnail?.image);

    return (
        <div className="base-info-display">
            <div className="base-info-container">
                <div className="base-info-item">
                    {info.thumbnail && (
                        <div>
                            <img
                                src={"http://localhost:8000/" + info.thumbnail.image}
                                alt={info.name}
                            />
                        </div>
                    )}
                    <div>{info.name}</div>
                    <div>{info.description}</div>
                    <div>{info.default_variant?.price}</div>
                    <div>{info.default_variant?.sku}</div>
                </div>
            </div>
        </div>
    );
};

export default BaseInfoDisplay;
