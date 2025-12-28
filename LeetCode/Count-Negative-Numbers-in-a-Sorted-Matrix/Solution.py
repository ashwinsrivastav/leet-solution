var countNegatives = function(grid) {
	return grid.flat().reduce((acc, curr) => {
		return curr < 0 ? acc + 1 : acc
	}, 0)
};