import { useState, useEffect } from 'react';
import InputNewData from "./InputNewData.tsx";
import * as React from "react";

const Fetch = ({newPeople, addPeople}) => {
  const [people, setPeople] = useState([]);
  useEffect(() => {
    fetch('http://127.0.0.1:5000/people')
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setPeople(data)
      });
  }, []);

  const addToList = (newEntry) => {
    // Add new entry to the list
    setPeople([...people, newEntry]);
  };

  return (
      <div>
          <h1>People</h1>
          <ul>
              {people.map((person, index) => (
                  <li key={person._id}>{person.name} paid {person.expense}</li>
              ))}
          </ul>
          {/*<InputNewData addToList={addToList()}/>*/}

      </div>
  );
};
export default Fetch;