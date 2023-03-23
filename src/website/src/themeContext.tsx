// src/ThemeContext.tsx
import { createContext, useContext, useState } from "react";

type ThemeContextType = {
    lightMode: boolean;
    toggleDarkMode: () => void;
};

const ThemeContext = createContext<ThemeContextType>({
    lightMode: false,
    toggleDarkMode: () => { },
});

export const useTheme = () => {
    return useContext(ThemeContext);
};

export const ThemeProvider: React.FC<React.PropsWithChildren<{}>> = ({
    children,
}) => {
    const [lightMode, setDarkMode] = useState(false);

    const toggleDarkMode = () => {
        setDarkMode(!lightMode);
    };

    return (
        <ThemeContext.Provider value={{ lightMode, toggleDarkMode }}>
            {children}
        </ThemeContext.Provider>
    );
};
