#
# PySNMP MIB module NMS-EPON-ONU-BATCH-UPDATE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-ONU-BATCH-UPDATE
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Integer32, IpAddress, Counter32, TimeTicks, NotificationType, ModuleIdentity, Gauge32, Bits, Counter64, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Integer32", "IpAddress", "Counter32", "TimeTicks", "NotificationType", "ModuleIdentity", "Gauge32", "Bits", "Counter64", "ObjectIdentity", "iso")
TruthValue, RowStatus, DisplayString, TextualConvention, PhysAddress, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention", "PhysAddress", "MacAddress")
nmsEponOnuBatchUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23))
onuUpdateLLIDs = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 1), PortList()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuUpdateLLIDs.setStatus('mandatory')
onuUpdateFileName = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 2), OctetString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuUpdateFileName.setStatus('mandatory')
onuUpdateAction = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("no_action", 0), ("update", 1), ("commit", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuUpdateAction.setStatus('mandatory')
onuUpdateResult = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("success", 0), ("processing", 1), ("other", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuUpdateResult.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-ONU-BATCH-UPDATE", onuUpdateLLIDs=onuUpdateLLIDs, nmsEponOnuBatchUpdate=nmsEponOnuBatchUpdate, onuUpdateResult=onuUpdateResult, onuUpdateAction=onuUpdateAction, onuUpdateFileName=onuUpdateFileName)
