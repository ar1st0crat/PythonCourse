import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { Course } from 'src/app/models/course';
import { Teacher } from 'src/app/models/teacher';
import { TeacherService } from 'src/app/services/teacher.service';


@Component({
  selector: 'app-course-dialog',
  templateUrl: './course-dialog.component.html',
  styleUrls: ['./course-dialog.component.scss']
})
export class CourseDialog {

  teachers: Teacher[];

  constructor(
    public teacherService: TeacherService,
    public dialogRef: MatDialogRef<CourseDialog>,
    @Inject(MAT_DIALOG_DATA) public data: Course) {
      this.teacherService.getTeachers().subscribe(t => this.teachers = t);
    }

  onSave(): void {
    const teacherId = this.data.teacher.id;
    this.data.teacher = this.teachers.find(t => t.id === teacherId);
    this.data.teacher_id = this.data.teacher.id;
    this.dialogRef.close(this.data);
  }

  onCancel(): void {
    this.dialogRef.close();
  }
}
