import React, { useState, FormEvent } from "react";
import axios from "axios";

const Login: React.FC = () => {
    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [error, setError] = useState<string | null>(null);

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                "http://localhost:8000/api/login/",
                {
                    username,
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
        } catch (err) {
            if (err instanceof Error) {
                console.log(err.message);
            } else if (axios.isAxiosError(err) && err.response) {
                console.log(err.response);
            }
            setError("Invalid credentials");
        }
    };

    return (
        <div>
            <h2>Login</h2>
            {error && <div>{error}</div>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="username">Username:</label>
                    <input
                        id="username"
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="password">Password:</label>
                    <input
                        id="password"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default Login;
