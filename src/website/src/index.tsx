import React from "react";
import ReactDOM from "react-dom/client";
import "./assets/css/index.css";
import reportWebVitals from "./reportWebVitals";
import App from "./App";

const root = ReactDOM.createRoot(
    document.getElementById("root") as HTMLElement
);
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);

if (process.env.NODE_ENV !== "production") {
    reportWebVitals(console.log);
}
