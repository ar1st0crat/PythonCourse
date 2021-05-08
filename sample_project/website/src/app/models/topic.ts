import { Synopsis } from './synopsis';

export interface Topic {
  id: number;
  no: number;
  name: string;
  description: string;
  course_id: number;
  synopses: Synopsis[];
}
