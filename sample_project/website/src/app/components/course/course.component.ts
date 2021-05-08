import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { MatDialog } from '@angular/material';
import { Router } from '@angular/router';
import { Course } from 'src/app/models/course';
import { CourseService } from 'src/app/services/course.service';
import { CourseDialog } from '../course-dialog/course-dialog.component';


@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.scss']
})
export class CourseComponent implements OnInit {

  @Input() course: Course;
  @Output() updateCourselistEvent = new EventEmitter();

  constructor(public dialog: MatDialog, private router: Router, private courseService: CourseService) { }

  ngOnInit() {
  }

  edit(): void {
    const courseCopy = Object.assign({}, this.course);

    const dialogRef = this.dialog.open(CourseDialog, {
      width: '720px',
      data: courseCopy
    });

    dialogRef.afterClosed().subscribe(edited => {
      if (edited !== undefined) {
        this.courseService.updateCourse(this.course.id, edited)
          .subscribe(() => {
            this.course = edited;
          });
      }
    });
  }

  delete(): void {
    const response = confirm(`Удалить курс '${this.course.name}'?`);
    if (response !== true) {
      return;
    }

    this.courseService.deleteCourse(this.course.id)
      .subscribe(() => {
        this.updateCourselistEvent.next();
      });
  }
}
