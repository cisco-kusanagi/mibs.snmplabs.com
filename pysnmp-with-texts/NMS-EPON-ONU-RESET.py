#
# PySNMP MIB module NMS-EPON-ONU-RESET (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-ONU-RESET
# Produced by pysmi-0.3.4 at Wed May  1 14:21:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, MibIdentifier, IpAddress, iso, Integer32, Unsigned32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress", "iso", "Integer32", "Unsigned32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nmsEponOnuReset = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25))
nmsEponOnuResetTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1), )
if mibBuilder.loadTexts: nmsEponOnuResetTable.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEponOnuResetTable.setDescription('A list of the ONU reset table entries. The corresponding onu id will input and corresponding onu will reset.')
nmsEponOnuResetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1, 1), ).setIndexNames((0, "NMS-EPON-ONU-RESET", "onuLlid"))
if mibBuilder.loadTexts: nmsEponOnuResetEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEponOnuResetEntry.setDescription('A collection of certain ONU reset operation table entry. The ONU id can be reset through this table.')
onuLlid = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: onuLlid.setStatus('mandatory')
if mibBuilder.loadTexts: onuLlid.setDescription('ONU LLID.')
onuReset = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no_action", 0), ("reset", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuReset.setStatus('mandatory')
if mibBuilder.loadTexts: onuReset.setDescription('ONU reset operation.1-reset,0-no action.')
mibBuilder.exportSymbols("NMS-EPON-ONU-RESET", nmsEponOnuResetTable=nmsEponOnuResetTable, nmsEponOnuResetEntry=nmsEponOnuResetEntry, onuLlid=onuLlid, nmsEponOnuReset=nmsEponOnuReset, onuReset=onuReset)
