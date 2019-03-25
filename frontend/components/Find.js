import React from "react";
import {Container, Row, Col, Button, InputGroup, FormControl, Nav} from "react-bootstrap";
import Navigation from "./Navigation";

class Find extends React.Component{

  render(){
    return(
      <InputGroup className="mb-3">
        <FormControl
            placeholder="Название проблемы"
            aria-label="Recipient's username"
            aria-describedby="basic-addon2"
          />
          <InputGroup.Append>
            <Button variant="outline-success">Поиск</Button>
          </InputGroup.Append>
          </InputGroup>
    );
  }


};

export default Find;
