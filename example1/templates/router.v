router #(
		.FIFO_DEPTH(`FIFO_DEPTH))
	) `NAME (
		.rx_req(router_rx_req[`ID]),
		.rx_ack(router_rx_ack[`ID]),
		.rx_dat(router_rx_dat[`ID])
	);