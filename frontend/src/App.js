import React from 'react';
import Table from 'react-bootstrap/Table'
import { useState } from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

const BASE_URL = 'http://127.0.0.1:8000'

function App() {
  const [price, setPrice] = useState([]);
  const [deposit, setDeposit] = useState([]);
  const [term, setTerm] = useState([]);
  const [list, setList] = useState([]);

  let handleSubmit = async (event) => {
    event.preventDefault();
    try {
      let response = await fetch(
        `${BASE_URL}/api/offer/?deposit=${deposit}&price=${price}&term=${term}`
      );
      let data = await response.json();
      if (response.status === 200) {
        console.log(data)
        setList(data)
      }
    } catch (err) {
      console.log(err);
    }
  }

  return (
    <Container fluid>
      <Row className="justify-content-md-center mt-5">
        <Col md="auto">
          <form onSubmit={handleSubmit}>
            <input
              id="price"
              name="price"
              placeholder='Стоимость недвижимости'
              type="number"
              onChange={event => setPrice(event.target.value)}
              value={price}
              min="0"
            />
            <input
              id="deposit"
              name="deposit"
              placeholder='Первоначальный взнос'
              type="number"
              value={deposit}
              min="0"
              onChange={event => setDeposit(event.target.value)}
            />
            <input
              id="term"
              name="term"
              placeholder='Срок'
              type="number"
              value={term}
              min="0"
              list="default"
              onChange={event => setTerm(event.target.value)}
            />
            <datalist id="default">
              <option>1</option>
              <option>1.5</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
              <option>6</option>
              <option>7</option>
              <option>8</option>
              <option>9</option>
              <option>10</option>
              <option>12</option>
              <option>15</option>
              <option>20</option>
              <option>25</option>
              <option>30</option>
            </datalist>
            <button type="submit">Показать</button>
          </form>
        </Col>
      </Row>
      <Row className="justify-content-md-center mt-5">
        <Col md="auto">
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
                  <td>{(price - deposit) * (list.rate_min / 100 / 12) / (1 - (1 + (list.rate_min / 100 / 12)) ** -(term * 12))}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
