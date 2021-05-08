import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Topic } from '../models/topic';


@Injectable({
  providedIn: 'root'
})
export class TopicService {

  uri = 'http://127.0.0.1:5000';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };

  constructor(private http: HttpClient) { }

  public getTopics(courseId: number): Observable<any> {
    return this.http.get(`${this.uri}/course/${courseId}/topics`);
  }

  public addTopic(courseId: number, topic: Topic): Observable<any> {
    return this.http.post(`${this.uri}/course/${courseId}/topics`, JSON.stringify(topic), this.httpOptions);
  }

  public updateTopic(topicId: number, topic: Topic): Observable<any> {
    return this.http.put(`${this.uri}/topic/${topicId}`, JSON.stringify(topic), this.httpOptions);
  }

  public deleteTopic(topicId: number): Observable<any> {
    return this.http.delete(`${this.uri}/topic/${topicId}`);
  }
}
