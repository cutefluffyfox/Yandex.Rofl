import React from "react";
import {Container, Row, Col, Button, InputGroup, FormControl, Nav} from "react-bootstrap";
import Navigation from "./Navigation";

class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      c: 0,
    };
    this.incr = this.incr.bind(this);
  };

  incr(){
    this.setState({c: this.state.c + 1})
  };

  render(){

    // let nav =
    // <Nav className="justify-content-end" activeKey="/home">
    //   <Nav.Item>
    //     <Nav.Link>Главная</Nav.Link>
    //   </Nav.Item>
    //   <Nav.Item>
    //     <Nav.Link eventKey="link-1">Популярное</Nav.Link>
    //   </Nav.Item>
    //   <Nav.Item>
    //     <Nav.Link eventKey="link-2">Войти</Nav.Link>
    //   </Nav.Item>
    //   <Nav.Item>
    //     <Nav.Link eventKey="link-3"> Регистрация </Nav.Link>
    //   </Nav.Item>
    // </Nav>;

    return(
      <Container style={{ height: '100%' }}>
        <Row style={{height:'40%'}}>
          <Col>
            <Navigation />
          </Col>
        </Row>
        <Row>
          <Col>
            <main>
            <InputGroup className="mb-3">
              <FormControl
                  placeholder={this.state.c}
                  aria-label="Recipient's username"
                  aria-describedby="basic-addon2"
                />
                <InputGroup.Append>
                  <Button variant="outline-success" onClick={this.incr}>Поиск</Button>
                </InputGroup.Append>
              </InputGroup>
            </main>
          </Col>
        </Row>
      </Container>
    );
  }
};

export default App;
