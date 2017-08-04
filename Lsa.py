class Lsa:
    'LSA structure'
    num_router_lsas = 0
    num_network_lsas = 0
    num_type3_lsas = 0    
    num_type4_lsas = 0
    num_external_lsas = 0

    def __init__(self, age, options, ls_type, ls_id, adv_rtr, seq):
        self.age = age
        self.options = options
        self.ls_type = ls_type
        self.ls_id = ls_id
        self.adv_rtr = adv_rtr
        self.seq = seq

        if ls_type is 1:
            Lsa.num_router_lsas += 1
        elif ls_type is 2:
            Lsa.num_network_lsas += 1
        elif ls_type is 3:
            Lsa.num_type3_lsas += 1
        elif ls_type is 4:
            Lsa.num_type4_lsas += 1
        elif ls_type is 5:
            Lsa.num_external_lsas += 1