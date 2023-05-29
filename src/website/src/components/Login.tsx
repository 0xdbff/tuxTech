/* eslint-disable react-hooks/rules-of-hooks */

import React, { useState, FormEvent } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import InputField from "./utils/inputField";
import useInputHandler from "../hooks/useInputHandler";
import { getWebsiteUrl } from "../utils/path";
import "../assets/css/registration.css";

const Login: React.FC = () => {
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [error, setError] = useState<string | null>(null);
    const navigate = useNavigate();

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                getWebsiteUrl() + "users/api/login/",
                {
                    email,
                    password,
                },
                {
                    headers: {
                        "Content-Type": "application/json",
                    },
                }
            );
            localStorage.setItem("access", response.data.access);
            localStorage.setItem("refresh", response.data.refresh);
            setError(null);

            navigate("/");
        } catch (err) {
            if (err instanceof Error) {
                console.log(err.message);
            } else if (axios.isAxiosError(err) && err.response) {
                console.log(err.response);
            }
            setError("Invalid credentials");
        }
    };

    const renderEmailField = () => {
        const emailFieldProps = useInputHandler({
            name: "email",
            value: email,
            onChange: setEmail,
            label: "Email",
            type: "email",
        });

        return <InputField {...emailFieldProps} />;
    };

    const renderPasswordField = () => {
        const passwordFieldProps = useInputHandler({
            name: "password",
            value: password,
            onChange: setPassword,
            label: "Password",
            type: "password",
        });

        return <InputField {...passwordFieldProps} />;
    };

    return (
        <div>
            <h2>Login</h2>
            {error && <div>{error}</div>}
            <form onSubmit={handleSubmit}>
                <h2>Ja tens conta TuxTech?</h2>
                {renderEmailField()}
                {renderPasswordField()}
                <div className="buttons-container">
                    <button type="submit">Login</button>
                </div>
                <div className="spacer"></div>
                <h3>Ou entra com uma rede Social</h3>
                <div className="spacer"></div>
                <div className="buttons-container-google">
                    <button type="submit">Login with Google</button>
                </div>
                <div className="buttons-container-fb">
                    <button type="submit">Login with Facebook</button>
                </div>
            </form>
        </div>);
};

export default Login;
