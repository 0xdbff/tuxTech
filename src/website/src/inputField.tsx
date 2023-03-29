// import React from "react";
// import "./inputField.css";
//
// interface InputFieldProps {
//     label: string;
//     name: string;
//     type: string;
//     onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
// }
//
// const InputField: React.FC<InputFieldProps> = ({
//     label,
//     name,
//     type,
//     onChange,
// }) => {
//     return (
//         <div className="input-field">
//             <label htmlFor={name}>{label}</label>
//             <input id={name} name={name} type={type} onChange={onChange} />
//         </div>
//     );
// };
//
// export default InputField;

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
            <input
                id={name}
                name={name}
                type={type}
                onChange={onChange}
                placeholder=" "
                className="input-placeholder"
            />
            <label htmlFor={name}>{label}</label>
        </div>
    );
};

export default InputField;
