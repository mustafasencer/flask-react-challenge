import React, {useEffect, useState} from 'react';
import '../App.css';
import {List, Message} from "semantic-ui-react";


function Brokers() {
    const [brokers, setBrokers] = useState([]);
    const [apiSuccess, setApiSuccess] = useState(true);
    useEffect(() => {
        fetch('/api/v1/broker', {method: "GET"})
            .then((response) => {
                return response.json();
            })
            .then((responseJson) => {
                setBrokers(responseJson);
            })
            .catch((error) => {
                setApiSuccess(false);
            });
    }, []);

    return (
        {apiSuccess} && brokers.length > 0 ? <List celled>
            {brokers.map(broker => {
                return (
                    <List.Item key={broker.id}>
                        <List.Icon name='id badge outline'/>
                        <List.Content>
                            <List.Header as='a'>{broker.email}</List.Header>
                            <List.Description>
                                <b>First Name: </b>
                                <i>{broker.firstname} <b> | </b></i>
                                <b>Last Name: </b>
                                <i>{broker.lastname} <b> | </b></i>
                                <b>Address: </b>
                                <i>{broker.address}</i>
                            </List.Description>
                            <List.Description>
                                <div>
                                    <b>Agency Title: </b>
                                    <i>{broker.title} <b> | </b></i>
                                    <b>Agency Domain: </b>
                                    <i>{broker.domain}</i>
                                </div>
                            </List.Description>
                        </List.Content>
                    </List.Item>
                );
            })}
        </List> : apiSuccess && brokers.length === 0 ? <Message info>
            <Message.Header>No Broker Found</Message.Header>
            <p>You can sign up a broker via the Home page.</p>
        </Message> : <Message negative>
            <Message.Header>Ooopss!</Message.Header>
            <p>An error occured during api call.</p>
        </Message>
    )

}

export default Brokers;
