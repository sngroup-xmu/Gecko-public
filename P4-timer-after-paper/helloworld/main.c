#include <stdint.h>
#include <inttypes.h>
#include <rte_eal.h>
#include <rte_ethdev.h>
#include <rte_cycles.h>
#include <rte_lcore.h>
#include <rte_mbuf.h>
#include <rte_ether.h>
#include <rte_ip.h>
#include <rte_udp.h>
#include <pthread.h>
#include <string.h>

#define RX_RING_SIZE 1024
//#define TX_RING_SIZE 512
#define TX_RING_SIZE 1024
#define NUM_MBUFS 8191*2
#define MBUF_CACHE_SIZE 512
#define BURST_SIZE 4
int literal_count = 0;
int clause_count = 0;
uint8_t packet_index = 0;
long long packet_num = 0;
int time_in_forward_packet = 0;
int time_in_print = 0;
long long tx = 0;

struct rte_mempool *mbuf_pool;
static const struct rte_eth_conf port_conf_default = {
	.rxmode = { .max_lro_pkt_size = RTE_ETHER_MAX_LEN }
};

static inline int
port_init(uint16_t port, struct rte_mempool *mbuf_pool)
{
	struct rte_eth_conf port_conf = port_conf_default;
	const uint16_t rx_rings = 2, tx_rings = 2;
	uint16_t nb_rxd = RX_RING_SIZE;
	uint16_t nb_txd = TX_RING_SIZE;
	int retval;
	uint16_t q;
	struct rte_eth_dev_info dev_info;
	struct rte_eth_txconf txconf;
	struct rte_eth_rxconf rxq_conf;
	struct rte_eth_conf local_port_conf = port_conf;

	if (!rte_eth_dev_is_valid_port(port))
		return -1;
	printf("111\n");
	/*获取当前网口信息，并存入dev_info中*/
	retval = rte_eth_dev_info_get(port, &dev_info);
	if (retval != 0) {
		printf("Error during getting device (port %u) info: %s\n",
				port, strerror(-retval));
		return retval;
	}

	/* Configure the Ethernet device. */
	/*配置网口参数，rx_rings和tx_rings是设置的接受/发送的队列数目*/
	retval = rte_eth_dev_configure(port, rx_rings, tx_rings, &port_conf);
	if (retval != 0)
		return retval;
	/*这个函数是去判断port网口是否支持nb_rxd/nb_txd个接受/发送描述符，*/
	/*如果不支持那么多会自动调整到边界个数*/
	retval = rte_eth_dev_adjust_nb_rx_tx_desc(port, &nb_rxd, &nb_txd);
	if (retval != 0)
		return retval;
	printf("222\n");
	/* Allocate and set up 1 RX queue per Ethernet port. */
	/*为网口设置接受队列，因为rx_rings为1，所以为网口设置一个接受队列*/
	/*rth_eth_dev_socket_id返回一个NUMA结构套接字，所谓的NUMA结构套接字是将多台服务器连接起来当做一台使用的技术*/
	rxq_conf = dev_info.default_rxconf;
	rxq_conf.offloads = local_port_conf.rxmode.offloads;
	for (q = 0; q < rx_rings; q++) {
		retval = rte_eth_rx_queue_setup(port, q, nb_rxd,
				rte_eth_dev_socket_id(port), &rxq_conf, mbuf_pool);
		if (retval < 0)
			return retval;
	}
	printf("444\n");
	txconf = dev_info.default_txconf;
	txconf.offloads = port_conf.txmode.offloads;
	/* Allocate and set up 1 TX queue per Ethernet port. */
	/*为port网口设置发送队列，比上一个函数少一个内存池参数，所以发送队列是没有缓冲区的*/
	for (q = 0; q < tx_rings; q++) {
		retval = rte_eth_tx_queue_setup(port, q, nb_txd,
				rte_eth_dev_socket_id(port), &txconf);
		if (retval < 0)
			return retval;
	}
	printf("333\n");
	/* Start the Ethernet port. */
	/*启动port网口*/
	retval = rte_eth_dev_start(port);
	if (retval < 0)
		return retval;

	/* Display the port MAC address. */
	struct rte_ether_addr addr;
	retval = rte_eth_macaddr_get(port, &addr);
	if (retval != 0)
		return retval;

	printf("Port %u MAC: %02" PRIx8 " %02" PRIx8 " %02" PRIx8
			   " %02" PRIx8 " %02" PRIx8 " %02" PRIx8 "\n",
			port,
			addr.addr_bytes[0], addr.addr_bytes[1],
			addr.addr_bytes[2], addr.addr_bytes[3],
			addr.addr_bytes[4], addr.addr_bytes[5]);
	printf("444\n");
	/* Enable RX in promiscuous mode for the Ethernet device. */
	/*设置网口的混杂模式，不管是不是发给它的都会接受*/
	retval = rte_eth_promiscuous_enable(port);
	if (retval != 0)
		return retval;

	return 0;
}

int main(int argc, char *argv[]){
	if(rte_eal_init(argc,argv)<0) rte_exit(EXIT_FAILURE, "init failed\n");
	printf("hello word!\n");
	struct rte_mempool *mempool = rte_pktmbuf_pool_create("mypool",14016,256,0,RTE_MBUF_DEFAULT_BUF_SIZE,rte_socket_id());
	if(mempool == NULL) rte_exit(EXIT_FAILURE, "create mempool failed\n");
	int n = rte_eth_dev_count_avail();
	if(n == 0) rte_exit(EXIT_FAILURE, "rte_eth_dev_count_avail failed\n");
	uint16_t port_id = 0;
	if(rte_eth_dev_get_port_by_name("0000:18:00.0",&port_id)!=0) rte_exit(EXIT_FAILURE, "get port failed\n");
	struct  rte_eth_dev_info dev_info;
	rte_eth_dev_info_get(port_id, &dev_info);
	printf("%d\n",(int)port_id);
	printf("%d\n",n);

	port_init(port_id, mbuf_pool);

	return 0;
}
