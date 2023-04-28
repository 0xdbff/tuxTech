/* eslint-disable react-hooks/rules-of-hooks */

import React, { useState } from "react";
import InputField from "./inputField";
import SelectField from "./selectField";
import useInputHandler from "./useInputHandler";
import "./registration.css";

const Registration: React.FC = () => {
    const [formData, setFormData] = useState({
        first_name: "",
        last_name: "",
        email: "",
        username: "",
        gender: "",
        nif: "",
        date_of_birth: "",
        is_subscribed_to_news: false,
    });

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        // Replace with your Django REST API endpoint
        const apiUrl = "https://your-django-api.com/api/register/";

        try {
            const response = await fetch(apiUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });

            if (response.ok) {
                const data = await response.json();
                console.log("Registration successful", data);
            } else {
                console.error("Registration failed");
            }
        } catch (error) {
            console.error("Error:", error);
        }
    };

    const renderFirstNameField = () => {
        const firstNameFieldProps = useInputHandler({
            name: "first_name",
            value: formData.first_name,
            onChange: setFormData,
            label: "First Name*",
            type: "text",
        });

        return <InputField {...firstNameFieldProps} />;
    };

    const renderLastNameField = () => {
        const lastNameFieldProps = useInputHandler({
            name: "last_name",
            value: formData.last_name,
            onChange: setFormData,
            label: "Last Name*",
            type: "text",
        });

        return <InputField {...lastNameFieldProps} />;
    };

    const renderEmailField = () => {
        const emailFieldProps = useInputHandler({
            name: "email",
            value: formData.email,
            onChange: setFormData,
            label: "Email*",
            type: "email",
        });

        return <InputField {...emailFieldProps} />;
    };

    // !TODO
    // !TODO
    // !TODO
    // const renderGenderField = () => {
    //     const genderFieldProps = useInputHandler({
    //         name: "gender",
    //         value: formData.gender,
    //         onChange: setFormData,
    //         label: "Gender",
    //         type: "select",
    //     });
    //
    //     return (
    //         <SelectField
    //             {...genderFieldProps}
    //             id="gender"
    //             options={[
    //                 { value: "", label: "Select Gender" },
    //                 { value: "male", label: "Male" },
    //                 { value: "female", label: "Female" },
    //                 { value: "other", label: "Other" },
    //             ]}
    //         />
    //     );
    // };

    const renderNifField = () => {
        const nifFieldProps = useInputHandler({
            name: "nif",
            value: formData.nif,
            onChange: setFormData,
            label: "NIF",
            type: "text",
        });

        return <InputField {...nifFieldProps} />;
    };

    const renderDateOfBirthField = () => {
        const dateOfBirthFieldProps = useInputHandler({
            name: "date_of_birth",
            value: formData.date_of_birth,
            onChange: setFormData,
            label: "Date of Birth*",
            type: "date",
        });

        return <InputField {...dateOfBirthFieldProps} />;
    };

    const renderIsSubscribedToNewsField = () => {
        const isSubscribedToNewsFieldProps = useInputHandler({
            name: "is_subscribed_to_news",
            value: formData.is_subscribed_to_news,
            onChange: setFormData,
            label: "Subscribe to Newsletter",
            type: "checkbox",
        });

        return <InputField {...isSubscribedToNewsFieldProps} />;
    };

    return (
        <div className="registration">
            <div className="registration-container">
                <div className="form-container">
                    <form onSubmit={handleSubmit}>
                        <h2> O registo é facil e grátis!</h2>
                        {renderFirstNameField()}
                        {renderLastNameField()}
                        {renderEmailField()}
                        {renderNifField()}
                        {renderDateOfBirthField()}
                        {renderIsSubscribedToNewsField()}
                        <button type="submit">Register</button>
                    </form>
                </div>
            </div>
        </div>
    );
};
// {renderGenderField()}

export default Registration;
