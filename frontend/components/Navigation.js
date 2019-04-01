import React from 'react';
import {Container, Row, Col, Button, InputGroup, FormControl, Navbar, Nav} from "react-bootstrap";

class Navigation extends React.Component{
  constructor(props){
    super(props);
    }


  render(){
    let mainNav =
      <Navbar collapseOnSelect expand="lg" bg="light" variant="light">
        <Navbar.Brand
            onClick={() => this.props.switchNavigation(0)}
            style={{
              cursor: "pointer",
            }}
          >
          CROC
        </Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
              <Nav className="mr-auto">
              </Nav>
              <Nav>
                <Nav.Link onClick={() => this.props.switchNavigation(1)}>Добавить</Nav.Link>
                <Nav.Link eventKey={2} onClick={() => this.props.getShowModal(true)}>
                  Авторизация
                </Nav.Link>
              </Nav>
            </Navbar.Collapse>
      </Navbar>;
    return(mainNav);
  }
}

export default Navigation;
