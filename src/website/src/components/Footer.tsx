// Footer.tsx
import React, { useContext, useEffect, useState } from "react";
import { MiddleContentContext } from "../contexts/middleContentContext";
import "../assets/css/footer.css";

const Footer: React.FC = () => {
    const { middleContentRef } = useContext(MiddleContentContext);
    const [isVisible, setIsVisible] = useState(true);

    useEffect(() => {
        const handleScroll = () => {
            if (
                middleContentRef?.current &&
                window.scrollY + window.innerHeight >=
                middleContentRef.current.clientHeight
            ) {
                setIsVisible(true);
            } else {
                setIsVisible(true);
            }
        };

        window.addEventListener("scroll", handleScroll);
        return () => {
            window.removeEventListener("scroll", handleScroll);
        };
    }, [middleContentRef]);

    return (
        <footer className={`footer${isVisible ? " footer-visible" : ""}`}>
            <h1>Footer Content A lot of Content Here </h1>
            <h1>Footer Content A lot of Content Here </h1>
            <h1>Footer Content A lot of Content Here </h1>
            <h1>Footer Content A lot of Content Here </h1>
        </footer>
    );
};

export default Footer;
