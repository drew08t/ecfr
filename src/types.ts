export interface agency {
  slug: string;
  instance: number;
  display_name: string;
  name: string;
  short_name: string;
  sortable_name: string;
  TITLE: number;
  SUBTITLE?: string;
  CHAPTER?: string;
  SUBCHAP?: string;
  PART?: string;
}

export interface analysis {
  slug: string;
  year: number;
  word_count?: number;
}

export interface year {
  id: number;
  totalWords: number;
  slugs: slug[];
}

export interface slug {
  slug: string;
  totalWords: number;
}
