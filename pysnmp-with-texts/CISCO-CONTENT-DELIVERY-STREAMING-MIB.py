#
# PySNMP MIB module CISCO-CONTENT-DELIVERY-STREAMING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONTENT-DELIVERY-STREAMING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, ObjectIdentity, ModuleIdentity, Bits, IpAddress, MibIdentifier, Counter32, Integer32, iso, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Bits", "IpAddress", "MibIdentifier", "Counter32", "Integer32", "iso", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoContentDeliveryStreamingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 708))
ciscoContentDeliveryStreamingMIB.setRevisions(('2009-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoContentDeliveryStreamingMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoContentDeliveryStreamingMIB.setLastUpdated('200909300000Z')
if mibBuilder.loadTexts: ciscoContentDeliveryStreamingMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoContentDeliveryStreamingMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134-1706 USA Tel: +1 800 553-NETS E-mail: cs-cds@cisco.com')
if mibBuilder.loadTexts: ciscoContentDeliveryStreamingMIB.setDescription("This MIB instrumentation is for managing the Content Delivery and Streaming functionality on Cisco devices. Contents are ingested into content delivery network and then distributed to clients. There are two types of contents in content delivery network - live and VOD. VOD contents can be pre-positioned or dynamically cached into the content delivery network. Live stream is ingested and delivered to a large audience using one-to-many split. Streaming protocols are supported, by different streaming modules. These include HTTP, RTSP, Microsoft Media Server, RTMP and their varieties. ACRONYM: CDN Content Delivery Network FMS Flash Media Streaming HC High Capacity MS Movie Streamer RTMP Real Time Messaging Protocol VOD Video On Demand WMT Window Media Technology GLOSSARY: Dynamic cache Content is dynamically ingested into Content Delivery Network when the server does not find a client's requested content in its local hard disk storage. Origin Server The server on which all original copies of content reside. It locates outside the CDN. Pre-position The content is ingested into Content Delivery Network at or near the point of planned use to reduce reaction time, and to ensure timely response to requests during initial phase of an operation. Real Time Messaging Protocol A multimedia streaming and RPC protocol primarily used in Adobe Flash. Upstream Server Upstream server is a server that is located higher in the Content Delivery Network hierarchy.")
class CiscoCdsBandwidthUnitType(TextualConvention, Integer32):
    description = 'The unit of measurement for the bandwidth rate: bytesPerSec - number of bytes per second kiloBytesPerSec - number of kilobytes per second megaBytesPerSec - number of megabytes per second gigaBytesPerSec - number of gigabytes per second'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("bytesPerSec", 1), ("kiloBytesPerSec", 2), ("megaBytesPerSec", 3), ("gigaBytesPerSec", 4))

ciscoCdsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 708, 1))
ccdsStreamingModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1))
ccdsStreamingStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1), )
if mibBuilder.loadTexts: ccdsStreamingStatsTable.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsTable.setDescription('This table contains the general statistics information for all streaming modules in content delivery environment.')
ccdsStreamingStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsIndex"))
if mibBuilder.loadTexts: ccdsStreamingStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsEntry.setDescription("An entry (conceptual row) in the 'ccdsStreamingStatsTable'. Each row provides statistics for one streaming module or one live program. The ccdsStreamingStatsIndex identifies this entry. The ccdsStreamingStatsType indicates the entry type. If an entry represents a streaming module, it is created when the streaming module is enabled and delelted when the streaming module is disabled. If an entry represents a live program, it is created when the live program is added and deleted when the live program is removed.")
ccdsStreamingStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ccdsStreamingStatsIndex.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsIndex.setDescription("An arbitrary index number to represent a statistics entry for a given type of streaming module instance or a live program. The type of this entry is identified by the value of the corresponding instance of 'ccdsStreamingStatsType'. The agent creates a row in this table when the streaming module is enabled and destroys it when the streaming module is disabled. The instance identifier value usage/re-usage and its management is implementation specific.")
ccdsStreamingStatsDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsDescr.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsDescr.setDescription('This object indicates a human-readable string representing this streaming module instance or live program.')
ccdsStreamingStatsModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("http", 2), ("wmt", 3), ("ms", 4), ("fms", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsModuleType.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsModuleType.setDescription("This object indicates the type of this statistic table entry. 'unknown' - If the module type is unknown, it is a module not yet defined at MIB design time. This is for extension purpose. 'http' - This is a http module. 'wmt' - This is a windows media technology module. 'ms' - This is a movie streamer module. 'fms' - This is a flash media streaming module.")
ccdsStreamingStatsRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsRequests.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsRequests.setDescription("This object indicates the total number of end-user requests this streaming instance has received. The value of this object is sum total of the value of corresponding instance of 'ccdsStreamingStatsLiveRequests' and 'ccdsStreamingStatsVODRequests'.")
ccdsStreamingStatsLiveRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsLiveRequests.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsLiveRequests.setDescription('This object indicates the total number of end-user requests for live streams.')
ccdsStreamingStatsVODRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsVODRequests.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsVODRequests.setDescription('This object indicates the total number of end-user requests for Video On Demand contents.')
ccdsStreamingStatsPrepHitRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsPrepHitRequests.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsPrepHitRequests.setDescription('This object indicates the total number of end-user requests for which requested contents are pre-positioned into local cache beforehand. These requests are served from local cache.')
ccdsStreamingStatsCacheHitRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsCacheHitRequests.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsCacheHitRequests.setDescription('This object indicates the total number of end-user requests which are served from previously cached contents.')
ccdsStreamingStatsMissRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsMissRequests.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsMissRequests.setDescription('This object indicates the total number of end-user requests for which the requested contents are not available in local cache. These requests are either served by dynamically caching the content from origin server, or not served at all if the contents are not available on origin server.')
ccdsStreamingStatsClientErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsClientErrors.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsClientErrors.setDescription('This object indicates the total number of failed end-user requests due to errors from the client-side.')
ccdsStreamingStatsServerErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsServerErrors.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsServerErrors.setDescription('This object indicates the total number of failed end-user requests, due to errors encountered in either streaming module or upstream server, or the origin server.')
ccdsStreamingStatsBlockedRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsBlockedRequests.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsBlockedRequests.setDescription('This object indicates the total number of end-user requests blocked by this streaming module instance. Requests are refused and error response are sent. The reason might be one of, but not limited to, URL filtering, Authentication failure, or rule template match, etc.')
ccdsStreamingStatsServedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 13), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsServedBytes.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsServedBytes.setDescription("This object indicates the total number of bytes in the response served by this streaming module instance. The value of this object is same as the value of the corresponding instance of 'ccdsStreamingStatsHCServedBytes' (64 bit version), differing only in the capacity.")
ccdsStreamingStatsHCServedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 14), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsHCServedBytes.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsHCServedBytes.setDescription("This object indicates the total number of bytes in the response served by this streaming module instance. The value of this object is same as the value of the corresponding instance of 'ccdsStreamingStatsServedBytes' (32 bit version), differing only in the capacity.")
ccdsStreamingStatsLiveBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 15), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsLiveBytes.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsLiveBytes.setDescription("This object indicates total live stream bytes served by this streaming module instance. The value of this object is same as the value of the corresponding instance of 'ccdsStreamingStatsHCLiveBytes' (64 bit version), differing only in the capacity.")
ccdsStreamingStatsHCLiveBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 16), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsHCLiveBytes.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsHCLiveBytes.setDescription("This object indicates total live stream bytes served by this streaming module instance. The value of this object is same as the value of the corresponding instance of 'ccdsStreamingStatsLiveBytes' (32 bit version), differing only in the capacity.")
ccdsStreamingStatsVODBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 17), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsVODBytes.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsVODBytes.setDescription("This object indicates total bytes served for VOD requests, which are read from local cache, by this streaming module instance. The value of this object is same as the value of the corresponding instance of 'ccdsStreamingStatsHCVODBytes' (64 bit version), differing only in the capacity.")
ccdsStreamingStatsHCVODBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 18), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsHCVODBytes.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsHCVODBytes.setDescription("This object indicates total bytes served for VOD requests, which are read from local cache, by this streaming module instance. The value of this object is same as the value of the corresponding instance of 'ccdsStreamingStatsVODBytes' (32 bit version), differing only in the capacity.")
ccdsStreamingStatsBandwidthUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 19), CiscoCdsBandwidthUnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsBandwidthUnit.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsBandwidthUnit.setDescription("This object indicates the type unit for the bandwidth rate in the value of the corresponding instance of 'ccdsStreamingStatsBandwidthRate'.")
ccdsStreamingStatsBandwidthRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 20), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsBandwidthRate.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsBandwidthRate.setDescription('This object indicates the current bandwidth rate occupied by this streaming module instance.')
ccdsStreamingStatsConcurrentRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdsStreamingStatsConcurrentRequests.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsConcurrentRequests.setDescription('This object indicates the number of concurrent requests this streaming module instance is serving at current time.')
ciscoCdsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 708, 2))
ciscoCdsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 708, 2, 1))
ciscoCdsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 708, 2, 2))
ciscoCdsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 708, 2, 1, 1)).setObjects(("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdsMIBCompliance = ciscoCdsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCdsMIBCompliance.setDescription('The compliance statement for Cisco Systems entities which implement CISCO-CONTENT-DELIVERY-STREAMING-MIB.')
ccdsStreamingStatsGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 708, 2, 2, 1)).setObjects(("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsDescr"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsModuleType"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsRequests"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsClientErrors"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsServerErrors"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsBlockedRequests"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsPrepHitRequests"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsCacheHitRequests"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsMissRequests"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsLiveRequests"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsLiveBytes"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsHCLiveBytes"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsVODRequests"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsVODBytes"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsHCVODBytes"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsServedBytes"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsHCServedBytes"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsBandwidthUnit"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsBandwidthRate"), ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsConcurrentRequests"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccdsStreamingStatsGeneralGroup = ccdsStreamingStatsGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: ccdsStreamingStatsGeneralGroup.setDescription('A collection of objects providing general statistics information of streaming module.')
mibBuilder.exportSymbols("CISCO-CONTENT-DELIVERY-STREAMING-MIB", CiscoCdsBandwidthUnitType=CiscoCdsBandwidthUnitType, ccdsStreamingStatsCacheHitRequests=ccdsStreamingStatsCacheHitRequests, ccdsStreamingStatsVODBytes=ccdsStreamingStatsVODBytes, ccdsStreamingStatsVODRequests=ccdsStreamingStatsVODRequests, ccdsStreamingStatsLiveBytes=ccdsStreamingStatsLiveBytes, ccdsStreamingStatsBlockedRequests=ccdsStreamingStatsBlockedRequests, ciscoCdsMIBObjects=ciscoCdsMIBObjects, ccdsStreamingStatsServedBytes=ccdsStreamingStatsServedBytes, ccdsStreamingStatsEntry=ccdsStreamingStatsEntry, ciscoCdsMIBCompliances=ciscoCdsMIBCompliances, ccdsStreamingStatsRequests=ccdsStreamingStatsRequests, ccdsStreamingStatsBandwidthUnit=ccdsStreamingStatsBandwidthUnit, ccdsStreamingStatsClientErrors=ccdsStreamingStatsClientErrors, ccdsStreamingStatsServerErrors=ccdsStreamingStatsServerErrors, ccdsStreamingStatsHCServedBytes=ccdsStreamingStatsHCServedBytes, ciscoCdsMIBConformance=ciscoCdsMIBConformance, ccdsStreamingStatsModuleType=ccdsStreamingStatsModuleType, ccdsStreamingStatsMissRequests=ccdsStreamingStatsMissRequests, ccdsStreamingStatsDescr=ccdsStreamingStatsDescr, ccdsStreamingStatsTable=ccdsStreamingStatsTable, ccdsStreamingModule=ccdsStreamingModule, ccdsStreamingStatsBandwidthRate=ccdsStreamingStatsBandwidthRate, ccdsStreamingStatsIndex=ccdsStreamingStatsIndex, ciscoCdsMIBCompliance=ciscoCdsMIBCompliance, PYSNMP_MODULE_ID=ciscoContentDeliveryStreamingMIB, ccdsStreamingStatsPrepHitRequests=ccdsStreamingStatsPrepHitRequests, ccdsStreamingStatsHCLiveBytes=ccdsStreamingStatsHCLiveBytes, ccdsStreamingStatsHCVODBytes=ccdsStreamingStatsHCVODBytes, ciscoCdsMIBGroups=ciscoCdsMIBGroups, ccdsStreamingStatsConcurrentRequests=ccdsStreamingStatsConcurrentRequests, ccdsStreamingStatsLiveRequests=ccdsStreamingStatsLiveRequests, ciscoContentDeliveryStreamingMIB=ciscoContentDeliveryStreamingMIB, ccdsStreamingStatsGeneralGroup=ccdsStreamingStatsGeneralGroup)
