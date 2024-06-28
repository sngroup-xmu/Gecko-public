/***********************  P A R S E R  **************************/

parser aIngressParser(packet_in      pkt,
    out headers          hdr,
    out my_ingress_metadata_t         meta,
    out ingress_intrinsic_metadata_t  ig_intr_md)
{
    state start {
        pkt.extract(ig_intr_md);
        pkt.advance(PORT_METADATA_SIZE);
        transition parse_ethernet;
    }
    
    state parse_ethernet {
        pkt.extract(hdr.ethernet);
        transition select(hdr.ethernet.ether_type) {
			ETHERTYPE_ALBION :  parse_albion;
            default          :  reject;
        }
    }

    state parse_albion {
        pkt.extract(hdr.albion);
		transition select(hdr.albion.opration) {
            100              :  parse_albion_timer;
            101              :  parse_albion_timer;
            default          :  parse_albion_data;
        }
    }

    state parse_albion_data {
        pkt.extract(hdr.albion_data);
		transition accept;
    }

    state parse_albion_timer {
        pkt.extract(hdr.albion_timer);
		transition accept;
    }
}


/***************** M A T C H - A C T I O N  *********************/

control aIngress(
    /* User */
    inout headers                       hdr,
    inout my_ingress_metadata_t                      meta,
    /* Intrinsic */
    in    ingress_intrinsic_metadata_t               ig_intr_md,
    in    ingress_intrinsic_metadata_from_parser_t   ig_prsr_md,
    inout ingress_intrinsic_metadata_for_deparser_t  ig_dprsr_md,
    inout ingress_intrinsic_metadata_for_tm_t        ig_tm_md)
{
    @pragma stage 0
    Register<bit<32>,bit<32>>(1,0) register_request_id_low; 		
	RegisterAction<bit<32>, bit<32>, bit<32>>(register_request_id_low) register_request_id_low_add = { 
        void apply(inout bit<32> value_r, out bit<32> value_t){ 
            value_r = value_r + 1;
            value_t = value_r;
        } 
    }; 

    @pragma stage 0
    Register<bit<32>,bit<32>>(1,0) register_timer; 		
	RegisterAction<bit<32>, bit<32>, bit<32>>(register_timer) register_timer_add = { 
        void apply(inout bit<32> value_r, out bit<32> value_t){ 
            value_r = value_r + 1;
            value_t = value_r;
        } 
    }; 
    RegisterAction<bit<32>, bit<32>, bit<32>>(register_timer) register_timer_read = { 
        void apply(inout bit<32> value_r, out bit<32> value_t){ 
            value_t = value_r;
        } 
    };
    RegisterAction<bit<32>, bit<32>, bit<32>>(register_timer) register_timer_zero = { 
        void apply(inout bit<32> value_r, out bit<32> value_t){ 
            value_r = 0;
        } 
    };

    @pragma stage 0
    Register<bit<32>,bit<32>>(1,0) register_num; 		
	RegisterAction<bit<32>, bit<32>, bit<32>>(register_num) register_num_add = { 
        void apply(inout bit<32> value_r, out bit<32> value_t){ 
            value_t = value_r;
            value_r = value_r + 1;
        } 
    }; 
    RegisterAction<bit<32>, bit<32>, bit<32>>(register_num) register_num_zero = { 
        void apply(inout bit<32> value_r, out bit<32> value_t){ 
            value_r = 0;
        } 
    };

    @pragma stage 1
    Register<bit<32>,bit<32>>(1,0) register_request_id_high; 		
	RegisterAction<bit<32>, bit<32>, bit<32>>(register_request_id_high) register_request_id_high_add = { 
        void apply(inout bit<32> value_r, out bit<32> value_t){ 
            value_r = value_r + 1;
            value_t = value_r;
        } 
    }; 

    #define register_request_id_high_record(number)            \
    Register<bit<32>,bit<32>>(14000,0) register_request_id_high_record_##number##; 	\	
	RegisterAction<bit<32>, bit<32>, bit<32>>(register_request_id_high_record_##number##) register_request_id_high_record_##number##_w = { \
        void apply(inout bit<32> value_r, out bit<32> value_t){ \
            value_r = hdr.albion.request_id_high;\
        } \
    }; \
    RegisterAction<bit<32>, bit<32>, bit<32>>(register_request_id_high_record_##number##) register_request_id_high_record_##number##_r = { \
        void apply(inout bit<32> value_r, out bit<32> value_t){ \
            value_t = value_r;\
            value_r = 0; \
        } \
    }; 
    #define register_request_id_low_record(number)            \
    Register<bit<32>,bit<32>>(14000,0) register_request_id_low_record_##number##; 		\
	RegisterAction<bit<32>, bit<32>, bit<32>>(register_request_id_low_record_##number##) register_request_id_low_record_##number##_w = { \
        void apply(inout bit<32> value_r, out bit<32> value_t){ \
            value_r = hdr.albion.request_id_low;\
        } \
    }; \
    RegisterAction<bit<32>, bit<32>, bit<32>>(register_request_id_low_record_##number##) register_request_id_low_record_##number##_r = { \
        void apply(inout bit<32> value_r, out bit<32> value_t){ \
            value_t = value_r;\
            value_r = 0; \
        } \
    }; 
    #define register_triple_record(number)            \
    Register<bit<8>,bit<32>>(14000,0) register_triple_record_##number##; 		\
	RegisterAction<bit<8>, bit<32>, bit<8>>(register_triple_record_##number##) register_triple_record_##number##_set = { \
        void apply(inout bit<8> value_r, out bit<8> value_t){ \
            value_r = 7;\
        } \
    }; \
    RegisterAction<bit<8>, bit<32>, bit<8>>(register_triple_record_##number##) register_triple_record_##number##_read = { \
        void apply(inout bit<8> value_r, out bit<8> value_t){ \
            value_t = value_r;\
            value_r = 0; \
        } \
    }; 

    #define register_record_define(number) \
    register_request_id_high_record(##number##) \
    register_request_id_low_record(##number##) \
    register_triple_record(##number##)

    register_record_define(0)
    register_record_define(1)
    register_record_define(2)
    register_record_define(3)
    register_record_define(4)
    register_record_define(5)
    register_record_define(6)
    register_record_define(7)
    register_record_define(8)
    register_record_define(9)

    #define table_register_request_id_high_record_interaction(number)    \
    action action_register_request_id_high_record_##number##_w(){   \
        register_request_id_high_record_##number##_w.execute(hdr.albion.time);    \
    }   \
    action action_register_request_id_high_record_##number##_r(){   \
        hdr.albion_timer.request_id_high_##number## = register_request_id_high_record_##number##_r.execute(hdr.albion.time);  \
    } \
    table table_register_request_id_high_record_##number##_interaction{ \
        key = { hdr.albion.opration: exact;}  \
        actions = {  \
            action_register_request_id_high_record_##number##_w;  \
            action_register_request_id_high_record_##number##_r;  \
        }  \
        const entries = {  \
            2:    action_register_request_id_high_record_##number##_w();  \
            100:  action_register_request_id_high_record_##number##_r();  \
		}  \
        size = 2;  \
    }

    #define table_register_request_id_low_record_interaction(number)    \
    action action_register_request_id_low_record_##number##_w(){  \
        register_request_id_low_record_##number##_w.execute(hdr.albion.time); \
    }  \
    action action_register_request_id_low_record_##number##_r(){  \
        hdr.albion_timer.request_id_low_##number## = register_request_id_low_record_##number##_r.execute(hdr.albion.time); \
    }  \
    table table_register_request_id_low_record_##number##_interaction{  \
        key = { hdr.albion.opration: exact;}  \
        actions = {  \
            action_register_request_id_low_record_##number##_w;  \
            action_register_request_id_low_record_##number##_r;  \
        }  \
        const entries = {  \
            2:    action_register_request_id_low_record_##number##_w();  \
            100:  action_register_request_id_low_record_##number##_r();  \
		}  \
        size = 2;  \
    }

    #define table_register_triple_record_interaction(number)  \
    action action_register_triple_record_##number##_set(){  \
        register_triple_record_##number##_set.execute(hdr.albion.time); \
    }  \
    action action_register_triple_record_##number##_read(){ \
        hdr.albion_timer.state_##number## = register_triple_record_##number##_read.execute(hdr.albion.time); \
    }  \
    table table_register_triple_record_##number##_interaction{ \
        key = { hdr.albion.opration: exact;} \
        actions = { \
            action_register_triple_record_##number##_set; \
            action_register_triple_record_##number##_read; \
        } \
        const entries = { \
            2:    action_register_triple_record_##number##_set(); \
            100:  action_register_triple_record_##number##_read(); \
		} \
        size = 2; \
    }

    #define table_register_record_define(number) \
    table_register_request_id_high_record_interaction(##number##) \
    table_register_request_id_low_record_interaction(##number##) \
    table_register_triple_record_interaction(##number##)

    table_register_record_define(0)
    table_register_record_define(1)
    table_register_record_define(2)
    table_register_record_define(3)
    table_register_record_define(4)
    table_register_record_define(5)
    table_register_record_define(6)
    table_register_record_define(7)
    table_register_record_define(8)
    table_register_record_define(9)

    #define opration_2_record(number) \
    table_register_request_id_high_record_##number##_interaction.apply(); \
    table_register_request_id_low_record_##number##_interaction.apply(); \
    table_register_triple_record_##number##_interaction.apply();

    #define opration_100_record_read(number) \
    table_register_request_id_high_record_##number##_interaction.apply(); \
    table_register_request_id_low_record_##number##_interaction.apply(); \
    table_register_triple_record_##number##_interaction.apply();

	apply {
        if(hdr.albion.isValid())
        {
            //stage 0
            if(hdr.albion.opration == 0){
                hdr.albion.request_id_low = register_request_id_low_add.execute(0);
            }
            else if(hdr.albion.opration == 100){
                if(hdr.albion_timer.times == 0){
                    hdr.albion.time   = register_timer_add.execute(0);
                    register_num_zero.execute(0);
                    hdr.albion_timer.times = hdr.albion_timer.const_time;
                }
                else{
                    hdr.albion_timer.times = hdr.albion_timer.times - 1;
                }
                ig_tm_md.ucast_egress_port = 196;
            }
            else if(hdr.albion.opration == 101){
                register_timer_zero.execute(0);
                register_num_zero.execute(0);
                ig_tm_md.ucast_egress_port = 196;
                hdr.albion.opration = 100;
            }
            else if(hdr.albion.opration == 1){
                hdr.albion.time = register_timer_read.execute(0);
                hdr.albion.num  = register_num_add.execute(0);
                hdr.albion.opration = 2;
            }

            //stage 1
            if(hdr.albion.opration == 0){
                if(hdr.albion.request_id_low == 0)
                {
                    hdr.albion.request_id_high = register_request_id_high_add.execute(0);
                }
                ig_tm_md.ucast_egress_port = 136;
            }
            else if(hdr.albion.opration == 2){
                meta.time_1 = hdr.albion.time << 3;
                meta.time_2 = hdr.albion.time << 1;
                if(hdr.albion.num == 0){
                    opration_2_record(0)
                }
            }
            else if(hdr.albion.opration == 100){
                if(hdr.albion.time == 14000){
                    hdr.albion.opration  = 101;
                    hdr.albion.time = 0;
                }
                else{
                    opration_100_record_read(0)
                }
            }

            //stage 2
            if(hdr.albion.opration == 2){
                if(hdr.albion.CS_id_1 == 1){
                    ig_tm_md.ucast_egress_port = 56;
                }
                else if(hdr.albion.CS_id_1 == 2){
                    ig_tm_md.ucast_egress_port = 48;
                }
                else if(hdr.albion.CS_id_1 == 3){
                    ig_tm_md.ucast_egress_port = 40;
                }
                else if(hdr.albion.CS_id_1 == 4){
                    ig_tm_md.ucast_egress_port = 32;
                }
                hdr.albion.index = meta.time_1 + meta.time_2;
                if(hdr.albion.num == 1){
                    opration_2_record(1)
                }
            }
            else if(hdr.albion.opration == 100){
                opration_100_record_read(1)
            }

            //stage 3
            if(hdr.albion.opration == 2){
                hdr.albion.index = hdr.albion.index + hdr.albion.num;
                if(hdr.albion.num == 2){
                    opration_2_record(2)
                }
            }
            else if(hdr.albion.opration == 100){
                opration_100_record_read(2)
            }

            //stage 4
            if(hdr.albion.opration == 2){
                if(hdr.albion.num == 3){
                    opration_2_record(3)
                }
            }
            else if(hdr.albion.opration == 100){
                opration_100_record_read(3)
            }

            //stage 5
            if(hdr.albion.opration == 2){
                if(hdr.albion.num == 4){
                    opration_2_record(4)
                }
            }
            else if(hdr.albion.opration == 100){
                opration_100_record_read(4)
            }

            //stage 6
            if(hdr.albion.opration == 2){
                if(hdr.albion.num == 5){
                    opration_2_record(5)
                }
            }
            else if(hdr.albion.opration == 100){
                opration_100_record_read(5)
            }

            //stage 7
            if(hdr.albion.opration == 2){
                if(hdr.albion.num == 6){
                    opration_2_record(6)
                }
            }
            else if(hdr.albion.opration == 100){
                opration_100_record_read(6)
            }

            //stage 8
            if(hdr.albion.opration == 2){
                if(hdr.albion.num == 7){
                    opration_2_record(7)
                }
            }
            else if(hdr.albion.opration == 100){
                opration_100_record_read(7)
            }

            //stage 9
            if(hdr.albion.opration == 2){
                if(hdr.albion.num == 8){
                    opration_2_record(8)
                }
            }
            else if(hdr.albion.opration == 100){
                opration_100_record_read(8)
            }

            //stage 10
            if(hdr.albion.opration == 2){
                if(hdr.albion.num == 9){
                    opration_2_record(9)
                }
            }
            else if(hdr.albion.opration == 100){
                opration_100_record_read(9)
            }


        }
	}
}

/*********************  D E P A R S E R  ************************/

control aIngressDeparser(packet_out pkt,
    /* User */
    inout headers                       hdr,
    in    my_ingress_metadata_t                      meta,
    /* Intrinsic */
    in    ingress_intrinsic_metadata_for_deparser_t  ig_dprsr_md)
{
	apply{
		pkt.emit(hdr);
	}
}