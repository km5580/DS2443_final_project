import { useState } from 'react';

function Operation() {
  const [result, setResult] = useState("");
  const [query, setQuery] = useState("")

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const headers = { 'Content-Type': 'application/json' }
      let res = await fetch("http://127.0.0.1:5000/query" + "?query=" + query, {
        method: "GET",
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
      });
      let resJson = await res.json()
      if (res.status === 200) {
        setResult(resJson.result)
      } else {
        alert("Something wrong")
      }
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <>
    <header>
    <h2>Query</h2>
    </header>
    <form onSubmit={handleSubmit}>
    <textarea 
          rows="4" 
          cols="50"
          type="string" 
          name="query" 
          value={query} 
          onChange={(e) => setQuery(e.target.value)}
        />
      <br></br>
      <input type="submit" value="Run this Query"/>
    </form>
    <h2>Results</h2>
    <>{result}</>
    </>
  )
}

export default Operation;
