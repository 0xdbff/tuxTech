// index.tsx
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import { ThemeProvider } from "./themeContext";
import reportWebVitals from "./reportWebVitals";
import StoreHeader from "./header";
import Footer from "./footer";

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

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
