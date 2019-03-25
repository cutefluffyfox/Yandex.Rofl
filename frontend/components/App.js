import React from "react";
import {Container, Row, Col, Button, InputGroup, FormControl, Nav} from "react-bootstrap";
import Navigation from "./Navigation";
import Find from "./Find";

class App extends React.Component{

  constructor(props){
    super(props);
    // this.state = {
    //   c: 0,
    // };
    this.print = this.print.bind(this);
  };

  print(){
    console.log("All work")
  };

  render(){
    console.log("All work")
    return(
      <Container style={{ height: '100%' }}>
        <Row style={{height:'40%'}}>
          <Col>
            <Navigation />
          </Col>
        </Row>
        <Row>
          <Col>
            <Find />
          </Col>
        </Row>
      </Container>
    );
  }
};

export default App;
