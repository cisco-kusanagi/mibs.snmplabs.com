#
# PySNMP MIB module CISCO-CDSTV-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CDSTV-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Dscp, = mibBuilder.importSymbols("DIFFSERV-DSCP-TC", "Dscp")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Integer32, Gauge32, Counter32, MibIdentifier, iso, IpAddress, Bits, Counter64, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "iso", "IpAddress", "Bits", "Counter64", "TimeTicks", "ModuleIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoCdstvServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 754))
ciscoCdstvServerMIB.setRevisions(('2012-12-12 00:00', '2010-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCdstvServerMIB.setRevisionsDescriptions(('Added support for recorder server role.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCdstvServerMIB.setLastUpdated('201212120000Z')
if mibBuilder.loadTexts: ciscoCdstvServerMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCdstvServerMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cds@cisco.com')
if mibBuilder.loadTexts: ciscoCdstvServerMIB.setDescription("This MIB module defines server configuration that faciliate the management of the Cisco Content Delivery System for TV (CDS-TV) product family. CDS-TV is a suite of products and software applications providing ingest, storage, caching, streaming, playout and on-demand delivery of video to television or set-top-box clients. Abbreviations: CDS Content Delivery System CDSM Content Delivery System Manager ISA Interactive Services Architecture ISV Integrated Streamer-Vault FSI File Service Interface FTP File Transfer Protocol MPEG Motion Picture Experts Group MSA Managed Services Architecture NDVR Network Digital Video Recorder RTSP Real-Time Streaming Protocol STB Set-Top Box VVI Virtual Video Infrastructure Device Roles: Vault: Content delivery application responsible for ingesting and storing video content and making it available to streamers and/or caching nodes. Caching Nodes: Content delivery application responsible for caching content from vault (using CCP) and then streaming content out to streamers over HTTP or CCP. Streamer: Content delivery application responsible for streaming video out to STB's. ISV: Content delivery application capable of acting as both a vault and as a streamer in a single device. Controller (also called 'CDSM'): CDS application providing a web-based interface for monitoring, control and configuration of CDS devices(streamers, vaults, caching nodes and ISV's), device arrays/groups, and the complete CDS deployment. Recorder: Content delivery application responsible for recording NDVR content and delivering it to streamers. Role-specific objects: cdstvServerCommonObjects apply to all roles cdstvServerStreamingObjects apply to streamer and ISV role specified by cdstvServerRole cdstvServerStorageObjects apply to vault and ISV role specified by cdstvServerRole cdstvServerCachingObjects apply to cachingserver role specified by cdstvServerRole")
class CiscoCdstvEcn(TextualConvention, Integer32):
    description = 'The Explicit Congestion Notification (ECN) field consists of two bits that denote the end points of a transfer protocol as ECN-capable, or that ECN is not being used. The possible values of the ECN Capable Transport Codepoint (ECT) are: ect1(1) - Use ECN with ECT(1) setting. ect0(2) - Use ECN with ECT(0) setting (recommended). congestion(3) - Congestion is experienced by router. disabled(4) - Do not use ECN Setting the ECN field to 3 is performed by the router to indicate congestion is experienced. ECN is set separately for cache and transport interfaces. ECN can also be set for HTTP Streamers when HTTP is selected as the cache-fill protocol for VVI.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ect1", 1), ("ect0", 2), ("congestion", 3), ("disabled", 4))

ciscoCdstvServerMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 0))
ciscoCdstvServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1))
ciscoCdstvServerMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 2))
ciscoCdstvServerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 1))
cdstvServerCommonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1))
cdstvServerStreamingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2))
cdstvServerStorageObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3))
cdstvServerCachingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4))
cdstvServerRole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("isv", 1), ("vault", 2), ("streamer", 3), ("controller", 4), ("cachingserver", 5), ("recorder", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerRole.setStatus('current')
if mibBuilder.loadTexts: cdstvServerRole.setDescription('This object indicates the type/role of this server: isv(1) - Cisco CDS Integrated Streamer Vault vault(2) - Cisco CDS Vault streamer(3) - Cisco CDS Streamer controller(4) - Cisco CDS Manager (CDSM) cachingserver(5) - Cisco CDS Caching Node/Server recorder(6) - Cisco CDS Recorder')
cdstvServerPartNo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerPartNo.setStatus('current')
if mibBuilder.loadTexts: cdstvServerPartNo.setDescription('This object indicates the part number of this device, which uniquely identifies the type of hardware this CDS application is running on, for example, CDE-420 2S3.')
cdstvServerID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerID.setStatus('current')
if mibBuilder.loadTexts: cdstvServerID.setDescription("This object indicates the unique server ID assigned to this device. Server ID's are auto-assigned by the CDS when servers are configured and are used to uniquely identify, optionally with the group ID, a device in the CDS.")
cdstvServerGroupID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerGroupID.setStatus('current')
if mibBuilder.loadTexts: cdstvServerGroupID.setDescription("This object indicates the group ID of the group this server belong to. Group ID's are auto-assigned when server groups are configured in the CDS.")
cdstvServerHostname = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerHostname.setStatus('current')
if mibBuilder.loadTexts: cdstvServerHostname.setDescription('This object specifies the optional fully qualified hostname for this server, for example, vault.cisco.com.')
cdstvServerTTL = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(16)).setUnits('hops').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerTTL.setStatus('current')
if mibBuilder.loadTexts: cdstvServerTTL.setDescription('This object specifies the IP time to live (TTL) for data packets.')
cdstvServerDefaultStreamCacheSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7))
cdstvCacheJumboFramesEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvCacheJumboFramesEnable.setStatus('current')
if mibBuilder.loadTexts: cdstvCacheJumboFramesEnable.setDescription("This object specifies the status of jumbo frames on cache interfaces: 'true' - Jumbo frames are enabled 'false' - Jumbo frames are disabled")
cdstvServerOffloadEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerOffloadEnable.setStatus('current')
if mibBuilder.loadTexts: cdstvServerOffloadEnable.setDescription("This object specifies the current offload status of the server. When Server Offload is enabled, the server is configured not to accept new provisioning. 'true' - Server offload is enabled 'false' - Server offload is disabled")
cdstvServerTransportCacheIPPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10))
cdstvServerNullStreamingEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerNullStreamingEnable.setStatus('current')
if mibBuilder.loadTexts: cdstvServerNullStreamingEnable.setDescription("This object specifies whether the streaming of null MPEG files is allowed or not: 'true' - Null MPEG streaming is allowed. 'false' - NUll MPEG streaming is not allowed.")
cdstvServerStartingTransportPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 1), InetPortNumber().clone(48879)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerStartingTransportPort.setStatus('current')
if mibBuilder.loadTexts: cdstvServerStartingTransportPort.setDescription('This object specifies the beginning default UDP port number used for stream and stream/cache interfaces on this streamer or ISV.')
cdstvServerEndingTransportPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 2), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerEndingTransportPort.setStatus('current')
if mibBuilder.loadTexts: cdstvServerEndingTransportPort.setDescription('This object specifies the ending default UDP port number used for stream and stream/cache interfaces on this streamer or ISV.')
cdstvStreamJumboFramesEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvStreamJumboFramesEnable.setStatus('current')
if mibBuilder.loadTexts: cdstvStreamJumboFramesEnable.setDescription("This object specifies the status of jumbo frames on stream interfaces of this streamer or ISV: 'true' - Jumbo frames are enabled. 'false' - Jumbo frames are disabled.")
cdstvServerStreamGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4))
cdstvServerStreamGroupName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerStreamGroupName.setStatus('current')
if mibBuilder.loadTexts: cdstvServerStreamGroupName.setDescription('This object indicates the name of the stream group this streamer or ISV is a member of. Group name for a stream group is configured in the CDSM.')
cdstvServerStreamGroupID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerStreamGroupID.setStatus('current')
if mibBuilder.loadTexts: cdstvServerStreamGroupID.setDescription('This object indicates the ID of the stream group this streamer or ISV is a member of. Stream group ID is auto-assigned by CDS when the stream group is created.')
cdstvServerStreamerIsCache = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerStreamerIsCache.setStatus('current')
if mibBuilder.loadTexts: cdstvServerStreamerIsCache.setDescription("This object specifies whether 'Streamer Is Cache' is enabled on this streamer. If 'Streamer Is Cache' is enabled, the Streamer can be used as a possible cache-fill source by a Streamer in a different Stream Group. All Stream Groups that have at least one Streamer with 'Streamer is Cache' enabled are displayed on the 'Stream to Cache Map' page, where the Stream Group can be selected as a possible cache-fill source and given a preference. Only the Streamers with 'Streamer Is Cache' enabled are used as possible cache-fill sources. The protocol used for cache-fill responses from Streamers is always CCP. 'true' - 'Streamer Is Cache' is enabled 'false' - 'Streamer Is Cache' is disabled")
cdstvVaultMirrorCopies = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setUnits('copies').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvVaultMirrorCopies.setStatus('current')
if mibBuilder.loadTexts: cdstvVaultMirrorCopies.setDescription('This object specifies the number of content copies on a Vault or ISV that will ensure there is at least one copy at each site.')
cdstvServerCacheGroupInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4, 1))
cdstvServerCacheGroupName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerCacheGroupName.setStatus('current')
if mibBuilder.loadTexts: cdstvServerCacheGroupName.setDescription('This object indicates the name of the cache group this Caching Node is a member of. Group name for a caching group is configured in the CDSM.')
cdstvServerCacheGroupID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerCacheGroupID.setStatus('current')
if mibBuilder.loadTexts: cdstvServerCacheGroupID.setDescription('This object indicates the ID of the caching group this Caching Node is a member of. Caching Group ID is auto-assigned by the CDS when a caching group is created.')
cdstvVaultLocalCopies = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setUnits('copies').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvVaultLocalCopies.setStatus('current')
if mibBuilder.loadTexts: cdstvVaultLocalCopies.setDescription('This object specifies the number of local copies on a Vaults or ISV at a site.')
cdstvServerFTPOutSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3))
cdstvServerVaultGroupInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 4))
cdstvServerFTPOutInterface = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("management", 1), ("ingest", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerFTPOutInterface.setStatus('current')
if mibBuilder.loadTexts: cdstvServerFTPOutInterface.setDescription('This object specifies whether the management interface or the ingest interface is used for FTP pull and FTP push on a Vault or ISV. management(1) - Management interface is used for FTP pull and FTP push ingest(2) - Ingest interface is used for FTP pull and FTP push')
cdstvServerFTPOutBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('Mbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerFTPOutBandwidth.setStatus('current')
if mibBuilder.loadTexts: cdstvServerFTPOutBandwidth.setDescription('This object specifies the maximum bandwidth allowed for FTP functionality on a Vault or ISV.')
cdstvServerFTPOutSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('sessions').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerFTPOutSessions.setStatus('current')
if mibBuilder.loadTexts: cdstvServerFTPOutSessions.setDescription('This object specifies the maximum number of FTP out sessions allowed on a Vault or ISV.')
cdstvServerVaultGroupName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 4, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerVaultGroupName.setStatus('current')
if mibBuilder.loadTexts: cdstvServerVaultGroupName.setDescription('This object indicates the name of the vault group this Vault is a member of. Group name for a vault group is configured in the CDSM.')
cdstvServerVaultGroupID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 4, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerVaultGroupID.setStatus('current')
if mibBuilder.loadTexts: cdstvServerVaultGroupID.setDescription('This object indicates the ID of the vault group this Vault is a member of. Vault Group ID is auto-assigned by the CDS when a vault group is configured.')
cdstvServerSourceAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7, 1), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerSourceAddressType.setStatus('current')
if mibBuilder.loadTexts: cdstvServerSourceAddressType.setDescription('This object specifies the type of the default source IP address (specified by the cdstvServerSourceAddress) for all stream and cache interfaces.')
cdstvServerSourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7, 2), InetAddress().clone('192.168.207.65')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerSourceAddress.setStatus('current')
if mibBuilder.loadTexts: cdstvServerSourceAddress.setDescription('This object specifies the default source IP address for all stream and cache interfaces. The type of this address is specified by the cdstvServerSourceAddressType.')
cdstvServerCachePort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7, 3), InetPortNumber().clone(48879)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerCachePort.setStatus('current')
if mibBuilder.loadTexts: cdstvServerCachePort.setDescription('This object specifies the default UDP port number used for cache traffic between servers.')
cdstvServerTransportDSCP = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 1), Dscp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerTransportDSCP.setStatus('current')
if mibBuilder.loadTexts: cdstvServerTransportDSCP.setDescription('This object specifies the Differentiated Services Code Point (DSCP) for the Transport Interface on this server. DSCP uses six bits of the DiffServ field, which was originally the ToS octet, to mark all outgoing packets with a specific DSCP value. Cache or transport traffic may require certain forwarding behavior, known as the per-hop behavior (PHB), which is specified in the DSCP. The network gives priority to marked traffic. Generally, the lower number has lower priority and the higher number has higher priority. DSCP is set separately for cache and transport interfaces. DSCP can also be set for HTTP Streamers when HTTP is selected as the cache-fill protocol for VVI.')
cdstvServerTransportECN = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 2), CiscoCdstvEcn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerTransportECN.setStatus('current')
if mibBuilder.loadTexts: cdstvServerTransportECN.setDescription('This object specifies the Explicit Congestion Notification (ECN) for the Transport Interface on this server.')
cdstvServerCacheDSCP = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 3), Dscp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerCacheDSCP.setStatus('current')
if mibBuilder.loadTexts: cdstvServerCacheDSCP.setDescription('his object specifies the Differentiated Services Code Point (DSCP) for the Cache Interface on this server. DSCP uses six bits of the DiffServ field, which was originally the ToS octet, to mark all outgoing packets with a specific DSCP value. Cache or transport traffic may require certain forwarding behavior, known as the per-hop behavior (PHB), which is specified in the DSCP. The network gives priority to marked traffic. Generally, the lower number has lower priority and the higher number has higher priority. DSCP is set separately for cache and transport interfaces. DSCP can also be set for HTTP Streamers when HTTP is selected as the cache-fill protocol for VVI.')
cdstvServerCacheECN = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 4), CiscoCdstvEcn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerCacheECN.setStatus('current')
if mibBuilder.loadTexts: cdstvServerCacheECN.setDescription('This object specifies the Explicit Congestion Notification (ECN) for the Cache Interface on this server.')
ciscoCdstvServerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2))
ciscoCdstvServerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 1, 1)).setObjects(("CISCO-CDSTV-SERVER-MIB", "ciscoCdstvServerMIBMainObjectGroup"), ("CISCO-CDSTV-SERVER-MIB", "ciscoCdstvServerMIBStreamingObjectGroup"), ("CISCO-CDSTV-SERVER-MIB", "ciscoCdstvServerMIBStorageObjectGroup"), ("CISCO-CDSTV-SERVER-MIB", "ciscoCdstvServerMIBCachingObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBCompliance = ciscoCdstvServerMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvServerMIBCompliance.setDescription('The compliance statement for the entities which implement the Cisco CDS TV Server setup MIB.')
ciscoCdstvServerMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 1)).setObjects(("CISCO-CDSTV-SERVER-MIB", "cdstvServerRole"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerPartNo"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerID"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerGroupID"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerHostname"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerTTL"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerSourceAddress"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCachePort"), ("CISCO-CDSTV-SERVER-MIB", "cdstvCacheJumboFramesEnable"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerOffloadEnable"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerTransportDSCP"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerTransportECN"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheDSCP"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheECN"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerSourceAddressType"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerNullStreamingEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBMainObjectGroup = ciscoCdstvServerMIBMainObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvServerMIBMainObjectGroup.setDescription('A collection of common objects that provide CDS-TV server configuration for all device roles.')
ciscoCdstvServerMIBStreamingObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 2)).setObjects(("CISCO-CDSTV-SERVER-MIB", "cdstvServerStartingTransportPort"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerEndingTransportPort"), ("CISCO-CDSTV-SERVER-MIB", "cdstvStreamJumboFramesEnable"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerStreamGroupName"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerStreamGroupID"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerStreamerIsCache"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBStreamingObjectGroup = ciscoCdstvServerMIBStreamingObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvServerMIBStreamingObjectGroup.setDescription('A collection of streaming objects that provide CDS-TV server configuration for all streamers and ISVs.')
ciscoCdstvServerMIBStorageObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 3)).setObjects(("CISCO-CDSTV-SERVER-MIB", "cdstvVaultMirrorCopies"), ("CISCO-CDSTV-SERVER-MIB", "cdstvVaultLocalCopies"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerFTPOutInterface"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerFTPOutBandwidth"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerFTPOutSessions"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerVaultGroupName"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerVaultGroupID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBStorageObjectGroup = ciscoCdstvServerMIBStorageObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvServerMIBStorageObjectGroup.setDescription('A collection of storage objects that provide CDS-TV server configuration for vaults.')
ciscoCdstvServerMIBCachingObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 4)).setObjects(("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheGroupName"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheGroupID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBCachingObjectGroup = ciscoCdstvServerMIBCachingObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvServerMIBCachingObjectGroup.setDescription('A collection of caching objects that provide CDS-TV server configuration for Caching Nodes.')
mibBuilder.exportSymbols("CISCO-CDSTV-SERVER-MIB", cdstvServerFTPOutSessions=cdstvServerFTPOutSessions, ciscoCdstvServerMIBCompliance=ciscoCdstvServerMIBCompliance, cdstvServerFTPOutSettings=cdstvServerFTPOutSettings, PYSNMP_MODULE_ID=ciscoCdstvServerMIB, ciscoCdstvServerMIBNotifs=ciscoCdstvServerMIBNotifs, cdstvServerVaultGroupID=cdstvServerVaultGroupID, ciscoCdstvServerMIBGroups=ciscoCdstvServerMIBGroups, cdstvServerStreamingObjects=cdstvServerStreamingObjects, ciscoCdstvServerMIBCachingObjectGroup=ciscoCdstvServerMIBCachingObjectGroup, cdstvServerTransportECN=cdstvServerTransportECN, ciscoCdstvServerMIBConform=ciscoCdstvServerMIBConform, cdstvServerID=cdstvServerID, cdstvServerDefaultStreamCacheSettings=cdstvServerDefaultStreamCacheSettings, cdstvVaultMirrorCopies=cdstvVaultMirrorCopies, cdstvServerCacheGroupID=cdstvServerCacheGroupID, cdstvVaultLocalCopies=cdstvVaultLocalCopies, cdstvServerOffloadEnable=cdstvServerOffloadEnable, cdstvServerStreamerIsCache=cdstvServerStreamerIsCache, cdstvServerRole=cdstvServerRole, cdstvServerVaultGroupName=cdstvServerVaultGroupName, ciscoCdstvServerMIBStreamingObjectGroup=ciscoCdstvServerMIBStreamingObjectGroup, cdstvServerCommonObjects=cdstvServerCommonObjects, cdstvServerGroupID=cdstvServerGroupID, cdstvServerStreamGroupID=cdstvServerStreamGroupID, cdstvServerSourceAddress=cdstvServerSourceAddress, cdstvServerStartingTransportPort=cdstvServerStartingTransportPort, cdstvServerStreamGroupName=cdstvServerStreamGroupName, cdstvServerStreamGroupInfo=cdstvServerStreamGroupInfo, cdstvServerCacheECN=cdstvServerCacheECN, cdstvServerTTL=cdstvServerTTL, cdstvServerCachingObjects=cdstvServerCachingObjects, cdstvServerStorageObjects=cdstvServerStorageObjects, cdstvServerSourceAddressType=cdstvServerSourceAddressType, cdstvServerNullStreamingEnable=cdstvServerNullStreamingEnable, cdstvServerVaultGroupInformation=cdstvServerVaultGroupInformation, cdstvServerFTPOutBandwidth=cdstvServerFTPOutBandwidth, cdstvServerCacheGroupName=cdstvServerCacheGroupName, cdstvServerCacheGroupInformation=cdstvServerCacheGroupInformation, cdstvCacheJumboFramesEnable=cdstvCacheJumboFramesEnable, cdstvServerFTPOutInterface=cdstvServerFTPOutInterface, ciscoCdstvServerMIBCompliances=ciscoCdstvServerMIBCompliances, cdstvStreamJumboFramesEnable=cdstvStreamJumboFramesEnable, cdstvServerHostname=cdstvServerHostname, cdstvServerEndingTransportPort=cdstvServerEndingTransportPort, ciscoCdstvServerMIBMainObjectGroup=ciscoCdstvServerMIBMainObjectGroup, cdstvServerTransportDSCP=cdstvServerTransportDSCP, cdstvServerCachePort=cdstvServerCachePort, cdstvServerTransportCacheIPPkts=cdstvServerTransportCacheIPPkts, ciscoCdstvServerMIBStorageObjectGroup=ciscoCdstvServerMIBStorageObjectGroup, ciscoCdstvServerMIB=ciscoCdstvServerMIB, ciscoCdstvServerMIBObjects=ciscoCdstvServerMIBObjects, cdstvServerCacheDSCP=cdstvServerCacheDSCP, cdstvServerPartNo=cdstvServerPartNo, CiscoCdstvEcn=CiscoCdstvEcn)
