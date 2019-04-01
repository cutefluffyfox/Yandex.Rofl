import React from "react";
import {Image, Button, Modal, Container, Row, Col,
          FormControl, InputGroup} from "react-bootstrap";

class Autorization extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      showModal: this.props.showModal,
    }
  }

  componentWillReceiveProps(nextProps){
    this.setState({
        showModal: nextProps.showModal,
    })
  }

  render(){
    return(
      <Modal
        onHide={this.props.closeWindow}
        show={this.state.showModal}
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header
            closeButton
            variant="dark"
        >
          <Modal.Title id="contained-modal-title-vcenter">
            Авторизация
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Container>
            <Row>
              <Col md={12} lg={6} style={{paddingBottom: "20px"}}>
                <h5>Регистрация</h5>
                <InputGroup className="mb-3">
                  <FormControl
                    placeholder="ФИО"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <InputGroup className="mb-3">
                  <FormControl
                    placeholder="Логин"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <InputGroup className="mb-3">
                  <FormControl
                    placeholder="Пароль"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <InputGroup className="mb-3">
                  <FormControl
                    placeholder="Подтверждение пароля"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <Button
                    variant="outline-dark"
                >Зарегистрироваться</Button>
              </Col>
              <Col md={12} lg={6}>
                <h5>Вход</h5>
                <InputGroup className="mb-3">
                  <FormControl
                    placeholder="Логин"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <InputGroup className="mb-3">
                  <FormControl
                    type="password"
                    placeholder="Пароль"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <Button
                    style={{
                      marginLeft: "80%"
                    }}
                    variant="outline-primary"
                >Войти</Button>
              </Col>
            </Row>
          </Container>
        </Modal.Body>
      </Modal>
    )
  }
}

export default Autorization;
