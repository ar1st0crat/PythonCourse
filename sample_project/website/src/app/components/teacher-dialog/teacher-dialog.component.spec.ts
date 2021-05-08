import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeacherDialogComponent } from './teacher-dialog.component';

describe('TeacherDialogComponent', () => {
  let component: TeacherDialogComponent;
  let fixture: ComponentFixture<TeacherDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeacherDialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeacherDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
