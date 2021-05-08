import { HttpClient, HttpEventType } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FileService {

  SERVER_URL = 'http://localhost:5000';

  constructor(private httpClient: HttpClient) { }

  public upload(data: FormData, topicId: number, isPdf: boolean): Observable<any> {
    let uploadURL = `${this.SERVER_URL}/topic/${topicId}/synopsis_pdf`;
    if (!isPdf) {
      uploadURL = `${this.SERVER_URL}/topic/${topicId}/synopsis_pptx`;
    }

    return this.httpClient.post<any>(uploadURL, data, {
      reportProgress: true,
      observe: 'events'
    })
    .pipe(map((event) => {

      switch (event.type) {

        case HttpEventType.UploadProgress:
          const progress = Math.round(100 * event.loaded / event.total);
          return { status: 'progress', message: progress.toString() };

        case HttpEventType.Response:
          return { status: 'ready', message: 'загружено!' };

        default:
          return `Unhandled event: ${event.type}`;
      }
    })
    );
  }

  public download(url: string): Observable<any> {
    return this.httpClient.get(
      `${this.SERVER_URL}/uploads/${url}`,
      {
        responseType: 'blob'
      });
  }
}
