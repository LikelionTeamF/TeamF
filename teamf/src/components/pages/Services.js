import '../../App.css';
import React, { useState } from "react";
import axios from "axios";

function Services() {
  const [text, setText] = useState("없음");
  
  const clicked = () => {
    axios
      .get("http://192.168.135.207:8000/", {
        params: {
          abc: "가나다",
        },
      })
      .then((response) => setText(JSON.stringify(response.data)));
  };

  return (
    <div>
      <h1>{text}</h1>
      <button onClick={clicked}>클릭</button>
    </div>
  );
}

export default Services;