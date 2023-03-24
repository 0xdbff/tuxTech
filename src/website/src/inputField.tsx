import React from "react";
import "./inputField.css";

interface InputFieldProps {
    label: string;
    name: string;
    type: string;
    onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

const InputField: React.FC<InputFieldProps> = ({
    label,
    name,
    type,
    onChange,
}) => {
    return (
        <div className="input-field">
            <label htmlFor={name}>{label}</label>
            <input id={name} name={name} type={type} onChange={onChange} />
        </div>
    );
};

export default InputField;
