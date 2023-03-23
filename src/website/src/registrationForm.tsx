import React, { useState } from "react";
import axios from "axios";

interface RegistrationFormProps { }

const RegistrationForm: React.FC<RegistrationFormProps> = () => {
    const [formData, setFormData] = useState({
        email: "",
        username: "",
        password: "",
        nif: "",
        receive_news: false,
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleCheckChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, checked } = e.target;
        setFormData({ ...formData, [name]: checked });
    };

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                "http://localhost:8000/register/",
                formData
            );
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="username"
                placeholder="Username"
                value={formData.username}
                onChange={handleChange}
                required
            />
            <input
                type="password"
                name="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="nif"
                placeholder="NIF"
                value={formData.nif}
                onChange={handleChange}
            />
            <input
                type="checkbox"
                name="receive_news"
                checked={formData.receive_news}
                onChange={handleCheckChange}
            />
            <label htmlFor="receive_news">Receive news</label>
            <button type="submit">Register</button>
        </form>
    );
};

export default RegistrationForm;
