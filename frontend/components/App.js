import React from "react";
import {Container, Row, Col} from "react-bootstrap";
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
      problems: [
        {
          problem: 'Это образец проблемы №1',
          answer: 'Ответ на проблему №1'
        },
        {
          problem: 'Это образец проблемы №2',
          answer: 'Ответ на проблему №2'
        },
        {
          problem: 'Ы',
          answer: 'КУ'
        },
        {
          problem: 'Это образец проблемы №4',
          answer: 'Ответ на проблему №4'
        },
        {
          problem: 'Это образец проблемы №5',
          answer: 'Ответ на проблему №5'
        },
      ],
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
          <Col>
            <Find getResult={this.getResult}/>
            <Results data={(this.state.problems.length) ? this.state.problems: [] } />
          </Col>;
        break;
      case 1:
        mainBlock =
          <Col>
            <AddAnswer/>
          </Col>
        break;
      default:
        mainBlock = null;
    }
    return(
      <Container style={{ height: '100%' }}>
        <Row style={{height: (this.state.problems.length) ? '10%' : '40%'}}>
          <Col>
            <Navigation switchNavigation={this.changeRender}/>
          </Col>
        </Row>
        <Row>
          {mainBlock}
        </Row>
      </Container>
    );
  }
};

export default App;
