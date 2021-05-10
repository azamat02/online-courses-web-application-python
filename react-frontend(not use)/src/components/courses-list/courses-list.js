import React, {Component} from 'react'
import CourseItem from '../course-item/course-item'
import './courses-list.css'

export default class CoursesList extends Component{
    constructor(params) {
        super(params)

        this.data = [
            {courseImg:'', courseTitle: "Course #1", courseDesc:"30 lessons", courseId:1},
            {courseImg:'', courseTitle: "Course #2", courseDesc:"20 lessons", courseId:2},
            {courseImg:'', courseTitle: "Course #3", courseDesc:"10 lessons", courseId:3},
            {courseImg:'', courseTitle: "Course #4", courseDesc:"40 lessons", courseId:4},
        ]
    }

    renderItems = (arr)=>{
        return arr.map((elem)=>{
            let {courseTitle, courseDesc, courseId} = elem
            return <CourseItem courseImg={""} courseTitle={courseTitle} courseDesc={courseDesc} courseId={courseId}/>
        })
    }

    render() {
        let items = this.renderItems(this.data)
        return (
            <>
                <p className="title">Courses</p>
                <div className="courses-list">
                    {items}
                </div>
            </>
        )
    }
}