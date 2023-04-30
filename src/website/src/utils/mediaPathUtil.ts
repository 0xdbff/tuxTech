export function getMediaPath(relativePath: string) {
    const env = process.env.NODE_ENV;

    if (env === "production") {
        return process.env.PUBLIC_URL_PROD + "media/" + relativePath;
    } else {
        return process.env.PUBLIC_URL_DEV  + relativePath;
    }
}