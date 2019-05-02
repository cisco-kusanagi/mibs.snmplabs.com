#
# PySNMP MIB module NETWORK-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETWORK-SERVICES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:47:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, iso, MibIdentifier, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Gauge32, ModuleIdentity, IpAddress, ObjectIdentity, Bits, Counter32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "MibIdentifier", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Gauge32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Bits", "Counter32", "Counter64", "TimeTicks")
TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString")
application = ModuleIdentity((1, 3, 6, 1, 2, 1, 27))
application.setRevisions(('2000-03-03 00:00', '1999-05-12 00:00', '1997-08-17 00:00', '1993-11-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: application.setRevisionsDescriptions(('This revision, published in RFC 2788, changes a number of DisplayStrings to SnmpAdminStrings. Note that this change is not strictly supported by SMIv2. However, the alternative of deprecating the old objects and defining new objects would have a more adverse impact on backward compatibility and interoperability, given the particular semantics of these objects. The defining reference for distinguished names has also been updated from RFC 1779 to RFC 2253.', 'This revision fixes a few small technical problems found in previous versions, mostly in regards to the conformance groups for different versions of this MIB. No changes have been made to the objects this MIB defines since RFC 2248.', 'This revision, published in RFC 2248, adds the applDescription and applURL objects, adds the quiescing state to the applOperStatus object and renames the MIB from the APPLICATION-MIB to the NETWORK-SERVICE-MIB.', 'The original version of this MIB was published in RFC 1565',))
if mibBuilder.loadTexts: application.setLastUpdated('200003030000Z')
if mibBuilder.loadTexts: application.setOrganization('IETF Mail and Directory Management Working Group')
if mibBuilder.loadTexts: application.setContactInfo(' Ned Freed Postal: Innosoft International, Inc. 1050 Lakes Drive West Covina, CA 91790 US Tel: +1 626 919 3600 Fax: +1 626 919 3614 E-Mail: ned.freed@innosoft.com')
if mibBuilder.loadTexts: application.setDescription('The MIB module describing network service applications')
class DistinguishedName(TextualConvention, OctetString):
    description = 'A Distinguished Name represented in accordance with RFC 2253, presented in the UTF-8 charset defined in RFC 2279.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class URLString(TextualConvention, OctetString):
    description = 'A Uniform Resource Locator represented in accordance with RFCs 1738 and 2368, presented in the NVT ASCII charset defined in RFC 854.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

applTable = MibTable((1, 3, 6, 1, 2, 1, 27, 1), )
if mibBuilder.loadTexts: applTable.setStatus('current')
if mibBuilder.loadTexts: applTable.setDescription('The table holding objects which apply to all different kinds of applications providing network services. Each network service application capable of being monitored should have a single entry in this table.')
applEntry = MibTableRow((1, 3, 6, 1, 2, 1, 27, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: applEntry.setStatus('current')
if mibBuilder.loadTexts: applEntry.setDescription('An entry associated with a single network service application.')
applIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: applIndex.setStatus('current')
if mibBuilder.loadTexts: applIndex.setDescription('An index to uniquely identify the network service application. This attribute is the index used for lexicographic ordering of the table.')
applName = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applName.setStatus('current')
if mibBuilder.loadTexts: applName.setDescription('The name the network service application chooses to be known by.')
applDirectoryName = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 3), DistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applDirectoryName.setStatus('current')
if mibBuilder.loadTexts: applDirectoryName.setDescription('The Distinguished Name of the directory entry where static information about this application is stored. An empty string indicates that no information about the application is available in the directory.')
applVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applVersion.setStatus('current')
if mibBuilder.loadTexts: applVersion.setDescription('The version of network service application software. This field is usually defined by the vendor of the network service application software.')
applUptime = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applUptime.setStatus('current')
if mibBuilder.loadTexts: applUptime.setDescription('The value of sysUpTime at the time the network service application was last initialized. If the application was last initialized prior to the last initialization of the network management subsystem, then this object contains a zero value.')
applOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("halted", 3), ("congested", 4), ("restarting", 5), ("quiescing", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: applOperStatus.setStatus('current')
if mibBuilder.loadTexts: applOperStatus.setDescription("Indicates the operational status of the network service application. 'down' indicates that the network service is not available. 'up' indicates that the network service is operational and available. 'halted' indicates that the service is operational but not available. 'congested' indicates that the service is operational but no additional inbound associations can be accommodated. 'restarting' indicates that the service is currently unavailable but is in the process of restarting and will be available soon. 'quiescing' indicates that service is currently operational but is in the process of shutting down. Additional inbound associations may be rejected by applications in the 'quiescing' state.")
applLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applLastChange.setStatus('current')
if mibBuilder.loadTexts: applLastChange.setDescription('The value of sysUpTime at the time the network service application entered its current operational state. If the current state was entered prior to the last initialization of the local network management subsystem, then this object contains a zero value.')
applInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applInboundAssociations.setStatus('current')
if mibBuilder.loadTexts: applInboundAssociations.setDescription('The number of current associations to the network service application, where it is the responder. An inbound association occurs when another application successfully connects to this one.')
applOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applOutboundAssociations.setStatus('current')
if mibBuilder.loadTexts: applOutboundAssociations.setDescription('The number of current associations to the network service application, where it is the initiator. An outbound association occurs when this application successfully connects to another one.')
applAccumulatedInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applAccumulatedInboundAssociations.setStatus('current')
if mibBuilder.loadTexts: applAccumulatedInboundAssociations.setDescription('The total number of associations to the application entity since application initialization, where it was the responder.')
applAccumulatedOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applAccumulatedOutboundAssociations.setStatus('current')
if mibBuilder.loadTexts: applAccumulatedOutboundAssociations.setDescription('The total number of associations to the application entity since application initialization, where it was the initiator.')
applLastInboundActivity = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applLastInboundActivity.setStatus('current')
if mibBuilder.loadTexts: applLastInboundActivity.setDescription('The value of sysUpTime at the time this application last had an inbound association. If the last association occurred prior to the last initialization of the network subsystem, then this object contains a zero value.')
applLastOutboundActivity = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applLastOutboundActivity.setStatus('current')
if mibBuilder.loadTexts: applLastOutboundActivity.setDescription('The value of sysUpTime at the time this application last had an outbound association. If the last association occurred prior to the last initialization of the network subsystem, then this object contains a zero value.')
applRejectedInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applRejectedInboundAssociations.setStatus('current')
if mibBuilder.loadTexts: applRejectedInboundAssociations.setDescription('The total number of inbound associations the application entity has rejected, since application initialization. Rejected associations are not counted in the accumulated association totals. Note that this only counts associations the application entity has rejected itself; it does not count rejections that occur at lower layers of the network. Thus, this counter may not reflect the true number of failed inbound associations.')
applFailedOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applFailedOutboundAssociations.setStatus('current')
if mibBuilder.loadTexts: applFailedOutboundAssociations.setDescription('The total number associations where the application entity is initiator and association establishment has failed, since application initialization. Failed associations are not counted in the accumulated association totals.')
applDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 16), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applDescription.setStatus('current')
if mibBuilder.loadTexts: applDescription.setDescription('A text description of the application. This information is intended to identify and briefly describe the application in a status display.')
applURL = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 17), URLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applURL.setStatus('current')
if mibBuilder.loadTexts: applURL.setDescription('A URL pointing to a description of the application. This information is intended to identify and describe the application in a status display.')
assocTable = MibTable((1, 3, 6, 1, 2, 1, 27, 2), )
if mibBuilder.loadTexts: assocTable.setStatus('current')
if mibBuilder.loadTexts: assocTable.setDescription('The table holding a set of all active application associations.')
assocEntry = MibTableRow((1, 3, 6, 1, 2, 1, 27, 2, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "NETWORK-SERVICES-MIB", "assocIndex"))
if mibBuilder.loadTexts: assocEntry.setStatus('current')
if mibBuilder.loadTexts: assocEntry.setDescription('An entry associated with an association for a network service application.')
assocIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: assocIndex.setStatus('current')
if mibBuilder.loadTexts: assocIndex.setDescription('An index to uniquely identify each association for a network service application. This attribute is the index that is used for lexicographic ordering of the table. Note that the table is also indexed by the applIndex.')
assocRemoteApplication = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocRemoteApplication.setStatus('current')
if mibBuilder.loadTexts: assocRemoteApplication.setDescription("The name of the system running remote network service application. For an IP-based application this should be either a domain name or IP address. For an OSI application it should be the string encoded distinguished name of the managed object. For X.400(1984) MTAs which do not have a Distinguished Name, the RFC 2156 syntax 'mta in globalid' used in X400-Received: fields can be used. Note, however, that not all connections an MTA makes are necessarily to another MTA.")
assocApplicationProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocApplicationProtocol.setStatus('current')
if mibBuilder.loadTexts: assocApplicationProtocol.setDescription("An identification of the protocol being used for the application. For an OSI Application, this will be the Application Context. For Internet applications, OID values of the form {applTCPProtoID port} or {applUDPProtoID port} are used for TCP-based and UDP-based protocols, respectively. In either case 'port' corresponds to the primary port number being used by the protocol. The usual IANA procedures may be used to register ports for new protocols.")
assocApplicationType = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("uainitiator", 1), ("uaresponder", 2), ("peerinitiator", 3), ("peerresponder", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocApplicationType.setStatus('current')
if mibBuilder.loadTexts: assocApplicationType.setDescription('This indicates whether the remote application is some type of client making use of this network service (e.g., a Mail User Agent) or a server acting as a peer. Also indicated is whether the remote end initiated an incoming connection to the network service or responded to an outgoing connection made by the local application. MTAs and messaging gateways are considered to be peers for the purposes of this variable.')
assocDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocDuration.setStatus('current')
if mibBuilder.loadTexts: assocDuration.setDescription('The value of sysUpTime at the time this association was started. If this association started prior to the last initialization of the network subsystem, then this object contains a zero value.')
applConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 3))
applGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 3, 1))
applCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 3, 2))
applCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 1)).setObjects(("NETWORK-SERVICES-MIB", "applRFC1565Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applCompliance = applCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: applCompliance.setDescription('The compliance statement for RFC 1565 implementations which support the Network Services Monitoring MIB for basic monitoring of network service applications. This is the basic compliance statement for RFC 1565.')
assocCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 2)).setObjects(("NETWORK-SERVICES-MIB", "applRFC1565Group"), ("NETWORK-SERVICES-MIB", "assocRFC1565Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocCompliance = assocCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: assocCompliance.setDescription('The compliance statement for RFC 1565 implementations which support the Network Services Monitoring MIB for basic monitoring of network service applications and their associations.')
applRFC2248Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 3)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2248Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC2248Compliance = applRFC2248Compliance.setStatus('deprecated')
if mibBuilder.loadTexts: applRFC2248Compliance.setDescription('The compliance statement for RFC 2248 implementations which support the Network Services Monitoring MIB for basic monitoring of network service applications.')
assocRFC2248Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 4)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2248Group"), ("NETWORK-SERVICES-MIB", "assocRFC2248Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC2248Compliance = assocRFC2248Compliance.setStatus('deprecated')
if mibBuilder.loadTexts: assocRFC2248Compliance.setDescription('The compliance statement for RFC 2248 implementations which support the Network Services Monitoring MIB for basic monitoring of network service applications and their associations.')
applRFC2788Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 5)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2788Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC2788Compliance = applRFC2788Compliance.setStatus('current')
if mibBuilder.loadTexts: applRFC2788Compliance.setDescription('The compliance statement for RFC 2788 implementations which support the Network Services Monitoring MIB for basic monitoring of network service applications.')
assocRFC2788Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 6)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2788Group"), ("NETWORK-SERVICES-MIB", "assocRFC2788Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC2788Compliance = assocRFC2788Compliance.setStatus('current')
if mibBuilder.loadTexts: assocRFC2788Compliance.setDescription('The compliance statement for RFC 2788 implementations which support the Network Services Monitoring MIB for basic monitoring of network service applications and their associations.')
applRFC1565Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 7)).setObjects(("NETWORK-SERVICES-MIB", "applName"), ("NETWORK-SERVICES-MIB", "applVersion"), ("NETWORK-SERVICES-MIB", "applUptime"), ("NETWORK-SERVICES-MIB", "applOperStatus"), ("NETWORK-SERVICES-MIB", "applLastChange"), ("NETWORK-SERVICES-MIB", "applInboundAssociations"), ("NETWORK-SERVICES-MIB", "applOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastInboundActivity"), ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"), ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC1565Group = applRFC1565Group.setStatus('obsolete')
if mibBuilder.loadTexts: applRFC1565Group.setDescription('A collection of objects providing basic monitoring of network service applications. This is the original set of such objects defined in RFC 1565.')
assocRFC1565Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 2)).setObjects(("NETWORK-SERVICES-MIB", "assocRemoteApplication"), ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"), ("NETWORK-SERVICES-MIB", "assocApplicationType"), ("NETWORK-SERVICES-MIB", "assocDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC1565Group = assocRFC1565Group.setStatus('obsolete')
if mibBuilder.loadTexts: assocRFC1565Group.setDescription("A collection of objects providing basic monitoring of network service applications' associations. This is the original set of such objects defined in RFC 1565.")
applRFC2248Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 3)).setObjects(("NETWORK-SERVICES-MIB", "applName"), ("NETWORK-SERVICES-MIB", "applVersion"), ("NETWORK-SERVICES-MIB", "applUptime"), ("NETWORK-SERVICES-MIB", "applOperStatus"), ("NETWORK-SERVICES-MIB", "applLastChange"), ("NETWORK-SERVICES-MIB", "applInboundAssociations"), ("NETWORK-SERVICES-MIB", "applOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastInboundActivity"), ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"), ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applDescription"), ("NETWORK-SERVICES-MIB", "applURL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC2248Group = applRFC2248Group.setStatus('deprecated')
if mibBuilder.loadTexts: applRFC2248Group.setDescription('A collection of objects providing basic monitoring of network service applications. This group was originally defined in RFC 2248; note that applDirectoryName is missing.')
assocRFC2248Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 4)).setObjects(("NETWORK-SERVICES-MIB", "assocRemoteApplication"), ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"), ("NETWORK-SERVICES-MIB", "assocApplicationType"), ("NETWORK-SERVICES-MIB", "assocDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC2248Group = assocRFC2248Group.setStatus('deprecated')
if mibBuilder.loadTexts: assocRFC2248Group.setDescription("A collection of objects providing basic monitoring of network service applications' associations. This group was originally defined by RFC 2248.")
applRFC2788Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 5)).setObjects(("NETWORK-SERVICES-MIB", "applName"), ("NETWORK-SERVICES-MIB", "applDirectoryName"), ("NETWORK-SERVICES-MIB", "applVersion"), ("NETWORK-SERVICES-MIB", "applUptime"), ("NETWORK-SERVICES-MIB", "applOperStatus"), ("NETWORK-SERVICES-MIB", "applLastChange"), ("NETWORK-SERVICES-MIB", "applInboundAssociations"), ("NETWORK-SERVICES-MIB", "applOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastInboundActivity"), ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"), ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applDescription"), ("NETWORK-SERVICES-MIB", "applURL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    applRFC2788Group = applRFC2788Group.setStatus('current')
if mibBuilder.loadTexts: applRFC2788Group.setDescription('A collection of objects providing basic monitoring of network service applications. This is the appropriate group for RFC 2788 -- it adds the applDirectoryName object missing in RFC 2248.')
assocRFC2788Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 6)).setObjects(("NETWORK-SERVICES-MIB", "assocRemoteApplication"), ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"), ("NETWORK-SERVICES-MIB", "assocApplicationType"), ("NETWORK-SERVICES-MIB", "assocDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    assocRFC2788Group = assocRFC2788Group.setStatus('current')
if mibBuilder.loadTexts: assocRFC2788Group.setDescription("A collection of objects providing basic monitoring of network service applications' associations. This is the appropriate group for RFC 2788.")
applTCPProtoID = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 4))
applUDPProtoID = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 5))
mibBuilder.exportSymbols("NETWORK-SERVICES-MIB", applTable=applTable, applName=applName, assocRFC2248Compliance=assocRFC2248Compliance, applRFC2248Group=applRFC2248Group, assocRFC2788Group=assocRFC2788Group, applConformance=applConformance, applAccumulatedInboundAssociations=applAccumulatedInboundAssociations, applCompliances=applCompliances, assocRFC2248Group=assocRFC2248Group, applUDPProtoID=applUDPProtoID, applIndex=applIndex, application=application, applEntry=applEntry, applOperStatus=applOperStatus, applRFC2248Compliance=applRFC2248Compliance, assocIndex=assocIndex, applVersion=applVersion, assocRemoteApplication=assocRemoteApplication, applURL=applURL, applRFC2788Compliance=applRFC2788Compliance, applUptime=applUptime, URLString=URLString, applInboundAssociations=applInboundAssociations, assocCompliance=assocCompliance, applAccumulatedOutboundAssociations=applAccumulatedOutboundAssociations, assocTable=assocTable, assocRFC2788Compliance=assocRFC2788Compliance, assocApplicationProtocol=assocApplicationProtocol, assocDuration=assocDuration, applRejectedInboundAssociations=applRejectedInboundAssociations, applDirectoryName=applDirectoryName, applLastInboundActivity=applLastInboundActivity, assocApplicationType=assocApplicationType, applRFC1565Group=applRFC1565Group, applFailedOutboundAssociations=applFailedOutboundAssociations, DistinguishedName=DistinguishedName, applDescription=applDescription, applTCPProtoID=applTCPProtoID, applGroups=applGroups, applCompliance=applCompliance, applLastOutboundActivity=applLastOutboundActivity, assocEntry=assocEntry, applRFC2788Group=applRFC2788Group, applLastChange=applLastChange, PYSNMP_MODULE_ID=application, assocRFC1565Group=assocRFC1565Group, applOutboundAssociations=applOutboundAssociations)
