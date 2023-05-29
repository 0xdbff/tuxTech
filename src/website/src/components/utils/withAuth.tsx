import React from "react";
import { Navigate } from "react-router-dom";

interface Props {
    [key: string]: any;
}

const withAuth = (WrappedComponent: React.ComponentType<Props>) => {
    return (props: Props) => {
        const isLoggedIn = !!localStorage.getItem("access");

        if (!isLoggedIn) {
            return <Navigate to="/login" replace />;
        }

        return <WrappedComponent {...props} />;
    };
};

export default withAuth;

