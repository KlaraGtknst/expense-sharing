import TextField from "./components/TextField.tsx";
import DynamicList from "./components/DynamicList.tsx";
import InputNewData from "./components/InputNewData.tsx";
import NumberInputBasic from "./components/NumberInput.tsx";
import Fetch from "./components/fetch.jsx";
import Input from "./components/Input.tsx";
import * as PropTypes from "prop-types";
import '@vaadin/horizontal-layout';
import {Button} from "@mui/material";
import {styled} from "@mui/system";
import {useState} from "react";
import * as React from "react";


TextField.propTypes = {
    size: PropTypes.string,
    hiddenLabel: PropTypes.bool,
    defaultValue: PropTypes.string,
    variant: PropTypes.string,
    id: PropTypes.string
};

function clickMe() {
  // alert("You clicked me!");
    // Simple POST request with a JSON body using fetch
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ person: 'React POST Request Example', expense: 0 })
    };
    fetch('http://127.0.0.1:5000/settings', requestOptions)
        .then(response => response.json())
        .then(data => this.setState({ postId: data.id }));
}

const ButtonToggle = styled(Button)`
  opacity: 0.7;
  ${({ active }) =>
    active &&
    `
    opacity: 1; 
  `}
`;
export default function App() {
  return (
      <div className="App">
          <h1>Hello CodeSandbox.</h1>
          <h2>Start editing to see some magic happen!</h2>
          <div><Fetch/></div>
          <vaadin-horizontal-layout theme="spacing padding">
              {/*<div><TextField/></div>*/}
              {/*<div><Input/></div>*/}
              {/*<div><NumberInputBasic/></div>*/}
              {/*<div><DynamicList/></div>*/}
                <div><InputNewData/></div>  # TODO: callback an class und dann zu fetch
              {/*<div>*/}
              {/*    <Button onClick={clickMe}>*/}
              {/*        Pink theme*/}
              {/*    </Button>*/}
              {/*</div>*/}
          </vaadin-horizontal-layout>

      </div>
  );
}

