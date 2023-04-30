import "./assets/css/App.css";
import Home from "./pages/HomePage";
import { BrowserRouter, Route, Routes } from "react-router-dom";
// const backendUrl = process.env.REACT_APP_BACKEND_URL;

const App: React.FC = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
            </Routes>
        </BrowserRouter>
    );
};

export default App;
