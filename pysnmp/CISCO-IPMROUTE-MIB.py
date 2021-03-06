#
# PySNMP MIB module CISCO-IPMROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPMROUTE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
ipMRouteInterfaceEntry, ipMRouteNextHopEntry, ipMRouteEntry = mibBuilder.importSymbols("IPMROUTE-STD-MIB", "ipMRouteInterfaceEntry", "ipMRouteNextHopEntry", "ipMRouteEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Gauge32, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Unsigned32, ObjectIdentity, Counter64, Bits, IpAddress, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Counter64", "Bits", "IpAddress", "ModuleIdentity", "TimeTicks")
TruthValue, TextualConvention, RowStatus, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString", "TimeStamp")
ciscoIpMRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 2))
ciscoIpMRouteMIB.setRevisions(('2005-03-07 00:00', '2000-12-22 00:00', '2000-05-15 00:00', '1999-02-08 00:00', '1996-10-11 00:00',))
if mibBuilder.loadTexts: ciscoIpMRouteMIB.setLastUpdated('200503070000Z')
if mibBuilder.loadTexts: ciscoIpMRouteMIB.setOrganization('ciscoSytems')
ciscoIpMRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 2, 1))
ciscoIpMRoute = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1))
ciscoIpMRouteNumberOfEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteNumberOfEntries.setStatus('current')
ciscoIpMRouteTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2), )
if mibBuilder.loadTexts: ciscoIpMRouteTable.setStatus('current')
ciscoIpMRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1), )
ipMRouteEntry.registerAugmentions(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteEntry"))
ciscoIpMRouteEntry.setIndexNames(*ipMRouteEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoIpMRouteEntry.setStatus('current')
ciscoIpMRoutePruneFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRoutePruneFlag.setStatus('current')
ciscoIpMRouteSparseFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteSparseFlag.setStatus('current')
ciscoIpMRouteConnectedFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteConnectedFlag.setStatus('current')
ciscoIpMRouteLocalFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteLocalFlag.setStatus('current')
ciscoIpMRouteRegisterFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteRegisterFlag.setStatus('current')
ciscoIpMRouteRpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteRpFlag.setStatus('current')
ciscoIpMRouteSptFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteSptFlag.setStatus('current')
ciscoIpMRouteBps = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteBps.setStatus('deprecated')
ciscoIpMRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteMetric.setStatus('deprecated')
ciscoIpMRouteMetricPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteMetricPreference.setStatus('current')
ciscoIpMRouteInLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('Kbits/second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteInLimit.setStatus('obsolete')
ciscoIpMRouteLastUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 23), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteLastUsed.setStatus('current')
ciscoIpMRouteInLimit2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 24), Gauge32()).setUnits('Kbits/second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteInLimit2.setStatus('current')
ciscoIpMRouteJoinFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 25), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteJoinFlag.setStatus('current')
ciscoIpMRouteMsdpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 26), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteMsdpFlag.setStatus('current')
ciscoIpMRouteProxyJoinFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 27), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteProxyJoinFlag.setStatus('current')
ciscoIpMRoutePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRoutePkts.setStatus('current')
ciscoIpMRouteDifferentInIfPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteDifferentInIfPkts.setStatus('current')
ciscoIpMRouteOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteOctets.setStatus('current')
ciscoIpMRouteBps2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 31), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteBps2.setStatus('current')
ciscoIpMRouteMetric2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 32), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteMetric2.setStatus('current')
ciscoIpMRouteNextHopTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3), )
if mibBuilder.loadTexts: ciscoIpMRouteNextHopTable.setStatus('current')
ciscoIpMRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3, 1), )
ipMRouteNextHopEntry.registerAugmentions(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopEntry"))
ciscoIpMRouteNextHopEntry.setIndexNames(*ipMRouteNextHopEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoIpMRouteNextHopEntry.setStatus('current')
ciscoIpMRouteNextHopOutLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3, 1, 9), Gauge32()).setUnits('Kbits/second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteNextHopOutLimit.setStatus('current')
ciscoIpMRouteNextHopMacHdr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteNextHopMacHdr.setStatus('current')
ciscoIpMRouteNextHopPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteNextHopPkts.setStatus('current')
ciscoIpMRouteHeartBeatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4), )
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatTable.setStatus('current')
ciscoIpMRouteHeartBeatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatGroupAddr"))
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatEntry.setStatus('current')
ciscoIpMRouteHeartBeatGroupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatGroupAddr.setStatus('current')
ciscoIpMRouteHeartBeatSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatSourceAddr.setStatus('current')
ciscoIpMRouteHeartBeatInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatInterval.setStatus('current')
ciscoIpMRouteHeartBeatWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatWindowSize.setStatus('current')
ciscoIpMRouteHeartBeatCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatCount.setStatus('current')
ciscoIpMRouteHeartBeatMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatMinimum.setStatus('current')
ciscoIpMRouteHeartBeatAlertTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatAlertTime.setStatus('current')
ciscoIpMRouteHeartBeatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoIpMRouteHeartBeatStatus.setStatus('current')
ciscoIpMRouteInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5), )
if mibBuilder.loadTexts: ciscoIpMRouteInterfaceTable.setStatus('current')
ciscoIpMRouteInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1), )
ipMRouteInterfaceEntry.registerAugmentions(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteInterfaceEntry"))
ciscoIpMRouteInterfaceEntry.setIndexNames(*ipMRouteInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoIpMRouteInterfaceEntry.setStatus('current')
ciscoIpMRouteIfInMcastOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteIfInMcastOctets.setStatus('current')
ciscoIpMRouteIfOutMcastOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteIfOutMcastOctets.setStatus('current')
ciscoIpMRouteIfInMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteIfInMcastPkts.setStatus('current')
ciscoIpMRouteIfHCInMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteIfHCInMcastPkts.setStatus('current')
ciscoIpMRouteIfOutMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteIfOutMcastPkts.setStatus('current')
ciscoIpMRouteIfHCOutMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoIpMRouteIfHCOutMcastPkts.setStatus('current')
ciscoIpMRouteNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 2, 3))
ciscoIpMRouteMissingHeartBeatsNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 2, 3, 1))
ciscoIpMRouteMissingHeartBeatsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 2, 3, 1, 0))
ciscoIpMRouteMissingHeartBeats = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 2, 3, 1, 0, 1)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatSourceAddr"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatInterval"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatWindowSize"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatCount"))
if mibBuilder.loadTexts: ciscoIpMRouteMissingHeartBeats.setStatus('current')
ciscoIpMRouteMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 2, 2))
ciscoIpMRouteMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1))
ciscoIpMRouteMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2))
ciscoIpMRouteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1, 1)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBCompliance = ciscoIpMRouteMIBCompliance.setStatus('obsolete')
ciscoIpMRouteMIBComplianceV11R01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1, 2)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMIBGroupV11R01"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBComplianceV11R01 = ciscoIpMRouteMIBComplianceV11R01.setStatus('deprecated')
ciscoIpMRouteMIBComplianceV12R00S = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1, 3)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMIBGroupV12R00S"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBComplianceV12R00S = ciscoIpMRouteMIBComplianceV12R00S.setStatus('deprecated')
ciscoIpMRouteMIBComplianceV12R28S = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1, 4)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMIBGroupV12R28S"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMIBIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBComplianceV12R28S = ciscoIpMRouteMIBComplianceV12R28S.setStatus('current')
ciscoIpMRouteMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 1)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePruneFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSparseFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteConnectedFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLocalFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRegisterFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRpFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSptFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteBps"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetric"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetricPreference"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteInLimit"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLastUsed"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopOutLimit"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopMacHdr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBGroup = ciscoIpMRouteMIBGroup.setStatus('obsolete')
ciscoIpMRouteMIBGroupV11R01 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 2)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePruneFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSparseFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteConnectedFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLocalFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRegisterFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRpFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSptFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteBps"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetric"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetricPreference"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLastUsed"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteInLimit2"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteJoinFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMsdpFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteProxyJoinFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopOutLimit"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopMacHdr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBGroupV11R01 = ciscoIpMRouteMIBGroupV11R01.setStatus('deprecated')
ciscoIpMRouteMIBHeartBeatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 3)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatSourceAddr"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatInterval"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatWindowSize"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatCount"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatMinimum"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatAlertTime"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBHeartBeatGroup = ciscoIpMRouteMIBHeartBeatGroup.setStatus('current')
ciscoIpMRouteMIBGroupV12R00S = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 4)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNumberOfEntries"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePruneFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSparseFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteConnectedFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLocalFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRegisterFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRpFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSptFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetricPreference"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLastUsed"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteInLimit2"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteJoinFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMsdpFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteProxyJoinFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePkts"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteDifferentInIfPkts"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteOctets"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteBps2"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetric2"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopOutLimit"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopMacHdr"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopPkts"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfInMcastOctets"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfOutMcastOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBGroupV12R00S = ciscoIpMRouteMIBGroupV12R00S.setStatus('deprecated')
ciscoIpMRouteMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 5)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMissingHeartBeats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBNotifGroup = ciscoIpMRouteMIBNotifGroup.setStatus('current')
ciscoIpMRouteMIBGroupV12R28S = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 6)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNumberOfEntries"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePruneFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSparseFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteConnectedFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLocalFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRegisterFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRpFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSptFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetricPreference"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLastUsed"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteInLimit2"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteJoinFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMsdpFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteProxyJoinFlag"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePkts"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteDifferentInIfPkts"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteOctets"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteBps2"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetric2"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopOutLimit"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopMacHdr"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBGroupV12R28S = ciscoIpMRouteMIBGroupV12R28S.setStatus('current')
ciscoIpMRouteMIBIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 7)).setObjects(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfInMcastOctets"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfOutMcastOctets"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfInMcastPkts"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfHCInMcastPkts"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfOutMcastPkts"), ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfHCOutMcastPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpMRouteMIBIfGroup = ciscoIpMRouteMIBIfGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPMROUTE-MIB", ciscoIpMRouteMIBGroup=ciscoIpMRouteMIBGroup, ciscoIpMRouteIfInMcastPkts=ciscoIpMRouteIfInMcastPkts, ciscoIpMRouteMIBNotifGroup=ciscoIpMRouteMIBNotifGroup, ciscoIpMRouteHeartBeatTable=ciscoIpMRouteHeartBeatTable, ciscoIpMRouteMissingHeartBeatsNotificationPrefix=ciscoIpMRouteMissingHeartBeatsNotificationPrefix, ciscoIpMRouteInterfaceEntry=ciscoIpMRouteInterfaceEntry, ciscoIpMRouteHeartBeatEntry=ciscoIpMRouteHeartBeatEntry, ciscoIpMRouteNextHopOutLimit=ciscoIpMRouteNextHopOutLimit, ciscoIpMRouteHeartBeatMinimum=ciscoIpMRouteHeartBeatMinimum, ciscoIpMRouteMIBCompliances=ciscoIpMRouteMIBCompliances, ciscoIpMRouteNextHopEntry=ciscoIpMRouteNextHopEntry, ciscoIpMRouteSparseFlag=ciscoIpMRouteSparseFlag, ciscoIpMRouteMIBGroupV12R28S=ciscoIpMRouteMIBGroupV12R28S, ciscoIpMRouteHeartBeatGroupAddr=ciscoIpMRouteHeartBeatGroupAddr, ciscoIpMRouteMIBComplianceV11R01=ciscoIpMRouteMIBComplianceV11R01, ciscoIpMRouteMIB=ciscoIpMRouteMIB, ciscoIpMRouteRpFlag=ciscoIpMRouteRpFlag, ciscoIpMRouteHeartBeatStatus=ciscoIpMRouteHeartBeatStatus, ciscoIpMRouteJoinFlag=ciscoIpMRouteJoinFlag, ciscoIpMRouteMIBHeartBeatGroup=ciscoIpMRouteMIBHeartBeatGroup, ciscoIpMRouteRegisterFlag=ciscoIpMRouteRegisterFlag, ciscoIpMRouteLocalFlag=ciscoIpMRouteLocalFlag, ciscoIpMRouteIfHCInMcastPkts=ciscoIpMRouteIfHCInMcastPkts, ciscoIpMRouteMissingHeartBeatsNotifications=ciscoIpMRouteMissingHeartBeatsNotifications, ciscoIpMRouteEntry=ciscoIpMRouteEntry, ciscoIpMRouteMIBCompliance=ciscoIpMRouteMIBCompliance, ciscoIpMRouteTable=ciscoIpMRouteTable, ciscoIpMRouteConnectedFlag=ciscoIpMRouteConnectedFlag, ciscoIpMRouteMetric=ciscoIpMRouteMetric, ciscoIpMRouteMetricPreference=ciscoIpMRouteMetricPreference, ciscoIpMRouteNumberOfEntries=ciscoIpMRouteNumberOfEntries, ciscoIpMRouteHeartBeatSourceAddr=ciscoIpMRouteHeartBeatSourceAddr, ciscoIpMRouteIfOutMcastOctets=ciscoIpMRouteIfOutMcastOctets, ciscoIpMRouteIfHCOutMcastPkts=ciscoIpMRouteIfHCOutMcastPkts, ciscoIpMRouteMIBComplianceV12R28S=ciscoIpMRouteMIBComplianceV12R28S, ciscoIpMRoutePruneFlag=ciscoIpMRoutePruneFlag, ciscoIpMRouteNotifications=ciscoIpMRouteNotifications, ciscoIpMRouteInterfaceTable=ciscoIpMRouteInterfaceTable, ciscoIpMRouteMIBGroups=ciscoIpMRouteMIBGroups, ciscoIpMRouteIfInMcastOctets=ciscoIpMRouteIfInMcastOctets, ciscoIpMRoutePkts=ciscoIpMRoutePkts, ciscoIpMRouteMIBGroupV11R01=ciscoIpMRouteMIBGroupV11R01, ciscoIpMRoute=ciscoIpMRoute, ciscoIpMRouteInLimit=ciscoIpMRouteInLimit, ciscoIpMRouteDifferentInIfPkts=ciscoIpMRouteDifferentInIfPkts, ciscoIpMRouteMissingHeartBeats=ciscoIpMRouteMissingHeartBeats, ciscoIpMRouteNextHopMacHdr=ciscoIpMRouteNextHopMacHdr, PYSNMP_MODULE_ID=ciscoIpMRouteMIB, ciscoIpMRouteNextHopPkts=ciscoIpMRouteNextHopPkts, ciscoIpMRouteMIBConformance=ciscoIpMRouteMIBConformance, ciscoIpMRouteHeartBeatInterval=ciscoIpMRouteHeartBeatInterval, ciscoIpMRouteMIBGroupV12R00S=ciscoIpMRouteMIBGroupV12R00S, ciscoIpMRouteMIBIfGroup=ciscoIpMRouteMIBIfGroup, ciscoIpMRouteBps2=ciscoIpMRouteBps2, ciscoIpMRouteMIBComplianceV12R00S=ciscoIpMRouteMIBComplianceV12R00S, ciscoIpMRouteOctets=ciscoIpMRouteOctets, ciscoIpMRouteHeartBeatWindowSize=ciscoIpMRouteHeartBeatWindowSize, ciscoIpMRouteHeartBeatAlertTime=ciscoIpMRouteHeartBeatAlertTime, ciscoIpMRouteNextHopTable=ciscoIpMRouteNextHopTable, ciscoIpMRouteIfOutMcastPkts=ciscoIpMRouteIfOutMcastPkts, ciscoIpMRouteProxyJoinFlag=ciscoIpMRouteProxyJoinFlag, ciscoIpMRouteInLimit2=ciscoIpMRouteInLimit2, ciscoIpMRouteHeartBeatCount=ciscoIpMRouteHeartBeatCount, ciscoIpMRouteMIBObjects=ciscoIpMRouteMIBObjects, ciscoIpMRouteSptFlag=ciscoIpMRouteSptFlag, ciscoIpMRouteMsdpFlag=ciscoIpMRouteMsdpFlag, ciscoIpMRouteMetric2=ciscoIpMRouteMetric2, ciscoIpMRouteBps=ciscoIpMRouteBps, ciscoIpMRouteLastUsed=ciscoIpMRouteLastUsed)
