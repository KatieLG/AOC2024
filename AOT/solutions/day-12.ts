type Arr<T, K extends Array<number> = []> = K["length"] extends T ? K : Arr<T, [number, ...K]>;
type IsEven<N> = N extends 0
	? true
	: N extends 1
		? false
		: Arr<N> extends [infer _ extends number, infer _ extends number, ...infer C extends number[]]
			? IsEven<C["length"]>
			: false;
type ToArr<S extends string, C extends string[] = []> = S extends `${infer A extends
	string}${infer R extends string}`
	? ToArr<R, [...C, A]>
	: C;

type NaughtyOrNice<Name extends string> = IsEven<ToArr<Name>["length"]> extends true
	? "naughty"
	: "nice";
type FormatNames<T extends string[][]> = {
	[K in keyof T]: {
		name: T[K][0];
		count: T[K][2] extends `${infer C extends number}` ? C : never;
		rating: NaughtyOrNice<T[K][0]>;
	};
};
