#
# PySNMP MIB module NMS-EPON-ONU-BATCH-UPDATE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-ONU-BATCH-UPDATE
# Produced by pysmi-0.3.4 at Wed May  1 14:21:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ObjectIdentity, TimeTicks, IpAddress, Counter64, ModuleIdentity, Integer32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ObjectIdentity", "TimeTicks", "IpAddress", "Counter64", "ModuleIdentity", "Integer32", "Gauge32", "iso")
RowStatus, TextualConvention, MacAddress, PhysAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "PhysAddress", "DisplayString", "TruthValue")
nmsEponOnuBatchUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23))
onuUpdateLLIDs = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 1), PortList()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuUpdateLLIDs.setStatus('mandatory')
if mibBuilder.loadTexts: onuUpdateLLIDs.setDescription('ONU LLID list, which defines the ONU to be updated.')
onuUpdateFileName = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 2), OctetString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuUpdateFileName.setStatus('mandatory')
if mibBuilder.loadTexts: onuUpdateFileName.setDescription('The file name in OLT flash, which is ONU bin file and must be existed.')
onuUpdateAction = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("no_action", 0), ("update", 1), ("commit", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuUpdateAction.setStatus('mandatory')
if mibBuilder.loadTexts: onuUpdateAction.setDescription('The update operation indication. 0-no action for update, 1-action for update.')
onuUpdateResult = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("success", 0), ("processing", 1), ("other", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuUpdateResult.setStatus('mandatory')
if mibBuilder.loadTexts: onuUpdateResult.setDescription('The result for update. 0-success, 1-processing, 2-other result values and reserved for system.')
mibBuilder.exportSymbols("NMS-EPON-ONU-BATCH-UPDATE", nmsEponOnuBatchUpdate=nmsEponOnuBatchUpdate, onuUpdateResult=onuUpdateResult, onuUpdateAction=onuUpdateAction, onuUpdateLLIDs=onuUpdateLLIDs, onuUpdateFileName=onuUpdateFileName)
