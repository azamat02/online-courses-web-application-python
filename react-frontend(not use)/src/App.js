import React,{Component} from "react"
import CoursesSlider from "./components/courses-slider"
import Navbar from './components/navbar'
import CoursesList from "./components/courses-list"
import Footer from "./components/footer"
import './App.css'
import {Modal, Button} from 'react-bootstrap'

export default class App extends Component{
  constructor(props){
    super(props)
    
    this.state = {

    }
  }

  render() {
    return (
      <>
        <Navbar/>
        <main>
          <CoursesSlider/>
          <CoursesList/>
        </main>
        <Footer/>
      </>
    )
  }
}
