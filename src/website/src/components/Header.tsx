import React, { useRef, useState, useEffect } from "react";
import {
    FaHeart,
    FaShoppingCart,
    FaSearch,
    FaUserCircle,
    FaBars,
    FaTimes,
    FaMoon,
    FaSun,
} from "react-icons/fa";
import "../assets/css/header.css";
import Login from "./Login";
import { useTheme } from "../contexts/themeContext";
import { getStaticPath } from "../utils/path";

interface StoreHeaderProps {
    logoUrl: string;
}

const useHideHeaderOnScroll = () => {
    const headerRef = useRef<HTMLDivElement | null>(null);
    const lastScrollPosition = useRef(0);
    const [isHeaderVisible] = useState(true);

    const handleScroll = () => {
        const currentScrollPosition = window.pageYOffset;
        const headerElement = headerRef.current;

        if (headerElement) {
            if (currentScrollPosition < lastScrollPosition.current - 20) {
                headerElement.classList.remove("hidden");
                headerElement.style.top = "0px";
            } else if (currentScrollPosition > lastScrollPosition.current + 20) {
                headerElement.classList.add("hidden");
                headerElement.style.top = "-60px";
            }
        }

        lastScrollPosition.current = currentScrollPosition;
    };

    useEffect(() => {
        window.addEventListener("scroll", handleScroll);
        return () => {
            window.removeEventListener("scroll", handleScroll);
        };
    }, []);

    return { headerRef, isHeaderVisible };
};

const StoreHeader: React.FC<StoreHeaderProps> = () => {
    const { headerRef, isHeaderVisible } = useHideHeaderOnScroll();
    const [isLoginFormOpen, setIsLoginFormOpen] = useState(false);
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const { lightMode, toggleDarkMode } = useTheme();

    const logoUrl = getStaticPath("l.svg");

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

    const renderFavIcon = () => {
        return (
            <div>
                <FaHeart className="icon" />
            </div>
        );
    };

    const renderCartIcon = () => {
        return (
            <div>
                <FaShoppingCart className="icon" />
            </div>
        );
    };

    const renderUserIcon = () => {
        return (
            <div onClick={toggleLoginForm}>
                <FaUserCircle className="icon" />
            </div>
        );
    };

    const renderLoginForm = () => {
        return (
            <div className={`login-form-container ${isLoginFormOpen ? "open" : ""}`}>
                <div className="registration-link-container">
                    <a href="/register" onClick={toggleLoginForm}>
                        Register
                    </a>
                </div>
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

    return (
        <header
            className={`header ${isHeaderVisible ? "" : "hidden"}`}
            ref={headerRef}
        >
            <div className="container">
                <div className="menuIcon" onClick={toggleMenu}>
                    {isMenuOpen ? <FaTimes /> : <FaBars />}
                </div>
                {renderMenu()}
                <div className="logoContainer">
                    <img src={logoUrl} alt=" " className="logo" />
                </div>
                <div className="icons">
                    {renderSearchBar()}
                    {renderDarkModeToggle()}
                    {renderFavIcon()}
                    {renderCartIcon()}
                    {renderUserIcon()}
                </div>
                {renderLoginForm()}
            </div>
        </header>
    );
};

export default StoreHeader;
