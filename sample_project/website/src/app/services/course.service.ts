import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Course } from '../models/course';


@Injectable({
  providedIn: 'root'
})
export class CourseService {

  uri = 'http://127.0.0.1:5000';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };

  constructor(private http: HttpClient) { }

  public getCourses(): Observable<any> {
    return this.http.get(`${this.uri}/courses`);
  }

  public getCourse(courseId: number): Observable<any> {
    return this.http.get(`${this.uri}/course/${courseId}`);
  }

  public addCourse(course: Course): Observable<any> {
    return this.http.post(`${this.uri}/courses`, JSON.stringify(course), this.httpOptions);
  }

  public updateCourse(courseId: number, course: Course): Observable<any> {
    return this.http.put(`${this.uri}/course/${courseId}`, JSON.stringify(course), this.httpOptions);
  }

  public deleteCourse(courseId: number): Observable<any> {
    return this.http.delete(`${this.uri}/course/${courseId}`);
  }
}
