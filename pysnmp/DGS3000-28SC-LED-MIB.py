#
# PySNMP MIB module DGS3000-28SC-LED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS3000-28SC-LED-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:30:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, ObjectIdentity, Integer32, NotificationType, ModuleIdentity, Counter64, Unsigned32, TimeTicks, Bits, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "ObjectIdentity", "Integer32", "NotificationType", "ModuleIdentity", "Counter64", "Unsigned32", "TimeTicks", "Bits", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_Dgs3000Proj_DGS3000_28SCax, = mibBuilder.importSymbols("SWDGS3000PRIMGMT-MIB", "dlink-Dgs3000Proj-DGS3000-28SCax")
swLedMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4))
if mibBuilder.loadTexts: swLedMIB.setLastUpdated('201106100000Z')
if mibBuilder.loadTexts: swLedMIB.setOrganization('D-Link Corp.')
swLedMIBObject = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1))
swLedInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1, 1), )
if mibBuilder.loadTexts: swLedInfoTable.setStatus('current')
swLedInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1, 1, 1), ).setIndexNames((0, "DGS3000-28SC-LED-MIB", "swLedInfoUnitId"))
if mibBuilder.loadTexts: swLedInfoEntry.setStatus('current')
swLedInfoUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLedInfoUnitId.setStatus('current')
swLedInfoFrontPanelLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLedInfoFrontPanelLedStatus.setStatus('current')
mibBuilder.exportSymbols("DGS3000-28SC-LED-MIB", swLedInfoUnitId=swLedInfoUnitId, swLedInfoTable=swLedInfoTable, swLedMIBObject=swLedMIBObject, swLedInfoFrontPanelLedStatus=swLedInfoFrontPanelLedStatus, swLedMIB=swLedMIB, swLedInfoEntry=swLedInfoEntry, PYSNMP_MODULE_ID=swLedMIB)
