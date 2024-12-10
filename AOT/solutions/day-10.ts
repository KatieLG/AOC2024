enum Gift {
	Coal = 0,
	Train = 1,
	Bicycle = 1 << 1,
	Traditional = Train | Bicycle,
	SuccessorToTheNintendoSwitch = 1 << 2,
	TikTokPremium = 1 << 3,
	Vape = 1 << 4,
	OnTheMove = Coal | Bicycle | TikTokPremium | Vape,
	OnTheCouch = OnTheMove ^ Bicycle | SuccessorToTheNintendoSwitch,
}
