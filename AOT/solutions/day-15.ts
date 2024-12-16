type Item = [string, number];
type GetRoute<
	T extends string,
	result extends Item[] = [],
	current extends number[] = [],
> = T extends `-${infer A}`
	? GetRoute<A, result, [...current, 1]>
	: T extends `${infer A}-${infer B}`
		? GetRoute<B, [...result, [A, result extends [] ? 0 : current["length"]]], [1]>
		: T extends ""
			? result
			: [...result, [T, current["length"]]];
