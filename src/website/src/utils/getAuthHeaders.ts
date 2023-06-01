import getAccessToken from "./tokenManager";

const getAuthHeaders = async () => {
    const accessToken = await  getAccessToken();
    return {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
    };
};

export default getAuthHeaders;
