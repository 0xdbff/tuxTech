import { useEffect, useState } from "react";

const applyBlurToImage = (
    image: HTMLImageElement,
    blurRadius: number
): string => {
    const canvas = document.createElement("canvas");
    const context = canvas.getContext("2d") as CanvasRenderingContext2D;
    canvas.width = image.width;
    canvas.height = image.height;

    context.drawImage(image, 0, 0, image.width, image.height);
    context.filter = `blur(${blurRadius}px)`;

    return canvas.toDataURL();
};

const useBlurredBackground = (
    imageSrc: string,
    blurRadius: number
): string | null => {
    const [blurredImage, setBlurredImage] = useState<string | null>(null);

    useEffect(() => {
        const image = new Image();
        image.src = imageSrc;
        image.onload = () => {
            setBlurredImage(applyBlurToImage(image, blurRadius));
        };
    }, [imageSrc, blurRadius]);

    return blurredImage;
};

export default useBlurredBackground;
