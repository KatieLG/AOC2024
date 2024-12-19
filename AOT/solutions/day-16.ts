type Curry<Args extends unknown[], Return> = {
	<Input extends unknown[]>(
		...args: Input
	): Input extends Args
		? Return
		: Args extends [...Input, ...infer Rest extends unknown[]]
			? Curry<Rest, Return>
			: never;
};

declare function DynamicParamsCurrying<Args extends unknown[], Return>(
	func: (...args: Args) => Return,
): Curry<Args, Return>;
