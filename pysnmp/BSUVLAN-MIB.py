#
# PySNMP MIB module BSUVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSUVLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, iso, ObjectIdentity, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32, Bits, NotificationType, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "iso", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32", "Bits", "NotificationType", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniBsuVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 11))
if mibBuilder.loadTexts: aniBsuVlan.setLastUpdated('0210251725Z')
if mibBuilder.loadTexts: aniBsuVlan.setOrganization('Aperto Networks')
aniBsuVlanConf = MibIdentifier((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1))
aniBsuVlanConfMgmtVlanId = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfMgmtVlanId.setStatus('current')
aniBsuVlanConfOuterTagId = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfOuterTagId.setStatus('current')
aniBsuVlanConfMgmtVlanIdPriority = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfMgmtVlanIdPriority.setStatus('current')
aniBsuVlanConfOuterTagPriority = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfOuterTagPriority.setStatus('current')
aniBsuVlanConfSUMgmtVlanIdList = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfSUMgmtVlanIdList.setStatus('current')
mibBuilder.exportSymbols("BSUVLAN-MIB", aniBsuVlanConfSUMgmtVlanIdList=aniBsuVlanConfSUMgmtVlanIdList, aniBsuVlanConfOuterTagPriority=aniBsuVlanConfOuterTagPriority, aniBsuVlanConf=aniBsuVlanConf, aniBsuVlanConfMgmtVlanId=aniBsuVlanConfMgmtVlanId, aniBsuVlanConfOuterTagId=aniBsuVlanConfOuterTagId, aniBsuVlanConfMgmtVlanIdPriority=aniBsuVlanConfMgmtVlanIdPriority, PYSNMP_MODULE_ID=aniBsuVlan, aniBsuVlan=aniBsuVlan)
