from itertools import product

from tabulate import tabulate

class GridExperiments:
    def __init__(self, params_lists):
        self.keys = list(params_lists.keys())
        self.params_lists = params_lists
    def get_tabular(self):
        params = self.get_params()
        results = [query_first({"payload": {"kwargs": row}}) for row in params]
        return tabulate(
            [
                [
                    row[k]
                    for k in self.keys
                ] + [
                    res["_id"] if res else False,
                    min(res["payload"]["losses"]) if res else None
                ]
                for row, res in zip(params, results)
            ],
            headers=self.keys + ["done?", "min-loss"],
            tablefmt="fancy_grid"
        )
    def get_params(self):
        return self.__get_params_helper(self.params_lists)
    def __get_params_helper(self, d):
        return [
            {
                k: vv
                for k, vv in zip(self.keys, v)
            }
            for v in product(*[d[k] for k in self.keys])
        ]