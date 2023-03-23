// Footer.tsx
import React, { useContext, useEffect, useState } from "react";
import { MiddleContentContext } from "./middleContentContext";
import "./footer.css";

const Footer: React.FC = () => {
    const { middleContentRef } = useContext(MiddleContentContext);
    const [isVisible, setIsVisible] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            if (
                middleContentRef?.current &&
                window.scrollY + window.innerHeight >=
                middleContentRef.current.clientHeight
            ) {
                setIsVisible(true);
            } else {
                setIsVisible(false);
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
