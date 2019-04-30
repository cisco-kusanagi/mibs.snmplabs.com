#
# PySNMP MIB module INT-SERV-GUARANTEED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INT-SERV-GUARANTEED-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
intSrv, = mibBuilder.importSymbols("INT-SERV-MIB", "intSrv")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Bits, Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Integer32, TimeTicks, ModuleIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Integer32", "TimeTicks", "ModuleIdentity", "NotificationType", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
intSrvGuaranteed = ModuleIdentity((1, 3, 6, 1, 2, 1, 52, 4))
if mibBuilder.loadTexts: intSrvGuaranteed.setLastUpdated('9511030500Z')
if mibBuilder.loadTexts: intSrvGuaranteed.setOrganization('IETF Integrated Services Working Group')
intSrvGuaranteedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 1))
intSrvGuaranteedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 2))
intSrvGuaranteedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 3))
intSrvGuaranteedIfTable = MibTable((1, 3, 6, 1, 2, 1, 52, 4, 1, 1), )
if mibBuilder.loadTexts: intSrvGuaranteedIfTable.setStatus('current')
intSrvGuaranteedIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvGuaranteedIfEntry.setStatus('current')
intSrvGuaranteedIfC = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfC.setStatus('current')
intSrvGuaranteedIfD = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfD.setStatus('current')
intSrvGuaranteedIfSlack = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfSlack.setStatus('current')
intSrvGuaranteedIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfStatus.setStatus('current')
intSrvGuaranteedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 3, 1))
intSrvGuaranteedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 3, 2))
intSrvGuaranteedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 4, 3, 2, 1)).setObjects(("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfAttribGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedCompliance = intSrvGuaranteedCompliance.setStatus('current')
intSrvGuaranteedIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 3, 1, 2)).setObjects(("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfC"), ("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfD"), ("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfSlack"), ("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedIfAttribGroup = intSrvGuaranteedIfAttribGroup.setStatus('current')
mibBuilder.exportSymbols("INT-SERV-GUARANTEED-MIB", intSrvGuaranteedCompliances=intSrvGuaranteedCompliances, intSrvGuaranteedIfStatus=intSrvGuaranteedIfStatus, intSrvGuaranteedIfAttribGroup=intSrvGuaranteedIfAttribGroup, intSrvGuaranteedIfD=intSrvGuaranteedIfD, intSrvGuaranteed=intSrvGuaranteed, intSrvGuaranteedIfSlack=intSrvGuaranteedIfSlack, intSrvGuaranteedIfTable=intSrvGuaranteedIfTable, intSrvGuaranteedGroups=intSrvGuaranteedGroups, intSrvGuaranteedObjects=intSrvGuaranteedObjects, intSrvGuaranteedCompliance=intSrvGuaranteedCompliance, intSrvGuaranteedConformance=intSrvGuaranteedConformance, intSrvGuaranteedNotifications=intSrvGuaranteedNotifications, intSrvGuaranteedIfC=intSrvGuaranteedIfC, intSrvGuaranteedIfEntry=intSrvGuaranteedIfEntry, PYSNMP_MODULE_ID=intSrvGuaranteed)
