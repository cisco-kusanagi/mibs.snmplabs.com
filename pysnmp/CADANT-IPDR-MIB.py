#
# PySNMP MIB module CADANT-IPDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-IPDR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:28:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
cadExperimental, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadExperimental")
InetAddressIPv4or6, = mibBuilder.importSymbols("CADANT-TC", "InetAddressIPv4or6")
InetAddress, InetAddressType, InetPortNumber, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber", "InetAddressIPv4")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Integer32, iso, IpAddress, MibIdentifier, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "iso", "IpAddress", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter32")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
cadIpdrMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30))
cadIpdrMib.setRevisions(('2015-06-25 00:00', '2014-04-23 00:00', '2009-09-28 00:00', '2009-09-17 00:00', '2009-08-17 00:00', '2009-01-06 00:00', '2007-11-19 00:00', '2006-05-09 00:00', '2005-06-01 00:00',))
if mibBuilder.loadTexts: cadIpdrMib.setLastUpdated('201506250000Z')
if mibBuilder.loadTexts: cadIpdrMib.setOrganization('Arris International, Inc.')
cadIpdrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1))
cadIpdrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2))
cadIpdrExportEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrExportEnabled.setStatus('current')
cadIpdrQueryPort = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(4737)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrQueryPort.setStatus('current')
cadIpdrStreamingPort = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(4737)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrStreamingPort.setStatus('current')
cadIpdrDataAckWindow = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrDataAckWindow.setStatus('current')
cadIpdrDataAckTimeout = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrDataAckTimeout.setStatus('current')
cadIpdrKeepAliveInterval = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrKeepAliveInterval.setStatus('current')
cadIpdrExportAllCounts = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrExportAllCounts.setStatus('current')
cadIpdrExportCpeInfo = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrExportCpeInfo.setStatus('current')
cadIpdrSessionId = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrSessionId.setStatus('current')
cadIpdrExportMode = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpdrExportMode.setStatus('current')
cadIpdrCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11), )
if mibBuilder.loadTexts: cadIpdrCollectorTable.setStatus('current')
cadIpdrCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1), ).setIndexNames((0, "CADANT-IPDR-MIB", "cadIpdrCollectorPriority"), (0, "CADANT-IPDR-MIB", "cadIpdrCollectorIpAddress"))
if mibBuilder.loadTexts: cadIpdrCollectorEntry.setStatus('current')
cadIpdrCollectorPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1))
if mibBuilder.loadTexts: cadIpdrCollectorPriority.setStatus('current')
cadIpdrCollectorIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCollectorIpAddrType.setStatus('current')
cadIpdrCollectorIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 3), InetAddressIPv4or6())
if mibBuilder.loadTexts: cadIpdrCollectorIpAddress.setStatus('current')
cadIpdrCollectorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 4), InetPortNumber().clone(4737)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCollectorPort.setStatus('current')
cadIpdrCollectorActive = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCollectorActive.setStatus('current')
cadIpdrCollectorPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCollectorPrimary.setStatus('current')
cadIpdrCollectorOutIntRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCollectorOutIntRecs.setStatus('current')
cadIpdrCollectorOutStpRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCollectorOutStpRecs.setStatus('current')
cadIpdrCollectorSupIntRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCollectorSupIntRecs.setStatus('current')
cadIpdrCollectorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrCollectorStatus.setStatus('current')
cadIpdrReportCycleTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12), )
if mibBuilder.loadTexts: cadIpdrReportCycleTable.setStatus('current')
cadIpdrReportCycleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1), ).setIndexNames((0, "CADANT-IPDR-MIB", "cadIpdrReportStartHH"), (0, "CADANT-IPDR-MIB", "cadIpdrReportStartMM"))
if mibBuilder.loadTexts: cadIpdrReportCycleEntry.setStatus('current')
cadIpdrReportStartHH = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)))
if mibBuilder.loadTexts: cadIpdrReportStartHH.setStatus('current')
cadIpdrReportStartMM = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59)))
if mibBuilder.loadTexts: cadIpdrReportStartMM.setStatus('current')
cadIpdrReportInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 1440)).clone(60)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrReportInterval.setStatus('current')
cadIpdrReportOutIntRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrReportOutIntRecs.setStatus('current')
cadIpdrReportOutStpRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrReportOutStpRecs.setStatus('current')
cadIpdrReportSupIntRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrReportSupIntRecs.setStatus('current')
cadIpdrReportStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrReportStatus.setStatus('current')
cadIpdrServiceTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13), )
if mibBuilder.loadTexts: cadIpdrServiceTable.setStatus('current')
cadIpdrServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1), ).setIndexNames((0, "CADANT-IPDR-MIB", "cadIpdrServiceSessionId"))
if mibBuilder.loadTexts: cadIpdrServiceEntry.setStatus('current')
cadIpdrServiceSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1))
if mibBuilder.loadTexts: cadIpdrServiceSessionId.setStatus('current')
cadIpdrServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 13)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrServiceType.setStatus('current')
cadIpdrServiceMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrServiceMethod.setStatus('current')
cadIpdrServicePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrServicePriority.setStatus('current')
cadIpdrServiceDataAckWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(200)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrServiceDataAckWindow.setStatus('current')
cadIpdrServiceDataAckTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrServiceDataAckTimeout.setStatus('current')
cadIpdrServiceReportCycleSet = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrServiceReportCycleSet.setStatus('current')
cadIpdrServiceEvtPaceGap = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrServiceEvtPaceGap.setStatus('current')
cadIpdrServiceAllCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrServiceAllCounts.setStatus('current')
cadIpdrServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrServiceStatus.setStatus('current')
cadIpdrReportCycleSetTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14), )
if mibBuilder.loadTexts: cadIpdrReportCycleSetTable.setStatus('current')
cadIpdrReportCycleSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1), ).setIndexNames((0, "CADANT-IPDR-MIB", "cadIpdrReportCycleSetSet"), (0, "CADANT-IPDR-MIB", "cadIpdrReportCycleSetStartHH"), (0, "CADANT-IPDR-MIB", "cadIpdrReportCycleSetStartMM"))
if mibBuilder.loadTexts: cadIpdrReportCycleSetEntry.setStatus('current')
cadIpdrReportCycleSetSet = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1))
if mibBuilder.loadTexts: cadIpdrReportCycleSetSet.setStatus('current')
cadIpdrReportCycleSetStartHH = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)))
if mibBuilder.loadTexts: cadIpdrReportCycleSetStartHH.setStatus('current')
cadIpdrReportCycleSetStartMM = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59)))
if mibBuilder.loadTexts: cadIpdrReportCycleSetStartMM.setStatus('current')
cadIpdrReportCycleSetInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 1440)).clone(60)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrReportCycleSetInterval.setStatus('current')
cadIpdrReportCycleSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrReportCycleSetStatus.setStatus('current')
cadIpdrCountsTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15), )
if mibBuilder.loadTexts: cadIpdrCountsTable.setStatus('current')
cadIpdrCountsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1), ).setIndexNames((0, "CADANT-IPDR-MIB", "cadIpdrCountsSessionId"), (0, "CADANT-IPDR-MIB", "cadIpdrCountsCollectorPriority"), (0, "CADANT-IPDR-MIB", "cadIpdrCountsCollectorIpAddress"), (0, "CADANT-IPDR-MIB", "cadIpdrCountsStartHH"), (0, "CADANT-IPDR-MIB", "cadIpdrCountsStartMM"), (0, "CADANT-IPDR-MIB", "cadIpdrCountsAdhocIndex"))
if mibBuilder.loadTexts: cadIpdrCountsEntry.setStatus('current')
cadIpdrCountsSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1))
if mibBuilder.loadTexts: cadIpdrCountsSessionId.setStatus('current')
cadIpdrCountsCollectorPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1))
if mibBuilder.loadTexts: cadIpdrCountsCollectorPriority.setStatus('current')
cadIpdrCountsCollectorIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 3), InetAddressIPv4or6())
if mibBuilder.loadTexts: cadIpdrCountsCollectorIpAddress.setStatus('current')
cadIpdrCountsStartHH = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)))
if mibBuilder.loadTexts: cadIpdrCountsStartHH.setStatus('current')
cadIpdrCountsStartMM = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59)))
if mibBuilder.loadTexts: cadIpdrCountsStartMM.setStatus('current')
cadIpdrCountsAdhocIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: cadIpdrCountsAdhocIndex.setStatus('current')
cadIpdrCountsStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrCountsStartTime.setStatus('current')
cadIpdrCountsStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrCountsStopTime.setStatus('current')
cadIpdrCountsIntRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCountsIntRecs.setStatus('current')
cadIpdrCountsSupIntRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCountsSupIntRecs.setStatus('current')
cadIpdrCountsStartRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCountsStartRecs.setStatus('current')
cadIpdrCountsStopRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCountsStopRecs.setStatus('current')
cadIpdrCountsEventRecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrCountsEventRecs.setStatus('current')
cadIpdrCountsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrCountsStatus.setStatus('current')
cadIpdrSessionCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16), )
if mibBuilder.loadTexts: cadIpdrSessionCollectorTable.setStatus('current')
cadIpdrSessionCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1), ).setIndexNames((0, "CADANT-IPDR-MIB", "cadIpdrSessionCollectorSessionId"), (0, "CADANT-IPDR-MIB", "cadIpdrSessionCollectorPriority"), (0, "CADANT-IPDR-MIB", "cadIpdrSessionCollectorIpAddress"))
if mibBuilder.loadTexts: cadIpdrSessionCollectorEntry.setStatus('current')
cadIpdrSessionCollectorSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1))
if mibBuilder.loadTexts: cadIpdrSessionCollectorSessionId.setStatus('current')
cadIpdrSessionCollectorPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1))
if mibBuilder.loadTexts: cadIpdrSessionCollectorPriority.setStatus('current')
cadIpdrSessionCollectorIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrSessionCollectorIpAddrType.setStatus('current')
cadIpdrSessionCollectorIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 4), InetAddressIPv4or6())
if mibBuilder.loadTexts: cadIpdrSessionCollectorIpAddress.setStatus('current')
cadIpdrSessionCollectorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 5), InetPortNumber().clone(4737)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrSessionCollectorPort.setStatus('current')
cadIpdrSessionCollectorActive = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrSessionCollectorActive.setStatus('current')
cadIpdrSessionCollectorPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpdrSessionCollectorPrimary.setStatus('current')
cadIpdrSessionCollectorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIpdrSessionCollectorStatus.setStatus('current')
cadIpdrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 1))
cadIpdrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2))
cadIpdrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 1, 1)).setObjects(("CADANT-IPDR-MIB", "cadIpdrBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadIpdrMIBCompliance = cadIpdrMIBCompliance.setStatus('current')
cadIpdrBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 1)).setObjects(("CADANT-IPDR-MIB", "cadIpdrExportEnabled"), ("CADANT-IPDR-MIB", "cadIpdrQueryPort"), ("CADANT-IPDR-MIB", "cadIpdrStreamingPort"), ("CADANT-IPDR-MIB", "cadIpdrDataAckWindow"), ("CADANT-IPDR-MIB", "cadIpdrDataAckTimeout"), ("CADANT-IPDR-MIB", "cadIpdrKeepAliveInterval"), ("CADANT-IPDR-MIB", "cadIpdrExportAllCounts"), ("CADANT-IPDR-MIB", "cadIpdrExportCpeInfo"), ("CADANT-IPDR-MIB", "cadIpdrSessionId"), ("CADANT-IPDR-MIB", "cadIpdrExportMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadIpdrBasicGroup = cadIpdrBasicGroup.setStatus('current')
cadIpdrCollectorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 2)).setObjects(("CADANT-IPDR-MIB", "cadIpdrCollectorIpAddrType"), ("CADANT-IPDR-MIB", "cadIpdrCollectorPort"), ("CADANT-IPDR-MIB", "cadIpdrCollectorActive"), ("CADANT-IPDR-MIB", "cadIpdrCollectorPrimary"), ("CADANT-IPDR-MIB", "cadIpdrCollectorOutIntRecs"), ("CADANT-IPDR-MIB", "cadIpdrCollectorOutStpRecs"), ("CADANT-IPDR-MIB", "cadIpdrCollectorSupIntRecs"), ("CADANT-IPDR-MIB", "cadIpdrCollectorStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadIpdrCollectorGroup = cadIpdrCollectorGroup.setStatus('current')
cadIpdrReportGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 3)).setObjects(("CADANT-IPDR-MIB", "cadIpdrReportOutIntRecs"), ("CADANT-IPDR-MIB", "cadIpdrReportOutStpRecs"), ("CADANT-IPDR-MIB", "cadIpdrReportSupIntRecs"), ("CADANT-IPDR-MIB", "cadIpdrReportStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadIpdrReportGroup = cadIpdrReportGroup.setStatus('current')
cadIpdrServiceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 4)).setObjects(("CADANT-IPDR-MIB", "cadIpdrServiceType"), ("CADANT-IPDR-MIB", "cadIpdrServiceMethod"), ("CADANT-IPDR-MIB", "cadIpdrServicePriority"), ("CADANT-IPDR-MIB", "cadIpdrServiceDataAckWindow"), ("CADANT-IPDR-MIB", "cadIpdrServiceDataAckTimeout"), ("CADANT-IPDR-MIB", "cadIpdrServiceReportCycleSet"), ("CADANT-IPDR-MIB", "cadIpdrServiceEvtPaceGap"), ("CADANT-IPDR-MIB", "cadIpdrServiceAllCounts"), ("CADANT-IPDR-MIB", "cadIpdrServiceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadIpdrServiceGroup = cadIpdrServiceGroup.setStatus('current')
cadIpdrReportCycleSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 5)).setObjects(("CADANT-IPDR-MIB", "cadIpdrReportCycleSetInterval"), ("CADANT-IPDR-MIB", "cadIpdrReportCycleSetStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadIpdrReportCycleSetGroup = cadIpdrReportCycleSetGroup.setStatus('current')
cadIpdrCountsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 6)).setObjects(("CADANT-IPDR-MIB", "cadIpdrCountsStartTime"), ("CADANT-IPDR-MIB", "cadIpdrCountsStopTime"), ("CADANT-IPDR-MIB", "cadIpdrCountsIntRecs"), ("CADANT-IPDR-MIB", "cadIpdrCountsSupIntRecs"), ("CADANT-IPDR-MIB", "cadIpdrCountsStartRecs"), ("CADANT-IPDR-MIB", "cadIpdrCountsStopRecs"), ("CADANT-IPDR-MIB", "cadIpdrCountsEventRecs"), ("CADANT-IPDR-MIB", "cadIpdrCountsStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadIpdrCountsGroup = cadIpdrCountsGroup.setStatus('current')
cadIpdrSessionCollectorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 7)).setObjects(("CADANT-IPDR-MIB", "cadIpdrSessionCollectorIpAddrType"), ("CADANT-IPDR-MIB", "cadIpdrSessionCollectorPort"), ("CADANT-IPDR-MIB", "cadIpdrSessionCollectorActive"), ("CADANT-IPDR-MIB", "cadIpdrSessionCollectorPrimary"), ("CADANT-IPDR-MIB", "cadIpdrSessionCollectorStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadIpdrSessionCollectorGroup = cadIpdrSessionCollectorGroup.setStatus('current')
mibBuilder.exportSymbols("CADANT-IPDR-MIB", cadIpdrCountsAdhocIndex=cadIpdrCountsAdhocIndex, cadIpdrReportCycleTable=cadIpdrReportCycleTable, cadIpdrServiceMethod=cadIpdrServiceMethod, cadIpdrServiceDataAckTimeout=cadIpdrServiceDataAckTimeout, cadIpdrQueryPort=cadIpdrQueryPort, cadIpdrCountsCollectorPriority=cadIpdrCountsCollectorPriority, cadIpdrSessionCollectorActive=cadIpdrSessionCollectorActive, cadIpdrExportAllCounts=cadIpdrExportAllCounts, cadIpdrReportCycleSetStartMM=cadIpdrReportCycleSetStartMM, cadIpdrReportCycleSetTable=cadIpdrReportCycleSetTable, cadIpdrCountsStartMM=cadIpdrCountsStartMM, cadIpdrKeepAliveInterval=cadIpdrKeepAliveInterval, cadIpdrSessionCollectorGroup=cadIpdrSessionCollectorGroup, cadIpdrReportCycleSetGroup=cadIpdrReportCycleSetGroup, cadIpdrSessionCollectorIpAddrType=cadIpdrSessionCollectorIpAddrType, cadIpdrReportInterval=cadIpdrReportInterval, cadIpdrCountsEventRecs=cadIpdrCountsEventRecs, cadIpdrReportCycleSetStartHH=cadIpdrReportCycleSetStartHH, cadIpdrExportMode=cadIpdrExportMode, cadIpdrServiceAllCounts=cadIpdrServiceAllCounts, cadIpdrCollectorPriority=cadIpdrCollectorPriority, cadIpdrServiceSessionId=cadIpdrServiceSessionId, cadIpdrCountsGroup=cadIpdrCountsGroup, cadIpdrCollectorSupIntRecs=cadIpdrCollectorSupIntRecs, cadIpdrMib=cadIpdrMib, cadIpdrCollectorPort=cadIpdrCollectorPort, cadIpdrCollectorPrimary=cadIpdrCollectorPrimary, cadIpdrCountsTable=cadIpdrCountsTable, cadIpdrReportOutIntRecs=cadIpdrReportOutIntRecs, cadIpdrMIBConformance=cadIpdrMIBConformance, cadIpdrCountsSessionId=cadIpdrCountsSessionId, cadIpdrExportCpeInfo=cadIpdrExportCpeInfo, cadIpdrSessionCollectorPriority=cadIpdrSessionCollectorPriority, cadIpdrExportEnabled=cadIpdrExportEnabled, cadIpdrBasicGroup=cadIpdrBasicGroup, cadIpdrReportStartHH=cadIpdrReportStartHH, cadIpdrCountsStopRecs=cadIpdrCountsStopRecs, cadIpdrServiceStatus=cadIpdrServiceStatus, cadIpdrReportCycleSetStatus=cadIpdrReportCycleSetStatus, cadIpdrCountsStartRecs=cadIpdrCountsStartRecs, cadIpdrStreamingPort=cadIpdrStreamingPort, cadIpdrCollectorOutIntRecs=cadIpdrCollectorOutIntRecs, cadIpdrCountsStartHH=cadIpdrCountsStartHH, cadIpdrCountsIntRecs=cadIpdrCountsIntRecs, cadIpdrServiceEntry=cadIpdrServiceEntry, cadIpdrSessionCollectorStatus=cadIpdrSessionCollectorStatus, cadIpdrMIBGroups=cadIpdrMIBGroups, cadIpdrDataAckWindow=cadIpdrDataAckWindow, cadIpdrReportCycleSetEntry=cadIpdrReportCycleSetEntry, cadIpdrCollectorStatus=cadIpdrCollectorStatus, cadIpdrMIBCompliance=cadIpdrMIBCompliance, PYSNMP_MODULE_ID=cadIpdrMib, cadIpdrServiceGroup=cadIpdrServiceGroup, cadIpdrReportSupIntRecs=cadIpdrReportSupIntRecs, cadIpdrCountsStatus=cadIpdrCountsStatus, cadIpdrCountsStopTime=cadIpdrCountsStopTime, cadIpdrCollectorTable=cadIpdrCollectorTable, cadIpdrReportCycleSetSet=cadIpdrReportCycleSetSet, cadIpdrServiceTable=cadIpdrServiceTable, cadIpdrMIBObjects=cadIpdrMIBObjects, cadIpdrSessionCollectorIpAddress=cadIpdrSessionCollectorIpAddress, cadIpdrCollectorEntry=cadIpdrCollectorEntry, cadIpdrCollectorIpAddress=cadIpdrCollectorIpAddress, cadIpdrSessionCollectorSessionId=cadIpdrSessionCollectorSessionId, cadIpdrServiceReportCycleSet=cadIpdrServiceReportCycleSet, cadIpdrReportOutStpRecs=cadIpdrReportOutStpRecs, cadIpdrReportStartMM=cadIpdrReportStartMM, cadIpdrCountsSupIntRecs=cadIpdrCountsSupIntRecs, cadIpdrDataAckTimeout=cadIpdrDataAckTimeout, cadIpdrCountsCollectorIpAddress=cadIpdrCountsCollectorIpAddress, cadIpdrSessionCollectorPort=cadIpdrSessionCollectorPort, cadIpdrReportStatus=cadIpdrReportStatus, cadIpdrServiceType=cadIpdrServiceType, cadIpdrReportCycleSetInterval=cadIpdrReportCycleSetInterval, cadIpdrServiceEvtPaceGap=cadIpdrServiceEvtPaceGap, cadIpdrReportCycleEntry=cadIpdrReportCycleEntry, cadIpdrCountsStartTime=cadIpdrCountsStartTime, cadIpdrMIBCompliances=cadIpdrMIBCompliances, cadIpdrCollectorOutStpRecs=cadIpdrCollectorOutStpRecs, cadIpdrServicePriority=cadIpdrServicePriority, cadIpdrCollectorActive=cadIpdrCollectorActive, cadIpdrSessionCollectorPrimary=cadIpdrSessionCollectorPrimary, cadIpdrReportGroup=cadIpdrReportGroup, cadIpdrSessionId=cadIpdrSessionId, cadIpdrCollectorGroup=cadIpdrCollectorGroup, cadIpdrSessionCollectorEntry=cadIpdrSessionCollectorEntry, cadIpdrCollectorIpAddrType=cadIpdrCollectorIpAddrType, cadIpdrCountsEntry=cadIpdrCountsEntry, cadIpdrSessionCollectorTable=cadIpdrSessionCollectorTable, cadIpdrServiceDataAckWindow=cadIpdrServiceDataAckWindow)
