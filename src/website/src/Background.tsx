// Background.tsx
import React from "react";
// import "./Background.css";

interface BackgroundProps {
    imageUrl: string;
    gradient: string;
    linkUrl?: string;
    rotation?: number;
}

const Background: React.FC<BackgroundProps> = ({
    imageUrl,
    gradient,
    linkUrl,
    rotation,
}) => {
    const backgroundImage = `linear-gradient(${gradient}), url(${imageUrl})`;

    return (
        <div
            className="background"
            style={{
                backgroundImage,
                transform: rotation ? `rotate(${rotation}deg)` : undefined,
            }}
        >
            {linkUrl && <a href={linkUrl} className="background-link"></a>}
        </div>
    );
};

export default Background;
