// import React from "react";
// import "./header.css";
//
// import { FaSearch, FaUserCircle } from "react-icons/fa";
// // import styles from './StoreHeader.module.css';
// import "./header.css";
//
// interface StoreHeaderProps {
//     logoUrl: string;
// }
//
// const StoreHeader: React.FC<StoreHeaderProps> = ({ logoUrl }) => {
//     return (
//         <div className="container">
//             <div className="logoContainer">
//                 <img src={logoUrl} alt="Store logo" className="logo" />
//             </div>
//             <nav className="menu"></nav>
//             <div className="login">
//                 <div className="search">
//                     <FaSearch style={{ marginRight: "10px", fontSize: "16px" }} />
//                     <input type="text" placeholder="Search products" />
//                 </div>
//                 <div className="user">
//                     <FaUserCircle style={{ fontSize: "24px" }} />
//                 </div>
//             </div>
//         </div>
//     );
// };
//
// export default StoreHeader;
import React, { useState } from "react";
import { FaSearch, FaUserCircle, FaBars, FaTimes } from "react-icons/fa";
import "./header.css";

interface StoreHeaderProps {
    logoUrl: string;
}

const StoreHeader: React.FC<StoreHeaderProps> = ({ logoUrl }) => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
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
        return <FaUserCircle className="userIcon" />;
    };

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
                    {renderSearchBar()}
                    {renderUserIcon()}
                </div>
            </div>
        </header>
    );
};

export default StoreHeader;
