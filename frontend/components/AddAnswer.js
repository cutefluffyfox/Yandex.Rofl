import React from "react";
import {InputGroup, FormControl, Button} from "react-bootstrap";

class AddAnswer extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      id: '',
      callback: '',
      reply: '',
      description: '',
    }
  }


  render(){
    return(
    <div
      style={{
        marginTop: "0px",
        marginLeft: "20%",
      }}
      >
      <InputGroup className="mb-3" style={{
            width: "50%",
            minWidth: "100px",
            minHeight: "32px",
      }}>
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
            style={{minHeight: "41px"}}
            aria-label="Default"
            placeholder="Краткий ответ на проблему"
            aria-describedby="inputGroup-sizing"
          />
        </InputGroup>
        <InputGroup
          style={{paddingBottom:"20px"}}>
          <InputGroup.Prepend>
            <InputGroup.Text
              style={{width: "100px", textAlign:"center"}}>Ответ</InputGroup.Text>
          </InputGroup.Prepend>
          <FormControl
            onChange={event => {
              this.setState({
                description: event.target.value,
              })
            }}
            style={{minHeight: "41px"}}
            as="textarea"
            placeholder="Решение"
            aria-label="With textarea" />
        </InputGroup>
        <Button variant="primary" size="lg" block
          style={{
            height: "100%",
          }}>
            Отправить решение
        </Button>
      </div>
    </div>
  );
  };
}
export default AddAnswer;
