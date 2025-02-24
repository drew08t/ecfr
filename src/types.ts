export interface agency {
  cfr_references: cfr_reference[];
  children?: agency[];
  display_name: string;
  short_name: string;
  slug: string;
  sortable_name: string;
}

export interface cfr_reference {
  title: number;
  subtitle?: string;
  chapter?: string;
  subchapter?: string;
  part?: string;
}
