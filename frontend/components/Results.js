import React from "react";
import {Card, Button, Popover} from "react-bootstrap";
import SearchItem from "./SearchItem";



class Results extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      answer: this.props.data,
      found: this.props.found,
    };
    this.find = this.find.bind(this);
  }

  find(text){
    txt = text.split();
    for(var i = 0; i < txt.length; i++){
      text.replace(txt[i], <span style={{background:"#E2FF16"}}>{txt[i]}</span>)
    }


  }

  componentWillReceiveProps(nextProps){
    this.setState({
      answer: nextProps.data,
    })
  }

  render(){
    let renderProblems = this.state.answer.map((v, i) =>
      <SearchItem key={i} problem={v.description} answer={v.reply} id={v.problem_id} mem={v.CALLBACKMEMO} find={this.find}/>
    );
    let header = (this.state.answer.length) ? <Card.Header> Ответы: </Card.Header>: null;

    return(
      <div>
        {header}
        {renderProblems}
      </div>
    )
  }

}

export default Results;
