import React, { useState, useEffect } from "react";
import axios from "axios";
import { getWebsiteUrl } from "../utils/path";
import { AiFillLeftCircle, AiFillRightCircle } from "react-icons/ai";
import getAuthHeaders from "../utils/getAuthHeaders";

interface AdvertisementsProps {
    startingIndex: number;
}

interface AdvertisementContract {
    id: number;
    start_date: string;
    end_date: string;
    advertisement_image: string;
    ad_text: string;
    priority: number;
}

const Advertisements: React.FC<AdvertisementsProps> = ({ startingIndex }) => {
    const [ads, setAds] = useState<AdvertisementContract[]>([]);
    const [currentAdIndex, setCurrentAdIndex] = useState(startingIndex);

    useEffect(() => {
        const fetchAds = async () => {
            try {
                const response = await axios.get(
                    getWebsiteUrl() + "store/api/advertisements/",
                    { headers: await getAuthHeaders() }
                );
                setAds(response.data);
            } catch (error) {
                console.error("Failed to fetch advertisements:", error);
            }
        };
        fetchAds();
    }, []);

    useEffect(() => {
        if (ads.length > 0) {
            const timer = setInterval(() => {
                setCurrentAdIndex((prevIndex) => (prevIndex + 1) % ads.length);
            }, 20000);
            return () => clearInterval(timer);
        }
    }, [ads]);

    const nextAd = () => {
        if (ads.length > 0) {
            setCurrentAdIndex((prevIndex) => (prevIndex + 1) % ads.length);
        }
    };

    const prevAd = () => {
        if (ads.length > 0) {
            setCurrentAdIndex((prevIndex) =>
                prevIndex === 0 ? ads.length - 1 : prevIndex - 1
            );
        }
    };

    return (
        <div className="banner">
            {ads.length > 0 && currentAdIndex < ads.length ? (
                <>
                    <button
                        className="scroll-button scroll-button--left"
                        onClick={prevAd}
                    >
                        <AiFillLeftCircle />
                    </button>
                    <img
                        src={ads[currentAdIndex].advertisement_image}
                        alt={ads[currentAdIndex].ad_text}
                    />
                    <button
                        className="scroll-button scroll-button--right"
                        onClick={nextAd}
                    >
                        <AiFillRightCircle />
                    </button>
                </>
            ) : (
                <p>No advertisements available</p>
            )}
        </div>
    );
};

export default Advertisements;
