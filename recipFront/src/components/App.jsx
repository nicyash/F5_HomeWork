import React from "react";
import {Link, Route, Routes,} from 'react-router-dom'

import "../styles/App.css";
import Main from "./Main.jsx";
import Recips from "./Recips.jsx";
import RecipFiltr from "./RecipFiltr.jsx";
import TestApp from "./TestApp.jsx";


class App extends React.Component {
    render() {
        return(
            <div className="App">
                <nav>
                    <h1>Рецепты</h1>
                    <div className="header href">
                        <Link to="/">Домашняя страница</Link>
                        <Link to="/recips">Все рецепты</Link>
                        <Link to="/testapp">API</Link>
                    </div>
                </nav>
                <Routes>
                    <Route path="/testapp" element={<TestApp />} />
                    <Route path="/recips" element={<Recips />} />
                    <Route path="/" element={<Main />} />
               </Routes>
               <RecipFiltr/>
            </div>
        )
    }
}

export default App;