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
          problem: 'Это образец проблемы №3',
          answer: 'Ответ на проблему №3'
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
  };

  getResult(parametr){
    this.setState({
      answer: parametr,
    })
  }


  print(){
    console.log("All work")
  };

  render(){
    console.log("All work")
    return(
      <Container style={{ height: '100%' }}>
        <Row style={{height: (this.state.problems.length) ? '10%' : '40%'}}>
          <Col>
            <Navigation />
          </Col>
        </Row>
        <Row>
          <Col>
            <Find getResult={this.getResult}/>
            <Results data={this.state.problems} />
          </Col>
        </Row>
      </Container>
    );
  }
};

export default App;
