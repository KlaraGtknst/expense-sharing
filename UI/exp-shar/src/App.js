import TextField from "./components/TextField.tsx";
import NumberInputBasic from "./components/NumberInput.tsx";
import Fetch from "./components/fetch.jsx";
import * as PropTypes from "prop-types";
import '@vaadin/horizontal-layout';


TextField.propTypes = {
    size: PropTypes.string,
    hiddenLabel: PropTypes.bool,
    defaultValue: PropTypes.string,
    variant: PropTypes.string,
    id: PropTypes.string
};
export default function App() {
  return (
      <div className="App">
          <h1>Hello CodeSandbox.</h1>
          <h2>Start editing to see some magic happen!</h2>
          <div><Fetch/></div>
          <vaadin-horizontal-layout theme="spacing padding">
              <div><TextField/></div>
              <div><NumberInputBasic/></div>
          </vaadin-horizontal-layout>

      </div>
  );
}

