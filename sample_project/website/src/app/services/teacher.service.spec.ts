import { TestBed } from '@angular/core/testing';

import { TeacherService } from './teacher.service';

describe('TeacherService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TeacherService = TestBed.get(TeacherService);
    expect(service).toBeTruthy();
  });
});
