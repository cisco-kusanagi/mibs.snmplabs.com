#
# PySNMP MIB module CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, IpAddress, Bits, Gauge32, ModuleIdentity, TimeTicks, Counter64, NotificationType, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "IpAddress", "Bits", "Gauge32", "ModuleIdentity", "TimeTicks", "Counter64", "NotificationType", "MibIdentifier", "Counter32")
TextualConvention, RowStatus, TimeStamp, StorageType, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TimeStamp", "StorageType", "TruthValue", "DisplayString")
ciscoL4L7moduleResourceLimitMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 480))
ciscoL4L7moduleResourceLimitMIB.setRevisions(('2013-02-20 00:00', '2012-09-20 00:00', '2011-06-10 00:00', '2011-04-15 00:00', '2010-12-06 00:00', '2008-03-07 00:00', '2008-02-07 00:00', '2006-06-19 00:00', '2005-08-05 00:00',))
if mibBuilder.loadTexts: ciscoL4L7moduleResourceLimitMIB.setLastUpdated('201302200000Z')
if mibBuilder.loadTexts: ciscoL4L7moduleResourceLimitMIB.setOrganization('Cisco Systems, Inc.')
ciscoL4L7ResourceLimitNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 480, 0))
ciscoL4L7ResourceLimitMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 480, 1))
ciscoResourceLimitMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 480, 2))
crlResource = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1))
crlNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 2))
crlNotificationOnlyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3))
class CiscoResourceClass(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CiscoResourceLimitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("all", 1), ("macAddresses", 2), ("concurrentConns", 3), ("mgmtConnections", 4), ("proxyConns", 5), ("probes", 6), ("stickyEntries", 7), ("natTranslations", 8), ("regexState", 9), ("aclMemory", 10), ("syslogBuffer", 11), ("ipReassemBuffer", 12), ("tcpOOOBuffer", 13), ("sslConnections", 14), ("hosts", 15), ("ipsecSessions", 16), ("asdmSessions", 17), ("sshSessions", 18), ("telnetSessions", 19), ("cpu", 20), ("memory", 21))

class CiscoRateLimitResourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("all", 1), ("arpRequestsXmt", 2), ("arpResponses", 3), ("bandwidth", 4), ("connections", 5), ("appInspections", 6), ("syslog", 7), ("sslBandwidth", 8), ("sslConnections", 9), ("mgmtBandwidth", 10), ("throughput", 11), ("missedMac", 12), ("httpCompression", 13))

class CiscoResourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))
    namedValues = NamedValues(("lMacAddresses", 1), ("lConcurrentConns", 2), ("lMgmtConnections", 3), ("lProxyConns", 4), ("lProbes", 5), ("lStickyEntries", 6), ("lNatTranslations", 7), ("lRegexState", 8), ("lAclMemory", 9), ("lIpReassemBuffer", 10), ("lSyslogBuffer", 11), ("lTcpOOOBuffer", 12), ("lSslConnections", 13), ("lHosts", 14), ("lIpsecSessions", 15), ("lAsdmSessions", 16), ("lSshSessions", 17), ("lTelnetSessions", 18), ("rlArpRequestsXmt", 19), ("rlArpResponses", 20), ("rlBandwidth", 21), ("rlConnections", 22), ("rlAppInspections", 23), ("rlSyslog", 24), ("rlSslBandwidth", 25), ("rlSslConnections", 26), ("rlMgmtBandwidth", 27), ("rlThroughput", 28), ("rlMissedMac", 29), ("rlHttpCompression", 30))

class CiscoBufferUtilPercentage(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10000)

