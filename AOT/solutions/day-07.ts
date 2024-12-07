const createRoute7 = <A extends string, B extends string, C extends string>(
	author: string,
	route: [A, B, C],
): { author: string; route: [A, B, C]; createdAt: number } => ({
	author,
	route,
	createdAt: Date.now(),
});
