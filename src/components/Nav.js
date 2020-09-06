import React from 'react';
import '../App.css';
import {Link} from "react-router-dom";

function Nav() {

    return (
        <div className="Nav">
            {/*<img src="../../public/logo.png" alt=""/>*/}
            <div>
                <h3>Flask React App</h3>
            </div>
            <div className="Nav-Links">
                <Link to="/">Home</Link>
                <b>|</b>
                <Link to="/brokers">Brokers</Link>
            </div>
        </div>
    );
}

export default Nav;
