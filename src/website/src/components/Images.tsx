import React, { useEffect, useState } from "react";

function Images() {
    const [mediaItems, setMediaItems] = useState([]);

    useEffect(() => {
        fetch("http://localhost:8000/api/media/")
            .then((response) => response.json())
            .then((data) => setMediaItems(data));
    }, []);

    return (
        <div>
            {mediaItems.map(
                (media: {
                    id: number;
                    name: string;
                    media_type: string;
                    url: string;
                }) => (
                    <img key={media.id} src={media.url} alt={media.name} />
                )
            )}
        </div>
    );
}

export default Images;
