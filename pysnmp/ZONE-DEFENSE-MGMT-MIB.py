#
# PySNMP MIB module ZONE-DEFENSE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZONE-DEFENSE-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Gauge32, Bits, ModuleIdentity, iso, NotificationType, Counter32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Gauge32", "Bits", "ModuleIdentity", "iso", "NotificationType", "Counter32", "Integer32", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
swZoneDefenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 92))
if mibBuilder.loadTexts: swZoneDefenseMIB.setLastUpdated('1004120000Z')
if mibBuilder.loadTexts: swZoneDefenseMIB.setOrganization('D-Link Corp.')
swZoneDefenseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 92, 1))
swZoneDefenseTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1), )
if mibBuilder.loadTexts: swZoneDefenseTable.setStatus('current')
swZoneDefenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1, 1), ).setIndexNames((0, "ZONE-DEFENSE-MGMT-MIB", "swZoneDefenseAddress"))
if mibBuilder.loadTexts: swZoneDefenseEntry.setStatus('current')
swZoneDefenseAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: swZoneDefenseAddress.setStatus('current')
swZoneDefenseRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swZoneDefenseRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZONE-DEFENSE-MGMT-MIB", swZoneDefenseTable=swZoneDefenseTable, swZoneDefenseRowStatus=swZoneDefenseRowStatus, PYSNMP_MODULE_ID=swZoneDefenseMIB, swZoneDefenseAddress=swZoneDefenseAddress, swZoneDefenseMIBObjects=swZoneDefenseMIBObjects, swZoneDefenseMIB=swZoneDefenseMIB, swZoneDefenseEntry=swZoneDefenseEntry)
