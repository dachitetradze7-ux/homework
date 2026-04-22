import { useState } from "react";
import { useEffect } from "react";
import useLocalStorage from "./useLocalStorage";
import React from "react";


function App() {

  // const [username, setUsername] = useLocalStorage();

  const [user, setUser] = useLocalStorage("user", "jon doe" )
  return (
    <>
    <input type="text" name="username" onChange={(e) => setUser(e.target.value)} value={user} />
    <h1>{user}</h1>
    </>
  )
  



}

export default App;