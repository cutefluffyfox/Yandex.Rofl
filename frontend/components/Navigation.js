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
        <Nav.Link eventKey="link-0"
          onClick={() => this.props.switchNavigation(0)}
        >Главная</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link-1"
          onClick={() => this.props.switchNavigation(1)}
        >Добавить решение</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link-2"
          onClick={() => this.props.switchNavigation(2)}
        >Войти</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link-3"
          onClick={() => this.props.switchNavigation(3)}
        > Регистрация </Nav.Link>
      </Nav.Item>
    </Nav>
  )
  }
}

export default Navigation;
