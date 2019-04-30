#
# PySNMP MIB module NNCGNI00X7-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI00X7-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
nncExtDevice, = mibBuilder.importSymbols("NNCGNI00X1-SMI", "nncExtDevice")
PositionIndex, = mibBuilder.importSymbols("NNCGNI00X4-MIB", "PositionIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, Counter32, MibIdentifier, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, ModuleIdentity, Unsigned32, NotificationType, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Counter32", "MibIdentifier", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "ModuleIdentity", "Unsigned32", "NotificationType", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
nncExtDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1), ).setIndexNames((0, "NNCGNI00X7-MIB", "nncExtDevPosnIdx"), (0, "NNCGNI00X7-MIB", "nncExtDevPortIdx"), (0, "NNCGNI00X7-MIB", "nncExtDevCctIdx"))
if mibBuilder.loadTexts: nncExtDeviceEntry.setStatus('mandatory')
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
mibBuilder.exportSymbols("NNCGNI00X7-MIB", nncExtDevBusyOut=nncExtDevBusyOut, nncExtDevUIName=nncExtDevUIName, nncExtDevOutputSignalling=nncExtDevOutputSignalling, nncExtDevLoopback=nncExtDevLoopback, SignallingBits=SignallingBits, PortIndex=PortIndex, nncExtDevUIType=nncExtDevUIType, nncExtDevConnectedTo=nncExtDevConnectedTo, nncExtDeviceEntry=nncExtDeviceEntry, nncExtDevPortIdx=nncExtDevPortIdx, nncExtDeviceTable=nncExtDeviceTable, nncExtDevCctIdx=nncExtDevCctIdx, LoopbackType=LoopbackType, nncExtDevCallStatus=nncExtDevCallStatus, nncExtDevPosnIdx=nncExtDevPosnIdx, nncExtDevConnectedToUIName=nncExtDevConnectedToUIName, nncExtDevInputSignalling=nncExtDevInputSignalling, CircuitIndex=CircuitIndex, nncExtDevName=nncExtDevName)
