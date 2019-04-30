#
# PySNMP MIB module A3COM-HUAWEI-LswSMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-LswSMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
huaweiDatacomm, huaweiMgmt = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "huaweiDatacomm", "huaweiMgmt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, Counter32, Bits, ObjectIdentity, Unsigned32, Counter64, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Counter32", "Bits", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26))
smonExtendObject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1))
hwdot1qVlanStatNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanStatNumber.setStatus('mandatory')
hwdot1qVlanStatStatusTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2), )
if mibBuilder.loadTexts: hwdot1qVlanStatStatusTable.setStatus('mandatory')
hwdot1qVlanStatStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswSMON-MIB", "hwdot1qVlanStatEnableIndex"))
if mibBuilder.loadTexts: hwdot1qVlanStatStatusEntry.setStatus('mandatory')
hwdot1qVlanStatEnableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanStatEnableIndex.setStatus('mandatory')
hwdot1qVlanStatEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanStatEnableStatus.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-HUAWEI-LswSMON-MIB", hwdot1qVlanStatStatusTable=hwdot1qVlanStatStatusTable, hwdot1qVlanStatEnableStatus=hwdot1qVlanStatEnableStatus, hwSmonExtend=hwSmonExtend, smonExtendObject=smonExtendObject, hwdot1qVlanStatStatusEntry=hwdot1qVlanStatStatusEntry, hwdot1qVlanStatEnableIndex=hwdot1qVlanStatEnableIndex, hwdot1qVlanStatNumber=hwdot1qVlanStatNumber)
