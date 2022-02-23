# Smartservo Makeblock MS-12A

The documentation for this servo is limited, but it can be ordered for [some 4.69 USD](https://www.aliexpress.com/item/1005003242499052.html).

## Connector

According to [this forum post](https://forum.makeblock.com/t/smart-servo-connector-type/15935) the connector is a Molex 51004 4-pin connector (0.079" or 2.00mm pitch) with [MicroBlade 53015 counterpart](https://www.digikey.ca/en/products/detail/molex/0530150410/1785079).

## Datasheet

The [Datasheet](makeblock-smart-servo-ms-12a-cth-datasheet.pdf) contains only a limited amount of information.

## Communication

It looks like the 4 pins are for VCC, GND and TX and RX, as stated in [these blog post](https://forum.makeblock.com/t/smart-servo-ms-12a-not-working-with-arduino/13438/12) with reference to a non-working Arduino library MeSmartServo.h as `mysmartservo(PORT5)` for the regular UART2 on port5. And some codelines:

``` c
MSmartServo mysmartservo(1);
mysmartservo.begin(115200);
mysmartservo.assignDevIdReauest();
```

## Library

The [MSmartServo Library v1.0.0](https://github.com/Makeblock-official/MSmartServo-Driver/tree/master/MSmartServo) is from March 2017.

The [Makeblock Library v3.27](https://github.com/Makeblock-official/Makeblock-Libraries/blob/master/src/MeSmartServo.h) from 2016.

## Website

Makeblock has some information on its website [https://www.makeblock.com/project/smart-servo-ms-12a](https://www.makeblock.com/project/smart-servo-ms-12a). But it seems it has not have an update since 2018.