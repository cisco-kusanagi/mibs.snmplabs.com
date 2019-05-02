#
# PySNMP MIB module RADIUS-AUTH-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADIUS-AUTH-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:06:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Unsigned32, Counter32, NotificationType, mib_2, MibIdentifier, Integer32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Unsigned32", "Counter32", "NotificationType", "mib-2", "MibIdentifier", "Integer32", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
radiusAuthClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 1, 2))
radiusAuthClientMIB.setRevisions(('2006-08-21 00:00', '1999-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: radiusAuthClientMIB.setRevisionsDescriptions(('Revised version as published in RFC 4668. This version obsoletes that of RFC 2618 by deprecating the MIB table containing IPv4-only address formats and defining a new table to add support for version neutral IP address formats. The remaining MIB objects from RFC 2618 are carried forward into this version.', 'Initial version as published in RFC 2618.',))
if mibBuilder.loadTexts: radiusAuthClientMIB.setLastUpdated('200608210000Z')
if mibBuilder.loadTexts: radiusAuthClientMIB.setOrganization('IETF RADIUS Extensions Working Group.')
if mibBuilder.loadTexts: radiusAuthClientMIB.setContactInfo(' Bernard Aboba Microsoft One Microsoft Way Redmond, WA 98052 US Phone: +1 425 936 6605 EMail: bernarda@microsoft.com')
if mibBuilder.loadTexts: radiusAuthClientMIB.setDescription('The MIB module for entities implementing the client side of the Remote Authentication Dial-In User Service (RADIUS) authentication protocol. Copyright (C) The Internet Society (2006). This version of this MIB module is part of RFC 4668; see the RFC itself for full legal notices.')
radiusMIB = ObjectIdentity((1, 3, 6, 1, 2, 1, 67))
if mibBuilder.loadTexts: radiusMIB.setStatus('current')
if mibBuilder.loadTexts: radiusMIB.setDescription('The OID assigned to RADIUS MIB work by the IANA.')
radiusAuthentication = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1))
radiusAuthClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1))
radiusAuthClient = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1))
radiusAuthClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientInvalidServerAddresses.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientInvalidServerAddresses.setDescription('The number of RADIUS Access-Response packets received from unknown addresses.')
radiusAuthClientIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientIdentifier.setReference('RFC 2865 section 5.32')
if mibBuilder.loadTexts: radiusAuthClientIdentifier.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientIdentifier.setDescription('The NAS-Identifier of the RADIUS authentication client. This is not necessarily the same as sysName in MIB II.')
radiusAuthServerTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3), )
if mibBuilder.loadTexts: radiusAuthServerTable.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthServerTable.setDescription('The (conceptual) table listing the RADIUS authentication servers with which the client shares a secret.')
radiusAuthServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1), ).setIndexNames((0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"))
if mibBuilder.loadTexts: radiusAuthServerEntry.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthServerEntry.setDescription('An entry (conceptual row) representing a RADIUS authentication server with which the client shares a secret.')
radiusAuthServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: radiusAuthServerIndex.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthServerIndex.setDescription('A number uniquely identifying each RADIUS Authentication server with which this client communicates.')
radiusAuthServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerAddress.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthServerAddress.setDescription('The IP address of the RADIUS authentication server referred to in this table entry.')
radiusAuthClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientServerPortNumber.setReference('RFC 2865 section 3')
if mibBuilder.loadTexts: radiusAuthClientServerPortNumber.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientServerPortNumber.setDescription('The UDP port the client is using to send requests to this server.')
radiusAuthClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientRoundTripTime.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientRoundTripTime.setDescription('The time interval (in hundredths of a second) between the most recent Access-Reply/Access-Challenge and the Access-Request that matched it from this RADIUS authentication server.')
radiusAuthClientAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRequests.setReference('RFC 2865 section 4.1')
if mibBuilder.loadTexts: radiusAuthClientAccessRequests.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientAccessRequests.setDescription('The number of RADIUS Access-Request packets sent to this server. This does not include retransmissions.')
radiusAuthClientAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRetransmissions.setReference('RFC 2865 sections 2.5, 4.1')
if mibBuilder.loadTexts: radiusAuthClientAccessRetransmissions.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientAccessRetransmissions.setDescription('The number of RADIUS Access-Request packets retransmitted to this RADIUS authentication server.')
radiusAuthClientAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessAccepts.setReference('RFC 2865 section 4.2')
if mibBuilder.loadTexts: radiusAuthClientAccessAccepts.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientAccessAccepts.setDescription('The number of RADIUS Access-Accept packets (valid or invalid) received from this server.')
radiusAuthClientAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRejects.setReference('RFC 2865 section 4.3')
if mibBuilder.loadTexts: radiusAuthClientAccessRejects.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientAccessRejects.setDescription('The number of RADIUS Access-Reject packets (valid or invalid) received from this server.')
radiusAuthClientAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessChallenges.setReference('RFC 2865 section 4.4')
if mibBuilder.loadTexts: radiusAuthClientAccessChallenges.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientAccessChallenges.setDescription('The number of RADIUS Access-Challenge packets (valid or invalid) received from this server.')
radiusAuthClientMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientMalformedAccessResponses.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientMalformedAccessResponses.setDescription('The number of malformed RADIUS Access-Response packets received from this server. Malformed packets include packets with an invalid length. Bad authenticators or Message Authenticator attributes or unknown types are not included as malformed access responses.')
radiusAuthClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 11), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientBadAuthenticators.setReference('RFC 2865 section 3, RFC 2869 section 5.14')
if mibBuilder.loadTexts: radiusAuthClientBadAuthenticators.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientBadAuthenticators.setDescription('The number of RADIUS Access-Response packets containing invalid authenticators or Message Authenticator attributes received from this server.')
radiusAuthClientPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientPendingRequests.setReference('RFC 2865 section 2')
if mibBuilder.loadTexts: radiusAuthClientPendingRequests.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientPendingRequests.setDescription('The number of RADIUS Access-Request packets destined for this server that have not yet timed out or received a response. This variable is incremented when an Access-Request is sent and decremented due to receipt of an Access-Accept, Access-Reject, Access-Challenge, timeout, or retransmission.')
radiusAuthClientTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 13), Counter32()).setUnits('timeouts').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientTimeouts.setReference('RFC 2865 section 2, RFC 2869 section 2.3.2')
if mibBuilder.loadTexts: radiusAuthClientTimeouts.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientTimeouts.setDescription('The number of authentication timeouts to this server. After a timeout, the client may retry to the same server, send to a different server, or give up. A retry to the same server is counted as a retransmit as well as a timeout. A send to a different server is counted as a Request as well as a timeout.')
radiusAuthClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 14), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientUnknownTypes.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientUnknownTypes.setDescription('The number of RADIUS packets of unknown type that were received from this server on the authentication port.')
radiusAuthClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 15), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientPacketsDropped.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientPacketsDropped.setDescription('The number of RADIUS packets that were received from this server on the authentication port and dropped for some other reason.')
radiusAuthServerExtTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4), )
if mibBuilder.loadTexts: radiusAuthServerExtTable.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServerExtTable.setDescription('The (conceptual) table listing the RADIUS authentication servers with which the client shares a secret.')
radiusAuthServerExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1), ).setIndexNames((0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerExtIndex"))
if mibBuilder.loadTexts: radiusAuthServerExtEntry.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServerExtEntry.setDescription('An entry (conceptual row) representing a RADIUS authentication server with which the client shares a secret.')
radiusAuthServerExtIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: radiusAuthServerExtIndex.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServerExtIndex.setDescription('A number uniquely identifying each RADIUS Authentication server with which this client communicates.')
radiusAuthServerInetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerInetAddressType.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServerInetAddressType.setDescription('The type of address format used for the radiusAuthServerInetAddress object.')
radiusAuthServerInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerInetAddress.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServerInetAddress.setDescription('The IP address of the RADIUS authentication server referred to in this table entry, using the version-neutral IP address format.')
radiusAuthClientServerInetPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 4), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientServerInetPortNumber.setReference('RFC 2865 section 3')
if mibBuilder.loadTexts: radiusAuthClientServerInetPortNumber.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientServerInetPortNumber.setDescription('The UDP port the client is using to send requests to this server. The value of zero (0) is invalid.')
radiusAuthClientExtRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtRoundTripTime.setReference('RFC 2865 section 2')
if mibBuilder.loadTexts: radiusAuthClientExtRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtRoundTripTime.setDescription('The time interval (in hundredths of a second) between the most recent Access-Reply/Access-Challenge and the Access-Request that matched it from this RADIUS authentication server.')
radiusAuthClientExtAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessRequests.setReference('RFC 2865 section 4.1')
if mibBuilder.loadTexts: radiusAuthClientExtAccessRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtAccessRequests.setDescription('The number of RADIUS Access-Request packets sent to this server. This does not include retransmissions. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessRetransmissions.setReference('RFC 2865 sections 2.5, 4.1')
if mibBuilder.loadTexts: radiusAuthClientExtAccessRetransmissions.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtAccessRetransmissions.setDescription('The number of RADIUS Access-Request packets retransmitted to this RADIUS authentication server. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessAccepts.setReference('RFC 2865 section 4.2')
if mibBuilder.loadTexts: radiusAuthClientExtAccessAccepts.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtAccessAccepts.setDescription('The number of RADIUS Access-Accept packets (valid or invalid) received from this server. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessRejects.setReference('RFC 2865 section 4.3')
if mibBuilder.loadTexts: radiusAuthClientExtAccessRejects.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtAccessRejects.setDescription('The number of RADIUS Access-Reject packets (valid or invalid) received from this server. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessChallenges.setReference('RFC 2865 section 4.4')
if mibBuilder.loadTexts: radiusAuthClientExtAccessChallenges.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtAccessChallenges.setDescription('The number of RADIUS Access-Challenge packets (valid or invalid) received from this server. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 11), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtMalformedAccessResponses.setReference('RFC 2865 sections 3, 4')
if mibBuilder.loadTexts: radiusAuthClientExtMalformedAccessResponses.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtMalformedAccessResponses.setDescription('The number of malformed RADIUS Access-Response packets received from this server. Malformed packets include packets with an invalid length. Bad authenticators or Message Authenticator attributes or unknown types are not included as malformed access responses. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 12), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtBadAuthenticators.setReference('RFC 2865 section 3')
if mibBuilder.loadTexts: radiusAuthClientExtBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtBadAuthenticators.setDescription('The number of RADIUS Access-Response packets containing invalid authenticators or Message Authenticator attributes received from this server. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 13), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtPendingRequests.setReference('RFC 2865 section 2')
if mibBuilder.loadTexts: radiusAuthClientExtPendingRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtPendingRequests.setDescription('The number of RADIUS Access-Request packets destined for this server that have not yet timed out or received a response. This variable is incremented when an Access-Request is sent and decremented due to receipt of an Access-Accept, Access-Reject, Access-Challenge, timeout, or retransmission.')
radiusAuthClientExtTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 14), Counter32()).setUnits('timeouts').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtTimeouts.setReference('RFC 2865 sections 2.5, 4.1')
if mibBuilder.loadTexts: radiusAuthClientExtTimeouts.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtTimeouts.setDescription('The number of authentication timeouts to this server. After a timeout, the client may retry to the same server, send to a different server, or give up. A retry to the same server is counted as a retransmit as well as a timeout. A send to a different server is counted as a Request as well as a timeout. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 15), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtUnknownTypes.setReference('RFC 2865 section 4')
if mibBuilder.loadTexts: radiusAuthClientExtUnknownTypes.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtUnknownTypes.setDescription('The number of RADIUS packets of unknown type that were received from this server on the authentication port. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 16), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtPacketsDropped.setDescription('The number of RADIUS packets that were received from this server on the authentication port and dropped for some other reason. This counter may experience a discontinuity when the RADIUS Client module within the managed entity is reinitialized, as indicated by the current value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientCounterDiscontinuity = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 17), TimeTicks()).setUnits('centiseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientCounterDiscontinuity.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientCounterDiscontinuity.setDescription('The number of centiseconds since the last discontinuity in the RADIUS Client counters. A discontinuity may be the result of a reinitialization of the RADIUS Client module within the managed entity.')
radiusAuthClientMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2))
radiusAuthClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1))
radiusAuthClientMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2))
radiusAuthClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 1)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthClientMIBCompliance = radiusAuthClientMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientMIBCompliance.setDescription('The compliance statement for authentication clients implementing the RADIUS Authentication Client MIB. Implementation of this module is for IPv4-only entities, or for backwards compatibility use with entities that support both IPv4 and IPv6.')
radiusAuthClientExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 2)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthClientExtMIBCompliance = radiusAuthClientExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtMIBCompliance.setDescription('The compliance statement for authentication clients implementing the RADIUS Authentication Client IPv6 Extensions MIB. Implementation of this module is for entities that support IPv6, or support IPv4 and IPv6.')
radiusAuthClientMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 1)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientRoundTripTime"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRetransmissions"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessAccepts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRejects"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessChallenges"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMalformedAccessResponses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientBadAuthenticators"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPendingRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientTimeouts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientUnknownTypes"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPacketsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthClientMIBGroup = radiusAuthClientMIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAuthClientMIBGroup.setDescription('The basic collection of objects providing management of RADIUS Authentication Clients.')
radiusAuthClientExtMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 2)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerInetAddressType"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerInetAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerInetPortNumber"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtRoundTripTime"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRetransmissions"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessAccepts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRejects"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessChallenges"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtMalformedAccessResponses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtBadAuthenticators"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtPendingRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtTimeouts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtUnknownTypes"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtPacketsDropped"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientCounterDiscontinuity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthClientExtMIBGroup = radiusAuthClientExtMIBGroup.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientExtMIBGroup.setDescription('The collection of extended objects providing management of RADIUS Authentication Clients using version-neutral IP address format.')
mibBuilder.exportSymbols("RADIUS-AUTH-CLIENT-MIB", radiusMIB=radiusMIB, radiusAuthentication=radiusAuthentication, radiusAuthServerExtEntry=radiusAuthServerExtEntry, radiusAuthServerIndex=radiusAuthServerIndex, radiusAuthClientExtAccessChallenges=radiusAuthClientExtAccessChallenges, radiusAuthClientMalformedAccessResponses=radiusAuthClientMalformedAccessResponses, radiusAuthClientIdentifier=radiusAuthClientIdentifier, radiusAuthClientExtAccessRejects=radiusAuthClientExtAccessRejects, radiusAuthClientCounterDiscontinuity=radiusAuthClientCounterDiscontinuity, radiusAuthClientExtPendingRequests=radiusAuthClientExtPendingRequests, radiusAuthClientBadAuthenticators=radiusAuthClientBadAuthenticators, radiusAuthServerInetAddress=radiusAuthServerInetAddress, radiusAuthClientMIB=radiusAuthClientMIB, radiusAuthClientMIBCompliance=radiusAuthClientMIBCompliance, radiusAuthServerExtIndex=radiusAuthServerExtIndex, radiusAuthClientServerInetPortNumber=radiusAuthClientServerInetPortNumber, radiusAuthServerEntry=radiusAuthServerEntry, radiusAuthServerAddress=radiusAuthServerAddress, radiusAuthClientMIBGroup=radiusAuthClientMIBGroup, radiusAuthServerTable=radiusAuthServerTable, radiusAuthClientAccessChallenges=radiusAuthClientAccessChallenges, radiusAuthClientAccessRejects=radiusAuthClientAccessRejects, radiusAuthClientExtBadAuthenticators=radiusAuthClientExtBadAuthenticators, radiusAuthClientServerPortNumber=radiusAuthClientServerPortNumber, radiusAuthClientAccessRequests=radiusAuthClientAccessRequests, radiusAuthClientExtAccessRequests=radiusAuthClientExtAccessRequests, radiusAuthClientMIBCompliances=radiusAuthClientMIBCompliances, radiusAuthClientUnknownTypes=radiusAuthClientUnknownTypes, radiusAuthClientExtAccessRetransmissions=radiusAuthClientExtAccessRetransmissions, radiusAuthClientMIBGroups=radiusAuthClientMIBGroups, radiusAuthClientExtMIBCompliance=radiusAuthClientExtMIBCompliance, radiusAuthClientInvalidServerAddresses=radiusAuthClientInvalidServerAddresses, radiusAuthClientExtAccessAccepts=radiusAuthClientExtAccessAccepts, radiusAuthClientExtPacketsDropped=radiusAuthClientExtPacketsDropped, radiusAuthServerInetAddressType=radiusAuthServerInetAddressType, radiusAuthClientMIBConformance=radiusAuthClientMIBConformance, radiusAuthClient=radiusAuthClient, radiusAuthClientPacketsDropped=radiusAuthClientPacketsDropped, radiusAuthClientExtTimeouts=radiusAuthClientExtTimeouts, radiusAuthClientExtMIBGroup=radiusAuthClientExtMIBGroup, radiusAuthClientAccessRetransmissions=radiusAuthClientAccessRetransmissions, radiusAuthClientExtMalformedAccessResponses=radiusAuthClientExtMalformedAccessResponses, radiusAuthClientExtUnknownTypes=radiusAuthClientExtUnknownTypes, radiusAuthClientRoundTripTime=radiusAuthClientRoundTripTime, radiusAuthClientPendingRequests=radiusAuthClientPendingRequests, radiusAuthClientTimeouts=radiusAuthClientTimeouts, radiusAuthClientExtRoundTripTime=radiusAuthClientExtRoundTripTime, radiusAuthServerExtTable=radiusAuthServerExtTable, radiusAuthClientMIBObjects=radiusAuthClientMIBObjects, PYSNMP_MODULE_ID=radiusAuthClientMIB, radiusAuthClientAccessAccepts=radiusAuthClientAccessAccepts)
