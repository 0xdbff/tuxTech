import getAccessToken from "./tokenManager";

const getAuthHeaders = () => {
    const accessToken = getAccessToken();
    return {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
    };
};

export default getAuthHeaders;
