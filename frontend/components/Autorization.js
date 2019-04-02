import React from "react";
import {Image, Button, Modal, Container, Row, Col,
          FormControl, InputGroup, Alert} from "react-bootstrap";

class Autorization extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      showModal: this.props.showModal,
      enter: {
        login: '',
        password: '',
      },
      registration: {
        login: '',
        password: '',
        reppassword: '',
        user_name: ''
      },
      textAlert: '',
      variant: "danger",
    }
    this.enter = this.enter.bind(this);
    this.writeDataRegistration = this.writeDataRegistration.bind(this);
    this.writeDataLogin = this.writeDataLogin.bind(this);
    this.registration = this.registration.bind(this);
    this.same = this.same.bind(this);
  }

  componentWillReceiveProps(nextProps){
    this.setState({
        showModal: nextProps.showModal,
    })
  }

  registration(){
    let login = this.state.registration.login;
    let password = this.state.registration.password;
    let user_name = this.state.registration.user_name
    const main = this;
    if(this.state.registration.password != this.state.registration.reppassword){
      main.setState({
        textAlert: "Пароли  не совпадают!",
      })
    }

    else if(!this.state.registration.login.length ||
            !this.state.registration.Password.length ||
            !this.state.registration.reppassword.length ||
            !this.state.registration.user_name.length){
      main.setState({
        textAlert: "Не все поля заполнены!",
      })
      return;
    }

    else{
    fetch('/Register',
    {
      method: 'post',
      headers: {
        'Content-Type':'application/json',
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
      },
      body: JSON.stringify({
       "login": login,
       "password": password,
       "user_name": user_name,
      }),
    })
    .then(
    function(response) {
      if (response.status !== 200) {
        console.log('Status Code: ' +
          response.status);
        return;
      }
      // Examine the text in the response
      response.json()
      .then(function(data) {
        console.log(data);
        if(data == "Password Error"){
          main.setState({
            textAlert: "Пароль должен содержать:\n  1)Буквы и цифры,\n  2)Длина от 6 до 32.",
          })
        }
      });
    }
  )
  .catch(
    function(err) {
      console.log('Fetch Error :-S', err);
    });
  }
}

  enter(){
    let login = this.state.enter.login;
    let password = this.state.enter.password;
    const main = this;


    fetch('/Find',
    {
      method: 'post',
      headers: {
        'Content-Type':'application/json',
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
      },
      body: JSON.stringify({
       "login": login,
       "password": password,
      }),
    })
    .then(
    function(response) {
      if (response.status !== 200) {
        console.log('Status Code: ' +
          response.status);
        return;
      }
      // Examine the text in the response
      response.json()
      .then(function(data) {
        console.log(data);
      });
    }
  )
  .catch(
    function(err) {
      console.log('Fetch Error :-S', err);
    });
  }

  writeDataRegistration(first, second){
      this.same();
      this.setState({
        registration: {
          ...this.state.registration,
          [second]: first.target.value,
        }
    })
  }

  writeDataLogin(first, second){
      this.setState({
        enter: {
          ...this.state.enter,
          [second]: first.target.value,
        }
    })
  }

  same(){
    let answer = (this.state.registration.password != this.state.registration.reppassword) ? true : false;
    let ret = (answer) ? "Пароли  не совпадают!" : '';
    this.setState({
      textAlert: {ret},
    })
  }

  render(){

    let modalAlert =
    (this.state.textAlert.length) ?
    <Alert dismissible variant="danger"
        onClick={() => {
          this.setState({
            textAlert: '',
          })
        }}>
      <p>{this.state.textAlert}</p>
      </Alert>: null;

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
              <Col md={12} lg={6} xs={12} style={{paddingBottom: "20px"}}>
                <h5>Регистрация</h5>
                <InputGroup className="mb-3">
                  <FormControl
                    onChange={(e) => this.writeDataRegistration(e, 'user_name')}
                    placeholder="ФИО"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <InputGroup className="mb-3">
                  <FormControl
                    onChange={(e) => this.writeDataRegistration(e, 'login')}
                    placeholder="Логин"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <InputGroup className="mb-3">
                  <FormControl
                    onChange={(e) => this.writeDataRegistration(e, 'password')}
                    placeholder="Пароль"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                {modalAlert}
                <InputGroup className="mb-3">
                  <FormControl
                    onChange={(e) => this.writeDataRegistration(e, 'reppassword')}
                    placeholder="Подтверждение пароля"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <Button
                    onClick={this.registration}
                    variant="outline-dark"
                >Зарегистрироваться</Button>

              </Col>
              <Col md={12} lg={6} xs={6}>
                <h5>Вход</h5>
                <InputGroup className="mb-3">
                  <FormControl
                    onChange={(e) => this.writeDataLogin(e, 'login')}
                    placeholder="Логин"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <InputGroup className="mb-3">
                  <FormControl
                    onChange={(e) => this.writeDataLogin(e, 'password')}
                    type="password"
                    placeholder="Пароль"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <Button
                    onClick={this.enter}
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
