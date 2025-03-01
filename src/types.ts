export interface agency {
  slug: string;
  display_name: string;
  name: string;
  short_name: string;
  sortable_name: string;
  title: number;
  subtitle?: string;
  chapter?: string;
  subchapter?: string;
  part?: string;
}

export interface analysis {
  slug: string;
  year: number;
  word_count?: number;
}
