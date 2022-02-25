from ps2controller import PS2Controller

ps2ctl = PS2Controller(di_pin_no=13, do_pin_no=12, cs_pin_no=15, clk_pin_no=14)

ps2ctl.run()
