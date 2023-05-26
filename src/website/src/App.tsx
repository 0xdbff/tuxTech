import "./assets/css/App.css";
import Home from "./pages/HomePage";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ProductsPage from "./pages/ProductsPage";
import ProductInfo from "./pages/ProductInfo";
import Login from "./pages/LoginPage";
// const backendUrl = process.env.REACT_APP_BACKEND_URL;

const App: React.FC = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/product-info/:uuid" element={<ProductInfo />} />
                <Route path="/products/*" element={<ProductsPage />} />
            </Routes>
        </BrowserRouter>
    );
};

export default App;
