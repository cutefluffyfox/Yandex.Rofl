import React from "react";
import {Container, Row, Col, Image} from "react-bootstrap";
import Navigation from "./Navigation";
import Find from "./Find";
import Results from "./Results";
import AddAnswer from "./AddAnswer";

class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      switch: 0,
      answer: "",
    }
    this.print = this.print.bind(this);
    this.getResult = this.getResult.bind(this);
    this.changeRender = this.changeRender.bind(this);
  };


  getResult(parametr){
    this.setState({
      answer: parametr,
    })
  }


  changeRender(num){
    this.setState({
      switch: num,
    }, console.log(num));
  }

  print(){
    console.log("All work")
  };

  render(){
    let mainBlock = null;

    switch (this.state.switch) {
      case 0:
        mainBlock =
        <Row style={{
                marginTop: (this.state.answer.length) ? "0%" : "11%",
              }}>
          <Col md={{ span: 4, offset: 4 }}>
            <Image src="./image/Croc_logo_eng_RGB.png" rounded
                   style={{width: "100%"}}/>
          </Col>
          <Col md={12}
               style={{
                 paddingTop: "20px",
               }}>
            <Find getResult={this.getResult}/>
            <Results data={(this.state.answer.length) ? this.state.answer: [] } />
          </Col>
        </Row>;
        break;
      case 1:
        mainBlock =
        <Row style={{paddingTop: "10%"}}>
          <Col>
            <AddAnswer/>
          </Col>
        </Row>
        break;
      default:
        mainBlock = null;
    }
    return(
      <Container style={{ height: '100%', width: "100%" }}>
        <Row>
          <Col>
            <Navigation switchNavigation={this.changeRender}/>
          </Col>
        </Row>
          {mainBlock}
      </Container>
    );
  }
};

export default App;
