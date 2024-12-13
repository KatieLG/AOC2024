const survivalRatio4 = (input: string | number) => {
	const quarter = typeof input === "string" ? input : `${input} Q1`;
	const data = quarterlyData[quarter];
	if (!data) {
		throw new Error("Data not found");
	}
	return data.housingIndex / data.minimumWage;
};

type QuarterlyData = {
	[key: string]: {
		/** inflation corrected housing price index */
		housingIndex: number;

		/** inflation corrected North Pole minimum wage */
		minimumWage: number;
	};
};

const quarterlyData: QuarterlyData = {
	"2009 Q1": {
		housingIndex: 159.50891,
		minimumWage: 92.85234,
	},
	"2009 Q2": {
		housingIndex: 153.21658,
		minimumWage: 92.48525,
	},
	"2009 Q3": {
		housingIndex: 147.7367,
		minimumWage: 101.66865,
	},
	"2009 Q4": {
		housingIndex: 145.75099,
		minimumWage: 100.89109,
	},
	"2024 Q1": {
		housingIndex: 214.9681,
		minimumWage: 73.98181,
	},
	"2024 Q2": {
		housingIndex: 218.21312,
		minimumWage: 73.52088,
	},
};
