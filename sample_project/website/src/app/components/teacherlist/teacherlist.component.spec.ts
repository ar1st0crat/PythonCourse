import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeacherlistComponent } from './teacherlist.component';

describe('TeacherlistComponent', () => {
  let component: TeacherlistComponent;
  let fixture: ComponentFixture<TeacherlistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeacherlistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeacherlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
