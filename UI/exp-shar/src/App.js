import TextField from "./components/TextField.tsx";
import InputNewData from "./components/InputNewData.tsx";
import Fetch from "./components/fetch.jsx";
import * as PropTypes from "prop-types";
import '@vaadin/horizontal-layout';
import {Button} from "@mui/material";
import {styled} from "@mui/system";
import {useCallback, useState} from "react";
import * as React from "react";


TextField.propTypes = {
    size: PropTypes.string,
    hiddenLabel: PropTypes.bool,
    defaultValue: PropTypes.string,
    variant: PropTypes.string,
    id: PropTypes.string
};

function clickMe() {
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
    const [newPeople, setPeople] = useState([]);

    const addPeople = useCallback(() => {
    setPeople((t) => [...t, "New Todo"]);
  }, [newPeople]);

  return (
      <div className="App">
          <h1>Expense Sharing</h1>
          <h2>WIP</h2>
          <div><Fetch  people={newPeople} addPeople={addPeople} /></div>
          <vaadin-horizontal-layout theme="spacing padding">

                <div><InputNewData/></div>  # TODO: callback an class und dann zu fetch: https://react.dev/learn/passing-props-to-a-component

          </vaadin-horizontal-layout>

      </div>
  );
}

