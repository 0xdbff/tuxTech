/* eslint-disable react-hooks/rules-of-hooks */
import axios from "axios";
import { getWebsiteUrl } from "./path";
import { useNavigate } from "react-router-dom";

const isTokenExpired = (token: string): boolean => {
    try {
        const payload = JSON.parse(atob(token.split(".")[1]));
        const exp = payload.exp * 1000;
        return Date.now() > exp;
    } catch (err) {
        console.error("Error checking token expiration:", err);
        return true;
    }
};

const getAccessToken = async (): Promise<string | null> => {
    const navigate = useNavigate();
    const refreshToken = localStorage.getItem("refresh");
    const accessToken = localStorage.getItem("access");

    if (!accessToken || !refreshToken) {
        navigate("/login");
        return null;
    }

    if (!isTokenExpired(accessToken)) {
        return accessToken;
    }

    try {
        const response = await axios.post(
            getWebsiteUrl() + "users/api/refresh_token/",
            {
                refresh: refreshToken,
            }
        );
        const newAccessToken = response.data.access;
        localStorage.setItem("access", newAccessToken);
        return newAccessToken;
    } catch (error) {
        console.error("Error refreshing token:", error);
        return null;
    }
};

export default getAccessToken;
