function App() {
  const [tasks, setTasks] = useState([])

  const handleSubmit = (e) =>{
    e.preventDefault();
    let newTask = e.target.value.elements.username;
    setTasks((prev) => [...prev, newTask])
  }
  
  


  return (
    <>
      <form onSubmit={handleSubmit} action="">
        <input placeholder="task" name="username" />
        <button type="submit">Add task</button>
      </form>

      <h2>tasks</h2>
      <ul>
        {tasks.map((value, item) => {
          return <li key={item}>{value}</li>
        })}
            
      </ul>
    </>

  )

}


export default App;