import React from 'react';
import {Container, Row, Col, Button, InputGroup, FormControl, Navbar, Nav} from "react-bootstrap";

class Navigation extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      id: this.props.id,
    }
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
          <img src="frontend/image/Logo-04.png"
               style={{
                 height: "40px",
               }}
          />
        </Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
              <Nav className="mr-auto">
              </Nav>
              <Nav>
                <Nav.Link onClick={() => this.props.switchNavigation(1)}>Добавить</Nav.Link>
              </Nav>
            </Navbar.Collapse>
      </Navbar>;
    return(mainNav);
  }
}

export default Navigation;
