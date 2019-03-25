import React from "react";
import {Container, Row, Col, Button, InputGroup, FormControl, Nav} from "react-bootstrap";
import Find from "./Find";

class Result extends React.Components{
  constructor(props){
    super(props);
  }

  render(){
    return(
      <h3>{this.props.data}</h3>
    )
  }

}

export default Result;
