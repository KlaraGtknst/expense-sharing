import { useState, useEffect } from 'react';

const Fetch = () => {
  const [people, listPeople] = useState([]);
  useEffect(() => {
    fetch('http://127.0.0.1:5000/settings')
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        console.log(data);

      });
  }, []);
  return (
    <div>
        <h1>People</h1>
      {/*{people.map((person) => (*/}
      {/*  <div key={person._id}>*/}
      {/*    <h2>{person.name}</h2>*/}
      {/*    <p>{person.expense}</p>*/}
      {/*  </div>*/}
      {/*))}*/}
    </div>
  );
};
export default Fetch;