import * as React from 'react';
import {useState} from 'react';

import { TextField } from '@mui/material';

const Input = () => {
    const [textInput, setTextInput] = useState('');

    const handleTextInputChange = event => {
        setTextInput(event.target.value);
    };

    const getTextInput = () => {
        return textInput;
    }

    return(
        <TextField
            label="Text Input"
            value= {textInput}
            onChange= {handleTextInputChange}
        />
    );
}

export default Input;