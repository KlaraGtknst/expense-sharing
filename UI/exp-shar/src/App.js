import TextField from "./components/TextField.tsx";
import NumberInputBasic from "./components/NumberInput.tsx";
import Fetch from "./components/fetch.jsx";
import * as PropTypes from "prop-types";
import '@vaadin/horizontal-layout';
import {Button} from "@mui/material";
import {styled} from "@mui/system";
import {useState} from "react";


TextField.propTypes = {
    size: PropTypes.string,
    hiddenLabel: PropTypes.bool,
    defaultValue: PropTypes.string,
    variant: PropTypes.string,
    id: PropTypes.string
};

function clickMe() {
  alert("You clicked me!");
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
              <div><TextField/></div>
              <div><NumberInputBasic/></div>
              <div>
                  <Button onClick={clickMe}>
                      Pink theme
                  </Button>
              </div>
          </vaadin-horizontal-layout>

      </div>
  );
}

