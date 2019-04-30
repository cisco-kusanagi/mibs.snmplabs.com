#
# PySNMP MIB module XYLAN-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-OAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter32, NotificationType, Integer32, Counter64, iso, ObjectIdentity, ModuleIdentity, MibIdentifier, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter32", "NotificationType", "Integer32", "Counter64", "iso", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanOamArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanOamArch")
xylanOam = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 28, 1))
xylanOamF4VPTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1), )
if mibBuilder.loadTexts: xylanOamF4VPTable.setStatus('mandatory')
xylanOamF4VPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1), ).setIndexNames((0, "XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"), (0, "XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"), (0, "XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"))
if mibBuilder.loadTexts: xylanOamF4VPEntry.setStatus('mandatory')
xylanOamF4VPSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPSlotIndex.setStatus('mandatory')
xylanOamF4VPPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPPortIndex.setStatus('mandatory')
xylanOamF4VPVpiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPVpiIndex.setStatus('mandatory')
xylanOamF4VPAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF4VPAdminEnable.setStatus('mandatory')
xylanOamF4VPAisEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF4VPAisEnable.setStatus('mandatory')
xylanOamF4VPRdiEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF4VPRdiEnable.setStatus('mandatory')
xylanOamF4VPContCheckEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF4VPContCheckEnable.setStatus('mandatory')
xylanOamF4VPTrapOnAlarmEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF4VPTrapOnAlarmEnable.setStatus('mandatory')
xylanOamF4VPLoopbackEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF4VPLoopbackEnable.setStatus('mandatory')
xylanOamF4VPLoopbackType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("end-to-end", 1), ("access-line", 2), ("inter-domain", 3), ("network-to-endpoint", 4), ("intra-domain", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF4VPLoopbackType.setStatus('mandatory')
xylanOamF4VPLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("successful", 2), ("unsuccessful", 3), ("responsewaiting", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPLoopbackStatus.setStatus('mandatory')
xylanOamF4VPContCheckStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ready", 1), ("waitingActivate", 2), ("waitingDeactivate", 3), ("active", 4), ("disabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPContCheckStatus.setStatus('mandatory')
xylanOamF4VPAisRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPAisRxCount.setStatus('mandatory')
xylanOamF4VPAisTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPAisTxCount.setStatus('mandatory')
xylanOamF4VPRdiRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPRdiRxCount.setStatus('mandatory')
xylanOamF4VPRdiTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPRdiTxCount.setStatus('mandatory')
xylanOamF4VPLoopbackRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPLoopbackRxCount.setStatus('mandatory')
xylanOamF4VPLoopbackTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPLoopbackTxCount.setStatus('mandatory')
xylanOamF4VPContCheckRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPContCheckRxCount.setStatus('mandatory')
xylanOamF4VPContCheckTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPContCheckTxCount.setStatus('mandatory')
xylanOamF4VPLOCCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPLOCCount.setStatus('mandatory')
xylanOamF4VPLoopbackSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPLoopbackSuccessCount.setStatus('mandatory')
xylanOamF4VPLoopbackFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF4VPLoopbackFailureCount.setStatus('mandatory')
xylanOamF4VPSegmentAction = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("copy", 2), ("extract", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF4VPSegmentAction.setStatus('mandatory')
xylanOamF4VPEndtoendAction = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("copy", 2), ("extract", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF4VPEndtoendAction.setStatus('mandatory')
xylanOamF5VCTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2), )
if mibBuilder.loadTexts: xylanOamF5VCTable.setStatus('mandatory')
xylanOamTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3))
xylanOamF5VCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1), ).setIndexNames((0, "XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"), (0, "XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"), (0, "XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"), (0, "XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"))
if mibBuilder.loadTexts: xylanOamF5VCEntry.setStatus('mandatory')
xylanOamF5VCSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCSlotIndex.setStatus('mandatory')
xylanOamF5VCPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCPortIndex.setStatus('mandatory')
xylanOamF5VCVpiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCVpiIndex.setStatus('mandatory')
xylanOamF5VCVciIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCVciIndex.setStatus('mandatory')
xylanOamF5VCAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF5VCAdminEnable.setStatus('mandatory')
xylanOamF5VCAisEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF5VCAisEnable.setStatus('mandatory')
xylanOamF5VCRdiEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF5VCRdiEnable.setStatus('mandatory')
xylanOamF5VCContCheckEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF5VCContCheckEnable.setStatus('mandatory')
xylanOamF5VCTrapOnAlarmEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF5VCTrapOnAlarmEnable.setStatus('mandatory')
xylanOamF5VCLoopbackEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF5VCLoopbackEnable.setStatus('mandatory')
xylanOamF5VCLoopbackType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("end-to-end", 1), ("access-line", 2), ("inter-domain", 3), ("network-to-endpoint", 4), ("intra-domain", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF5VCLoopbackType.setStatus('mandatory')
xylanOamF5VCLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("successful", 2), ("unsuccessful", 3), ("responsewaiting", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCLoopbackStatus.setStatus('mandatory')
xylanOamF5VCContCheckStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ready", 1), ("waitingActivate", 2), ("waitingDeactivate", 3), ("active", 4), ("disabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCContCheckStatus.setStatus('mandatory')
xylanOamF5VCAisRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCAisRxCount.setStatus('mandatory')
xylanOamF5VCAisTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCAisTxCount.setStatus('mandatory')
xylanOamF5VCRdiRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCRdiRxCount.setStatus('mandatory')
xylanOamF5VCRdiTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCRdiTxCount.setStatus('mandatory')
xylanOamF5VCLoopbackRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCLoopbackRxCount.setStatus('mandatory')
xylanOamF5VCLoopbackTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCLoopbackTxCount.setStatus('mandatory')
xylanOamF5VCContCheckRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCContCheckRxCount.setStatus('mandatory')
xylanOamF5VCContCheckTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCContCheckTxCount.setStatus('mandatory')
xylanOamF5VCLOCCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCLOCCount.setStatus('mandatory')
xylanOamF5VCLoopbackSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCLoopbackSuccessCount.setStatus('mandatory')
xylanOamF5VCLoopbackFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanOamF5VCLoopbackFailureCount.setStatus('mandatory')
xylanOamF5VCSegmentAction = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("copy", 2), ("extract", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF5VCSegmentAction.setStatus('mandatory')
xylanOamF5VCEndtoendAction = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("copy", 2), ("extract", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanOamF5VCEndtoendAction.setStatus('mandatory')
xylanOamTrapVCAIS = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3) + (0,1)).setObjects(("XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"))
xylanOamTrapVCRDI = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3) + (0,2)).setObjects(("XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"))
xylanOamTrapVCLOC = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3) + (0,3)).setObjects(("XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"))
xylanOamTrapVCUnsuccessLoop = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3) + (0,4)).setObjects(("XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"), ("XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"))
xylanOamTrapVPAIS = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3) + (0,5)).setObjects(("XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"), ("XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"), ("XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"))
xylanOamTrapVPRDI = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3) + (0,6)).setObjects(("XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"), ("XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"), ("XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"))
xylanOamTrapVPLOC = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3) + (0,7)).setObjects(("XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"), ("XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"), ("XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"))
xylanOamTrapVPUnsuccessLoop = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3) + (0,8)).setObjects(("XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"), ("XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"), ("XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"))
mibBuilder.exportSymbols("XYLAN-OAM-MIB", xylanOamF5VCLoopbackRxCount=xylanOamF5VCLoopbackRxCount, xylanOamF4VPEntry=xylanOamF4VPEntry, xylanOamF5VCAisTxCount=xylanOamF5VCAisTxCount, xylanOamF4VPRdiTxCount=xylanOamF4VPRdiTxCount, xylanOamF4VPLoopbackEnable=xylanOamF4VPLoopbackEnable, xylanOamF5VCContCheckRxCount=xylanOamF5VCContCheckRxCount, xylanOamF4VPAdminEnable=xylanOamF4VPAdminEnable, xylanOamTrapVCLOC=xylanOamTrapVCLOC, xylanOamF4VPTable=xylanOamF4VPTable, xylanOamF4VPContCheckRxCount=xylanOamF4VPContCheckRxCount, xylanOamF5VCAisRxCount=xylanOamF5VCAisRxCount, xylanOamF5VCLOCCount=xylanOamF5VCLOCCount, xylanOamF4VPLoopbackRxCount=xylanOamF4VPLoopbackRxCount, xylanOamF4VPTrapOnAlarmEnable=xylanOamF4VPTrapOnAlarmEnable, xylanOamF4VPLoopbackStatus=xylanOamF4VPLoopbackStatus, xylanOamF4VPVpiIndex=xylanOamF4VPVpiIndex, xylanOamF4VPLOCCount=xylanOamF4VPLOCCount, xylanOamF5VCVciIndex=xylanOamF5VCVciIndex, xylanOamF4VPEndtoendAction=xylanOamF4VPEndtoendAction, xylanOamF5VCPortIndex=xylanOamF5VCPortIndex, xylanOamF5VCTable=xylanOamF5VCTable, xylanOamF4VPSegmentAction=xylanOamF4VPSegmentAction, xylanOamTrapVPRDI=xylanOamTrapVPRDI, xylanOamF4VPLoopbackType=xylanOamF4VPLoopbackType, xylanOamF5VCLoopbackTxCount=xylanOamF5VCLoopbackTxCount, xylanOamF4VPLoopbackFailureCount=xylanOamF4VPLoopbackFailureCount, xylanOamF4VPPortIndex=xylanOamF4VPPortIndex, xylanOamF4VPRdiEnable=xylanOamF4VPRdiEnable, xylanOamF5VCEndtoendAction=xylanOamF5VCEndtoendAction, xylanOamTrapVCRDI=xylanOamTrapVCRDI, xylanOamTrapVCUnsuccessLoop=xylanOamTrapVCUnsuccessLoop, xylanOam=xylanOam, xylanOamTrapVCAIS=xylanOamTrapVCAIS, xylanOamF5VCEntry=xylanOamF5VCEntry, xylanOamF5VCSegmentAction=xylanOamF5VCSegmentAction, xylanOamF5VCLoopbackEnable=xylanOamF5VCLoopbackEnable, xylanOamF4VPAisTxCount=xylanOamF4VPAisTxCount, xylanOamF5VCContCheckEnable=xylanOamF5VCContCheckEnable, xylanOamF5VCLoopbackStatus=xylanOamF5VCLoopbackStatus, xylanOamF5VCAdminEnable=xylanOamF5VCAdminEnable, xylanOamF4VPLoopbackSuccessCount=xylanOamF4VPLoopbackSuccessCount, xylanOamF5VCLoopbackType=xylanOamF5VCLoopbackType, xylanOamF5VCLoopbackFailureCount=xylanOamF5VCLoopbackFailureCount, xylanOamF4VPAisRxCount=xylanOamF4VPAisRxCount, xylanOamF4VPAisEnable=xylanOamF4VPAisEnable, xylanOamF5VCContCheckTxCount=xylanOamF5VCContCheckTxCount, xylanOamF5VCLoopbackSuccessCount=xylanOamF5VCLoopbackSuccessCount, xylanOamTrapVPAIS=xylanOamTrapVPAIS, xylanOamF4VPContCheckTxCount=xylanOamF4VPContCheckTxCount, xylanOamF5VCContCheckStatus=xylanOamF5VCContCheckStatus, xylanOamF5VCTrapOnAlarmEnable=xylanOamF5VCTrapOnAlarmEnable, xylanOamF4VPSlotIndex=xylanOamF4VPSlotIndex, xylanOamF5VCVpiIndex=xylanOamF5VCVpiIndex, xylanOamTrapVPUnsuccessLoop=xylanOamTrapVPUnsuccessLoop, xylanOamF5VCAisEnable=xylanOamF5VCAisEnable, xylanOamF4VPContCheckEnable=xylanOamF4VPContCheckEnable, xylanOamF5VCRdiTxCount=xylanOamF5VCRdiTxCount, xylanOamF5VCRdiEnable=xylanOamF5VCRdiEnable, xylanOamF4VPRdiRxCount=xylanOamF4VPRdiRxCount, xylanOamF4VPLoopbackTxCount=xylanOamF4VPLoopbackTxCount, xylanOamF5VCSlotIndex=xylanOamF5VCSlotIndex, xylanOamTraps=xylanOamTraps, xylanOamF5VCRdiRxCount=xylanOamF5VCRdiRxCount, xylanOamTrapVPLOC=xylanOamTrapVPLOC, xylanOamF4VPContCheckStatus=xylanOamF4VPContCheckStatus)