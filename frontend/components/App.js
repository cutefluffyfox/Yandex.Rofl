import React from "react";
import {Container, Row, Col, Image, Modal, Button} from "react-bootstrap";
import Navigation from "./Navigation";
import Find from "./Find";
import Results from "./Results";
import AddAnswer from "./AddAnswer";

class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      switch: 0,
      answer: [],
    }
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
    });
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
            : <Image src="frontend/image/Croc_logo_eng_RGB.png"
                   rounded
                   style={{width: "100%"}}/> }
          </Col>
          <Col md={12}
               style={{
                 paddingTop: "20px",
               }}>
            <Find getResult={this.getResult}/>
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
        mainBlock = null;
        errorModal =
            <Modal
              show
              size="lg"
              aria-labelledby="contained-modal-title-vcenter"
              centered
            >
              <Modal.Header>
                  <Modal.Title id="contained-modal-title-vcenter">
                      Ууупсс... Что-то пошло не так!
                  </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                  <h4>Ошибка соединения!</h4>
                  <p>
                    Страница не смогла загрузиться.<br/>
                    Перезагрузите страницу!
                  </p>
                </Modal.Body>
                <Modal.Footer>
                  <Button
                    onClick={
                      () => {
                        window.location.reload()
                      }
                    }
                  >Close</Button>
                </Modal.Footer>
          </Modal>;
    }
    return(
      <Container style={{ height: '100%', width: "100%" }}>
        <Row>
          <Col>
            <Navigation switchNavigation={this.changeRender}/>
          </Col>
        </Row>
          {mainBlock}
          {errorModal}
      </Container>
    );
  }
};

export default App;
