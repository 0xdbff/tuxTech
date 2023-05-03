const getAuthHeaders = () => {
    const accessToken = localStorage.getItem("access");
    return {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
    };
};

export default getAuthHeaders;
