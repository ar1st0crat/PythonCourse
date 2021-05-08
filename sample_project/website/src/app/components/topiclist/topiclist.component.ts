import { Component, OnInit, ViewChildren, QueryList, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Topic } from 'src/app/models/topic';
import { CourseService } from 'src/app/services/course.service';
import { TopicService } from 'src/app/services/topic.service';
import { TopicComponent } from '../topic/topic.component';

@Component({
  selector: 'app-topiclist',
  templateUrl: './topiclist.component.html',
  styleUrls: ['./topiclist.component.scss']
})
export class TopiclistComponent implements OnInit {

  @ViewChildren(TopicComponent) topicComponents: QueryList<TopicComponent>;

  courseId: number;
  courseName: string;
  topics: Topic[];

  constructor(private topicService: TopicService,
              private courseService: CourseService,
              private route: ActivatedRoute) { }

  ngOnInit() {

    const routeParams = this.route.snapshot.paramMap;
    this.courseId = Number(routeParams.get('courseId'));

    this.courseService
        .getCourse(this.courseId)
        .subscribe(c => {
          this.courseName = c.name;
        });

    this.topicService
        .getTopics(this.courseId)
        .subscribe(t => {
          this.topics = t;
        });
  }

  public add(): void {
    let newNo = 1;
    if (this.topics.length > 0) {
      newNo = this.topics[this.topics.length - 1].no + 1;
    }

    const newTopic = {
      id: 0,
      no: newNo,
      name: `Тема ${newNo}`,
      description: `Описание темы ${newNo}`,
      course_id: this.courseId,
      synopses: null
    };

    this.topicService
        .addTopic(this.courseId, newTopic)
        .subscribe(t => {
          this.topics.push(t);
        });
  }

  public remove(topicId: number): void {
    this.topics = this.topics.filter(t => t.id !== topicId);
  }
}
