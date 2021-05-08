import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material';
import { Teacher } from 'src/app/models/teacher';
import { TeacherService } from 'src/app/services/teacher.service';
import { TeacherDialog } from '../teacher-dialog/teacher-dialog.component';


@Component({
  selector: 'app-teacherlist',
  templateUrl: './teacherlist.component.html',
  styleUrls: ['./teacherlist.component.scss']
})
export class TeacherlistComponent implements OnInit {

  displayedColumns = ['name', 'email'];

  teachers: Teacher[];

  constructor(public dialog: MatDialog, private teacherService: TeacherService) { }

  ngOnInit() {
    this.updateTeachers();
  }

  updateTeachers(): void {
    this.teacherService
        .getTeachers()
        .subscribe(t => {
          this.teachers = t;
        });
  }

  public add(): void {

    const dialogRef = this.dialog.open(TeacherDialog,
    {
      width: '720px',
      data: {} as Teacher
    });

    dialogRef.afterClosed().subscribe(edited => {
      if (edited !== undefined) {
        this.teacherService.addTeacher(edited)
          .subscribe(() => this.updateTeachers());
      }
    });
  }
}
