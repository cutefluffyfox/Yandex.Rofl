import React from "react";
import {Button, InputGroup, FormControl, Spinner, Modal, Alert} from "react-bootstrap";

class Find extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      findString: this.props.findString,
      isLoading: false,
      getString: this.props.getString,
      idUser: this.props.idUser,
      see: false,
      results: false,
    }
    this.printFindString = this.printFindString.bind(this);
    this.sendSubmit = this.sendSubmit.bind(this);
  }

  componentWillReceiveProps(nextProps){
    this.setState({
      idUser: nextProps.idUser,
    })
  }

  printFindString(e){
    this.state.getString(this.state.findString);
    this.setState({findString : e.target.value});
  }

  sendSubmit(){
      if (this.state.isLoading)
        return;

      const main = this;
      let letter = this.state.findString;
      if(letter == ''){
          return;
        }
      else{
          main.setState({
            isLoading: true,
          });

          fetch('/Find',
          {
            method: 'post',
            headers: {
              'Content-Type':'application/json',
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
            },
            body: JSON.stringify({
             "searchValue": letter,
             "datetime": + new Date(),
             "idUser": main.state.idUser,
            }),
          })
          .then(
          function(response) {
            main.setState({
              isLoading: false,
            });
            if (response.status !== 200) {
              console.log('Looks like there was a problem. Status Code: ' +
                response.status);
              if(response.status === 500){
                  main.setState({
                    results: true,
                  });
              }
              else{
                main.setState({results: false})
              }
              return;
            }

            // Examine the text in the response
            response.json()
            .then(function(data) {
              console.log(data);
              (data != []) ? main.props.getResult(data.answers || []) : main.props.getResult(data);
              if(data.errors == 'server is busy'){
                main.setState({
                  see: true,
                });
              }
            });
          }
        )
        .catch(
          function(err) {
            main.setState({
              isLoading: false,
              see: true,
            });
          console.log('Fetch Error :-S', err);
        });
      }
  }

  render(){
    const main = this;
    let loading = (this.state.isLoading) ?
    <Spinner
      as="span"
      animation="grow"
      size="sm"
      role="status"
      aria-hidden="true"
      /> : null;

    let modalBusy =
      <Modal
          size="10%"
          centered
          show={this.state.see}
          onHide={() => {this.setState({see: false,})}}
          aria-labelledby="example-modal-sizes-title-sm"
        >
        <Modal.Header closeButton>
          <Modal.Title id="example-modal-sizes-title-sm">
            Ошибка запроса
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
                  <p>
                    Извините, сервер перегружен множеством запросов!<br/>
                    Повторите запрос.<br/>
                    Если ошибка повториться - перезагрузите страницу.
                  </p>
        </Modal.Body>
      </Modal>;

    let noResults =
      <Alert variant="secondary" style={{marginTop: "20px"}}>
            <p>
              Нет результатов по запросу "{this.state.findString}".
            </p>
      </Alert>

    return(
      <div>
      <InputGroup className="mb-3">
        {modalBusy}
        <FormControl
            onChange={this.printFindString}
            value={this.state.findString}
            name="Find"
            placeholder="Название проблемы"
            aria-label="Recipient's username"
            aria-describedby="basic-addon2"
            onKeyPress={ (event) => {
              if(event.key == 'Enter' ){
                main.sendSubmit();
              }
              return false;
            }}
          />
          <InputGroup.Append>
            <Button variant="outline-success"
              onClick={this.sendSubmit}>
                  {loading} Поиск
            </Button>
            </InputGroup.Append>
        </InputGroup>
        {(this.state.results) ? noResults : null}
        </div>
        );
      }
};

export default Find;
