import React, {Component} from 'react'
import './course-item.css'

export default class CourseItem extends Component{
    render() {
        let {courseTitle, courseDesc, courseId} = this.props
        return (
            <>
                <div className="course-card-item">
                    <div className="course-card-image">
                        image
                    </div>
                    <div className="course-card-content">
                        <p className="course-card-label">Course</p>
                        <p className="course-card-title">
                            {courseTitle}
                        </p>
                        <div className="course-card-desc">
                            <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-book" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke="#38393A" fill="none" stroke-linecap="round" stroke-linejoin="round">
                                <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                                <path d="M3 19a9 9 0 0 1 9 0a9 9 0 0 1 9 0" />
                                <path d="M3 6a9 9 0 0 1 9 0a9 9 0 0 1 9 0" />
                                <line x1="3" y1="6" x2="3" y2="19" />
                                <line x1="12" y1="6" x2="12" y2="19" />
                                <line x1="21" y1="6" x2="21" y2="19" />
                            </svg>
                            <span>
                                {courseDesc}
                            </span>
                        </div>
                        <p className="course-card-link">
                            <a href={courseId} className="course-card-link">Read more</a>
                        </p>
                    </div>
                </div>
            </>
        )
    }
}
