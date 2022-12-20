import { useState } from 'react';
import './Survey.css';

function Survey() {
  const [age, setAge] = useState("");
  const [sex, setSex] = useState("");
  const [bmi, setBmi] = useState("");
  const [children, setChildren] = useState("");
  const [smoke, setSmoke] = useState("");
  const [region, setRegion] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const headers = { 'Content-Type': 'application/json' }
      let res = await fetch("http://127.0.0.1:5000/survey" + "?age=" + age + "&sex=" + sex + "&bmi=" + bmi + "&children=" + children + "&smoke=" + smoke + "&region=" + region, {
        method: "GET",
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
      });
      let resJson = await res.json()
      if (res.status === 200) {
        alert("Your charge is " + resJson.result)
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
    <h2>Survey</h2>
    </header>
    <form onSubmit={handleSubmit}>
      <label>Enter your age:
        <input 
          type="number" 
          name="age" 
          value={age} 
          onChange={(e) => setAge(e.target.value)}
        />
        </label>
      <br></br>
      <label>Choose your gender:
      <select name="sex" id="sex" value={sex} onChange={(e) => setSex(e.target.value)}>
        <option value="female">female</option>
        <option value="male">male</option>
      </select>
      </label>
      <br></br>
      <label>Enter your bmi:
      <input 
        type="number" 
        name="bmi"
        value={bmi}
        onChange={(e) => setBmi(e.target.value)}
      />
      </label>
      <br></br>
      <label>Enter your number of children:
      <input 
        type="number" 
        name="children" 
        value={children}
        onChange={(e) => setChildren(e.target.value)}
      />
      </label>
      <br></br>
      <label>Do you smoke?
      <select name="smoke" id="smoke" value={smoke} onChange={(e) => setSmoke(e.target.value)}>
        <option value="no">no</option>
        <option value="yes">yes</option>
      </select>
      </label>
      <br></br>
      <label>Where are you?
      <select name="region" id="region" value={region} onChange={(e) => setRegion(e.target.value)}>
        <option value="southwest">southwest</option>
        <option value="southeast">southeast</option>
        <option value="northwest">northwest</option>
        <option value="northeast">northeast</option>
      </select>
      </label>
      <br></br>
        <input type="submit" />
    </form>
    </>
  )
}

export default Survey;
