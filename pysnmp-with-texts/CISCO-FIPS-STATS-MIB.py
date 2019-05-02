#
# PySNMP MIB module CISCO-FIPS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FIPS-STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:58:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, Unsigned32, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Integer32, ModuleIdentity, Gauge32, Counter64, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Unsigned32", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Integer32", "ModuleIdentity", "Gauge32", "Counter64", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFipsStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 999999))
ciscoFipsStatsMIB.setRevisions(('2003-03-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFipsStatsMIB.setRevisionsDescriptions(('The initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setLastUpdated('200303100000Z')
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setContactInfo('Cisco Systems 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-fips-stats-mib@cisco.com')
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setDescription('The Federal Information Processing Standards (FIPS) power-up self-test status MIB module')
ciscoFipsStatsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 0))
ciscoFipsStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1))
ciscoFipsStatsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2))
cfipsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1))
cfipsStatsGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1))
cfipsPostStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("running", 1), ("passed", 2), ("failed", 3), ("notAvailable", 4))).clone('notAvailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfipsPostStatus.setStatus('current')
if mibBuilder.loadTexts: cfipsPostStatus.setDescription('Indicates whether or not the FIPS power-up self-test passed.')
ciscoFipsStatsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1))
ciscoFipsStatsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2))
ciscoFipsStatsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1, 1)).setObjects(("CISCO-FIPS-STATS-MIB", "ciscoFipsStatsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFipsStatsMIBCompliance = ciscoFipsStatsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoFipsStatsMIBCompliance.setDescription('The compliance statement for agents which implement the CISCO FIPs Status MIB.')
ciscoFipsStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2, 1)).setObjects(("CISCO-FIPS-STATS-MIB", "cfipsPostStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFipsStatsMIBGroup = ciscoFipsStatsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFipsStatsMIBGroup.setDescription('The objects for FIPS configuration.')
mibBuilder.exportSymbols("CISCO-FIPS-STATS-MIB", PYSNMP_MODULE_ID=ciscoFipsStatsMIB, cfipsStatsGlobal=cfipsStatsGlobal, ciscoFipsStatsMIBObjects=ciscoFipsStatsMIBObjects, ciscoFipsStatsMIBCompliance=ciscoFipsStatsMIBCompliance, ciscoFipsStatsMIBGroup=ciscoFipsStatsMIBGroup, cfipsPostStatus=cfipsPostStatus, ciscoFipsStatsMIBConform=ciscoFipsStatsMIBConform, ciscoFipsStatsMIB=ciscoFipsStatsMIB, cfipsStats=cfipsStats, ciscoFipsStatsMIBCompliances=ciscoFipsStatsMIBCompliances, ciscoFipsStatsMIBNotifs=ciscoFipsStatsMIBNotifs, ciscoFipsStatsMIBGroups=ciscoFipsStatsMIBGroups)
