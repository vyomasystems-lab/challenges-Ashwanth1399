import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_write_read(dut):
    """Test for seq detection """
    clock = Clock(dut.PCLK, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    addr=22
    wdata=23
    # reset
    dut.PRESETn.value = 0
    await RisingEdge(dut.PCLK)
    dut.PRESETn.value = 1
    await RisingEdge(dut.PCLK)

    dut.PSEL.value  = 0
    dut.PENABLE.value  = 0
    await RisingEdge(dut.PCLK)
    cocotb.log.info(f'Idle')
    await FallingEdge(dut.PCLK)
    cocotb.log.info(f'Psel={dut.PSEL.value} Penable={dut.PENABLE.value}')

    dut.PADDR.value = addr
    dut.PWRITE.value= 1
    dut.PSEL.value  = 1
    dut.PWDATA.value= wdata
    await RisingEdge(dut.PCLK)
    cocotb.log.info(f'setup')
    await FallingEdge(dut.PCLK)
    cocotb.log.info(f'Paddr={int(dut.PADDR.value)} PWdata={int(dut.PWDATA.value)} Psel={dut.PSEL.value} PWrite={dut.PWRITE.value}')

    dut.PENABLE.value=1
    await RisingEdge(dut.PCLK)
    cocotb.log.info(f'access')
    await FallingEdge(dut.PCLK)
    cocotb.log.info(f'PSLVERR={dut.PSLVERR.value} Paddr={int(dut.PADDR.value)} PWdata={int(dut.PWDATA.value)}  Penable={(dut.PENABLE.value)}')
    dut.PSEL.value=0
    dut.PENABLE.value=0
    await RisingEdge(dut.PCLK)
    cocotb.log.info(f'Idle')
    await FallingEdge(dut.PCLK)
    cocotb.log.info(f'sel={dut.PSEL.value} enable={dut.PENABLE.value}')

    dut.PADDR.value = addr
    dut.PWRITE.value= 0
    dut.PSEL.value  = 1
    await RisingEdge(dut.PCLK)
    cocotb.log.info(f'setup')
    await FallingEdge(dut.PCLK)
    cocotb.log.info(f'addr={int(dut.PADDR.value)} sel={dut.PSEL.value} PWrite={dut.PWRITE.value}')

    dut.PENABLE.value=1
    await RisingEdge(dut.PCLK)
    await FallingEdge(dut.PCLK)
    cocotb.log.info(f'PSLVERR={(dut.PSLVERR.value)} Pen={(dut.PENABLE.value)} Rred={dut.PREADY.value} Rdata={int(dut.PRDATA.value)}')
    assert dut.PRDATA.value == wdata, "wdata is not same as rdata"