import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Teacher } from '../models/teacher';

@Injectable({
  providedIn: 'root'
})
export class TeacherService {

  uri = 'http://127.0.0.1:5000';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };

  constructor(private http: HttpClient) { }

  public getTeachers(): Observable<any> {
    return this.http.get(`${this.uri}/teachers`);
  }

  public addTeacher(teacher: Teacher): Observable<any> {
    return this.http.post(`${this.uri}/teachers`, JSON.stringify(teacher), this.httpOptions);
  }

  public updateTeacher(teacherId: number, teacher: Teacher): Observable<any> {
    return this.http.put(`${this.uri}/teacher/${teacherId}`, JSON.stringify(teacher), this.httpOptions);
  }

  public deleteTeacher(teacherId: number): Observable<any> {
    return this.http.delete(`${this.uri}/teacher/${teacherId}`);
  }
}
