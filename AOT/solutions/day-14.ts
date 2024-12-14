type PerfReview<T> = T extends AsyncGenerator<infer X> ? X : never;
