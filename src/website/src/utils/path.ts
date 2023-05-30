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

// export const getMediaPath = (django_app_name: string, relativePath: string) => {
//     return django_app_name
//         ? getWebsiteUrl() + django_app_name + "/media/" + relativePath
//         : getWebsiteUrl() + "media/" + relativePath;
// };
