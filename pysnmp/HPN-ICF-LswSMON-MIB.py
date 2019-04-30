#
# PySNMP MIB module HPN-ICF-LswSMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswSMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
hpnicfRhw, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfRhw")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, ObjectIdentity, TimeTicks, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Integer32, Gauge32, IpAddress, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Integer32", "Gauge32", "IpAddress", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26))
hpnicfsmonExtendObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1))
hpnicfdot1qVlanStatNumber = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qVlanStatNumber.setStatus('mandatory')
hpnicfdot1qVlanStatStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2), )
if mibBuilder.loadTexts: hpnicfdot1qVlanStatStatusTable.setStatus('mandatory')
hpnicfdot1qVlanStatStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-LswSMON-MIB", "hpnicfdot1qVlanStatEnableIndex"))
if mibBuilder.loadTexts: hpnicfdot1qVlanStatStatusEntry.setStatus('mandatory')
hpnicfdot1qVlanStatEnableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qVlanStatEnableIndex.setStatus('mandatory')
hpnicfdot1qVlanStatEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qVlanStatEnableStatus.setStatus('mandatory')
mibBuilder.exportSymbols("HPN-ICF-LswSMON-MIB", hpnicfdot1qVlanStatStatusEntry=hpnicfdot1qVlanStatStatusEntry, hpnicfdot1qVlanStatStatusTable=hpnicfdot1qVlanStatStatusTable, hpnicfdot1qVlanStatNumber=hpnicfdot1qVlanStatNumber, hpnicfsmonExtendObject=hpnicfsmonExtendObject, hpnicfdot1qVlanStatEnableIndex=hpnicfdot1qVlanStatEnableIndex, hpnicfSmonExtend=hpnicfSmonExtend, hpnicfdot1qVlanStatEnableStatus=hpnicfdot1qVlanStatEnableStatus)
