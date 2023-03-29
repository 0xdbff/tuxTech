/* eslint-disable react-hooks/rules-of-hooks */

import { useState } from "react";

interface UseInputHandlerConfig {
    name: string;
    value: any;
    onChange: (newFormData: any) => void;
    label: string;
    type: string;
}

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
        onChange({ ...onChange, [name]: newValue });
    };

    return {
        label,
        type,
        name,
        value: inputValue,
        onChange: handleChange,
    };
};

export default useInputHandler;
