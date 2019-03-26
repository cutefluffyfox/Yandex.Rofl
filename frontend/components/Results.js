import React from "react";
import {Container, Row, Col, Button, InputGroup, FormControl, Nav} from "react-bootstrap";


class Results extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      answer: this.props.data,
    };
  }

  render(){
    return(
      <h3>{this.state.data}</h3>
    )
  }

}

export default Results;
