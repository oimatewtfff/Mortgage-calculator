import React from 'react';
import Table from 'react-bootstrap/Table'
import { useState } from 'react';

const BASE_URL = 'http://127.0.0.1:8000'

function App() {
  const [price, setPrice] = useState([]);
  const [deposit, setDeposit] = useState([]);
  const [term, setTerm] = useState([]);
  const [list, setList] = useState([]);

  let handleSubmit = async (event) => {
    event.preventDefault();
      let response = await fetch(
        `${BASE_URL}/api/offer/?deposit=${deposit}&price=${price}&term=${term}`
      );
      let data = await response.json();
      console.log(data)
      setList(data)
  }
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          id="price"
          name="price"
          type="text"
          onChange={event => setPrice(event.target.value)}
          value={price}
        />
        <input
          id="deposit"
          name="deposit"
          type="text"
          value={deposit}
          onChange={event => setDeposit(event.target.value)}
        />
        <input
          id="term"
          name="term"
          type="text"
          value={term}
          onChange={event => setTerm(event.target.value)}
        />
        <button type="submit">Submit form</button>
      </form>
      <Table table position-relative variant="primary" className="mt-5">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Наименование банка</th>
                    <th>Ипотечная ставка, %</th>
                    <th>Платеж по ипотеке, Руб.</th>
                </tr>
            </thead>
            <tbody>
                {list.map(list => (
                    <tr key={list.id}>
                        <td>{list.id}</td>
                        <td>{list.bank_name}</td>
                        <td>{list.rate_min}</td>
                        <td>{(price-deposit)*(list.rate_min/100/12)/(1-(1+(list.rate_min/100/12))**-(term*12))}</td>
                    </tr>
                ))}
            </tbody>
        </Table>
    </div>
  );
}

export default App;
