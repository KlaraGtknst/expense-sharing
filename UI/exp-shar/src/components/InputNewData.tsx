import * as React from 'react';
import {useState} from 'react';

function TextFieldAndPostRequest() {
  const [textInputValue, setTextInputValue] = useState('');
  const [numberInputValue, setNumberInputValue] = useState('');

  const handleTextChange = (event) => {
    setTextInputValue(event.target.value);
  };

  const handleNumberChange = (event) => {
    setNumberInputValue(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      console.log(textInputValue, parseFloat(numberInputValue))
      const response = await fetch('http://127.0.0.1:5000/settings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ person: textInputValue, expense: parseFloat(numberInputValue) })
      });

      if (!response.ok) {
        throw new Error('Failed to send data to the server');
      }

      // Handle successful response if needed
      console.log('Data sent successfully', response, JSON.stringify({ person: textInputValue, expense: parseFloat(numberInputValue) }));
    } catch (error) {
      console.error('Error:', error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="text">Text Input:</label>
        <input
          type="text"
          id="text"
          value={textInputValue}
          onChange={handleTextChange}
          placeholder="Enter text..."
        />
      </div>
      <div>
        <label htmlFor="number">Number Input:</label>
        <input
          type="number"
          id="number"
          value={numberInputValue}
          onChange={handleNumberChange}
          placeholder="Enter number..."
        />
      </div>
      <button type="submit">Send to Backend</button>
    </form>
  );
}

export default TextFieldAndPostRequest;
