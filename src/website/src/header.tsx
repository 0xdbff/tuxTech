import React, { useState, useEffect } from "react";
import {
    FaSearch,
    FaUserCircle,
    FaBars,
    FaTimes,
    FaMoon,
    FaSun,
} from "react-icons/fa";
import "./header.css";
import Login from "./login";
import { useTheme } from "./themeContext";

interface StoreHeaderProps {
    logoUrl: string;
}

const StoreHeader: React.FC<StoreHeaderProps> = ({ logoUrl }) => {
    const [isLoginFormOpen, setIsLoginFormOpen] = useState(false);
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const { lightMode, toggleDarkMode } = useTheme();

    const renderDarkModeToggle = () => {
        return (
            <div onClick={toggleDarkMode} className="dark-mode-toggle">
                {lightMode ? <FaSun /> : <FaMoon />}
            </div>
        );
    };

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    const toggleLoginForm = () => {
        setIsLoginFormOpen(!isLoginFormOpen);
    };

    const renderMenu = () => {
        return (
            <nav className={`menu ${isMenuOpen ? "open" : ""}`}>
                <ul>
                    <li>Home</li>
                    <li>About Us</li>
                    <li>Contact</li>
                </ul>
            </nav>
        );
    };

    const renderSearchBar = () => {
        return (
            <div className="search">
                <FaSearch className="searchIcon" />
                <input type="text" placeholder="Search products" />
            </div>
        );
    };

    const renderUserIcon = () => {
        return (
            <div onClick={toggleLoginForm}>
                <FaUserCircle className="userIcon" />
            </div>
        );
    };

    const renderLoginForm = () => {
        return (
            <div className={`login-form-container ${isLoginFormOpen ? "open" : ""}`}>
                <Login />
            </div>
        );
    };

    const handleClickOutside = (e: MouseEvent) => {
        if (isLoginFormOpen) {
            const loginFormContainer = document.querySelector(
                ".login-form-container"
            );
            if (
                loginFormContainer &&
                !loginFormContainer.contains(e.target as Node)
            ) {
                setIsLoginFormOpen(false);
            }
        }
    };

    useEffect(() => {
        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, [isLoginFormOpen]);

    // return (
    //     <header className="header">
    //         <div className="container">
    //             <div className="logoContainer">
    //                 <img src={logoUrl} alt="Store logo" className="logo" />
    //             </div>
    //             <div className="menuIcon" onClick={toggleMenu}>
    //                 {isMenuOpen ? <FaTimes /> : <FaBars />}
    //             </div>
    //             {renderMenu()}
    //             <div className="login">
    //                 {renderMenu()}
    //                 {renderSearchBar()}
    //                 {renderDarkModeToggle()}
    //                 {renderUserIcon()}
    //                 {renderLoginForm()}
    //             </div>
    //         </div>
    //     </header>
    // );

    return (
        <header className="header">
            <div className="container">
                <div className="logoContainer">
                    <img src={logoUrl} alt="Store logo" className="logo" />
                </div>
                <div className="menuIcon" onClick={toggleMenu}>
                    {isMenuOpen ? <FaTimes /> : <FaBars />}
                </div>
                {renderMenu()}
                <div className="login">
                    <div className="icons">
                        {renderSearchBar()}
                        {renderDarkModeToggle()}
                        {renderUserIcon()}
                    </div>
                    {renderLoginForm()}
                </div>
            </div>
        </header>
    );
};

export default StoreHeader;
