import React, {useEffect, useState} from 'react';
import '../App.css';
import {Form, Input, Message, TextArea, Transition} from "semantic-ui-react";

function SignUp() {

    const [values, setValues] = useState({firstname: "", lastname: "", email: "", address: ""});
    const [alertShow, setAlertShow] = useState(false);
    const [alertMessage, setAlertMessage] = useState("");
    const [isError, setIsError] = useState(false);
    const [isLoading, setLoading] = useState(false);
    const [emailError, setEmailError] = useState(false);
    const [firstnameError, setfirstnameError] = useState(false);
    const [lastnameError, setlastnameError] = useState(false);
    const [addressError, setaddressError] = useState(false);

    useEffect(() => {
        if (alertShow) {
            const timer = setTimeout(() => {
                setAlertShow(false);
            }, 1000);
            return () => clearTimeout(timer);
        }
    }, [alertShow, alertMessage]);

    const handleChange = (e, {name, value}) => {
        setValues({...values, [name]: value});
    };

    const handleSubmit = () => {
        const body = {values};
        setLoading(true);

        if (body.values.firstname === '') {
            setfirstnameError(true);
            setLoading(false);
            return
        } else {
            setfirstnameError(false);
        }
        if (body.values.lastname === '') {
            setlastnameError(true);
            setLoading(false);
            return
        } else {
            setlastnameError(false);
        }
        if (body.values.address === '') {
            setaddressError(true);
            setLoading(false);
            return
        } else {
            setaddressError(false);
        }
        if (body.values.email === '') {
            setEmailError(true);
            setLoading(false);
            return
        } else {
            setEmailError(false);
        }

        fetch('/api/v1/broker', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body.values)
        })
            .then((response) => {
                return response.json();
            })
            .then((responseJson) => {
                setAlertShow(true);
                if (responseJson.status >= 400) {
                    setAlertMessage(responseJson.err_msg);
                    setIsError(true);
                    setLoading(false);
                    return
                }
                setAlertMessage("You have successfully signed up.");
                setIsError(false);
                setLoading(false);
                setValues({firstname: "", lastname: "", email: "", address: ""})
            })
            .catch((error) => {
                setAlertShow(true);
                setLoading(false);
            });
    };

    return (
        <Form className="Form" onSubmit={handleSubmit} loading={isLoading}>
            <Form.Group widths='equal'>
                <Form.Input
                    control={Input}
                    fluid
                    label='First name'
                    placeholder='First name'
                    name="firstname"
                    value={values.firstname}
                    onChange={handleChange}
                    error={firstnameError}
                />
                <Form.Input
                    control={Input}
                    label='Last name'
                    placeholder='Last name'
                    name="lastname"
                    value={values.lastname}
                    onChange={handleChange}
                    error={lastnameError}

                />
            </Form.Group>
            <Form.Input
                control={TextArea}
                label='Address'
                placeholder='Address'
                name="address"
                value={values.address}
                onChange={handleChange}
                error={addressError}
            />
            <Form.Input
                control={Input}
                label='Email'
                placeholder='test@cyberworld.com'
                name="email"
                value={values.email}
                onChange={handleChange}
                fluid
                error={emailError}
            />
            <Form.Button content='Submit'/>
            <Transition visible={alertShow}  duration={3000}>
                {!isError ? (<Message positive>
                    <Message.Header>Success!</Message.Header>
                    <p>{alertMessage}</p>
                </Message>) : (<Message negative>
                    <Message.Header>Ooops!</Message.Header>
                    <p>{alertMessage}</p>
                </Message>)}
            </Transition>

        </Form>
    );
}

export default SignUp;
