import React from "react";
import "./selectField.css";

interface SelectFieldProps {
    label: string;
    name: string;
    options: string[];
    onChange: (event: React.ChangeEvent<HTMLSelectElement>) => void;
    id?: string;
}

const SelectField: React.FC<SelectFieldProps> = ({
    label,
    name,
    options,
    onChange,
}) => {
    return (
        <div className="select-field">
            <label htmlFor={name}>{label}</label>
            <select id={name} name={name} onChange={onChange}>
                {options.map((option) => (
                    <option key={option} value={option}>
                        {option}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default SelectField;
