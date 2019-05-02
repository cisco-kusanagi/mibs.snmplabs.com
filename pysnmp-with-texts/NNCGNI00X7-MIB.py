#
# PySNMP MIB module NNCGNI00X7-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI00X7-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
nncExtDevice, = mibBuilder.importSymbols("NNCGNI00X1-SMI", "nncExtDevice")
PositionIndex, = mibBuilder.importSymbols("NNCGNI00X4-MIB", "PositionIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Counter32, MibIdentifier, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, TimeTicks, Unsigned32, ModuleIdentity, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "TimeTicks", "Unsigned32", "ModuleIdentity", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PortIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 12)

class CircuitIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 33)

class LoopbackType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("devNoLoopback", 1), ("devLoopbackA", 2), ("devLoopbackB", 3), ("devLoopBackC", 4), ("devChannelLoopback", 5), ("devDDSOCULoopback", 6), ("devDDSDSULoopback", 7), ("devDDSLatchOCULoopback", 8), ("devDDSLatchCSULoopback", 9), ("devDDSLatchDSOLoopback", 10), ("devDDSLatchHL96Loopback", 11), ("devDDSMJULoopback", 12), ("devDD-BlkLoopback", 13))

class SignallingBits(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

nncExtDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 9, 1), )
if mibBuilder.loadTexts: nncExtDeviceTable.setStatus('mandatory')
if mibBuilder.loadTexts: nncExtDeviceTable.setDescription('Configuration information for the Rptr modules in the system')
nncExtDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1), ).setIndexNames((0, "NNCGNI00X7-MIB", "nncExtDevPosnIdx"), (0, "NNCGNI00X7-MIB", "nncExtDevPortIdx"), (0, "NNCGNI00X7-MIB", "nncExtDevCctIdx"))
if mibBuilder.loadTexts: nncExtDeviceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nncExtDeviceEntry.setDescription('Configuration and status module for a device')
nncExtDevPosnIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 1), PositionIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDevPosnIdx.setStatus('mandatory')
nncExtDevPortIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 2), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDevPortIdx.setStatus('mandatory')
nncExtDevCctIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 3), CircuitIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDevCctIdx.setStatus('mandatory')
nncExtDevName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDevName.setStatus('mandatory')
nncExtDevLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("devNoLoopback", 1), ("devLoopbackA", 2), ("devLoopbackB", 3), ("devLoopBackC", 4), ("devChannelLoopback", 5), ("devDDSOCULoopback", 6), ("devDDSDSULoopback", 7), ("devDDSLatchOCULoopback", 8), ("devDDSLatchCSULoopback", 9), ("devDDSLatchDSOLoopback", 10), ("devDDSLatchHL96Loopback", 11), ("devDDSMJULoopback", 12), ("devDD-BlkLoopback", 13)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDevLoopback.setStatus('mandatory')
nncExtDevCallStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDevCallStatus.setStatus('mandatory')
nncExtDevBusyOut = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDevBusyOut.setStatus('mandatory')
nncExtDevOutputSignalling = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 8), SignallingBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDevOutputSignalling.setStatus('mandatory')
nncExtDevInputSignalling = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 9), SignallingBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDevInputSignalling.setStatus('mandatory')
nncExtDevConnectedTo = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDevConnectedTo.setStatus('mandatory')
nncExtDevUIName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDevUIName.setStatus('mandatory')
nncExtDevUIType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDevUIType.setStatus('mandatory')
nncExtDevConnectedToUIName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDevConnectedToUIName.setStatus('mandatory')
mibBuilder.exportSymbols("NNCGNI00X7-MIB", nncExtDevLoopback=nncExtDevLoopback, nncExtDevConnectedToUIName=nncExtDevConnectedToUIName, nncExtDevUIType=nncExtDevUIType, nncExtDeviceTable=nncExtDeviceTable, nncExtDevOutputSignalling=nncExtDevOutputSignalling, nncExtDevPosnIdx=nncExtDevPosnIdx, nncExtDevUIName=nncExtDevUIName, nncExtDevBusyOut=nncExtDevBusyOut, nncExtDeviceEntry=nncExtDeviceEntry, PortIndex=PortIndex, SignallingBits=SignallingBits, LoopbackType=LoopbackType, nncExtDevPortIdx=nncExtDevPortIdx, CircuitIndex=CircuitIndex, nncExtDevName=nncExtDevName, nncExtDevCctIdx=nncExtDevCctIdx, nncExtDevCallStatus=nncExtDevCallStatus, nncExtDevInputSignalling=nncExtDevInputSignalling, nncExtDevConnectedTo=nncExtDevConnectedTo)
