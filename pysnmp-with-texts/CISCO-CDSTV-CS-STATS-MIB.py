#
# PySNMP MIB module CISCO-CDSTV-CS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CDSTV-CS-STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, ObjectIdentity, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Gauge32, Unsigned32, ModuleIdentity, Integer32, TimeTicks, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "TimeTicks", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCdstvCsStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 743))
ciscoCdstvCsStatsMIB.setRevisions(('2012-05-17 00:00', '2010-07-29 00:00', '2010-06-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCdstvCsStatsMIB.setRevisionsDescriptions(('Added bandwidth reporting by content type support.', 'Added stream control message queue reporting support.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCdstvCsStatsMIB.setLastUpdated('201205170000Z')
if mibBuilder.loadTexts: ciscoCdstvCsStatsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCdstvCsStatsMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cds@cisco.com')
if mibBuilder.loadTexts: ciscoCdstvCsStatsMIB.setDescription("This MIB module defines objects describing the caching and streaming statistics objects that facilitate the management of the Cisco CDS-TV product family. CDS-TV is a suite of products and software applications providing ingest, storage, caching, streaming, playout and on-demand delivery of video to television or STB clients. ACRONYMS CCP Content Control Protocol CDN Content Distribution Network CDS Content Delivery System ISA Interactive Services Architecture ISV Integrated Streamer-Vault FSI File Service Interface FTP File Transfer Protocol HTTP Hyper-Text Transfer Protocol MPEG Motion Picture Experts Group MSA Managed Services Architecture NDVR Network Digital Video Recorder RTSP Real-Time Streaming Protocol STB Set-Top Box VOD Video On Demand GLOSSARY Catcher: Device responsible for receiving content (typically via satellite dishes and antennae) from content providers or from a Headend-In-The-Sky. Content Ingest: Acquisition of content (from a source such as a catcher or an FTP server) for the purpose of storing it locally in a vault and making it available to streamers and caching nodes as needed. Vault: Content delivery application responsible for ingesting video content, storing it, and making it available to streamers. Caching Node: Content delivery application responsible for caching content from a vault and streaming it to other caching nodes or streamers. Streamer: Content delivery application responsible for streaming video to STB's.")
ciscoCdstvStatsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 743, 0))
ciscoCdstvStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 743, 1))
ciscoCdstvStatsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 743, 2))
ciscoCdstvCacheStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1))
ciscoCdstvStreamStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2))
cdstvCacheCapacity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('kilobytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCacheCapacity.setStatus('current')
if mibBuilder.loadTexts: cdstvCacheCapacity.setDescription('This object indicates the total cache capacity of this streamer, caching node or ISV.')
cdstvCacheLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 2), Gauge32()).setUnits('kilobytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCacheLevel.setStatus('current')
if mibBuilder.loadTexts: cdstvCacheLevel.setDescription('This object indicates the used cache level for this streamer, caching node or ISV.')
cdstvFillReceiveStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 3), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvFillReceiveStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvFillReceiveStreams.setDescription('This object indicates the total number of cache fills this streamer, caching node or ISV gets from other devices. For a streamer or ISV, the source devices can be vaults, caching nodes or neighboring streamers. For caching nodes, the source can be vaults or neighboring caching nodes. For streamers, this metric includes both CCP and HTTP streams.')
cdstvFillStreamCommittedBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 4), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvFillStreamCommittedBW.setStatus('current')
if mibBuilder.loadTexts: cdstvFillStreamCommittedBW.setDescription('This object indicates the committed bandwidth for cache fills this streamer, caching node or ISV gets from other devices. For a streamer or ISV , the other devices can be vaults, caching nodes or neighboring streamers. For caching nodes, the other devices can be vaults or neighboring caching nodes. For streamers, this metric includes both CCP and HTTP streams.')
cdstvFillStreamActualBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 5), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvFillStreamActualBW.setStatus('current')
if mibBuilder.loadTexts: cdstvFillStreamActualBW.setDescription('This object indicates the actual bandwidth of cache fills this streamer, caching node or ISV gets from other devices. For a streamer or ISV, the other devices can be vaults, caching nodes or neighboring streamers. For caching nodes, the other devices can be vaults or neighboring caching nodes. For streamers, this metric includes both CCP and HTTP streams.')
cdstvDiskReadStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 6), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvDiskReadStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvDiskReadStreams.setDescription("This object indicates the disk-read stream count for this streamer, caching node or ISV, i.e. the number of streams served from this device's disks.")
cdstvDiskReadBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 7), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvDiskReadBW.setStatus('current')
if mibBuilder.loadTexts: cdstvDiskReadBW.setDescription("this object indicates the disk-read bandwidth for this streamer, caching node or ISV, i.e. the bandwidth of the streams read from this device's disk.")
cdstvCCPInfromVaultStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 8), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCCPInfromVaultStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvCCPInfromVaultStreams.setDescription('This object indicates the number of CCP streams from a vault filling this device.')
cdstvCCPInFromVaultStreamBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 9), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCCPInFromVaultStreamBW.setStatus('current')
if mibBuilder.loadTexts: cdstvCCPInFromVaultStreamBW.setDescription('This object indicates the bandwidth of CCP streams from a vault filling this device.')
cdstvCCPInFromCacheStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 10), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCCPInFromCacheStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvCCPInFromCacheStreams.setDescription('This object indicates the number of CCP streams from a caching node filling this caching node or streamer.')
cdstvCCPInFromCacheStreamBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 11), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCCPInFromCacheStreamBW.setStatus('current')
if mibBuilder.loadTexts: cdstvCCPInFromCacheStreamBW.setDescription('This object indicates the bandwidth of CCP streams from a caching node filling this device.')
cdstvCCPInFromStreamerStreamCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 12), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCCPInFromStreamerStreamCount.setStatus('current')
if mibBuilder.loadTexts: cdstvCCPInFromStreamerStreamCount.setDescription('This object indicates the number of CCP streams from another streamer filling this streamer.')
cdstvCCPInFromStreamerStreamBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCCPInFromStreamerStreamBW.setStatus('current')
if mibBuilder.loadTexts: cdstvCCPInFromStreamerStreamBW.setDescription('This object indicates the bandwidth of CCP streams from other streamers filling this streamer.')
cdstvActiveStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 1), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvActiveStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvActiveStreams.setDescription('This object specifies the number of active streams from this device. For a streamer, this includes CCP streams going out to other streamers. For caching nodes and vaults, this includes CCP streams going out to streamers or caching nodes. For vaults, this includes mirroring traffic as well.')
cdstvActiveStreamBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 2), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvActiveStreamBW.setStatus('current')
if mibBuilder.loadTexts: cdstvActiveStreamBW.setDescription('This object indicates the bandwidth of active streams from this device. For a streamer, this includes CCP streams going out to other streamers. For caching nodes and vaults, this includes CCP streams going out to streamers or caching nodes. For vaults, this includes mirroring traffic as well.')
cdstvUniqueStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 3), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvUniqueStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvUniqueStreams.setDescription('This object indicates the number of unique streams going out from this device.')
cdstvUniqueStreamBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 4), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvUniqueStreamBW.setStatus('current')
if mibBuilder.loadTexts: cdstvUniqueStreamBW.setDescription('This object indicates the bandwidth of unique streams going out from this device.')
cdstvCCPOutStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 5), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCCPOutStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvCCPOutStreams.setDescription('This object indicates the number of CCP streams going out from this device. For streamers, the destination is another streamer. For caching nodes, the destination is a streamer or another caching node. For vaults, the destination can be a streamer, caching node or vault.')
cdstvCCPOutStreamBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 6), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvCCPOutStreamBW.setStatus('current')
if mibBuilder.loadTexts: cdstvCCPOutStreamBW.setDescription('This object indicates the bandwidth of CCP streams going out from this device. For streamers, the destination is another streamer. For caching nodes, the destination is a streamer or another caching node. For vaults, the destination can be a streamer, caching node or vault.')
cdstvHTTPOutStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 7), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvHTTPOutStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvHTTPOutStreams.setDescription('This object indicates the number of HTTP streams going out from this caching node to streamers in a CDN setup.')
cdstvHTTPOutStreamBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 8), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvHTTPOutStreamBW.setStatus('current')
if mibBuilder.loadTexts: cdstvHTTPOutStreamBW.setDescription('This object indicates the bandwidth of HTTP streams going out from this caching node to streamers in a CDN setup.')
cdstvSessionSetupSuccess = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvSessionSetupSuccess.setStatus('current')
if mibBuilder.loadTexts: cdstvSessionSetupSuccess.setDescription('This object indicates the number of successfully setup sessions since the counter was reset (the reference). The seconds elapsed since the reference is indicated by cdstvSecondsSinceReference.')
cdstvSessionSetupFailures = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvSessionSetupFailures.setStatus('current')
if mibBuilder.loadTexts: cdstvSessionSetupFailures.setDescription('This object indicates the number of unsuccessfully setup (failed) sessions since the counter was reset (the reference). The seconds elapsed since the reference is indicated by cdstvSecondsSinceReference.')
cdstvSecondsSinceReference = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 11), TimeIntervalSec()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvSecondsSinceReference.setStatus('current')
if mibBuilder.loadTexts: cdstvSecondsSinceReference.setDescription('This object indicates the seconds elapsed since the last time the database was restarted and hence the cdstvSessionSetupSucess and cdstvSessionSetupFailures counters were reset.')
cdstvStreamControlMessageQueueMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 12), Unsigned32()).setUnits('elements').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvStreamControlMessageQueueMax.setStatus('current')
if mibBuilder.loadTexts: cdstvStreamControlMessageQueueMax.setDescription('This object indicates the maximum size of the stream control message queue used in CDS.')
cdstvStreamControlMessageQueueSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 13), Unsigned32()).setUnits('elements').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvStreamControlMessageQueueSize.setStatus('current')
if mibBuilder.loadTexts: cdstvStreamControlMessageQueueSize.setDescription('This object indicates the current size of the stream control message queue, i.e. the number of elements in the queue.')
cdstvSkippedPlaylistElements = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 14), Unsigned32()).setUnits('elements').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvSkippedPlaylistElements.setStatus('current')
if mibBuilder.loadTexts: cdstvSkippedPlaylistElements.setDescription('This object indicates the number of skipped playlist elements.')
cdstvStatsByContentTypeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15), )
if mibBuilder.loadTexts: cdstvStatsByContentTypeTable.setStatus('current')
if mibBuilder.loadTexts: cdstvStatsByContentTypeTable.setDescription('This table lists the fill (ingress) and stream (egress) counts as well as the bandwidth used by the ingress fills and egress streams on this streamer, differentiated by the content type.')
cdstvStatsByContentTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1), ).setIndexNames((0, "CISCO-CDSTV-CS-STATS-MIB", "cdstvContentType"))
if mibBuilder.loadTexts: cdstvStatsByContentTypeEntry.setStatus('current')
if mibBuilder.loadTexts: cdstvStatsByContentTypeEntry.setDescription('An entry (conceptual row) in the cdstvStatsByContentTypeTable. Each entry represents a content type and its active ingress and egress counts, as well as the bandwidth consumed by the active fills and streams, for this streamer. A row is added for each content type supported by a streamer and the number of rows does not change for a particular streamer.')
cdstvContentType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("legacyVod", 1), ("ndvrUniqueCopy", 2), ("ndvrCommonCopy", 3))))
if mibBuilder.loadTexts: cdstvContentType.setStatus('current')
if mibBuilder.loadTexts: cdstvContentType.setDescription('This object indicates the type of the content being ingested into or streamed out of a streamer. Possible values are: legacyVod(1) - Legacy VOD Content ndvrUniqueCopy(2) - NDVR Unique Copy Content ndvrCommonCopy(3) - NDVR Common Copy Content')
cdstvActiveEgressCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 2), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvActiveEgressCount.setStatus('current')
if mibBuilder.loadTexts: cdstvActiveEgressCount.setDescription('This object indicates the number of active egress streams from this streamer for the type of content indicated by cdstvContentType.')
cdstvActiveEgressBW = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 3), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvActiveEgressBW.setStatus('current')
if mibBuilder.loadTexts: cdstvActiveEgressBW.setDescription('This object indicates the bandwidth consumed by active egress streams from this streamer for the type of content indicated by cdstvContentType.')
cdstvActiveIngressCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 4), Gauge32()).setUnits('fill count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvActiveIngressCount.setStatus('current')
if mibBuilder.loadTexts: cdstvActiveIngressCount.setDescription('This object indicates the number of active ingress fills into this streamer for the type of content indicated by cdstvContentType.')
cdstvActiveIngressBW = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 5), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvActiveIngressBW.setStatus('current')
if mibBuilder.loadTexts: cdstvActiveIngressBW.setDescription('This object indicates the bandwidth consumed by active ingress fills into this streamer for the type of content indicated by cdstvContentType.')
cdstvHTTPInStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 14), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvHTTPInStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvHTTPInStreams.setDescription('This object indicates the number of HTTP streams filling this streamer.')
cdstvHTTPInStreamBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 15), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvHTTPInStreamBW.setStatus('current')
if mibBuilder.loadTexts: cdstvHTTPInStreamBW.setDescription('This object indicates the bandwidth of HTTP streams filling this streamer.')
cdstvActiveIngestStreams = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 16), Gauge32()).setUnits('stream count').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvActiveIngestStreams.setStatus('current')
if mibBuilder.loadTexts: cdstvActiveIngestStreams.setDescription('This object indicates the number of active ingest streams filling this vault.')
cdstvActiveIngestStreamBW = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 17), Gauge32()).setUnits('kilobits').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvActiveIngestStreamBW.setStatus('current')
if mibBuilder.loadTexts: cdstvActiveIngestStreamBW.setDescription('This object indicates the bandwidth of active ingest streams filling this vault.')
ciscoCdstvStatsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 1))
ciscoCdstvStatsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2))
ciscoCdstvStatsMIBModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 1, 1)).setObjects(("CISCO-CDSTV-CS-STATS-MIB", "ciscoCdstvStatsMIBCacheObjectGroup"), ("CISCO-CDSTV-CS-STATS-MIB", "ciscoCdstvStatsMIBStreamObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvStatsMIBModuleCompliance = ciscoCdstvStatsMIBModuleCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoCdstvStatsMIBModuleCompliance.setDescription('The compliance statement for the entities which implement the CISCO-CDSTV-STATS-MIB.')
ciscoCdstvStatsMIBModuleCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 1, 2)).setObjects(("CISCO-CDSTV-CS-STATS-MIB", "ciscoCdstvStatsMIBCacheObjectGroup"), ("CISCO-CDSTV-CS-STATS-MIB", "ciscoCdstvStatsMIBStreamObjectGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvStatsMIBModuleCompliance2 = ciscoCdstvStatsMIBModuleCompliance2.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoCdstvStatsMIBModuleCompliance2.setDescription('The compliance statement for the entities which implement the CISCO-CDSTV-STATS-MIB.')
ciscoCdstvStatsMIBModuleCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 1, 3)).setObjects(("CISCO-CDSTV-CS-STATS-MIB", "ciscoCdstvStatsMIBCacheObjectGroup"), ("CISCO-CDSTV-CS-STATS-MIB", "ciscoCdstvStatsMIBStreamObjectGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvStatsMIBModuleCompliance3 = ciscoCdstvStatsMIBModuleCompliance3.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvStatsMIBModuleCompliance3.setDescription('The compliance statement for the entities which implement the CISCO-CDSTV-STATS-MIB.')
ciscoCdstvStatsMIBCacheObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2, 1)).setObjects(("CISCO-CDSTV-CS-STATS-MIB", "cdstvCacheCapacity"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCacheLevel"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvFillReceiveStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvFillStreamCommittedBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvFillStreamActualBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvDiskReadStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvDiskReadBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInfromVaultStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromVaultStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromCacheStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromCacheStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromStreamerStreamCount"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromStreamerStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPInStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPInStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveIngestStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveIngestStreamBW"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvStatsMIBCacheObjectGroup = ciscoCdstvStatsMIBCacheObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvStatsMIBCacheObjectGroup.setDescription('A collection of objects providing caching statistics.')
ciscoCdstvStatsMIBStreamObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2, 2)).setObjects(("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupSuccess"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSecondsSinceReference"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvStatsMIBStreamObjectGroup = ciscoCdstvStatsMIBStreamObjectGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoCdstvStatsMIBStreamObjectGroup.setDescription('A collection of objects providing streaming statistics. ciscoCdstvStatsMIBStreamObjectGroup object is superseded by ciscoCdstvStatsMIBStreamObjectGroup2.')
ciscoCdstvStatsMIBStreamObjectGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2, 3)).setObjects(("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupSuccess"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupFailures"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSecondsSinceReference"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvStreamControlMessageQueueMax"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvStreamControlMessageQueueSize"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSkippedPlaylistElements"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvStatsMIBStreamObjectGroup2 = ciscoCdstvStatsMIBStreamObjectGroup2.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoCdstvStatsMIBStreamObjectGroup2.setDescription('A collection of objects providing streaming statistics. ciscoCdstvStatsMIBStreamObjectGroup2 object is superseded by ciscoCdstvStatsMIBStreamObjectGroup3.')
ciscoCdstvStatsMIBStreamObjectGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2, 4)).setObjects(("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreams"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreamBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupSuccess"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupFailures"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSecondsSinceReference"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvStreamControlMessageQueueMax"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvStreamControlMessageQueueSize"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSkippedPlaylistElements"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveEgressCount"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveEgressBW"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveIngressCount"), ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveIngressBW"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvStatsMIBStreamObjectGroup3 = ciscoCdstvStatsMIBStreamObjectGroup3.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvStatsMIBStreamObjectGroup3.setDescription('A collection of objects providing streaming statistics.')
mibBuilder.exportSymbols("CISCO-CDSTV-CS-STATS-MIB", cdstvCCPInFromCacheStreams=cdstvCCPInFromCacheStreams, cdstvCCPInFromStreamerStreamCount=cdstvCCPInFromStreamerStreamCount, cdstvActiveIngestStreamBW=cdstvActiveIngestStreamBW, cdstvFillStreamCommittedBW=cdstvFillStreamCommittedBW, cdstvSecondsSinceReference=cdstvSecondsSinceReference, ciscoCdstvStatsMIBStreamObjectGroup=ciscoCdstvStatsMIBStreamObjectGroup, cdstvActiveIngressBW=cdstvActiveIngressBW, cdstvCCPInFromStreamerStreamBW=cdstvCCPInFromStreamerStreamBW, cdstvUniqueStreams=cdstvUniqueStreams, cdstvSessionSetupSuccess=cdstvSessionSetupSuccess, cdstvContentType=cdstvContentType, ciscoCdstvCacheStats=ciscoCdstvCacheStats, ciscoCdstvCsStatsMIB=ciscoCdstvCsStatsMIB, cdstvFillReceiveStreams=cdstvFillReceiveStreams, cdstvHTTPInStreamBW=cdstvHTTPInStreamBW, cdstvDiskReadBW=cdstvDiskReadBW, cdstvStatsByContentTypeEntry=cdstvStatsByContentTypeEntry, cdstvActiveStreamBW=cdstvActiveStreamBW, cdstvSkippedPlaylistElements=cdstvSkippedPlaylistElements, ciscoCdstvStatsMIBCompliances=ciscoCdstvStatsMIBCompliances, cdstvActiveIngestStreams=cdstvActiveIngestStreams, ciscoCdstvStatsMIBObjects=ciscoCdstvStatsMIBObjects, ciscoCdstvStatsMIBCacheObjectGroup=ciscoCdstvStatsMIBCacheObjectGroup, ciscoCdstvStatsMIBModuleCompliance=ciscoCdstvStatsMIBModuleCompliance, cdstvCCPInFromVaultStreamBW=cdstvCCPInFromVaultStreamBW, cdstvDiskReadStreams=cdstvDiskReadStreams, ciscoCdstvStatsMIBModuleCompliance3=ciscoCdstvStatsMIBModuleCompliance3, ciscoCdstvStatsMIBStreamObjectGroup2=ciscoCdstvStatsMIBStreamObjectGroup2, cdstvCacheCapacity=cdstvCacheCapacity, cdstvCCPOutStreamBW=cdstvCCPOutStreamBW, cdstvCCPInfromVaultStreams=cdstvCCPInfromVaultStreams, ciscoCdstvStatsMIBConform=ciscoCdstvStatsMIBConform, cdstvActiveIngressCount=cdstvActiveIngressCount, ciscoCdstvStreamStats=ciscoCdstvStreamStats, cdstvCCPInFromCacheStreamBW=cdstvCCPInFromCacheStreamBW, cdstvActiveStreams=cdstvActiveStreams, cdstvHTTPOutStreams=cdstvHTTPOutStreams, cdstvStreamControlMessageQueueMax=cdstvStreamControlMessageQueueMax, ciscoCdstvStatsMIBStreamObjectGroup3=ciscoCdstvStatsMIBStreamObjectGroup3, ciscoCdstvStatsMIBGroups=ciscoCdstvStatsMIBGroups, PYSNMP_MODULE_ID=ciscoCdstvCsStatsMIB, cdstvHTTPInStreams=cdstvHTTPInStreams, ciscoCdstvStatsMIBModuleCompliance2=ciscoCdstvStatsMIBModuleCompliance2, cdstvStatsByContentTypeTable=cdstvStatsByContentTypeTable, cdstvCCPOutStreams=cdstvCCPOutStreams, cdstvFillStreamActualBW=cdstvFillStreamActualBW, cdstvActiveEgressCount=cdstvActiveEgressCount, cdstvCacheLevel=cdstvCacheLevel, cdstvSessionSetupFailures=cdstvSessionSetupFailures, cdstvActiveEgressBW=cdstvActiveEgressBW, cdstvUniqueStreamBW=cdstvUniqueStreamBW, cdstvHTTPOutStreamBW=cdstvHTTPOutStreamBW, cdstvStreamControlMessageQueueSize=cdstvStreamControlMessageQueueSize, ciscoCdstvStatsMIBNotifs=ciscoCdstvStatsMIBNotifs)
