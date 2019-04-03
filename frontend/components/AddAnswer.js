import React from "react";
import {InputGroup, FormControl, Button, Alert} from "react-bootstrap";

class AddAnswer extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      id: '',
      callback: '',
      reply: '',
      description: '',
      textAlert: '',
      isLoading: false,
      variant: "danger",
    }
    this.sendSubmit = this.sendSubmit.bind(this);
  }

  sendSubmit(){
    const main = this;
    if(!this.state.id.length ||
       !this.state.callback.length ||
       !this.state.reply.length ||
       !this.state.description.length){
         main.setState({
           textAlert: "Одно из полей все еще пустое. Заполните его!",
         })
         return;
       }
    else{
      fetch('/Record',
      {
        method: 'post',
        headers: {
          'Content-Type':'application/json',
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
        },
        body: JSON.stringify({
          "id": main.state.id,
          "callback": main.state.callback,
          "reply": main.state.reply,
          "description": main.state.description,
        }),
      })
      .then(
        function(response){
          if(response.status != 200){
            main.setState({textAlert: "Упссс... Проверьте подключение к интернету!"})
            console.log("Status Code:" + response.status);
            return
          }
          response.json()
          .then(function(data){
            console.log(data);
            if(data == "success"){
              main.setState({
                variant: "success",
                textAlert: "Ответ отправлен на сервер!",
                id: '',
                callback: '',
                reply: '',
                description: ''
              })
            }
          })
        }
       )
       .catch(
         function(err){
           main.setState({textAlert: "Упссс... Проверьте подключение к интернету!"})
           console.log("Fetch Error :-s", err)
         });
      }
  }



  render(){
    return(
    <div md={8}
      style={{
        marginTop: "0px",
        marginLeft: "10%",
      }}
    >
      <InputGroup
        className="mb-3"
        style={{
          width: "50%",
          minWidth: "100px",
          minHeight: "32px",
        }}
      >
        <InputGroup.Prepend>
          <InputGroup.Text id="inputGroup-sizing-default">ID</InputGroup.Text>
        </InputGroup.Prepend>
        <FormControl
          onChange={event => {
            this.setState({
              id: event.target.value,
            })
          }}
          style={{
            minWidth: "54px",
          }}
          aria-label="Default"
          placeholder="Номер id"
          aria-describedby="inputGroup-sizing"
          value={this.state.id}
        />
      </InputGroup>
      <div style={{
          width: "80%",
        }}>
        <InputGroup
          style={{paddingBottom:"20px"}}>
          <InputGroup.Prepend>
            <InputGroup.Text
              style={{width: "100px"}}>Проблема</InputGroup.Text>
          </InputGroup.Prepend>
          <FormControl
            onChange={event => {
              this.setState({
                callback: event.target.value,
              })
            }}
            value={this.state.callback}
            style={{minHeight: "41px"}}
            as="textarea"
            placeholder="Описание проблемы"
            aria-label="With textarea" />
        </InputGroup>
        <InputGroup
          style={{paddingBottom:"20px"}}>
          <InputGroup.Prepend>
            <InputGroup.Text
              style={{width: "100px"}}>Решение</InputGroup.Text>
          </InputGroup.Prepend>
          <FormControl
            onChange={event => {
              this.setState({
                reply: event.target.value,
              })
            }}
            value={this.state.reply}
            style={{minHeight: "41px"}}
            aria-label="Default"
            placeholder="Краткий ответ"
            aria-describedby="inputGroup-sizing"
          />
        </InputGroup>
        <InputGroup
          style={{paddingBottom:"20px"}}>
          <InputGroup.Prepend>
            <InputGroup.Text
              style={{width: "100px", textAlign:"center"}}>Доп.инфо</InputGroup.Text>
          </InputGroup.Prepend>
          <FormControl
            onChange={event => {
              this.setState({
                description: event.target.value,
              })
            }}
            value={this.state.description}
            style={{minHeight: "41px"}}
            as="textarea"
            placeholder="Решение"
            aria-label="With textarea" />
        </InputGroup>
        <Button variant="primary" size="lg" block
          style={{height: "100%"}}
          onClick={this.sendSubmit}>
            Отправить решение
        </Button>
      </div>
      <div
          style={{
              width: "80%",
              marginTop: "10px",
          }}
        >
        { (this.state.textAlert.length) ?
        <Alert dismissible variant={this.state.variant}
            onClick={() => {
              this.setState({
                textAlert: '',
              })
            }}>
          <p>{this.state.textAlert}</p>
          </Alert>: null}
      </div>
    </div>
  );
  };
}
export default AddAnswer;
