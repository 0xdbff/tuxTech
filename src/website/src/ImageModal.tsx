// ImageModal.tsx
import React, { useState, useEffect } from "react";
import "./ImageModal.css";

interface ImageModalProps {
    src: string;
    alt?: string;
}

const ImageModal: React.FC<ImageModalProps> = ({ src, alt }) => {
    const [isOpen, setIsOpen] = useState(false);

    useEffect(() => {
        const appContent = document.getElementById("app-content");
        if (appContent) {
            if (isOpen) {
                appContent.classList.add("blurred");
            } else {
                appContent.classList.remove("blurred");
            }
        }
    }, [isOpen]);

    const toggleModal = () => {
        setIsOpen(!isOpen);
    };

    return (
        <>
            <img className="thumbnail" src={src} alt={alt} onClick={toggleModal} />
            {isOpen && (
                <div className="modal-backdrop" onClick={toggleModal}>
                    <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                        <img className="modal-image" src={src} alt={alt} />
                    </div>
                </div>
            )}
        </>
    );
};

export default ImageModal;
