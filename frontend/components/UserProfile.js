import React from "react";
import {Container, Row, Cow} from "react-bootstrap";

export default class UserProfile extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      user:{
        user_name: this.props.user_data.user_name,
        login: this.props.user_data.login,
        token: this.props.user_data.token
      }
    }
  }

  componentWillReceiveProps(nextProps){
      this.setState({
        user: nextProps.user_data,
      })
  }

  render(){
      return(<h1>hallo</h1>);
  }
}
