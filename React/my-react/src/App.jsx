import { useState } from "react";


function App(){
  const [count,setcount]=useState(0);


  const increase= ()=>{
    setcount(count+1)
  };

  const decrease=()=>{
    setcount(count-1)

  }
  return (
    <div>
      <h1>{count}</h1>
      <button onClick={increase}>+</button>
      <button onClick={decrease}>-</button>
    </div>
  );

}

export default App;
