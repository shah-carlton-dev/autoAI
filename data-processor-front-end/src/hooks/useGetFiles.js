import { useState, useEffect } from "react";
import { API_URL } from "../utils/constants";
export function useGetFiles(page) {
    const [files, setFiles] = useState([]);
    useEffect(() => {
        fetch(`${API_URL}/getAllFiles`)
        .then(response => response.json())
        .then(data => setFiles(data));
    })

    return files;
}
