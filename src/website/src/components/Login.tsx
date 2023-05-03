/* eslint-disable react-hooks/rules-of-hooks */
import React, { useState, FormEvent } from "react";
import axios from "axios";
import InputField from "./utils/inputField";
import useInputHandler from "../hooks/useInputHandler";
import { getWebsiteUrl } from "../utils/path";
import getAuthHeaders from "../utils/getAuthHeaders";

const Login: React.FC = () => {
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [error, setError] = useState<string | null>(null);

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                getWebsiteUrl() + "/users/api/login/",
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
            // Redirect to your desired page
            // !TODO
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
            // onChange: (e) => setEmail(e.target.value),
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
            // onChange: (e) => setPassword(e.target.value),
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
                {renderEmailField()}
                {renderPasswordField()}
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default Login;
