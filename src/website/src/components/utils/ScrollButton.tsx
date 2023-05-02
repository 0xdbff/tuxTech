import React from "react";
import { AiFillLeftCircle, AiFillRightCircle } from "react-icons/ai";
import "../../assets/css/scrollButton.css";

interface ScrollButtonProps {
    direction: "left" | "right";
    onClick: () => void;
    className?: string;
}

const ScrollButton: React.FC<ScrollButtonProps> = ({
    direction,
    onClick,
    className = "",
}) => {
    return (
        <button
            className={`scroll-button scroll-button--${direction} ${className}`}
            onClick={onClick}
        >
            {direction === "left" ? <AiFillLeftCircle /> : <AiFillRightCircle />}
        </button>
    );
};

export default ScrollButton;
