import React from 'react';
import './App.css';
import {BrowserRouter, Route, Switch} from "react-router-dom";
import SignUp from "./components/SignUp";
import Brokers from "./components/Brokers";
import Nav from "./components/Nav";
import {Container} from "semantic-ui-react";

function App() {
    return (
        <Container className="Container">
            <BrowserRouter>
                <Nav/>
                <Switch>
                    <Route exact path="/">
                        <SignUp/>
                    </Route>
                    <Route path="/brokers">
                        <Brokers/>
                    </Route>
                </Switch>
            </BrowserRouter>
        </Container>

    );
}

export default App;
