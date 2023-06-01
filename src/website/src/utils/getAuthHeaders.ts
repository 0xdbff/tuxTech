import getAccessToken from "./tokenManager";

const getAuthHeaders = async () => {
    const accessToken = await getAccessToken();
    if (!accessToken) {
        return;
    }
    return {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
    };
};

export default getAuthHeaders;
