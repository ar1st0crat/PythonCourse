import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material';
import { Course } from 'src/app/models/course';
import { CourseService } from 'src/app/services/course.service';
import { CourseDialog } from '../course-dialog/course-dialog.component';


@Component({
  selector: 'app-courselist',
  templateUrl: './courselist.component.html',
  styleUrls: ['./courselist.component.scss']
})
export class CourselistComponent implements OnInit {

  courses: Course[];

  constructor(public dialog: MatDialog, private courseService: CourseService) {}

  ngOnInit() {
    this.updateCourses();
  }

  updateCourses(): void {
    this.courseService
        .getCourses()
        .subscribe(c => {
          this.courses = c;
        });
  }

  public add(): void {

    const dialogRef = this.dialog.open(CourseDialog,
    {
      width: '720px',
      data: { teacher: {} } as Course
    });

    dialogRef.afterClosed().subscribe(edited => {
      if (edited !== undefined) {
        this.courseService.addCourse(edited)
          .subscribe(() => this.updateCourses());
      }
    });
  }
}
