import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { FileService } from '../../services/file.service';

@Component({
  selector: 'app-synopsis',
  templateUrl: './synopsis.component.html',
  styleUrls: ['./synopsis.component.scss']
})
export class SynopsisComponent implements OnInit {

  isPdf: boolean;
  topicId: number;
  courseId: number;

  form: FormGroup;
  error: string;
  uploadResponse = { status: '', message: '' };

  constructor(private formBuilder: FormBuilder, private uploadService: FileService, private router: Router) {
    this.isPdf = this.router.getCurrentNavigation().extras.state.isPdf;
    this.topicId = this.router.getCurrentNavigation().extras.state.topicId;
    this.courseId = this.router.getCurrentNavigation().extras.state.courseId;
  }

  ngOnInit() {
    this.form = this.formBuilder.group({
      synopsis: ['']
    });
  }

  onFileChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('synopsis').setValue(file);
    }
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.form.get('synopsis').value);

    this.uploadService.upload(formData, this.topicId, this.isPdf).subscribe(
      (res) => {
        this.uploadResponse = res;
        if (res.status === 'ready') {
          this.router.navigate(['courses', this.courseId]);
        }
      },
      (err) => this.error = err
    );
  }
}
