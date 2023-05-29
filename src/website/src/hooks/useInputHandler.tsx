/* eslint-disable react-hooks/rules-of-hooks */
import { useState } from "react";

/**
 * Interface for useInputHandler configuration object.
 */
interface UseInputHandlerConfig {
    name: string;
    value: any;
    onChange: (newValue: any) => void;
    label: string;
    type: string;
}

/**
 * Custom hook to handle the state and change events of input fields.
 *
 * @param config - Configuration object for the input field.
 * @param config.name - The name attribute of the input field.
 * @param config.value - The initial value of the input field.
 * @param config.onChange - Callback function to handle the change event of the input field.
 * @param config.label - The label associated with the input field.
 * @param config.type - The input field's type attribute (e.g., "text", "email", "checkbox").
 *
 * @returns An object containing the label, type, name, value, and onChange properties
 *          to be spread onto the input field component.
 */
export const useInputHandler = ({
    name,
    value,
    onChange,
    label,
    type,
}: UseInputHandlerConfig) => {
    const [inputValue, setInputValue] = useState(value);

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { value, checked } = event.target;
        const newValue = type === "checkbox" ? checked : value;

        setInputValue(newValue);
        onChange(newValue);
    };

    return type === "checkbox"
        ? {
            label,
            type,
            name,
            checked: !!inputValue,
            onChange: handleChange,
        }
        : {
            label,
            type,
            name,
            value: inputValue,
            onChange: handleChange,
            checked: false,
        };
};

export default useInputHandler;
