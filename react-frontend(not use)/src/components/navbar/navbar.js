import React,{Component} from "react"
import './navbar.css'

export default class Navbar extends Component{
    render(){
        return (
            <>
                <nav className="navbar">
                    <ul className="nav-links">
                        <a href="/" className="logo">
                            <span>
                                ONLINE COURSES    
                            </span>    
                        </a>
                        <li className="nav-item active"><a href="/">Main page</a></li>
                        <li className="nav-item"><a href="/">Contacts</a></li>
                        <li className="nav-item"><a href="/">Help</a></li>
                    </ul>
                    <ul className="nav-links">
                        <li className="nav-item colored"><a href="/">Sign in</a></li>
                        <li className="nav-item button"><a href="/">Sign up</a></li>
                    </ul>
                </nav>
            </>
        )
    }
}