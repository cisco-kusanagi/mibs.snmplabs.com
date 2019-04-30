#
# PySNMP MIB module NMS-EPON-ONU-RESET (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-ONU-RESET
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, IpAddress, Integer32, Gauge32, ModuleIdentity, Unsigned32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "IpAddress", "Integer32", "Gauge32", "ModuleIdentity", "Unsigned32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nmsEponOnuReset = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25))
nmsEponOnuResetTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1), )
if mibBuilder.loadTexts: nmsEponOnuResetTable.setStatus('mandatory')
nmsEponOnuResetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1, 1), ).setIndexNames((0, "NMS-EPON-ONU-RESET", "onuLlid"))
if mibBuilder.loadTexts: nmsEponOnuResetEntry.setStatus('mandatory')
onuLlid = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: onuLlid.setStatus('mandatory')
onuReset = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no_action", 0), ("reset", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: onuReset.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-ONU-RESET", nmsEponOnuResetEntry=nmsEponOnuResetEntry, onuLlid=onuLlid, nmsEponOnuResetTable=nmsEponOnuResetTable, nmsEponOnuReset=nmsEponOnuReset, onuReset=onuReset)
