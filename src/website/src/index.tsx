// index.tsx
import React from "react";
import ReactDOM from "react-dom/client";
import "./assets/css/index.css";
import App from "./App";
import { ThemeProvider } from "./contexts/themeContext";
import reportWebVitals from "./reportWebVitals";
import StoreHeader from "./components/Header";
import Footer from "./components/Footer";

const logoUrl = "https://example.com/logo.png";

const root = ReactDOM.createRoot(
    document.getElementById("root") as HTMLElement
);
root.render(
    <React.StrictMode>
        <ThemeProvider>
            <StoreHeader logoUrl={logoUrl} />
            <App />
            <Footer />
        </ThemeProvider>
    </React.StrictMode>
);

if (process.env.NODE_ENV !== 'production') {
    reportWebVitals(console.log);
}
