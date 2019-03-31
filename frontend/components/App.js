import React from "react";
import {Container, Row, Col, Image, Button} from "react-bootstrap";
import Navigation from "./Navigation";
import Find from "./Find";
import Results from "./Results";
import AddAnswer from "./AddAnswer";
import ErrorModal from "./ErrorModal";
import Autorization from "./Autorization";

class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      switch: 0,
      answer: [],
      findString: '',
      showModal: false,
    }
    this.getResult = this.getResult.bind(this);
    this.changeRender = this.changeRender.bind(this);
    this.getString = this.getString.bind(this);
    this.getShowModal = this.getShowModal.bind(this);
  };

  getResult(parametr){
    this.setState({
      answer: parametr,
    })
  }

  getString(str){
    this.setState({
      findString: str,
    })
  }

  changeRender(num){
    this.setState({
      switch: num,
    });
  }

  getShowModal(par){
    this.setState({
      showModal: par
    })
  }


  render(){

    let mainBlock = null;
    let errorModal = null;

    switch (this.state.switch) {
      case 0:
        mainBlock =
        <Row style={{
          marginTop: (this.state.answer.length) ? "0%" : "15%",
        }}>
          <Col md={{ span: 4, offset: 4 }}>
            { (this.state.answer.length) ? null
              : <Image
                  src="frontend/image/Croc_logo_eng_RGB.png"
                  rounded
                  style={{width: "100%"}}
                />
            }
          </Col>
          <Col
            md={12}
            style={{
              paddingTop: "20px",
            }}
          >
            <Find getResult={this.getResult} findString={this.state.findString}
                  getString={this.getString}/>
            <Results data={this.state.answer } />
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
        errorModal = <ErrorModal />

    }
    return(
      <Container style={{ height: '100%', width: "100%" }} lenAnswer={this.state.answer.length}>
        <Row>
          <Col>
            <Navigation switchNavigation={this.changeRender}
                        getShowModal={this.getShowModal}/>
          </Col>
        </Row>
          {mainBlock}
          {errorModal}
          <Autorization showModal={this.state.showModal}/>
      </Container>
    );
  }
};

export default App;
