import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_write_read(dut):
    """Test for seq detection """
    clock = Clock(dut.P_clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    addr=22
    wdata=23
    # reset
    dut.P_rst.value = 0
    await RisingEdge(dut.P_clk)  
    dut.P_rst.value = 1
    await RisingEdge(dut.P_clk)
    cocotb.log.info(f'reset completed')
    
    dut.P_addr.value = addr
    dut.P_write.value= 1
    dut.P_selx.value  = 1
    dut.P_wdata.value= wdata
    await RisingEdge(dut.P_clk)
    cocotb.log.info(f'setup')

    dut.P_enable.value=1
    dut.P_ready.value =1
    await RisingEdge(dut.P_clk)
    cocotb.log.info(f'access')

    dut.P_enable.value=0
    dut.P_ready.value =0
    await RisingEdge(dut.P_clk)
    cocotb.log.info(f'idle')

    dut.P_addr.value = 0
    dut.P_write.value= 0
    dut.P_selx.value  = 0
    await RisingEdge(dut.P_clk)
    cocotb.log.info(f'idle')

    dut.P_addr.value = addr
    dut.P_selx.value  = 1
    await RisingEdge(dut.P_clk)
    cocotb.log.info(f'setup')

    dut.P_enable.value=1
    dut.P_ready.value =1
    await RisingEdge(dut.P_clk)
    await RisingEdge(dut.P_clk)
    cocotb.log.info(f'access')
    cocotb.log.info(f'Wdata={(dut.P_wdata.value)} Rdata={(dut.P_rdata.value)}')
    #assert dut.PRDATA.value == wdata, "wdata is not same as rdata"