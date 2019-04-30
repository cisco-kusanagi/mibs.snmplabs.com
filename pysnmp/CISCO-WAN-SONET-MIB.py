#
# PySNMP MIB module CISCO-WAN-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-SONET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PerfIntervalCount, = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, TimeTicks, Gauge32, MibIdentifier, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, ObjectIdentity, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "TimeTicks", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "ObjectIdentity", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWANSonetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 3))
ciscoWANSonetMIB.setRevisions(('2002-05-20 00:00', '2000-03-06 00:00',))
if mibBuilder.loadTexts: ciscoWANSonetMIB.setLastUpdated('200205200000Z')
if mibBuilder.loadTexts: ciscoWANSonetMIB.setOrganization('Cisco Systems, Inc.')
ciscoWANSonetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 3, 1))
cwsSection = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1))
cwsLine = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2))
cwsPath = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3))
cwsSectionAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1), )
if mibBuilder.loadTexts: cwsSectionAlarmTable.setStatus('current')
cwsSectionAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwsSectionAlarmEntry.setStatus('current')
cwsSectionStatisticalAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("minor", 1), ("major", 2), ("none", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionStatisticalAlarmSeverity.setStatus('current')
cwsSectionCurrentESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionCurrentESsThreshold.setStatus('current')
cwsSectionTotalESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionTotalESsThreshold.setStatus('current')
cwsSectionCurrentSESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setUnits('severely errored seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionCurrentSESsThreshold.setStatus('current')
cwsSectionTotalSESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setUnits('severely errored seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionTotalSESsThreshold.setStatus('current')
cwsSectionCurrentSEFSsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setUnits('severely errored framing seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionCurrentSEFSsThreshold.setStatus('current')
cwsSectionTotalSEFSsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setUnits('severely errored framing seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionTotalSEFSsThreshold.setStatus('current')
cwsSectionCurrentCVsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(25)).setUnits('coding violations').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionCurrentCVsThreshold.setStatus('current')
cwsSectionTotalCVsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(25)).setUnits('coding violations').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionTotalCVsThreshold.setStatus('current')
cwsSectionStatAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 511))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsSectionStatAlarmStatus.setStatus('current')
cwsSectionCurrent24HrTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2), )
if mibBuilder.loadTexts: cwsSectionCurrent24HrTable.setStatus('current')
cwsSectionCurrent24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwsSectionCurrent24HrEntry.setStatus('current')
cwsSectionCurrent24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSectionCurrent24HrESs.setStatus('current')
cwsSectionCurrent24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1, 2), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSectionCurrent24HrSESs.setStatus('current')
cwsSectionCurrent24HrSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1, 3), PerfIntervalCount()).setUnits('severely errored framing seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSectionCurrent24HrSEFSs.setStatus('current')
cwsSectionCurrent24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1, 4), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSectionCurrent24HrCVs.setStatus('current')
cwsSectionPrevious24HrTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3), )
if mibBuilder.loadTexts: cwsSectionPrevious24HrTable.setStatus('current')
cwsSectionPrevious24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwsSectionPrevious24HrEntry.setStatus('current')
cwsSectionPrevious24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSectionPrevious24HrESs.setStatus('current')
cwsSectionPrevious24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1, 2), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSectionPrevious24HrSESs.setStatus('current')
cwsSectionPrevious24HrSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1, 3), PerfIntervalCount()).setUnits('severely errored framing seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSectionPrevious24HrSEFSs.setStatus('current')
cwsSectionPrevious24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1, 4), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSectionPrevious24HrCVs.setStatus('current')
cwsLineAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1), )
if mibBuilder.loadTexts: cwsLineAlarmTable.setStatus('current')
cwsLineAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwsLineAlarmEntry.setStatus('current')
cwsLineStatisticalAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("minor", 1), ("major", 2), ("none", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLineStatisticalAlarmSeverity.setStatus('current')
cwsLineCurrentESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLineCurrentESsThreshold.setStatus('current')
cwsLineTotalESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLineTotalESsThreshold.setStatus('current')
cwsLineCurrentSESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLineCurrentSESsThreshold.setStatus('current')
cwsLineTotalSESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLineTotalSESsThreshold.setStatus('current')
cwsLineCurrentCVsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLineCurrentCVsThreshold.setStatus('current')
cwsLineTotalCVsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLineTotalCVsThreshold.setStatus('current')
cwsLineCurrentUASsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLineCurrentUASsThreshold.setStatus('current')
cwsLineTotalUASsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLineTotalUASsThreshold.setStatus('current')
cwsLineStatAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLineStatAlarmStatus.setStatus('current')
cwsLineCurrent24HrTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2), )
if mibBuilder.loadTexts: cwsLineCurrent24HrTable.setStatus('current')
cwsLineCurrent24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwsLineCurrent24HrEntry.setStatus('current')
cwsLineCurrent24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLineCurrent24HrESs.setStatus('current')
cwsLineCurrent24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 2), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLineCurrent24HrSESs.setStatus('current')
cwsLineCurrent24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 3), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLineCurrent24HrCVs.setStatus('current')
cwsLineCurrent24HrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 4), PerfIntervalCount()).setUnits('Unavailable seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLineCurrent24HrUASs.setStatus('current')
cwsFELineCurrent24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFELineCurrent24HrESs.setStatus('current')
cwsFELineCurrent24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 6), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFELineCurrent24HrSESs.setStatus('current')
cwsFELineCurrent24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 7), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFELineCurrent24HrCVs.setStatus('current')
cwsFELineCurrent24HrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 8), PerfIntervalCount()).setUnits('Unavailable seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFELineCurrent24HrUASs.setStatus('current')
cwsLinePrevious24HrTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3), )
if mibBuilder.loadTexts: cwsLinePrevious24HrTable.setStatus('current')
cwsLinePrevious24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwsLinePrevious24HrEntry.setStatus('current')
cwsLinePrevious24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLinePrevious24HrESs.setStatus('current')
cwsLinePrevious24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 2), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLinePrevious24HrSESs.setStatus('current')
cwsLinePrevious24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 3), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLinePrevious24HrCVs.setStatus('current')
cwsLinePrevious24HrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 4), PerfIntervalCount()).setUnits('Unavailable seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLinePrevious24HrUASs.setStatus('current')
cwsFELinePrevious24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFELinePrevious24HrESs.setStatus('current')
cwsFELinePrevious24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 6), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFELinePrevious24HrSESs.setStatus('current')
cwsFELinePrevious24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 7), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFELinePrevious24HrCVs.setStatus('current')
cwsFELinePrevious24HrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 8), PerfIntervalCount()).setUnits('Unavailable seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFELinePrevious24HrUASs.setStatus('current')
cwsPathAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1), )
if mibBuilder.loadTexts: cwsPathAlarmTable.setStatus('current')
cwsPathAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwsPathAlarmEntry.setStatus('current')
cwsPathStatisticalAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("minor", 1), ("major", 2), ("none", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsPathStatisticalAlarmSeverity.setStatus('current')
cwsPathCurrentESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsPathCurrentESsThreshold.setStatus('current')
cwsPathTotalESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsPathTotalESsThreshold.setStatus('current')
cwsPathCurrentSESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsPathCurrentSESsThreshold.setStatus('current')
cwsPathTotalSESsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsPathTotalSESsThreshold.setStatus('current')
cwsPathCurrentCVsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(25)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsPathCurrentCVsThreshold.setStatus('current')
cwsPathTotalCVsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(25)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsPathTotalCVsThreshold.setStatus('current')
cwsPathCurrentUASsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsPathCurrentUASsThreshold.setStatus('current')
cwsPathTotalUASsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsPathTotalUASsThreshold.setStatus('current')
cwsPathStatAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPathStatAlarmStatus.setStatus('current')
cwsPathCurrent24HrTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2), )
if mibBuilder.loadTexts: cwsPathCurrent24HrTable.setStatus('current')
cwsPathCurrent24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwsPathCurrent24HrEntry.setStatus('current')
cwsPathCurrent24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPathCurrent24HrESs.setStatus('current')
cwsPathCurrent24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 2), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPathCurrent24HrSESs.setStatus('current')
cwsPathCurrent24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 3), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPathCurrent24HrCVs.setStatus('current')
cwsPathCurrent24HrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 4), PerfIntervalCount()).setUnits('Unavailable seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPathCurrent24HrUASs.setStatus('current')
cwsFEPathCurrent24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFEPathCurrent24HrESs.setStatus('current')
cwsFEPathCurrent24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 6), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFEPathCurrent24HrSESs.setStatus('current')
cwsFEPathCurrent24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 7), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFEPathCurrent24HrCVs.setStatus('current')
cwsFEPathCurrent24HrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 8), PerfIntervalCount()).setUnits('Unavailable seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFEPathCurrent24HrUASs.setStatus('current')
cwsPathPrevious24HrTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3), )
if mibBuilder.loadTexts: cwsPathPrevious24HrTable.setStatus('current')
cwsPathPrevious24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwsPathPrevious24HrEntry.setStatus('current')
cwsPathPrevious24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPathPrevious24HrESs.setStatus('current')
cwsPathPrevious24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 2), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPathPrevious24HrSESs.setStatus('current')
cwsPathPrevious24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 3), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPathPrevious24HrCVs.setStatus('current')
cwsPathPrevious24HrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 4), PerfIntervalCount()).setUnits('Unavailable seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPathPrevious24HrUASs.setStatus('current')
cwsFEPathPrevious24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFEPathPrevious24HrESs.setStatus('current')
cwsFEPathPrevious24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 6), PerfIntervalCount()).setUnits('severely errored seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFEPathPrevious24HrSESs.setStatus('current')
cwsFEPathPrevious24HrCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 7), PerfIntervalCount()).setUnits('coding violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFEPathPrevious24HrCVs.setStatus('current')
cwsFEPathPrevious24HrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 8), PerfIntervalCount()).setUnits('Unavailable seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsFEPathPrevious24HrUASs.setStatus('current')
ciscoWANSonetMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 3, 2))
ciscoWANSonetMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 1))
ciscoWANSonetMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2))
ciscoWANSonetMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 1, 1)).setObjects(("CISCO-WAN-SONET-MIB", "ciscoWANSonetSectAlarmMIBGroup"), ("CISCO-WAN-SONET-MIB", "ciscoWANSonetLineAlarmMIBGroup"), ("CISCO-WAN-SONET-MIB", "ciscoWANSonetPathAlarmMIBGroup"), ("CISCO-WAN-SONET-MIB", "ciscoWANSonetLinePrev24HrMIBGroup"), ("CISCO-WAN-SONET-MIB", "ciscoWANSonetFELineAlarmMIBGroup"), ("CISCO-WAN-SONET-MIB", "ciscoWANSonetFELinePrev24HrMIBGroup"), ("CISCO-WAN-SONET-MIB", "ciscoWANSonetPathPrev24HrMIBGroup"), ("CISCO-WAN-SONET-MIB", "ciscoWANSonetFEPathAlarmMIBGroup"), ("CISCO-WAN-SONET-MIB", "ciscoWANSonetFEPathPrev24HrMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetMIBCompliance = ciscoWANSonetMIBCompliance.setStatus('current')
ciscoWANSonetSectAlarmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 1)).setObjects(("CISCO-WAN-SONET-MIB", "cwsSectionStatisticalAlarmSeverity"), ("CISCO-WAN-SONET-MIB", "cwsSectionCurrentESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsSectionTotalESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsSectionCurrentSESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsSectionTotalSESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsSectionCurrentSEFSsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsSectionTotalSEFSsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsSectionCurrentCVsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsSectionTotalCVsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsSectionStatAlarmStatus"), ("CISCO-WAN-SONET-MIB", "cwsSectionCurrent24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsSectionCurrent24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsSectionCurrent24HrSEFSs"), ("CISCO-WAN-SONET-MIB", "cwsSectionCurrent24HrCVs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetSectAlarmMIBGroup = ciscoWANSonetSectAlarmMIBGroup.setStatus('current')
ciscoWANSonetSectPrev24HrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 2)).setObjects(("CISCO-WAN-SONET-MIB", "cwsSectionPrevious24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsSectionPrevious24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsSectionPrevious24HrSEFSs"), ("CISCO-WAN-SONET-MIB", "cwsSectionPrevious24HrCVs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetSectPrev24HrMIBGroup = ciscoWANSonetSectPrev24HrMIBGroup.setStatus('current')
ciscoWANSonetLineAlarmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 3)).setObjects(("CISCO-WAN-SONET-MIB", "cwsLineStatisticalAlarmSeverity"), ("CISCO-WAN-SONET-MIB", "cwsLineCurrentESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsLineTotalESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsLineCurrentSESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsLineTotalSESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsLineCurrentCVsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsLineTotalCVsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsLineCurrentUASsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsLineTotalUASsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsLineStatAlarmStatus"), ("CISCO-WAN-SONET-MIB", "cwsLineCurrent24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsLineCurrent24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsLineCurrent24HrCVs"), ("CISCO-WAN-SONET-MIB", "cwsLineCurrent24HrUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetLineAlarmMIBGroup = ciscoWANSonetLineAlarmMIBGroup.setStatus('current')
ciscoWANSonetFELineAlarmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 4)).setObjects(("CISCO-WAN-SONET-MIB", "cwsFELineCurrent24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsFELineCurrent24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsFELineCurrent24HrCVs"), ("CISCO-WAN-SONET-MIB", "cwsFELineCurrent24HrUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetFELineAlarmMIBGroup = ciscoWANSonetFELineAlarmMIBGroup.setStatus('current')
ciscoWANSonetLinePrev24HrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 5)).setObjects(("CISCO-WAN-SONET-MIB", "cwsLinePrevious24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsLinePrevious24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsLinePrevious24HrCVs"), ("CISCO-WAN-SONET-MIB", "cwsLinePrevious24HrUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetLinePrev24HrMIBGroup = ciscoWANSonetLinePrev24HrMIBGroup.setStatus('current')
ciscoWANSonetFELinePrev24HrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 6)).setObjects(("CISCO-WAN-SONET-MIB", "cwsFELinePrevious24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsFELinePrevious24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsFELinePrevious24HrCVs"), ("CISCO-WAN-SONET-MIB", "cwsFELinePrevious24HrUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetFELinePrev24HrMIBGroup = ciscoWANSonetFELinePrev24HrMIBGroup.setStatus('current')
ciscoWANSonetPathAlarmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 7)).setObjects(("CISCO-WAN-SONET-MIB", "cwsPathStatisticalAlarmSeverity"), ("CISCO-WAN-SONET-MIB", "cwsPathCurrentESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsPathTotalESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsPathCurrentSESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsPathTotalSESsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsPathCurrentCVsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsPathTotalCVsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsPathCurrentUASsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsPathTotalUASsThreshold"), ("CISCO-WAN-SONET-MIB", "cwsPathStatAlarmStatus"), ("CISCO-WAN-SONET-MIB", "cwsPathCurrent24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsPathCurrent24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsPathCurrent24HrCVs"), ("CISCO-WAN-SONET-MIB", "cwsPathCurrent24HrUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetPathAlarmMIBGroup = ciscoWANSonetPathAlarmMIBGroup.setStatus('current')
ciscoWANSonetFEPathAlarmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 8)).setObjects(("CISCO-WAN-SONET-MIB", "cwsFEPathCurrent24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsFEPathCurrent24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsFEPathCurrent24HrCVs"), ("CISCO-WAN-SONET-MIB", "cwsFEPathCurrent24HrUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetFEPathAlarmMIBGroup = ciscoWANSonetFEPathAlarmMIBGroup.setStatus('current')
ciscoWANSonetPathPrev24HrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 9)).setObjects(("CISCO-WAN-SONET-MIB", "cwsPathPrevious24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsPathPrevious24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsPathPrevious24HrCVs"), ("CISCO-WAN-SONET-MIB", "cwsPathPrevious24HrUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetPathPrev24HrMIBGroup = ciscoWANSonetPathPrev24HrMIBGroup.setStatus('current')
ciscoWANSonetFEPathPrev24HrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 10)).setObjects(("CISCO-WAN-SONET-MIB", "cwsFEPathPrevious24HrESs"), ("CISCO-WAN-SONET-MIB", "cwsFEPathPrevious24HrSESs"), ("CISCO-WAN-SONET-MIB", "cwsFEPathPrevious24HrCVs"), ("CISCO-WAN-SONET-MIB", "cwsFEPathPrevious24HrUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWANSonetFEPathPrev24HrMIBGroup = ciscoWANSonetFEPathPrev24HrMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-SONET-MIB", cwsLineStatAlarmStatus=cwsLineStatAlarmStatus, cwsLineCurrentCVsThreshold=cwsLineCurrentCVsThreshold, cwsLineCurrent24HrESs=cwsLineCurrent24HrESs, cwsPathPrevious24HrESs=cwsPathPrevious24HrESs, cwsPathPrevious24HrUASs=cwsPathPrevious24HrUASs, cwsLinePrevious24HrESs=cwsLinePrevious24HrESs, cwsFEPathCurrent24HrCVs=cwsFEPathCurrent24HrCVs, cwsFELinePrevious24HrESs=cwsFELinePrevious24HrESs, cwsLineCurrentSESsThreshold=cwsLineCurrentSESsThreshold, cwsFELinePrevious24HrUASs=cwsFELinePrevious24HrUASs, cwsPathAlarmTable=cwsPathAlarmTable, cwsSectionCurrentSEFSsThreshold=cwsSectionCurrentSEFSsThreshold, cwsFEPathCurrent24HrSESs=cwsFEPathCurrent24HrSESs, cwsSection=cwsSection, cwsPathPrevious24HrTable=cwsPathPrevious24HrTable, cwsLineAlarmEntry=cwsLineAlarmEntry, cwsLineCurrent24HrCVs=cwsLineCurrent24HrCVs, cwsSectionCurrent24HrCVs=cwsSectionCurrent24HrCVs, cwsLineCurrent24HrUASs=cwsLineCurrent24HrUASs, ciscoWANSonetMIBCompliance=ciscoWANSonetMIBCompliance, cwsSectionCurrent24HrEntry=cwsSectionCurrent24HrEntry, cwsSectionAlarmTable=cwsSectionAlarmTable, cwsSectionPrevious24HrSESs=cwsSectionPrevious24HrSESs, cwsFELineCurrent24HrUASs=cwsFELineCurrent24HrUASs, cwsSectionCurrentCVsThreshold=cwsSectionCurrentCVsThreshold, cwsFEPathPrevious24HrESs=cwsFEPathPrevious24HrESs, ciscoWANSonetMIBCompliances=ciscoWANSonetMIBCompliances, cwsPathPrevious24HrCVs=cwsPathPrevious24HrCVs, cwsFEPathPrevious24HrUASs=cwsFEPathPrevious24HrUASs, cwsFELineCurrent24HrCVs=cwsFELineCurrent24HrCVs, ciscoWANSonetSectAlarmMIBGroup=ciscoWANSonetSectAlarmMIBGroup, ciscoWANSonetMIBConformance=ciscoWANSonetMIBConformance, cwsSectionCurrent24HrSEFSs=cwsSectionCurrent24HrSEFSs, cwsLineCurrent24HrTable=cwsLineCurrent24HrTable, cwsSectionTotalCVsThreshold=cwsSectionTotalCVsThreshold, ciscoWANSonetMIBObjects=ciscoWANSonetMIBObjects, cwsSectionCurrent24HrTable=cwsSectionCurrent24HrTable, ciscoWANSonetPathAlarmMIBGroup=ciscoWANSonetPathAlarmMIBGroup, cwsSectionTotalSEFSsThreshold=cwsSectionTotalSEFSsThreshold, cwsPathCurrentUASsThreshold=cwsPathCurrentUASsThreshold, cwsPath=cwsPath, ciscoWANSonetSectPrev24HrMIBGroup=ciscoWANSonetSectPrev24HrMIBGroup, cwsPathStatAlarmStatus=cwsPathStatAlarmStatus, cwsLineTotalCVsThreshold=cwsLineTotalCVsThreshold, ciscoWANSonetFELinePrev24HrMIBGroup=ciscoWANSonetFELinePrev24HrMIBGroup, cwsPathCurrent24HrESs=cwsPathCurrent24HrESs, cwsLinePrevious24HrEntry=cwsLinePrevious24HrEntry, ciscoWANSonetLineAlarmMIBGroup=ciscoWANSonetLineAlarmMIBGroup, cwsPathTotalUASsThreshold=cwsPathTotalUASsThreshold, PYSNMP_MODULE_ID=ciscoWANSonetMIB, cwsLineAlarmTable=cwsLineAlarmTable, cwsSectionCurrent24HrESs=cwsSectionCurrent24HrESs, cwsPathCurrentSESsThreshold=cwsPathCurrentSESsThreshold, cwsLineCurrentESsThreshold=cwsLineCurrentESsThreshold, cwsPathCurrent24HrCVs=cwsPathCurrent24HrCVs, cwsLinePrevious24HrTable=cwsLinePrevious24HrTable, cwsPathCurrentESsThreshold=cwsPathCurrentESsThreshold, cwsFELinePrevious24HrCVs=cwsFELinePrevious24HrCVs, cwsLineCurrentUASsThreshold=cwsLineCurrentUASsThreshold, cwsSectionAlarmEntry=cwsSectionAlarmEntry, cwsSectionPrevious24HrESs=cwsSectionPrevious24HrESs, cwsSectionPrevious24HrCVs=cwsSectionPrevious24HrCVs, ciscoWANSonetPathPrev24HrMIBGroup=ciscoWANSonetPathPrev24HrMIBGroup, ciscoWANSonetMIBGroups=ciscoWANSonetMIBGroups, cwsLineCurrent24HrEntry=cwsLineCurrent24HrEntry, cwsSectionStatisticalAlarmSeverity=cwsSectionStatisticalAlarmSeverity, cwsLinePrevious24HrCVs=cwsLinePrevious24HrCVs, cwsFEPathPrevious24HrSESs=cwsFEPathPrevious24HrSESs, cwsSectionCurrent24HrSESs=cwsSectionCurrent24HrSESs, cwsPathStatisticalAlarmSeverity=cwsPathStatisticalAlarmSeverity, ciscoWANSonetFEPathPrev24HrMIBGroup=ciscoWANSonetFEPathPrev24HrMIBGroup, cwsLinePrevious24HrSESs=cwsLinePrevious24HrSESs, cwsLine=cwsLine, cwsSectionCurrentESsThreshold=cwsSectionCurrentESsThreshold, cwsSectionPrevious24HrEntry=cwsSectionPrevious24HrEntry, cwsFELinePrevious24HrSESs=cwsFELinePrevious24HrSESs, cwsPathCurrentCVsThreshold=cwsPathCurrentCVsThreshold, cwsPathCurrent24HrTable=cwsPathCurrent24HrTable, cwsLineTotalUASsThreshold=cwsLineTotalUASsThreshold, cwsLineTotalSESsThreshold=cwsLineTotalSESsThreshold, ciscoWANSonetFEPathAlarmMIBGroup=ciscoWANSonetFEPathAlarmMIBGroup, cwsPathTotalSESsThreshold=cwsPathTotalSESsThreshold, cwsPathAlarmEntry=cwsPathAlarmEntry, cwsFEPathCurrent24HrUASs=cwsFEPathCurrent24HrUASs, cwsPathTotalESsThreshold=cwsPathTotalESsThreshold, cwsSectionPrevious24HrSEFSs=cwsSectionPrevious24HrSEFSs, cwsFELineCurrent24HrESs=cwsFELineCurrent24HrESs, cwsSectionTotalESsThreshold=cwsSectionTotalESsThreshold, cwsSectionTotalSESsThreshold=cwsSectionTotalSESsThreshold, cwsLineTotalESsThreshold=cwsLineTotalESsThreshold, cwsLineCurrent24HrSESs=cwsLineCurrent24HrSESs, cwsPathCurrent24HrUASs=cwsPathCurrent24HrUASs, ciscoWANSonetLinePrev24HrMIBGroup=ciscoWANSonetLinePrev24HrMIBGroup, cwsPathCurrent24HrSESs=cwsPathCurrent24HrSESs, cwsSectionStatAlarmStatus=cwsSectionStatAlarmStatus, cwsLineStatisticalAlarmSeverity=cwsLineStatisticalAlarmSeverity, cwsFEPathPrevious24HrCVs=cwsFEPathPrevious24HrCVs, cwsPathPrevious24HrEntry=cwsPathPrevious24HrEntry, cwsPathPrevious24HrSESs=cwsPathPrevious24HrSESs, cwsSectionPrevious24HrTable=cwsSectionPrevious24HrTable, cwsPathCurrent24HrEntry=cwsPathCurrent24HrEntry, cwsSectionCurrentSESsThreshold=cwsSectionCurrentSESsThreshold, cwsPathTotalCVsThreshold=cwsPathTotalCVsThreshold, cwsFEPathCurrent24HrESs=cwsFEPathCurrent24HrESs, cwsFELineCurrent24HrSESs=cwsFELineCurrent24HrSESs, cwsLinePrevious24HrUASs=cwsLinePrevious24HrUASs, ciscoWANSonetMIB=ciscoWANSonetMIB, ciscoWANSonetFELineAlarmMIBGroup=ciscoWANSonetFELineAlarmMIBGroup)