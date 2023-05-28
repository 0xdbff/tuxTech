import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import ProductsPage from "./pages/ProductsPage";
import ProductInfoPage from "./pages/ProductInfo";
import { ThemeProvider } from "./contexts/themeContext";
import "./assets/css/App.css";

const App: React.FC = () => {
    const initialTheme = localStorage.getItem("theme") || "dark";
    document.body.classList.add(
        "no-transition",
        initialTheme === "light" ? "light-mode" : "dark-mode"
    );

    return (
        <BrowserRouter>
            <ThemeProvider initialTheme={initialTheme}>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/product-info/:uuid" element={<ProductInfoPage />} />
                    <Route path="/products/*" element={<ProductsPage />} />
                </Routes>
            </ThemeProvider>
        </BrowserRouter>
    );
};

export default App;
