#
# PySNMP MIB module INTEGRATED-SERVICES-GUARANTEED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEGRATED-SERVICES-GUARANTEED-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
intSrv, = mibBuilder.importSymbols("INTEGRATED-SERVICES-MIB", "intSrv")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, ModuleIdentity, iso, TimeTicks, Counter64, Gauge32, ObjectIdentity, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "iso", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "Integer32", "Bits")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
intSrvGuaranteed = ModuleIdentity((1, 3, 6, 1, 2, 1, 52, 5))
if mibBuilder.loadTexts: intSrvGuaranteed.setLastUpdated('9511030500Z')
if mibBuilder.loadTexts: intSrvGuaranteed.setOrganization('IETF Integrated Services Working Group')
intSrvGuaranteedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 1))
intSrvGuaranteedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 2))
intSrvGuaranteedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3))
intSrvGuaranteedIfTable = MibTable((1, 3, 6, 1, 2, 1, 52, 5, 1, 1), )
if mibBuilder.loadTexts: intSrvGuaranteedIfTable.setStatus('current')
intSrvGuaranteedIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvGuaranteedIfEntry.setStatus('current')
intSrvGuaranteedIfBacklog = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfBacklog.setStatus('current')
intSrvGuaranteedIfDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfDelay.setStatus('current')
intSrvGuaranteedIfSlack = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfSlack.setStatus('current')
intSrvGuaranteedIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfStatus.setStatus('current')
intSrvGuaranteedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3, 1))
intSrvGuaranteedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3, 2))
intSrvGuaranteedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 5, 3, 2, 1)).setObjects(("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfAttribGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedCompliance = intSrvGuaranteedCompliance.setStatus('current')
intSrvGuaranteedIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 5, 3, 1, 2)).setObjects(("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfBacklog"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfDelay"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfSlack"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedIfAttribGroup = intSrvGuaranteedIfAttribGroup.setStatus('current')
mibBuilder.exportSymbols("INTEGRATED-SERVICES-GUARANTEED-MIB", intSrvGuaranteedIfTable=intSrvGuaranteedIfTable, intSrvGuaranteedIfStatus=intSrvGuaranteedIfStatus, intSrvGuaranteedConformance=intSrvGuaranteedConformance, intSrvGuaranteedIfAttribGroup=intSrvGuaranteedIfAttribGroup, PYSNMP_MODULE_ID=intSrvGuaranteed, intSrvGuaranteedIfDelay=intSrvGuaranteedIfDelay, intSrvGuaranteedCompliances=intSrvGuaranteedCompliances, intSrvGuaranteedCompliance=intSrvGuaranteedCompliance, intSrvGuaranteedIfEntry=intSrvGuaranteedIfEntry, intSrvGuaranteed=intSrvGuaranteed, intSrvGuaranteedIfBacklog=intSrvGuaranteedIfBacklog, intSrvGuaranteedObjects=intSrvGuaranteedObjects, intSrvGuaranteedIfSlack=intSrvGuaranteedIfSlack, intSrvGuaranteedGroups=intSrvGuaranteedGroups, intSrvGuaranteedNotifications=intSrvGuaranteedNotifications)
