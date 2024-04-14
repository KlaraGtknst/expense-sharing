function ListPeople() {

   const people = ['Person 1', 'Person 2', 'Person 3']
      return (
        <>
            <h2>People</h2>
            <ul>
                {people.map((person, index) => (
                <li key={index}>{person}</li>
                ))}
            </ul>
        </>
      );
}


export default ListPeople;