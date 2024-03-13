import 'bootstrap/dist/css/bootstrap.min.css';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
//import Stack from 'react-bootstrap/Stack'
import { useRef, useState, useEffect,  } from "react";


function App() {
  const [input, setInput] = useState("");
  const[bookData, setBookData] = useState([]);
  const [showResults, setShowResults] = useState(false)
  
  const recDiv = () => {
    <div>If you liked <i>{input}</i>, then you should try...</div>
  }
  
  const inputref = useRef();
  
  const handleChange = (e) => {
    setInput(e)
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setShowResults(true)
    fetchData(input)
    
  }

  async function getData(){
    return await fetch(`http://localhost:8000/input/${input}`,{
      method: "GET",
        headers:{ "Content-Type": "application/json" },
    })
  }

  const fetchData = (e) =>{
    //e.preventDefault();
    getData()
          .then((response)=> response.json())
          .then((data)=>{
            setBookData(data)
          })
   

  }
  
  return (
    <>
  

  <Container>
   <form  onSubmit={(e) => handleSubmit(e)}>
      <Form.Group className="mb-3" controlId="formBasicEmail">
      
        <Form.Label ref={inputref} ></Form.Label>
        <Form.Control type="text" placeholder="Enter a book!" onChange={ e => handleChange( e.target.value)}/>
        <Form.Text className="text-muted"> Enter a book to get started! </Form.Text>
        <Button variant="primary" type="submit" onClick={(e) => console.log(e)}> Submit </Button>
      
      </Form.Group>
    </form>
    
    {showResults && <div>If you liked <i>{input}</i>, then you should try...</div> }
    <ul>
      {bookData.map((el,i) => <li key={i}>{el}</li> )}
    </ul>
    </Container>
   
    </>
  );
}

export default App;
