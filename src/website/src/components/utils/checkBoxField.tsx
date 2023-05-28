import React from "react";
import "../../assets/css/checkboxField.css";

interface CheckboxFieldProps {
    label: string;
    name: string;
    checked: boolean;
    onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

const CheckboxField: React.FC<CheckboxFieldProps> = ({
    label,
    name,
    checked,
    onChange,
}) => {
    return (
        <div className="checkbox-field">
            <input
                id={name}
                name={name}
                type="checkbox"
                checked={checked}
                onChange={onChange}
            />
            <label htmlFor={name}>{label}</label>
        </div>
    );
};

export default CheckboxField;
