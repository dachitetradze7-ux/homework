import React, { useState, useEffect } from 'react';


const useAuth = () => {
  const [user, setUser] = useState(null)
  const [accounts, setAccounts] = useState([]) 

  useEffect(() => {
    const storedUser = JSON.parse(localStorage.getItem("loggeduser"))
    const storedAccount = JSON.parse(localStorage.getItem("accounts") || "[]")
    if (storedUser) setUser(storedUser)
    if (storedAccount) setAccounts(storedAccount)
  }, [])

  const register = (username, password) => {
    const newUser = { username, password }
    const updatedAccounts = [...accounts, newUser]
    setAccounts(updatedAccounts)
    setUser(newUser)
    localStorage.setItem('accounts', JSON.stringify(updatedAccounts))
    localStorage.setItem('loggeduser', JSON.stringify(newUser))
  }

  const login = (username, password) => {
    const foundUser = accounts.find(acc => acc.username === username && acc.password === password) 
    if (foundUser) {
      setUser(foundUser)
      localStorage.setItem('loggeduser', JSON.stringify(foundUser))
    } else {
      alert("araswordi useri an paroli")
    }
  }

  const logout = () => {
    setUser(null)
    localStorage.removeItem('loggeduser')
  }

  return { user, register, login, logout }
}

const useProduct = () => { 
  const [products, setProducts] = useState([])

  useEffect(() => {
    const storeProducts = JSON.parse(localStorage.getItem("products") || "[]")
    setProducts(storeProducts) 
  }, [])

  const addProduct = (product) => {
    const updatedProducts = [...products, product]
    setProducts(updatedProducts)
    localStorage.setItem("products", JSON.stringify(updatedProducts))
  }

  return { products, addProduct }
}

const Registration = ({ register }) => {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  const handleRegister = (e) => {
    e.preventDefault()
    register(username, password) 
  }

  return (
    <form onSubmit={handleRegister}>
      <input type="text" placeholder="username" onChange={(e) => setUsername(e.target.value)} value={username} /> 
      <input type="password" placeholder="password" onChange={(e) => setPassword(e.target.value)} value={password} />
      <button type="submit">register</button>
    </form>
  )
}

const Login = ({ login }) => {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  const handleLogin = (e) => {
    e.preventDefault()
    login(username, password)
  }

  return (
    <form onSubmit={handleLogin}>
      <input type="text" placeholder="username" onChange={(e) => setUsername(e.target.value)} value={username} />
      <input type="password" placeholder="password" onChange={(e) => setPassword(e.target.value)} value={password} />
      <button type="submit">login</button>
    </form>
  )
}

const AdminPanel = ({ logout, products, addProduct }) => {
  const [product, setProduct] = useState("")
  const [price, setPrice] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault()
    addProduct({ product, price })
    setProduct("")
    setPrice("")
  }

  return (
    <>
      <h2>admin panel</h2>
      <button onClick={logout}>logout</button>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="product" value={product} onChange={(e) => setProduct(e.target.value)} required />
        <input type="text" placeholder="price" value={price} onChange={(e) => setPrice(e.target.value)} required />
        <button type="submit">add product</button>
      </form>

      <table>
        <thead>
          <tr>
            <th>product</th>
            <th>price</th>
          </tr>
        </thead>
        <tbody>
          {products.map((p, index) => (
            <tr key={index}>
              <td>{p.product}</td>
              <td>{p.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  )
}

function App() {
  const { user, register, login, logout } = useAuth()
  const { products, addProduct } = useProduct() 

  return (
    <div className="App">
      {!user ? (
        <div>
          <h2>register</h2>
          <Registration register={register} />
          <h2>login</h2>
          <Login login={login} />
        </div>
      ) : (
        <AdminPanel
          logout={logout}
          products={products}
          addProduct={addProduct}
        />
      )}
    </div>
  )
}

export default App;