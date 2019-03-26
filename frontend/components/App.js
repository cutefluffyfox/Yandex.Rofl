import React from "react";
import {Container, Row, Col} from "react-bootstrap";
import Navigation from "./Navigation";
import Find from "./Find";
import Results from "./Results";

class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      answer: "",
    }
    this.print = this.print.bind(this);
    this.getResult = this.getResult.bind(this);
  };

  getResult(parametr){
    this.setState({
      answer: parametr
    })
  }


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
            <Find getResult={this.getResult}/>
            <Results data={this.state.answer}/>
          </Col>
        </Row>
      </Container>
    );
  }
};

export default App;
