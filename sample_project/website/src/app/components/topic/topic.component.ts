import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';
import { Topic } from 'src/app/models/topic';
import { TopicService } from 'src/app/services/topic.service';
import { FileService } from 'src/app/services/file.service';


@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.scss']
})
export class TopicComponent implements OnInit {

  @Input() topic: Topic;
  @Output() removeEvent = new EventEmitter();

  constructor(private topicService: TopicService,
              private uploadService: FileService,
              private router: Router) { }

  ngOnInit() {
  }

  public save() {
    this.topicService
        .updateTopic(this.topic.id, this.topic)
        .subscribe(() => alert('Тема сохранена!'));
  }

  public delete() {
    this.topicService
        .deleteTopic(this.topic.id)
        .subscribe(() => {
          this.removeEvent.next();
        });
  }

  public addPdf(id: number) {
    this.router.navigate(['/synopsis'], {
      state: {
        isPdf: true,
        topicId: id,
        courseId: this.topic.course_id
      }});
  }

  public addPptx(id: number) {
    this.router.navigate(['/synopsis'], {
      state: {
        isPdf: false,
        topicId: id,
        courseId: this.topic.course_id
      }});
  }

  download(event, url: string) {

    event.stopPropagation();

    let mimeType = 'application/pdf'
    if (url.endsWith('pptx')) {
      mimeType = 'application/powerpoint';
    }

    this.uploadService
        .download(url)
        .subscribe((response: any) => {
          const blob:any = new Blob([response], { type: mimeType });
          const url = window.URL.createObjectURL(blob);
          window.open(url);
          //window.location.href = response.url;
    });
  }
}
