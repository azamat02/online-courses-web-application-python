import React,{Component} from "react"
import './courses-slider.css'

export default class CoursesSlider extends Component{
    constructor(props) {
        super(props)

        // this.data = props.data;
        this.data = [
            {courseImage: 'https://bit.ly/2R5NtiC',  courseTitle: 'Course 1', courseDesc: 'Course 1 desc'},
            {courseImage: 'https://bit.ly/3tZ1m0F',  courseTitle: 'Course 2', courseDesc: 'Course 2 desc'},
            {courseImage: 'https://bit.ly/32UxkPT',  courseTitle: 'Course 3', courseDesc: 'Course 3 desc'},
            {courseImage: 'https://bit.ly/331Bx49',  courseTitle: 'Course 4', courseDesc: 'Course 4 desc'},
        ]

        this.state = {
            timerId: null,
            currentSlide: 0   
        }
    }

    componentDidMount() {
        this.timerId = setInterval(
            ()=>{this.changeData()}, 5000
        )
    }

    componentWillUnmount() {
        clearInterval(this.timerId)
    }

    changeData = ()=>{
        let dataLength = this.data.length
        dataLength -= 1
        if (this.state.currentSlide === dataLength) {
            this.setState({currentSlide:0})
        } else {
            let num = this.state.currentSlide
            num++
            this.setState({currentSlide: num})
        }
    }

    nextSlide = ()=>{
        let {currentSlide} = this.state
        let num = currentSlide;
        if(currentSlide === this.data.length-1) {
            num = 0
        }
        else {
            num ++
        }
        this.setState({currentSlide:num})
        console.log("next");
    }

    prevSlide = ()=>{
        let {currentSlide} = this.state
        let num = currentSlide;
        if(currentSlide === 0) {
            num = 3
        }
        else {
            num --
        }
        this.setState({currentSlide:num})
        console.log("prev");
    }

    render() {
        let {currentSlide} = this.state
        let {courseImage, courseTitle, courseDesc} = this.data[currentSlide]

        let dots = [0,1,2,3].map((elem)=>{
            if(elem === currentSlide){
                return (<span className="active-dot"></span>)
            } else {
                return (<span></span>)
            }
        })
        return (
            <>
                <div className="slider-container">
                    <div className="slider-image">
                        <img className="course-img" src={courseImage} alt=""/>
                    </div>
                    <div className="slider-content">
                        <div className="indicators">
                            <div className="indicator-dots">
                                  {dots} 
                            </div>
                            <div className="indicator-controllers">
                                <span onClick={()=>this.prevSlide()}><i className="fas fa-arrow-left"></i></span>
                                <span onClick={()=>this.nextSlide()}><i className="fas fa-arrow-right"></i></span>
                            </div>
                        </div>
                        <p className="course-title">
                            {courseTitle}
                        </p>
                        <p className="course-desc">
                            {courseDesc}
                        </p>
                        <button className="course-button">Подробнее</button>
                    </div>
                </div>
            </>
        )
    }

}