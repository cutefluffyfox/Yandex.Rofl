import React from "react";
import {Container, Row, Col} from "react-bootstrap";

class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      title: "Hello, World!",
    }
  }

  render(){
    return(
      <Container style={{ height: '100%' }}>
        <Row style={{height:'20%'}}>
          <Col>
            <header>Header</header>
          </Col>
        </Row>
        <Row>
          <Col>
            <main>Main</main>
          </Col>
        </Row>
        <Row>
          <Col>
            <footer>Footer</footer>
          </Col>
        </Row>
      </Container>
    );
  }
};

export default App;
