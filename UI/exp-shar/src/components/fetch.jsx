import { useState, useEffect } from 'react';

const Fetch = () => {
  const [people, setPeople] = useState([]);
  useEffect(() => {
    fetch('http://127.0.0.1:5000/settings')
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setPeople(data)
      });
  }, []);
  return (
      <div>
        <h1>People</h1>
        <ul>
          {people.map((person, index) => (
              <li key={person._id}>{person.name}</li>
          ))}
        </ul>
      </div>
  );
};
export default Fetch;