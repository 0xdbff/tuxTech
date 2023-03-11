import React from 'react';
import './header.css';

import { FaSearch, FaUserCircle } from 'react-icons/fa';
// import styles from './StoreHeader.module.css';
import './header.css'

interface StoreHeaderProps {
    logoUrl: string;
}

const StoreHeader: React.FC<StoreHeaderProps> = ({ logoUrl }) => {
    return (
        <div className='container'>
            <div className='logoContainer'>
                <img src={logoUrl} alt="Store logo" className='logo' />
            </div>
            <nav className='menu'>
            </nav>
            <div className='login'>
                <div className='search'>
                    <FaSearch />
                    <input type="text" placeholder="Search products" />
                </div>
                <div className='user'>
                    <FaUserCircle />
                    <span>Login</span>
                </div>
            </div>
        </div>
    );
};

export default StoreHeader;
