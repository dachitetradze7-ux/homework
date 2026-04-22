import React from "react";
import { useState } from "react";
import { useEffect } from "react";
function App() {
  const [formState, setFormState] = useState({});
  const hanldeChange = ( {name, value} ) => {
      setFormState((prev) => {
        return {...prev, [name]: value}
        

      })
      console.log(formState)

  }


  return (
    <>
      <input onChange={(e) => hanldeChange(e)} value={formState.username} name="username" type="text" placeholder="Username"/>
      <input onChange={(e) => hanldeChange(e)} value={formState.password} name="password" type="password" placeholder="password"/>

    </>

  )



}





function App () {
  const [url, setUrl] = useState("todos")
  const [data, setData] = useState([])
  
  
  useEffect(() => {
    async function getData() {
      const response = await fetch(`https://jsonplaceholder.typicode.com/${url}`)
      const info = await response.json()
      setData(info)
    }
    getData()

  }, [url])

  


    
   return (
    <>
      <button onClick={() => setUrl("posts")}>posts</button>
      <button onClick={() => setUrl("albums")}>albums</button>
      <button onClick={() => setUrl("todos")}>todos</button>
      
      <ul> 
          {data.map((value, index) => <li key={index}>{value.title}</li>)}
      </ul>

    </>
   )

}

