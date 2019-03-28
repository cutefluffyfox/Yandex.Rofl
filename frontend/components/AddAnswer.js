import React from "react";
import {InputGroup, FormControl, Button} from "react-bootstrap";

class AddAnswer extends React.Component{
  constructor(props){
    super(props);

  }

  render(){
    return(
    <div
      style={{
        marginTop: "8%"
      }}
      >
      <InputGroup className="mb-3" style={{
            width: "50%",
            paddingLeft: "10%",
      }}>
        <InputGroup.Prepend>
          <InputGroup.Text id="inputGroup-sizing-default">ID</InputGroup.Text>
        </InputGroup.Prepend>
        <FormControl
          aria-label="Default"
          placeholder="Номер id"
          aria-describedby="inputGroup-sizing"
          />
      </InputGroup>
      <div style={{
          width: "80%",
          marginLeft: "100px",
        }}>
        <InputGroup
          style={{paddingBottom:"20px"}}>
          <InputGroup.Prepend>
            <InputGroup.Text
              style={{width: "100px"}}>Проблема</InputGroup.Text>
          </InputGroup.Prepend>
          <FormControl
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
              style={{width: "100px"}}>Ответ</InputGroup.Text>
          </InputGroup.Prepend>
          <FormControl
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
