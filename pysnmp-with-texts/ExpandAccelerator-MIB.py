#
# PySNMP MIB module ExpandAccelerator-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ExpandAccelerator-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:11:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, enterprises, Counter64, TimeTicks, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, NotificationType, IpAddress, Integer32, Unsigned32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "enterprises", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "NotificationType", "IpAddress", "Integer32", "Unsigned32", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Enumerator00(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("down", 0), ("up", 1))

class Enumerator01(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ppp", 0), ("hdlc", 1), ("auto", 2))

class Enumerator02(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("on", 0), ("off", 1))

class Enumerator03(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("down", 0), ("up", 1))

class Enumerator04(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ppp", 0), ("hdlc", 1), ("auto", 2))

class Enumerator05(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("on", 0), ("off", 1), ("auto", 2))

class Enumerator06(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("bit-16", 0), ("bit-32", 1))

expand = MibIdentifier((1, 3, 6, 1, 4, 1, 3405))
accelerator = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 1))
acc4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 1, 1))
accelerator_4000_series = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 1), Unsigned32()).setLabel("accelerator-4000-series").setMaxAccess("readonly")
if mibBuilder.loadTexts: accelerator_4000_series.setStatus('mandatory')
if mibBuilder.loadTexts: accelerator_4000_series.setDescription('Expand Accelerator 4000 series base OID')
details = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2))
detailsInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1), )
if mibBuilder.loadTexts: detailsInterfaceTable.setStatus('mandatory')
detailsInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1), ).setIndexNames((0, "ExpandAccelerator-MIB", "interfaceName"))
if mibBuilder.loadTexts: detailsInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: detailsInterfaceEntry.setDescription('interface details table')
interfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceName.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceName.setDescription('interface name')
interfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 2), Enumerator00()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatus.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceStatus.setDescription('interface status')
interfaceCloackRate = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceCloackRate.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceCloackRate.setDescription('interface clock rate')
interfaceQueueMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 4), Enumerator01()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceQueueMode.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceQueueMode.setDescription('interface queuing mode')
interfaceFifoSystemLimits = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceFifoSystemLimits.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceFifoSystemLimits.setDescription('fifo system limits')
interfaceFairQueueSystemLimits = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceFairQueueSystemLimits.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceFairQueueSystemLimits.setDescription('fair queuing system limits')
interfaceFairQueueSessionLimits = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceFairQueueSessionLimits.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceFairQueueSessionLimits.setDescription('fair queuing session limits')
interfaceIgnoreDCD = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 8), Enumerator02()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceIgnoreDCD.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceIgnoreDCD.setDescription('ignore dcd')
interfaceBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceBandwidth.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceBandwidth.setDescription('bandwidth')
interfaceCountersPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceCountersPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceCountersPeriod.setDescription('period over which data is avaraged')
interfaceProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 11), Enumerator04()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceProtocolType.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceProtocolType.setDescription('interface encapsulation protocol type')
interfaceDCDMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 12), Enumerator05()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceDCDMode.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceDCDMode.setDescription('dcd mode')
interfaceCRCMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 13), Enumerator06()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceCRCMode.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceCRCMode.setDescription('crc mode')
statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3))
statInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1), )
if mibBuilder.loadTexts: statInterfaceTable.setStatus('mandatory')
statInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1), ).setIndexNames((0, "ExpandAccelerator-MIB", "interfaceName"))
if mibBuilder.loadTexts: statInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: statInterfaceEntry.setDescription('interface statistics table')
interfaceName2 = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceName2.setStatus('mandatory')
if mibBuilder.loadTexts: interfaceName2.setDescription('interface name')
systemUpInBytes_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 2), Unsigned32()).setLabel("systemUpInBytes-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpInBytes_Low.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpInBytes_Low.setDescription('bytes in since system up low 32-bit')
systemUpInBytes_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 3), Unsigned32()).setLabel("systemUpInBytes-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpInBytes_High.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpInBytes_High.setDescription('bytes in since system up high 32-bit')
systemUpInBytes_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 4), OctetString()).setLabel("systemUpInBytes-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUpInBytes_String.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpInBytes_String.setDescription('bytes in since system up string representation')
systemUpInPackets_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 5), Unsigned32()).setLabel("systemUpInPackets-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpInPackets_Low.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpInPackets_Low.setDescription('packets in since system up low 32-bit')
systemUpInPackets_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 6), Unsigned32()).setLabel("systemUpInPackets-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpInPackets_High.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpInPackets_High.setDescription('packets in since system up high 32-bit')
systemUpInPackets_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 7), OctetString()).setLabel("systemUpInPackets-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUpInPackets_String.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpInPackets_String.setDescription('packets in since system up string representation')
systemUpOutBytes_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 8), Unsigned32()).setLabel("systemUpOutBytes-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpOutBytes_Low.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpOutBytes_Low.setDescription('bytes out since system up low 32-bit')
systemUpOutBytes_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 9), Unsigned32()).setLabel("systemUpOutBytes-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpOutBytes_High.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpOutBytes_High.setDescription('bytes out since system up high 32-bit')
systemUpOutBytes_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 10), OctetString()).setLabel("systemUpOutBytes-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUpOutBytes_String.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpOutBytes_String.setDescription('bytes out since system up string representation')
systemUpOutPackets_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 11), Unsigned32()).setLabel("systemUpOutPackets-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpOutPackets_Low.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpOutPackets_Low.setDescription('packets out since system up low 32-bit')
systemUpOutPackets_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 12), Unsigned32()).setLabel("systemUpOutPackets-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpOutPackets_High.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpOutPackets_High.setDescription('packets out since system up high 32-bit')
systemUpOutPackets_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 13), OctetString()).setLabel("systemUpOutPackets-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUpOutPackets_String.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpOutPackets_String.setDescription('packets out since system up string representation')
systemUpDroppedBytes_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 14), Unsigned32()).setLabel("systemUpDroppedBytes-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpDroppedBytes_Low.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpDroppedBytes_Low.setDescription('bytes overrun since system up low 32-bit')
systemUpDroppedBytes_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 15), Unsigned32()).setLabel("systemUpDroppedBytes-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpDroppedBytes_High.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpDroppedBytes_High.setDescription('bytes overrun since system up high 32-bit')
systemUpDroppedBytes_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 16), OctetString()).setLabel("systemUpDroppedBytes-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUpDroppedBytes_String.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpDroppedBytes_String.setDescription('bytes overrun since system up string representation')
systemUpDroppedPackets_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 17), Unsigned32()).setLabel("systemUpDroppedPackets-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpDroppedPackets_Low.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpDroppedPackets_Low.setDescription('packets dropped since system up low 32-bit')
systemUpDroppedPackets_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 18), Unsigned32()).setLabel("systemUpDroppedPackets-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpDroppedPackets_High.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpDroppedPackets_High.setDescription('packets dropped since system up high 32-bit')
systemUpDroppedPackets_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 19), OctetString()).setLabel("systemUpDroppedPackets-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUpDroppedPackets_String.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpDroppedPackets_String.setDescription('packets dropped since system up string representation')
systemUpOverrunPackets_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 20), Unsigned32()).setLabel("systemUpOverrunPackets-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpOverrunPackets_Low.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpOverrunPackets_Low.setDescription('packets overrun since system up low 32-bit')
systemUpOverrunPackets_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 21), Unsigned32()).setLabel("systemUpOverrunPackets-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpOverrunPackets_High.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpOverrunPackets_High.setDescription('packets overrun since system up high 32-bit')
systemUpOverrunPackets_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 22), OctetString()).setLabel("systemUpOverrunPackets-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUpOverrunPackets_String.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpOverrunPackets_String.setDescription('packets overrun since system up string representation')
systemUpCrcErrors_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 23), Unsigned32()).setLabel("systemUpCrcErrors-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpCrcErrors_Low.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpCrcErrors_Low.setDescription('crc errors since system up low 32-bit')
systemUpCrcErrors_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 24), Unsigned32()).setLabel("systemUpCrcErrors-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpCrcErrors_High.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpCrcErrors_High.setDescription('crc errors since system up high 32-bit')
systemUpCrcErrors_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 25), OctetString()).setLabel("systemUpCrcErrors-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUpCrcErrors_String.setStatus('mandatory')
if mibBuilder.loadTexts: systemUpCrcErrors_String.setDescription('crc errors since system up string representation')
clearCountersInBytes_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 26), Unsigned32()).setLabel("clearCountersInBytes-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersInBytes_Low.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersInBytes_Low.setDescription('bytes in since clear counters low 32-bit')
clearCountersInBytes_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 27), Unsigned32()).setLabel("clearCountersInBytes-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersInBytes_High.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersInBytes_High.setDescription('bytes in since clear counters high 32-bit')
clearCountersInBytes_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 28), OctetString()).setLabel("clearCountersInBytes-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearCountersInBytes_String.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersInBytes_String.setDescription('bytes in since clear counters string representation')
clearCountersInPackets_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 29), Unsigned32()).setLabel("clearCountersInPackets-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersInPackets_Low.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersInPackets_Low.setDescription('packets in since clear counters low 32-bit')
clearCountersInPackets_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 30), Unsigned32()).setLabel("clearCountersInPackets-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersInPackets_High.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersInPackets_High.setDescription('packets in since clear counters high 32-bit')
clearCountersInPackets_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 31), OctetString()).setLabel("clearCountersInPackets-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearCountersInPackets_String.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersInPackets_String.setDescription('packets in since clear counters string representation')
clearCountersOutBytes_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 32), Unsigned32()).setLabel("clearCountersOutBytes-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersOutBytes_Low.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersOutBytes_Low.setDescription('bytes out since clear counters low 32-bit')
clearCountersOutBytes_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 33), Unsigned32()).setLabel("clearCountersOutBytes-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersOutBytes_High.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersOutBytes_High.setDescription('bytes out since clear counters high 32-bit')
clearCountersOutBytes_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 34), OctetString()).setLabel("clearCountersOutBytes-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearCountersOutBytes_String.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersOutBytes_String.setDescription('bytes out since clear counters string representation')
clearCountersOutPackets_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 35), Unsigned32()).setLabel("clearCountersOutPackets-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersOutPackets_Low.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersOutPackets_Low.setDescription('packets out since clear counters low 32-bit')
clearCountersOutPackets_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 36), Unsigned32()).setLabel("clearCountersOutPackets-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersOutPackets_High.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersOutPackets_High.setDescription('packets out since clear counters high 32-bit')
clearCountersOutPackets_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 37), OctetString()).setLabel("clearCountersOutPackets-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearCountersOutPackets_String.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersOutPackets_String.setDescription('packets out since clear counters string representation')
clearCountersDroppedBytes_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 38), Unsigned32()).setLabel("clearCountersDroppedBytes-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersDroppedBytes_Low.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersDroppedBytes_Low.setDescription('bytes dropped since clear counters low 32-bit')
clearCountersDroppedBytes_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 39), Unsigned32()).setLabel("clearCountersDroppedBytes-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersDroppedBytes_High.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersDroppedBytes_High.setDescription('bytes dropped since clear counters high 32-bit')
clearCountersDroppedBytes_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 40), OctetString()).setLabel("clearCountersDroppedBytes-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearCountersDroppedBytes_String.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersDroppedBytes_String.setDescription('bytes dropped since clear counters string representation')
clearCountersDroppedPackets_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 41), Unsigned32()).setLabel("clearCountersDroppedPackets-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersDroppedPackets_Low.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersDroppedPackets_Low.setDescription('packets dropped since clear counters low 32-bit')
clearCountersDroppedPackets_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 42), Unsigned32()).setLabel("clearCountersDroppedPackets-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersDroppedPackets_High.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersDroppedPackets_High.setDescription('packets dropped since clear counters high 32-bit')
clearCountersDroppedPackets_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 43), OctetString()).setLabel("clearCountersDroppedPackets-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearCountersDroppedPackets_String.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersDroppedPackets_String.setDescription('packets dropped since clear counters string representation')
clearCountersOverrunPackets_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 44), Unsigned32()).setLabel("clearCountersOverrunPackets-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersOverrunPackets_Low.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersOverrunPackets_Low.setDescription('packets overrun since clear counters low 32-bit')
clearCountersOverrunPackets_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 45), Unsigned32()).setLabel("clearCountersOverrunPackets-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersOverrunPackets_High.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersOverrunPackets_High.setDescription('packets overrun since clear counters high 32-bit')
clearCountersOverrunPackets_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 46), OctetString()).setLabel("clearCountersOverrunPackets-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearCountersOverrunPackets_String.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersOverrunPackets_String.setDescription('packets overrun since clear counters string representation')
clearCountersCrcErrors_Low = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 47), Unsigned32()).setLabel("clearCountersCrcErrors-Low").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersCrcErrors_Low.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersCrcErrors_Low.setDescription('crc error since clear counters low 32-bit')
clearCountersCrcErrors_High = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 48), Unsigned32()).setLabel("clearCountersCrcErrors-High").setMaxAccess("readonly")
if mibBuilder.loadTexts: clearCountersCrcErrors_High.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersCrcErrors_High.setDescription('crc error since clear counters high 32-bit')
clearCountersCrcErrors_String = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 49), OctetString()).setLabel("clearCountersCrcErrors-String").setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearCountersCrcErrors_String.setStatus('mandatory')
if mibBuilder.loadTexts: clearCountersCrcErrors_String.setDescription('crc error since clear counters string representation')
countersPeriodBytesInPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 50), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: countersPeriodBytesInPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: countersPeriodBytesInPerSec.setDescription('bytes in during countersPeriod')
countersPeriodPacketsInPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 51), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: countersPeriodPacketsInPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: countersPeriodPacketsInPerSec.setDescription('packets in last countersPeriod')
countersPeriodBytesOutPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 52), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: countersPeriodBytesOutPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: countersPeriodBytesOutPerSec.setDescription('bytes out last countersPeriod')
countersPeriodPacketsOutPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 53), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: countersPeriodPacketsOutPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: countersPeriodPacketsOutPerSec.setDescription('packets out last countersPeriod')
countersPeriodDroppedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 54), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: countersPeriodDroppedBytes.setStatus('mandatory')
if mibBuilder.loadTexts: countersPeriodDroppedBytes.setDescription('drop bytes last countersPeriod')
countersPeriodDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 55), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: countersPeriodDroppedPackets.setStatus('mandatory')
if mibBuilder.loadTexts: countersPeriodDroppedPackets.setDescription('drop packets last countersPeriod')
countersPeriodOverrunPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 56), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: countersPeriodOverrunPackets.setStatus('mandatory')
if mibBuilder.loadTexts: countersPeriodOverrunPackets.setDescription('packets overrun sine last countersPeriod')
countersPeriodCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 57), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: countersPeriodCrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: countersPeriodCrcErrors.setDescription('crc error sine last countersPeriod')
acceleration = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4))
accPeriod = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: accPeriod.setDescription('timed period for acceleration')
local = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 1))
aclSystemUp = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclSystemUp.setStatus('mandatory')
if mibBuilder.loadTexts: aclSystemUp.setDescription('acceleration since system up')
aclSinceClear = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclSinceClear.setStatus('mandatory')
if mibBuilder.loadTexts: aclSinceClear.setDescription('acceleration since cleared')
aclLastPeriod = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclLastPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: aclLastPeriod.setDescription('acceleration for last period of seconds')
remote = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 2))
acrSystemUp = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acrSystemUp.setStatus('mandatory')
if mibBuilder.loadTexts: acrSystemUp.setDescription('acceleration since system up')
acrSinceClear = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acrSinceClear.setStatus('mandatory')
if mibBuilder.loadTexts: acrSinceClear.setDescription('acceleration since cleared')
acrLastPeriod = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acrLastPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: acrLastPeriod.setDescription('acceleration for last period of seconds')
mibBuilder.exportSymbols("ExpandAccelerator-MIB", Enumerator00=Enumerator00, interfaceIgnoreDCD=interfaceIgnoreDCD, countersPeriodOverrunPackets=countersPeriodOverrunPackets, systemUpOverrunPackets_Low=systemUpOverrunPackets_Low, countersPeriodDroppedPackets=countersPeriodDroppedPackets, remote=remote, systemUpInPackets_Low=systemUpInPackets_Low, clearCountersOutPackets_String=clearCountersOutPackets_String, interfaceCRCMode=interfaceCRCMode, countersPeriodDroppedBytes=countersPeriodDroppedBytes, interfaceDCDMode=interfaceDCDMode, clearCountersOverrunPackets_String=clearCountersOverrunPackets_String, systemUpDroppedBytes_String=systemUpDroppedBytes_String, systemUpDroppedPackets_High=systemUpDroppedPackets_High, acc4000=acc4000, systemUpOutBytes_Low=systemUpOutBytes_Low, statInterfaceEntry=statInterfaceEntry, clearCountersDroppedBytes_Low=clearCountersDroppedBytes_Low, accelerator=accelerator, acrSystemUp=acrSystemUp, clearCountersInPackets_String=clearCountersInPackets_String, systemUpCrcErrors_String=systemUpCrcErrors_String, Enumerator04=Enumerator04, clearCountersDroppedPackets_String=clearCountersDroppedPackets_String, systemUpInBytes_String=systemUpInBytes_String, systemUpDroppedBytes_High=systemUpDroppedBytes_High, systemUpCrcErrors_Low=systemUpCrcErrors_Low, interfaceBandwidth=interfaceBandwidth, expand=expand, clearCountersCrcErrors_Low=clearCountersCrcErrors_Low, clearCountersOutBytes_High=clearCountersOutBytes_High, countersPeriodPacketsOutPerSec=countersPeriodPacketsOutPerSec, clearCountersOutPackets_Low=clearCountersOutPackets_Low, systemUpOutBytes_String=systemUpOutBytes_String, systemUpInPackets_High=systemUpInPackets_High, interfaceName=interfaceName, systemUpDroppedBytes_Low=systemUpDroppedBytes_Low, clearCountersInBytes_Low=clearCountersInBytes_Low, aclSinceClear=aclSinceClear, clearCountersDroppedBytes_High=clearCountersDroppedBytes_High, systemUpOutPackets_String=systemUpOutPackets_String, clearCountersDroppedPackets_High=clearCountersDroppedPackets_High, clearCountersInPackets_High=clearCountersInPackets_High, countersPeriodCrcErrors=countersPeriodCrcErrors, acrLastPeriod=acrLastPeriod, interfaceCloackRate=interfaceCloackRate, acceleration=acceleration, clearCountersInPackets_Low=clearCountersInPackets_Low, aclSystemUp=aclSystemUp, Enumerator01=Enumerator01, Enumerator06=Enumerator06, systemUpInBytes_High=systemUpInBytes_High, Enumerator05=Enumerator05, clearCountersCrcErrors_String=clearCountersCrcErrors_String, systemUpCrcErrors_High=systemUpCrcErrors_High, systemUpOutPackets_High=systemUpOutPackets_High, Enumerator03=Enumerator03, detailsInterfaceEntry=detailsInterfaceEntry, interfaceName2=interfaceName2, systemUpDroppedPackets_String=systemUpDroppedPackets_String, acrSinceClear=acrSinceClear, aclLastPeriod=aclLastPeriod, interfaceStatus=interfaceStatus, systemUpInBytes_Low=systemUpInBytes_Low, systemUpDroppedPackets_Low=systemUpDroppedPackets_Low, clearCountersDroppedPackets_Low=clearCountersDroppedPackets_Low, clearCountersInBytes_String=clearCountersInBytes_String, interfaceFairQueueSessionLimits=interfaceFairQueueSessionLimits, systemUpOutBytes_High=systemUpOutBytes_High, systemUpOverrunPackets_High=systemUpOverrunPackets_High, clearCountersOutBytes_Low=clearCountersOutBytes_Low, interfaceFifoSystemLimits=interfaceFifoSystemLimits, accelerator_4000_series=accelerator_4000_series, clearCountersOverrunPackets_Low=clearCountersOverrunPackets_Low, clearCountersOutBytes_String=clearCountersOutBytes_String, systemUpOverrunPackets_String=systemUpOverrunPackets_String, detailsInterfaceTable=detailsInterfaceTable, statistics=statistics, local=local, countersPeriodBytesOutPerSec=countersPeriodBytesOutPerSec, clearCountersInBytes_High=clearCountersInBytes_High, statInterfaceTable=statInterfaceTable, countersPeriodPacketsInPerSec=countersPeriodPacketsInPerSec, Enumerator02=Enumerator02, clearCountersDroppedBytes_String=clearCountersDroppedBytes_String, interfaceFairQueueSystemLimits=interfaceFairQueueSystemLimits, interfaceCountersPeriod=interfaceCountersPeriod, interfaceProtocolType=interfaceProtocolType, clearCountersOverrunPackets_High=clearCountersOverrunPackets_High, clearCountersCrcErrors_High=clearCountersCrcErrors_High, clearCountersOutPackets_High=clearCountersOutPackets_High, accPeriod=accPeriod, interfaceQueueMode=interfaceQueueMode, systemUpInPackets_String=systemUpInPackets_String, systemUpOutPackets_Low=systemUpOutPackets_Low, details=details, countersPeriodBytesInPerSec=countersPeriodBytesInPerSec)
