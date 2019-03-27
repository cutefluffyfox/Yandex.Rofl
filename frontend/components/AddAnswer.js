import React from "react";
import {InputGroup, FormControl} from "react-bootstrap";

class AddAnswer extends React.Component{
  constructor(props){
    super(props);

  }

  render(){
    return(
    <InputGroup className="mb-3" style={{
          width: "50%",
          paddingLeft: "10%"
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
  );
  };
}
export default AddAnswer;
