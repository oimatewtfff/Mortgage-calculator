import React from 'react';
import Table from 'react-bootstrap/Table'
import { useState } from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

const BASE_URL = 'http://127.0.0.1:8000'

function App() {
  const [price, setPrice] = useState('');
  const [deposit, setDeposit] = useState('');
  const [term, setTerm] = useState('');
  const [order, setOrder] = useState('');
  const [list, setList] = useState([]);

  let handleSubmit = async (event) => {
    event.preventDefault();
    try {
      let response = await fetch(
        `${BASE_URL}/api/offer/?ordering=${order}&deposit=${deposit}&price=${price}&term=${term}`
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
      <Row className="justify-content-md-center mt-5 text-center">
        <h1 class="display-6">Ипотечный калькулятор</h1>
      </Row>
      <Row className="justify-content-md-center mt-5">
        <Col sm={7}>
          <form onSubmit={handleSubmit}>
            <div class="input-group">
              <input
                class="form-control form-control-lg"
                id="price"
                name="price"
                placeholder='Стоимость недвижимости'
                type="number"
                onChange={event => setPrice(event.target.value)}
                value={price}
                min="0"
              />
              <input
                class="form-control form-control-lg"
                id="deposit"
                name="deposit"
                placeholder='Первоначальный взнос'
                type="number"
                value={deposit}
                min="0"
                onChange={event => setDeposit(event.target.value)}
              />
              <input
                class="form-control form-control-lg"
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
              <button class="btn btn-outline-secondary" type="submit">Показать</button>
            </div>
          </form>
        </Col>
      </Row>
      <Row className="justify-content-md-center mt-5">
        <Col md="auto">
          <form onSubmit={handleSubmit}>
            <div class="input-group input-group-sm mb-3">
              <input
                class="form-control"
                id="term"
                name="term"
                type="button"
                value="По возрастанию"
                onClick={event => setOrder("rate_min")}
              />
              <input
                class="form-control"
                id="term"
                name="term"
                type="button"
                value="По убыванию"
                onClick={event => setOrder("-rate_min")}
              />
            </div>
          </form>
          <figure class="text-center">
            <figcaption class="blockquote-footer">
              <cite title="Source Title">после выбора снова нажми "Показать"</cite>
            </figcaption>
          </figure>
        </Col>
      </Row>
      <Row className="justify-content-md-center mt-5">
        <Col md="auto">
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Наименование банка</th>
                <th>Ставка</th>
                <th>Ежемесячный платеж</th>
              </tr>
            </thead>
            <tbody>
              {list.map(list => (
                <tr key={list.id}>
                  <td>{list.bank_name}</td>
                  <td>от {list.rate_min}%</td>
                  <td>{Math.round((price - deposit) * (list.rate_min / 100 / 12) / (1 - (1 + (list.rate_min / 100 / 12)) ** -(term * 12)))} ₽</td>
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
