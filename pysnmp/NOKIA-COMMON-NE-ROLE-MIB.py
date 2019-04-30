#
# PySNMP MIB module NOKIA-COMMON-NE-ROLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-COMMON-NE-ROLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ntcCommonMibs, = mibBuilder.importSymbols("NOKIA-COMMON-MIB-OID-REGISTRATION-MIB", "ntcCommonMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, ModuleIdentity, iso, Bits, Gauge32, NotificationType, Counter64, IpAddress, ObjectIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "ModuleIdentity", "iso", "Bits", "Gauge32", "NotificationType", "Counter64", "IpAddress", "ObjectIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netCommonNERole = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6))
coneRoleTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1), )
if mibBuilder.loadTexts: coneRoleTable.setStatus('mandatory')
coneRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1, 1), ).setIndexNames((0, "NOKIA-COMMON-NE-ROLE-MIB", "coneRoleIndex"))
if mibBuilder.loadTexts: coneRoleEntry.setStatus('mandatory')
coneRoleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coneRoleIndex.setStatus('mandatory')
coneRowIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coneRowIdx.setStatus('mandatory')
coneInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coneInfo.setStatus('mandatory')
mibBuilder.exportSymbols("NOKIA-COMMON-NE-ROLE-MIB", coneRoleIndex=coneRoleIndex, netCommonNERole=netCommonNERole, coneRowIdx=coneRowIdx, coneRoleEntry=coneRoleEntry, coneInfo=coneInfo, coneRoleTable=coneRoleTable)
