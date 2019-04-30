#
# PySNMP MIB module HUAWEI-LswSMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LswSMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:34:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
huaweiDatacomm, huaweiMgmt = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "huaweiDatacomm", "huaweiMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, iso, Gauge32, MibIdentifier, Bits, IpAddress, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "iso", "Gauge32", "MibIdentifier", "Bits", "IpAddress", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26))
smonExtendObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1))
hwdot1qVlanStatNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanStatNumber.setStatus('mandatory')
hwdot1qVlanStatStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 2), )
if mibBuilder.loadTexts: hwdot1qVlanStatStatusTable.setStatus('mandatory')
hwdot1qVlanStatStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 2, 1), ).setIndexNames((0, "HUAWEI-LswSMON-MIB", "hwdot1qVlanStatEnableIndex"))
if mibBuilder.loadTexts: hwdot1qVlanStatStatusEntry.setStatus('mandatory')
hwdot1qVlanStatEnableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanStatEnableIndex.setStatus('mandatory')
hwdot1qVlanStatEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanStatEnableStatus.setStatus('mandatory')
mibBuilder.exportSymbols("HUAWEI-LswSMON-MIB", hwdot1qVlanStatEnableIndex=hwdot1qVlanStatEnableIndex, smonExtendObject=smonExtendObject, hwdot1qVlanStatNumber=hwdot1qVlanStatNumber, hwdot1qVlanStatStatusTable=hwdot1qVlanStatStatusTable, hwSmonExtend=hwSmonExtend, hwdot1qVlanStatEnableStatus=hwdot1qVlanStatEnableStatus, hwdot1qVlanStatStatusEntry=hwdot1qVlanStatStatusEntry)
