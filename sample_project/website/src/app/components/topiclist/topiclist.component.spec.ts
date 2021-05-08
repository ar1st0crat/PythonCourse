import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TopiclistComponent } from './topiclist.component';

describe('TopiclistComponent', () => {
  let component: TopiclistComponent;
  let fixture: ComponentFixture<TopiclistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TopiclistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopiclistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
