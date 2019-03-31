import React from "react";
import {Button, InputGroup, FormControl, Spinner} from "react-bootstrap";

class Find extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      findString: this.props.findString,
      isLoading: false,
      getString: this.props.getString,
    }
    this.printFindString = this.printFindString.bind(this);
    this.sendSubmit = this.sendSubmit.bind(this);
  }

  printFindString(e){
    this.state.getString(this.state.findString);
    this.setState({findString : e.target.value});
  }

  sendSubmit(){
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
             "datetime": new Date(),
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
              return;
            }
            // Examine the text in the response
            response.json()
            .then(function(data) {
              console.log(data);
              main.props.getResult(data);
            });
          }
        )
        .catch(
          function(err) {
            main.setState({
              isLoading: false,
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

    return(
      <InputGroup className="mb-3">
        <FormControl
            onChange={this.printFindString}
            value={this.state.findString}
            name="Find"
            placeholder="Название проблемы"
            aria-label="Recipient's username"
            aria-describedby="basic-addon2"
            onKeyPress={ (event) => {
              if(event.key == 'Enter'){
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
        );
      }
};

export default Find;
