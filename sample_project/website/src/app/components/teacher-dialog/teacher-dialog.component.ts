import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { Teacher } from 'src/app/models/teacher';


@Component({
  selector: 'app-teacher-dialog',
  templateUrl: './teacher-dialog.component.html',
  styleUrls: ['./teacher-dialog.component.scss']
})
export class TeacherDialog {

  constructor(
    public dialogRef: MatDialogRef<TeacherDialog>,
    @Inject(MAT_DIALOG_DATA) public data: Teacher) {
    }

  onSave(): void {
    this.data.degreeId = 1;
    this.data.positionId = 1;
    this.dialogRef.close(this.data);
  }

  onCancel(): void {
    this.dialogRef.close();
  }
}
