import React, { useRef, useState, useEffect } from "react";
import ScrollButton from "./ScrollButton";
import "../../assets/css/scrollableContainer.css";

interface ScrollableContainerProps {
    children: React.ReactNode;
    className?: string;
    scrollStep?: number;
    renderContent: (
        content: React.ReactNode,
        ref: React.Ref<HTMLDivElement>
    ) => JSX.Element;
}

const ScrollableContainer: React.FC<ScrollableContainerProps> = ({
    children,
    scrollStep = 100,
    renderContent,
}) => {
    const containerRef = useRef<HTMLDivElement>(null);
    const [canScrollLeft, setCanScrollLeft] = useState(false);
    const [canScrollRight, setCanScrollRight] = useState(false);

    useEffect(() => {
        const handleResize = () => {
            if (containerRef.current) {
                const { scrollLeft, scrollWidth, clientWidth } = containerRef.current;
                setCanScrollLeft(scrollLeft > 0);
                setCanScrollRight(scrollLeft + clientWidth < scrollWidth);
            }
        };

        handleResize();
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    const scroll = (direction: "left" | "right") => {
        if (containerRef.current) {
            containerRef.current.scrollBy({
                left: direction === "right" ? scrollStep : -scrollStep,
                behavior: "smooth",
            });
        }
    };

    return (
        <>
            {canScrollLeft && (
                <ScrollButton direction="left" onClick={() => scroll("left")} />
            )}
            {renderContent(children, containerRef)}
            {canScrollRight && (
                <ScrollButton direction="right" onClick={() => scroll("right")} />
            )}
        </>
    );
};

export default ScrollableContainer;
