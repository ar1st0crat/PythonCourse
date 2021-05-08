import { Teacher } from './teacher';

export interface Course {
  id: number;
  name: string;
  description: string;
  ects: number;
  image_url: string;
  teacher_id: number;
  teacher: Teacher;
}
