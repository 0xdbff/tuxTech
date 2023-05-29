import React, { useState } from "react";
import Login from "../components/Login";
import Registration from "../components/Registration";
import "../assets/css/loginPage.css";
import { getStaticPath } from "../utils/path";

const LoginPage: React.FC = () => {
    const logoUrl = getStaticPath("l.svg");

    return (
        <div>
            <div className="logoLoginContainer">
                <div className="logoLogin">
                    <img src={logoUrl} alt=" " className="logo" />
                </div>
            </div>
            <div className="loginPage">
                <div className="loginPage-container">
                    <div className="loginPage-container-register">
                        <Registration />
                    </div>
                    <div className="loginPage-container-login">
                        <Login />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default LoginPage;
