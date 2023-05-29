import { createContext, useContext, useState, useEffect } from "react";

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

export const ThemeProvider: React.FC<
    React.PropsWithChildren<{ initialTheme: string }>
> = ({ children, initialTheme }) => {
    const [lightMode, setLightMode] = useState(initialTheme === "light");

    const toggleDarkMode = () => {
        setLightMode(!lightMode);
    };

    useEffect(() => {
        // Remove the no-transition class to re-enable transitions after initial render
        setTimeout(() => {
            document.body.classList.remove("no-transition");
        }, 100);

        localStorage.setItem("theme", lightMode ? "light" : "dark");
        document.body.classList.add(lightMode ? "light-mode" : "dark-mode");
        document.body.classList.remove(lightMode ? "dark-mode" : "light-mode");
    }, [lightMode]);

    return (
        <ThemeContext.Provider value={{ lightMode, toggleDarkMode }}>
            {children}
        </ThemeContext.Provider>
    );
};
