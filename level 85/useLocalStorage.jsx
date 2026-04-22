import { useState } from "react";
import { useEffect } from "react";

function getSavedValue (key, initialValue) {
    const saved = JSON.parse(localStorage.getItem(key))
    if (!saved) {
        return initialValue
    }

    return saved
}



export default function useLocalStorage(key, initialValue) {
    const [value, setValue] = useState(() =>{
        return getSavedValue(initialValue)
    })

    useEffect(() => {
        localStorage.setItem(key, JSON.stringify(value))

    }, [value])

    return [value, setValue]

}