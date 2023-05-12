export function getStaticPath(relativePath: string) {
    const env = process.env.NODE_ENV;

    if (env === "production") {
        return process.env.REACT_APP_PUBLIC_URL_PROD + "static/" + relativePath;
    } else {
        return process.env.REACT_APP_PUBLIC_URL_DEV + "static/" + relativePath;
    }
}
