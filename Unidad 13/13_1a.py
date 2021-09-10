def __str__(self):
        res = ""
        act = self.prim
        while act:
            res += str(act.dato)
            act = act.prox
        res_f = ", ".join(res)
        return f"[{res_f}]"