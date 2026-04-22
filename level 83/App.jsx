function App () {
  const [accounts, setAccounts] = useState([]);
  const [loggedUSer, setLoggedUser] = useState(null);

  useEffect(() => {
    setAccounts(JSON.parse(localStorage.getItem("accounts")) || [])
    setLoggedUser(JSON.parse(localStorage.getItem("loggeduSer")) || [])
  }, [])
 

  // useEffect(() => {
  //   localStorage.setItem("accounts", JSON.stringify(accounts))

  // }, accounts)

  const handleRegister = (e) => {
    e.preventDefault();
    let account = {
      username: e.target.username.value,
      password: e.target.password.value
    }

    

    

    setAccounts((prev) => {
      const updated = [...prev, account];
      localStorage.setItem("accounts", JSON.stringify(updated));
      return updated
    })


  }

  const handleLogin = (e) => {
    e.preventDefault();
    const username = e.target.username.value;
    const password = e.target.password.value;

    const correctInfo = accounts.some(accounts.username === username & accounts.password === password )

    if (correctInfo) {
      setLoggedUser(username)
    }
  }





  return (
    <>
        <h2>register</h2>
        <form onSubmit={handleRegister}>
          <input placeholder="username" name="username" type="text" required/>
          <input placeholder="password" name="password" type="password" required/>
          <button type="submit">send</button>
        </form>
        <h2>log in</h2>

        <form onSubmit={() => handleform("login")}>
          <input placeholder="username" name="username" type="text" required/>
          <input placeholder="password" name="password" type="password" required/>
          <button type="submit">send</button>
        </form>
    </>
  )
}

export default App