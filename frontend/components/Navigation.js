import React from 'react';
import {Container, Row, Col, Button, InputGroup, FormControl, Nav} from "react-bootstrap";

class Navigation extends React.Component{
  constructor(props){
    super(props);
  }

  render(){
    return(
    <Nav className="justify-content-end" activeKey="/home">
      <Nav.Item>
        <Nav.Link>Главная</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link-1">Популярное</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link-2">Войти</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link-3"> Регистрация </Nav.Link>
      </Nav.Item>
    </Nav>
  )
  }
}

export default Navigation;
