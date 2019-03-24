import React from "react";

class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      title: "Hello, World!",
    }
  }

  render(){
    return(
      <div>
        <header>Header</header>
        <main>Main</main>
        <footer>Footer</footer>
      </div>
    );
  }
};

export default App;
