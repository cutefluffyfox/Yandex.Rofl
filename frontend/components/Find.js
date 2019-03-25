import React from "react";
import {Container, Row, Col, Button, InputGroup, FormControl, Nav} from "react-bootstrap";
import Navigation from "./Navigation";

class Find extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      findString: ''
    }
    this.printFindString = this.printFindString.bind(this);
    this.sendSubmit = this.sendSubmit.bind(this);
  }

  printFindString(e){
    this.setState({findString : e.target.value});
  }

  sendSubmit(){
    var letter = this.state.findString;
  }



  render(){
    return(
      <InputGroup className="mb-3">
        <FormControl
            onChange={this.printFindString}
            name="Find"
            placeholder="Название проблемы"
            aria-label="Recipient's username"
            aria-describedby="basic-addon2"
          />
          <InputGroup.Append>
            <Button variant="outline-success"
              onClick={this.sendSubmit}>
                  Поиск
            </Button>
          </InputGroup.Append>
          </InputGroup>
    );
  }


};

export default Find;
