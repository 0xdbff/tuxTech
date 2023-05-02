// Footer.tsx
import React, { useContext, useEffect, useState } from "react";
import { MiddleContentContext } from "../contexts/middleContentContext";
import "../assets/css/footer.css";

const Footer: React.FC = () => {
    return (
        <footer className={`footer`}>
            <h1>Footer Content A lot of Content Here </h1>
            <h1>Footer Content A lot of Content Here </h1>
            <h1>Footer Content A lot of Content Here </h1>
            <h1>Footer Content A lot of Content Here </h1>
        </footer>
    );
};

export default Footer;
