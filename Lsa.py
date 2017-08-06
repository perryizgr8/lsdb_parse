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
        self.ls_type = ls_type #TODO convert into number
        self.ls_id = ls_id
        self.adv_rtr = adv_rtr
        self.seq = seq

        if ls_type == '0x01':
            Lsa.num_router_lsas += 1
        elif ls_type == '0x02':
            Lsa.num_network_lsas += 1
        elif ls_type == '0x03':
            Lsa.num_type3_lsas += 1
        elif ls_type == '0x04':
            Lsa.num_type4_lsas += 1
        elif ls_type == '0x05':
            Lsa.num_external_lsas += 1