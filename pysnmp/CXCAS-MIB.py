#
# PySNMP MIB module CXCAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXCAS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
cxCAS, = mibBuilder.importSymbols("CXProduct-SMI", "cxCAS")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Integer32, IpAddress, MibIdentifier, iso, ModuleIdentity, TimeTicks, Bits, Gauge32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "iso", "ModuleIdentity", "TimeTicks", "Bits", "Gauge32", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dsx1ExtAbcdTxSignalingTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10), )
if mibBuilder.loadTexts: dsx1ExtAbcdTxSignalingTable.setStatus('mandatory')
dsx1ExtAbcdTxSignalingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1), ).setIndexNames((0, "CXCAS-MIB", "dsx1ExtAbcdTxSignalingTypeIndex"))
if mibBuilder.loadTexts: dsx1ExtAbcdTxSignalingEntry.setStatus('mandatory')
dsx1ExtAbcdTxSignalingTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ExtAbcdTxSignalingTypeIndex.setStatus('mandatory')
dsx1ExtAbcdEmOnHook = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdEmOnHook.setStatus('mandatory')
dsx1ExtAbcdEmOffHook = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdEmOffHook.setStatus('mandatory')
dsx1ExtAbcdEmSeizeAck = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdEmSeizeAck.setStatus('mandatory')
dsx1ExtAbcdEmClearForward = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdEmClearForward.setStatus('mandatory')
dsx1ExtAbcdEmClearBackward = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdEmClearBackward.setStatus('mandatory')
dsx1ExtAbcdFxLo = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdFxLo.setStatus('mandatory')
dsx1ExtAbcdFxLc = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdFxLc.setStatus('mandatory')
dsx1ExtAbcdFxRingingOn = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdFxRingingOn.setStatus('mandatory')
dsx1ExtAbcdFxLcf = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdFxLcf.setStatus('mandatory')
dsx1ExtAbcdFxLcfo = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdFxLcfo.setStatus('mandatory')
dsx1ExtAbcdFxRingingOff = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdFxRingingOff.setStatus('mandatory')
dsx1ExtAbcdAnswer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdAnswer.setStatus('mandatory')
dsx1ExtAbcdBusyOut = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdBusyOut.setStatus('mandatory')
dsx1ExtAbcdFaultyLink = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdFaultyLink.setStatus('mandatory')
dsx1ExtAbcdRxSignalingTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20), )
if mibBuilder.loadTexts: dsx1ExtAbcdRxSignalingTable.setStatus('mandatory')
dsx1ExtAbcdRxSignalingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20, 1), ).setIndexNames((0, "CXCAS-MIB", "dsx1ExtAbcdRxSignalingTypeIndex"), (0, "CXCAS-MIB", "dsx1ExtAbcdRxSignalingAbcdValue"))
if mibBuilder.loadTexts: dsx1ExtAbcdRxSignalingEntry.setStatus('mandatory')
dsx1ExtAbcdRxSignalingTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ExtAbcdRxSignalingTypeIndex.setStatus('mandatory')
dsx1ExtAbcdRxSignalingAbcdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ExtAbcdRxSignalingAbcdValue.setStatus('mandatory')
dsx1ExtAbcdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("on-hook", 1), ("off-hook", 2), ("ring-on", 3), ("lcf", 4), ("lcfo", 5), ("answer", 6), ("ring-off", 7), ("busy-out", 8), ("faulty-link", 9), ("seize", 10), ("proceed", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ExtAbcdValue.setStatus('mandatory')
mibBuilder.exportSymbols("CXCAS-MIB", dsx1ExtAbcdFxLcf=dsx1ExtAbcdFxLcf, dsx1ExtAbcdEmOnHook=dsx1ExtAbcdEmOnHook, dsx1ExtAbcdEmOffHook=dsx1ExtAbcdEmOffHook, dsx1ExtAbcdFxRingingOff=dsx1ExtAbcdFxRingingOff, dsx1ExtAbcdAnswer=dsx1ExtAbcdAnswer, dsx1ExtAbcdRxSignalingEntry=dsx1ExtAbcdRxSignalingEntry, dsx1ExtAbcdEmClearForward=dsx1ExtAbcdEmClearForward, dsx1ExtAbcdTxSignalingEntry=dsx1ExtAbcdTxSignalingEntry, dsx1ExtAbcdFxLo=dsx1ExtAbcdFxLo, dsx1ExtAbcdFxLcfo=dsx1ExtAbcdFxLcfo, dsx1ExtAbcdRxSignalingTypeIndex=dsx1ExtAbcdRxSignalingTypeIndex, dsx1ExtAbcdFxRingingOn=dsx1ExtAbcdFxRingingOn, dsx1ExtAbcdTxSignalingTable=dsx1ExtAbcdTxSignalingTable, dsx1ExtAbcdEmClearBackward=dsx1ExtAbcdEmClearBackward, dsx1ExtAbcdBusyOut=dsx1ExtAbcdBusyOut, dsx1ExtAbcdRxSignalingTable=dsx1ExtAbcdRxSignalingTable, dsx1ExtAbcdTxSignalingTypeIndex=dsx1ExtAbcdTxSignalingTypeIndex, dsx1ExtAbcdFaultyLink=dsx1ExtAbcdFaultyLink, dsx1ExtAbcdFxLc=dsx1ExtAbcdFxLc, dsx1ExtAbcdValue=dsx1ExtAbcdValue, dsx1ExtAbcdEmSeizeAck=dsx1ExtAbcdEmSeizeAck, dsx1ExtAbcdRxSignalingAbcdValue=dsx1ExtAbcdRxSignalingAbcdValue)
