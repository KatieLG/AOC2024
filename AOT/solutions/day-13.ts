type Demand<T, K = T> = {
	demand: T extends K ? (K extends T ? T : never) : never;
};