ciscoL4L7ResourceClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1), )
if mibBuilder.loadTexts: ciscoL4L7ResourceClassTable.setStatus('current')
ciscoL4L7ResourceClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassName"))
if mibBuilder.loadTexts: ciscoL4L7ResourceClassEntry.setStatus('current')
crlResourceClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1, 1, 1), CiscoResourceClass())
if mibBuilder.loadTexts: crlResourceClassName.setStatus('current')
crlResourceClassStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlResourceClassStorageType.setStatus('current')
crlResourceClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlResourceClassRowStatus.setStatus('current')
ciscoL4L7ResourceLimitTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2), )
if mibBuilder.loadTexts: ciscoL4L7ResourceLimitTable.setStatus('current')
ciscoL4L7ResourceLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassName"), (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitType"))
if mibBuilder.loadTexts: ciscoL4L7ResourceLimitEntry.setStatus('current')
crlResourceLimitType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 2), CiscoResourceLimitType())
if mibBuilder.loadTexts: crlResourceLimitType.setStatus('current')
crlResourceLimitValueType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absolute", 1), ("percentage", 2))).clone('percentage')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlResourceLimitValueType.setStatus('current')
crlResourceLimitMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlResourceLimitMin.setStatus('current')
crlResourceLimitMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlResourceLimitMax.setStatus('current')
crlResourceLimitStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlResourceLimitStorageType.setStatus('current')
crlResourceLimitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlResourceLimitRowStatus.setStatus('current')
crlResourceLimitCurrentUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlResourceLimitCurrentUsage.setStatus('current')
crlResourceLimitPeakUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlResourceLimitPeakUsage.setStatus('current')
crlResourceLimitReqsDeniedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlResourceLimitReqsDeniedCount.setStatus('current')
ciscoL4L7ResourceRateLimitTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4), )
if mibBuilder.loadTexts: ciscoL4L7ResourceRateLimitTable.setStatus('current')
ciscoL4L7ResourceRateLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassName"), (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceType"))
if mibBuilder.loadTexts: ciscoL4L7ResourceRateLimitEntry.setStatus('current')
crlRateLimitResourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 1), CiscoRateLimitResourceType())
if mibBuilder.loadTexts: crlRateLimitResourceType.setStatus('current')
crlRateLimitResourceMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlRateLimitResourceMin.setStatus('current')
crlRateLimitResourceMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlRateLimitResourceMax.setStatus('current')
crlRateLimitResourceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlRateLimitResourceStorageType.setStatus('current')
crlRateLimitResourceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlRateLimitResourceRowStatus.setStatus('current')
crlRateLimitResourceCurrentUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlRateLimitResourceCurrentUsage.setStatus('current')
crlRateLimitResourcePeakUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlRateLimitResourcePeakUsage.setStatus('current')
crlRateLimitResourceReqsDeniedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlRateLimitResourceReqsDeniedCount.setStatus('current')
ciscoL4L7ResourceUsageSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5), )
if mibBuilder.loadTexts: ciscoL4L7ResourceUsageSummaryTable.setStatus('current')
ciscoL4L7ResourceUsageSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryType"))
if mibBuilder.loadTexts: ciscoL4L7ResourceUsageSummaryEntry.setStatus('current')
crlResourceSummaryType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 1), CiscoResourceType())
if mibBuilder.loadTexts: crlResourceSummaryType.setStatus('current')
crlResourceSummaryCurrentUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlResourceSummaryCurrentUsage.setStatus('current')
crlResourceSummaryPeakUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlResourceSummaryPeakUsage.setStatus('current')
crlResourceSummaryReqsDeniedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlResourceSummaryReqsDeniedCount.setStatus('current')
crlResourceSummaryLastClearedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crlResourceSummaryLastClearedTime.setStatus('current')
crlResourceSummaryStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlResourceSummaryStorageType.setStatus('current')
crlResourceSummaryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crlResourceSummaryRowStatus.setStatus('current')
ciscoL4L7BufferUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6), )
if mibBuilder.loadTexts: ciscoL4L7BufferUtilizationTable.setStatus('current')
ciscoL4L7BufferUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrNetworkProcessor"))
if mibBuilder.loadTexts: ciscoL4L7BufferUtilizationEntry.setStatus('current')
clrNetworkProcessor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: clrNetworkProcessor.setStatus('current')
crlBufferUsageValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 2), Gauge32()).setUnits('buffers').setMaxAccess("readonly")
if mibBuilder.loadTexts: crlBufferUsageValue.setStatus('current')
crlPercentageBufferUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 3), CiscoBufferUtilPercentage()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: crlPercentageBufferUsage.setStatus('current')
crlPercentageBufferUsageDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 4), SnmpAdminString()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: crlPercentageBufferUsageDisplay.setStatus('current')
crlExternalBufferUsageValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 5), Gauge32()).setUnits('buffers').setMaxAccess("readonly")
if mibBuilder.loadTexts: crlExternalBufferUsageValue.setStatus('current')
crlExternalPercentageBufferUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 6), CiscoBufferUtilPercentage()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: crlExternalPercentageBufferUsage.setStatus('current')
crlExternalPercentageBufferUsageDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 7), SnmpAdminString()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: crlExternalPercentageBufferUsageDisplay.setStatus('current')
ciscoL4L7NpCpuUtilTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 7), )
if mibBuilder.loadTexts: ciscoL4L7NpCpuUtilTable.setStatus('current')
ciscoL4L7NpCpuUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 7, 1), ).setIndexNames((0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrNetworkProcessor"))
if mibBuilder.loadTexts: ciscoL4L7NpCpuUtilEntry.setStatus('current')
clrNpCpuUtilizationAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 7, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clrNpCpuUtilizationAverage.setStatus('current')
clrResourceLimitReachedNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clrResourceLimitReachedNotifEnabled.setStatus('current')
clrResourceRateLimitReachedNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clrResourceRateLimitReachedNotifEnabled.setStatus('current')
crlNotifType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("risingHighThresh", 1), ("fallingMinThresh", 2), ("fallingWatermarkThresh", 3), ("risingWatermarkThresh", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifType.setStatus('current')
crlNotifContextOrSystem = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("system", 1), ("context", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifContextOrSystem.setStatus('current')
crlNotifContextName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifContextName.setStatus('current')
crlNotifCurrentUsagePcnt = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 4), Unsigned32()).setUnits('percent').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifCurrentUsagePcnt.setStatus('current')
crlNotifMaxThresholdPcnt = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifMaxThresholdPcnt.setStatus('current')
crlNotifWatermarkPcnt = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifWatermarkPcnt.setStatus('current')
crlNotifMinThresholdPcnt = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifMinThresholdPcnt.setStatus('current')
crlNotifSourceType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("virtualIP", 1), ("realServer", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifSourceType.setStatus('current')
crlNotifRealServerName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 9), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifRealServerName.setStatus('current')
crlNotifVirtualIPAddrType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 10), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifVirtualIPAddrType.setStatus('current')
crlNotifVirtualIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 11), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crlNotifVirtualIPAddress.setStatus('current')
clrResourceLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 1)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitValueType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMax"))
if mibBuilder.loadTexts: clrResourceLimitReached.setStatus('deprecated')
clrResourceRateLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 2)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMax"))
if mibBuilder.loadTexts: clrResourceRateLimitReached.setStatus('deprecated')
clrResourceLimitReachedNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 3)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitCurrentUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMax"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMin"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"))
if mibBuilder.loadTexts: clrResourceLimitReachedNotif.setStatus('deprecated')
clrResourceRateLimitReachedNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 4)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceCurrentUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMax"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMin"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"))
if mibBuilder.loadTexts: clrResourceRateLimitReachedNotif.setStatus('deprecated')
clrResourceRateLimitReachedNotifRev1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 5)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceCurrentUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMax"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMin"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifSourceType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifRealServerName"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddrType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddress"))
if mibBuilder.loadTexts: clrResourceRateLimitReachedNotifRev1.setStatus('current')
clrResourceLimitReachedNotifRev1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 6)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitCurrentUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMax"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMin"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifSourceType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifRealServerName"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddrType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddress"))
if mibBuilder.loadTexts: clrResourceLimitReachedNotifRev1.setStatus('current')
ciscoL4L7ResourceLimitConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 480, 3))
ciscoL4L7ResourceLimitCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1))
ciscoL4L7ResourceLimitGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2))
ciscoL4L7ResourceLimitCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 1)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceClassGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitCompliance = ciscoL4L7ResourceLimitCompliance.setStatus('deprecated')
ciscoL4L7ResourceLimitComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 2)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceClassGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifEnabledGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitComplianceRev1 = ciscoL4L7ResourceLimitComplianceRev1.setStatus('deprecated')
ciscoL4L7ResourceLimitComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 3)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceClassGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifEnabledGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceUsageSummaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitComplianceRev2 = ciscoL4L7ResourceLimitComplianceRev2.setStatus('deprecated')
ciscoL4L7ResourceLimitComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 4)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceClassGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7BufferUtilizationGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifEnabledGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceUsageSummaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitComplianceRev3 = ciscoL4L7ResourceLimitComplianceRev3.setStatus('deprecated')
ciscoL4L7ResourceLimitComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 5)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceClassGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7BufferUtilizationGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7NpCpuUtilizationGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifEnabledGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceUsageSummaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitComplianceRev4 = ciscoL4L7ResourceLimitComplianceRev4.setStatus('deprecated')
ciscoL4L7ResourceLimitComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 6)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceClassGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7BufferUtilizationGroupRev1"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7NpCpuUtilizationGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifEnabledGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceUsageSummaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitComplianceRev5 = ciscoL4L7ResourceLimitComplianceRev5.setStatus('deprecated')
ciscoL4L7ResourceLimitComplianceRev6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 7)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceClassGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7BufferUtilizationGroupRev1"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7NpCpuUtilizationGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifEnabledGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceUsageSummaryGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifOnlyObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitComplianceRev6 = ciscoL4L7ResourceLimitComplianceRev6.setStatus('deprecated')
ciscoL4L7ResourceLimitComplianceRev7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 8)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceClassGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7BufferUtilizationGroupRev1"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7NpCpuUtilizationGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceRateLimitUsageGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifEnabledGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceUsageSummaryGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifOnlyObjectsGroup"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifOnlyObjectsGroupExt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "ciscoL4L7ResourceNotifGroupRev2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitComplianceRev7 = ciscoL4L7ResourceLimitComplianceRev7.setStatus('current')
ciscoL4L7ResourceClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 1)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassStorageType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceClassGroup = ciscoL4L7ResourceClassGroup.setStatus('current')
ciscoL4L7ResourceLimitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 2)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitValueType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMin"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMax"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitStorageType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitGroup = ciscoL4L7ResourceLimitGroup.setStatus('current')
ciscoL4L7ResourceRateLimitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 3)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMin"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMax"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceStorageType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceRateLimitGroup = ciscoL4L7ResourceRateLimitGroup.setStatus('current')
ciscoL4L7ResourceLimitUsageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 4)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitCurrentUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitPeakUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitReqsDeniedCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceLimitUsageGroup = ciscoL4L7ResourceLimitUsageGroup.setStatus('current')
ciscoL4L7ResourceRateLimitUsageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 5)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceCurrentUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourcePeakUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceReqsDeniedCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceRateLimitUsageGroup = ciscoL4L7ResourceRateLimitUsageGroup.setStatus('current')
ciscoL4L7ResourceNotifEnabledGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 6)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceLimitReachedNotifEnabled"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceRateLimitReachedNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceNotifEnabledGroup = ciscoL4L7ResourceNotifEnabledGroup.setStatus('current')
ciscoL4L7ResourceNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 7)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceLimitReached"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceRateLimitReached"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceNotifGroup = ciscoL4L7ResourceNotifGroup.setStatus('deprecated')
ciscoL4L7ResourceUsageSummaryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 8)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryCurrentUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryPeakUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryReqsDeniedCount"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryLastClearedTime"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryStorageType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceUsageSummaryGroup = ciscoL4L7ResourceUsageSummaryGroup.setStatus('current')
ciscoL4L7BufferUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 9)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlBufferUsageValue"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlPercentageBufferUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlPercentageBufferUsageDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7BufferUtilizationGroup = ciscoL4L7BufferUtilizationGroup.setStatus('deprecated')
ciscoL4L7NpCpuUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 10)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrNpCpuUtilizationAverage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7NpCpuUtilizationGroup = ciscoL4L7NpCpuUtilizationGroup.setStatus('current')
ciscoL4L7BufferUtilizationGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 11)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlBufferUsageValue"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlPercentageBufferUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlPercentageBufferUsageDisplay"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlExternalBufferUsageValue"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlExternalPercentageBufferUsage"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlExternalPercentageBufferUsageDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7BufferUtilizationGroupRev1 = ciscoL4L7BufferUtilizationGroupRev1.setStatus('current')
ciscoL4L7ResourceNotifGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 12)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceLimitReachedNotif"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceRateLimitReachedNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceNotifGroupRev1 = ciscoL4L7ResourceNotifGroupRev1.setStatus('deprecated')
ciscoL4L7ResourceNotifOnlyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 13)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceNotifOnlyObjectsGroup = ciscoL4L7ResourceNotifOnlyObjectsGroup.setStatus('current')
ciscoL4L7ResourceNotifGroupRev2 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 14)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceLimitReachedNotifRev1"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceRateLimitReachedNotifRev1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceNotifGroupRev2 = ciscoL4L7ResourceNotifGroupRev2.setStatus('current')
ciscoL4L7ResourceNotifOnlyObjectsGroupExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 15)).setObjects(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifSourceType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifRealServerName"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddrType"), ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL4L7ResourceNotifOnlyObjectsGroupExt = ciscoL4L7ResourceNotifOnlyObjectsGroupExt.setStatus('current')
mibBuilder.exportSymbols("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", CiscoRateLimitResourceType=CiscoRateLimitResourceType, crlResourceClassName=crlResourceClassName, ciscoL4L7ResourceLimitComplianceRev4=ciscoL4L7ResourceLimitComplianceRev4, clrResourceLimitReachedNotif=clrResourceLimitReachedNotif, ciscoL4L7BufferUtilizationTable=ciscoL4L7BufferUtilizationTable, ciscoL4L7ResourceRateLimitTable=ciscoL4L7ResourceRateLimitTable, clrResourceRateLimitReachedNotifEnabled=clrResourceRateLimitReachedNotifEnabled, CiscoBufferUtilPercentage=CiscoBufferUtilPercentage, ciscoResourceLimitMIBConform=ciscoResourceLimitMIBConform, clrNpCpuUtilizationAverage=clrNpCpuUtilizationAverage, ciscoL4L7NpCpuUtilizationGroup=ciscoL4L7NpCpuUtilizationGroup, ciscoL4L7ResourceNotifGroup=ciscoL4L7ResourceNotifGroup, crlExternalPercentageBufferUsageDisplay=crlExternalPercentageBufferUsageDisplay, ciscoL4L7ResourceNotifOnlyObjectsGroup=ciscoL4L7ResourceNotifOnlyObjectsGroup, ciscoL4L7ResourceNotifGroupRev1=ciscoL4L7ResourceNotifGroupRev1, crlNotifRealServerName=crlNotifRealServerName, crlPercentageBufferUsage=crlPercentageBufferUsage, crlNotifCurrentUsagePcnt=crlNotifCurrentUsagePcnt, clrResourceLimitReachedNotifEnabled=clrResourceLimitReachedNotifEnabled, crlNotifWatermarkPcnt=crlNotifWatermarkPcnt, crlPercentageBufferUsageDisplay=crlPercentageBufferUsageDisplay, ciscoL4L7ResourceUsageSummaryEntry=ciscoL4L7ResourceUsageSummaryEntry, crlResourceLimitMin=crlResourceLimitMin, crlBufferUsageValue=crlBufferUsageValue, ciscoL4L7ResourceLimitConformance=ciscoL4L7ResourceLimitConformance, ciscoL4L7ResourceLimitMIBObjects=ciscoL4L7ResourceLimitMIBObjects, ciscoL4L7ResourceNotifOnlyObjectsGroupExt=ciscoL4L7ResourceNotifOnlyObjectsGroupExt, ciscoL4L7ResourceClassEntry=ciscoL4L7ResourceClassEntry, crlNotifMinThresholdPcnt=crlNotifMinThresholdPcnt, ciscoL4L7ResourceLimitGroups=ciscoL4L7ResourceLimitGroups, ciscoL4L7ResourceRateLimitUsageGroup=ciscoL4L7ResourceRateLimitUsageGroup, crlExternalPercentageBufferUsage=crlExternalPercentageBufferUsage, ciscoL4L7ResourceLimitComplianceRev7=ciscoL4L7ResourceLimitComplianceRev7, CiscoResourceClass=CiscoResourceClass, crlNotificationOnlyObjects=crlNotificationOnlyObjects, clrResourceLimitReachedNotifRev1=clrResourceLimitReachedNotifRev1, clrNetworkProcessor=clrNetworkProcessor, crlExternalBufferUsageValue=crlExternalBufferUsageValue, ciscoL4L7ResourceLimitComplianceRev3=ciscoL4L7ResourceLimitComplianceRev3, ciscoL4L7BufferUtilizationGroupRev1=ciscoL4L7BufferUtilizationGroupRev1, crlNotifType=crlNotifType, ciscoL4L7ResourceRateLimitEntry=ciscoL4L7ResourceRateLimitEntry, crlNotifContextName=crlNotifContextName, ciscoL4L7ResourceUsageSummaryTable=ciscoL4L7ResourceUsageSummaryTable, PYSNMP_MODULE_ID=ciscoL4L7moduleResourceLimitMIB, crlResourceSummaryType=crlResourceSummaryType, crlResourceLimitValueType=crlResourceLimitValueType, crlResourceLimitRowStatus=crlResourceLimitRowStatus, clrResourceRateLimitReachedNotifRev1=clrResourceRateLimitReachedNotifRev1, ciscoL4L7ResourceLimitCompliances=ciscoL4L7ResourceLimitCompliances, ciscoL4L7ResourceLimitComplianceRev2=ciscoL4L7ResourceLimitComplianceRev2, ciscoL4L7ResourceLimitUsageGroup=ciscoL4L7ResourceLimitUsageGroup, ciscoL4L7ResourceClassGroup=ciscoL4L7ResourceClassGroup, ciscoL4L7ResourceUsageSummaryGroup=ciscoL4L7ResourceUsageSummaryGroup, crlNotifMaxThresholdPcnt=crlNotifMaxThresholdPcnt, ciscoL4L7ResourceLimitComplianceRev1=ciscoL4L7ResourceLimitComplianceRev1, crlRateLimitResourceReqsDeniedCount=crlRateLimitResourceReqsDeniedCount, ciscoL4L7ResourceNotifGroupRev2=ciscoL4L7ResourceNotifGroupRev2, crlNotifVirtualIPAddrType=crlNotifVirtualIPAddrType, crlResourceLimitReqsDeniedCount=crlResourceLimitReqsDeniedCount, ciscoL4L7NpCpuUtilTable=ciscoL4L7NpCpuUtilTable, crlResourceLimitPeakUsage=crlResourceLimitPeakUsage, crlResourceLimitType=crlResourceLimitType, ciscoL4L7ResourceLimitTable=ciscoL4L7ResourceLimitTable, crlRateLimitResourceStorageType=crlRateLimitResourceStorageType, crlRateLimitResourceType=crlRateLimitResourceType, crlRateLimitResourceMax=crlRateLimitResourceMax, ciscoL4L7ResourceClassTable=ciscoL4L7ResourceClassTable, crlResource=crlResource, ciscoL4L7BufferUtilizationEntry=ciscoL4L7BufferUtilizationEntry, crlRateLimitResourceRowStatus=crlRateLimitResourceRowStatus, ciscoL4L7ResourceLimitComplianceRev5=ciscoL4L7ResourceLimitComplianceRev5, clrResourceRateLimitReached=clrResourceRateLimitReached, CiscoResourceType=CiscoResourceType, ciscoL4L7ResourceLimitGroup=ciscoL4L7ResourceLimitGroup, ciscoL4L7BufferUtilizationGroup=ciscoL4L7BufferUtilizationGroup, crlResourceSummaryPeakUsage=crlResourceSummaryPeakUsage, crlResourceLimitStorageType=crlResourceLimitStorageType, crlResourceSummaryLastClearedTime=crlResourceSummaryLastClearedTime, ciscoL4L7ResourceLimitEntry=ciscoL4L7ResourceLimitEntry, crlResourceSummaryReqsDeniedCount=crlResourceSummaryReqsDeniedCount, crlRateLimitResourceMin=crlRateLimitResourceMin, crlResourceLimitCurrentUsage=crlResourceLimitCurrentUsage, clrResourceLimitReached=clrResourceLimitReached, crlResourceSummaryStorageType=crlResourceSummaryStorageType, CiscoResourceLimitType=CiscoResourceLimitType, crlNotifVirtualIPAddress=crlNotifVirtualIPAddress, crlResourceSummaryRowStatus=crlResourceSummaryRowStatus, clrResourceRateLimitReachedNotif=clrResourceRateLimitReachedNotif, ciscoL4L7NpCpuUtilEntry=ciscoL4L7NpCpuUtilEntry, crlResourceSummaryCurrentUsage=crlResourceSummaryCurrentUsage, crlRateLimitResourcePeakUsage=crlRateLimitResourcePeakUsage, crlRateLimitResourceCurrentUsage=crlRateLimitResourceCurrentUsage, ciscoL4L7ResourceLimitNotifs=ciscoL4L7ResourceLimitNotifs, crlResourceClassRowStatus=crlResourceClassRowStatus, ciscoL4L7ResourceRateLimitGroup=ciscoL4L7ResourceRateLimitGroup, ciscoL4L7moduleResourceLimitMIB=ciscoL4L7moduleResourceLimitMIB, ciscoL4L7ResourceLimitComplianceRev6=ciscoL4L7ResourceLimitComplianceRev6, crlResourceClassStorageType=crlResourceClassStorageType, crlNotificationObjects=crlNotificationObjects, crlNotifContextOrSystem=crlNotifContextOrSystem, ciscoL4L7ResourceNotifEnabledGroup=ciscoL4L7ResourceNotifEnabledGroup, crlResourceLimitMax=crlResourceLimitMax, crlNotifSourceType=crlNotifSourceType, ciscoL4L7ResourceLimitCompliance=ciscoL4L7ResourceLimitCompliance)
