export const getWebsiteUrl = () => {
    const env = process.env.NODE_ENV;

    if (env === "production") {
        return process.env.REACT_APP_PUBLIC_URL_PROD;
    } else {
        return process.env.REACT_APP_PUBLIC_URL_DEV;
    }
};

export const getStaticPath = (relativePath: string) => {
    return getWebsiteUrl() + "static/" + relativePath;
};

export const getMediaPath = (relativePath: string) => {
    return getWebsiteUrl() + "media/" + relativePath;
};
