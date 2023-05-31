import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import ProductsPage from "./pages/ProductsPage";
import ProductInfoPage from "./pages/ProductInfo";
import { ThemeProvider } from "./contexts/themeContext";
import withAuth from "./components/utils/withAuth";
import "./assets/css/App.css";

const App: React.FC = () => {
    const initialTheme = localStorage.getItem("theme") || "dark";

    const AuthenticatedHome = withAuth(Home);

    document.body.classList.add(
        "no-transition",
        initialTheme === "light" ? "light-mode" : "dark-mode"
    );

    return (
        <BrowserRouter>
            <ThemeProvider initialTheme={initialTheme}>
                <Routes>
                    <Route path="/" element={<AuthenticatedHome />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/product/:uuid" element={<ProductInfoPage />} />
                    <Route path="/products/*" element={<ProductsPage />} />
                </Routes>
            </ThemeProvider>
        </BrowserRouter>
    );
};

export default App;
