#
# PySNMP MIB module JUNIPER-RSVP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-RSVP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Integer32, ModuleIdentity, iso, NotificationType, TimeTicks, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Integer32", "ModuleIdentity", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Counter64")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
jnxRsvpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 30))
jnxRsvpMIB.setRevisions(('2007-06-28 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxRsvpMIB.setRevisionsDescriptions(('Extended jnxRsvpSessionName to support names up to 64 characters',))
if mibBuilder.loadTexts: jnxRsvpMIB.setLastUpdated('200402031905Z')
if mibBuilder.loadTexts: jnxRsvpMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxRsvpMIB.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxRsvpMIB.setDescription('The MIB modules for Resource ReSerVation Protocol.')
jnxRsvpOperation = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1))
jnxRsvpSessionTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1), )
if mibBuilder.loadTexts: jnxRsvpSessionTable.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionTable.setDescription('Defines the jnxRsvpSession Table for RSVP Sessions.')
jnxRsvpSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1), ).setIndexNames((0, "JUNIPER-RSVP-MIB", "jnxRsvpSessionName"), (0, "JUNIPER-RSVP-MIB", "jnxRsvpSessionIndex"))
if mibBuilder.loadTexts: jnxRsvpSessionEntry.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionEntry.setDescription('Defines an entry in the jnxRsvpSessionTable. The first index element jnxRsvpSessionName is similar to the LSP name in the MPLS MIB and can be used to co-relate the mplsLspEntry to an RSVP session entry. There could be multiple entries with the same jnxRsvpSessionName and hence the need for a secondary index which is just an Unsigned32 to identify each of them uniquely. A management application may walk through all entries with the same jnxRsvpSessionName and based on the other RSVP session information in each entry, such as jnxRsvpSessionFrom and/or jnxRsvpSessionTo may decide to query a particular RSVP session.')
jnxRsvpSessionName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: jnxRsvpSessionName.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionName.setDescription('Name of the RSVP Session. This is the same as LSP name.')
jnxRsvpSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: jnxRsvpSessionIndex.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionIndex.setDescription('RSVP Session index.')
jnxRsvpSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionState.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionState.setDescription('The operational state of the RSVP Session.')
jnxRsvpSessionFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionFrom.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionFrom.setDescription('Source IP address of this RSVP session.')
jnxRsvpSessionTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionTo.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionTo.setDescription('Destination IP address of this RSVP session.')
jnxRsvpSessionLspId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionLspId.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionLspId.setDescription('LSP ID of the sender for this RSVP session.')
jnxRsvpSessionTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionTunnelId.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionTunnelId.setDescription('Tunnel ID for the RSVP session.')
jnxRsvpSessionPathType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionPathType.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionPathType.setDescription('If the head-end router signals the type of path corresponding to an RSVP session; viz. primary or secondary path, then this information can be used on other routers as well to associate RSVP session information to an MPLS path of an LSP (tunnel).')
jnxRsvpSessionRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ingress", 1), ("transit", 2), ("egress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionRole.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionRole.setDescription('This value signifies the role of an RSVP session with respect to the start and end points of the session. This value MUST be set to ingress(1) at the head-end (source) of this session. This value MUST be set to egress(3) at the tail-end (destination) of the RSVP session. This value MUST be set to transit(2) on any other intermediate nodes that this RSVP session exists on.')
jnxRsvpSessionDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which any one or more of this RSVP Session's counters suffered a discontinuity. The relevant counters are jnxRsvpSessionMplsOctets and jnxRsvpSessionMplsPackets. If no such discontinuities have occurred since the last re-initialization of the local management subsystem, then then this object contains a zero value.")
jnxRsvpSessionMplsOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionMplsOctets.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionMplsOctets.setDescription('The number of MPLS octets that have been forwarded over this RSVP Session. The number reported is not realtime, may subject to several minutes delay. The delay is controllable by mpls statistics gathering interval, which by default is once every 5 minutes. If mpls statistics gathering is not enabled, this number will not increment. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of jnxRsvpSessionDiscontinuityTime.')
jnxRsvpSessionMplsPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionMplsPackets.setStatus('current')
if mibBuilder.loadTexts: jnxRsvpSessionMplsPackets.setDescription('The number of MPLS packets that have been forwarded over this RSVP Session. The number reported is not realtime, may subject to several minutes delay. The delay is controllable by mpls statistics gathering interval, which by default is once every 5 minutes. If mpls statistics gathering is not enabled, this number will not increment. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of jnxRsvpSessionDiscontinuityTime.')
mibBuilder.exportSymbols("JUNIPER-RSVP-MIB", jnxRsvpSessionLspId=jnxRsvpSessionLspId, jnxRsvpSessionEntry=jnxRsvpSessionEntry, jnxRsvpSessionRole=jnxRsvpSessionRole, jnxRsvpSessionDiscontinuityTime=jnxRsvpSessionDiscontinuityTime, jnxRsvpSessionMplsOctets=jnxRsvpSessionMplsOctets, jnxRsvpSessionFrom=jnxRsvpSessionFrom, jnxRsvpSessionMplsPackets=jnxRsvpSessionMplsPackets, jnxRsvpSessionPathType=jnxRsvpSessionPathType, jnxRsvpSessionTable=jnxRsvpSessionTable, jnxRsvpSessionTunnelId=jnxRsvpSessionTunnelId, jnxRsvpSessionState=jnxRsvpSessionState, jnxRsvpSessionIndex=jnxRsvpSessionIndex, jnxRsvpMIB=jnxRsvpMIB, PYSNMP_MODULE_ID=jnxRsvpMIB, jnxRsvpSessionTo=jnxRsvpSessionTo, jnxRsvpOperation=jnxRsvpOperation, jnxRsvpSessionName=jnxRsvpSessionName)
