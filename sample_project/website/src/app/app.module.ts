import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { MatCardModule, MatButtonModule, MatIconModule, MatSelectModule, MatTableModule,
         MatDialogModule, MatFormFieldModule, MatInputModule, MatToolbarModule } from '@angular/material';
import { MatExpansionModule } from '@angular/material/expansion';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { HeaderComponent } from './components/header/header.component';
import { CourselistComponent } from './components/courselist/courselist.component';
import { CourseComponent } from './components/course/course.component';
import { TopiclistComponent } from './components/topiclist/topiclist.component';
import { SynopsisComponent } from './components/synopsis/synopsis.component';
import { TeacherlistComponent } from './components/teacherlist/teacherlist.component';
import { TopicComponent } from './components/topic/topic.component';
import { CourseDialog  } from './components/course-dialog/course-dialog.component';
import { TeacherDialog } from './components/teacher-dialog/teacher-dialog.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    CourselistComponent,
    CourseComponent,
    TopiclistComponent,
    SynopsisComponent,
    TeacherlistComponent,
    TopicComponent,
    CourseDialog,
    TeacherDialog
  ],
  entryComponents: [
    CourseDialog,
    TeacherDialog
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatButtonModule,
    MatCardModule,
    MatIconModule,
    MatExpansionModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatExpansionModule,
    MatToolbarModule,
    MatSelectModule,
    MatTableModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    RouterModule.forRoot([
      { path: '', component: CourselistComponent },
      { path: 'courses/:courseId', component: TopiclistComponent },
      { path: 'teachers', component: TeacherlistComponent },
      { path: 'synopsis', component: SynopsisComponent }
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
