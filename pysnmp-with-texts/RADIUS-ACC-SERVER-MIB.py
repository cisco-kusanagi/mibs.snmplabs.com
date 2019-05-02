#
# PySNMP MIB module RADIUS-ACC-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADIUS-ACC-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:44:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
mib_2, iso, MibIdentifier, ObjectIdentity, Gauge32, TimeTicks, Bits, ModuleIdentity, NotificationType, Integer32, Counter32, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "iso", "MibIdentifier", "ObjectIdentity", "Gauge32", "TimeTicks", "Bits", "ModuleIdentity", "NotificationType", "Integer32", "Counter32", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
radiusAccServMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 2, 1))
radiusAccServMIB.setRevisions(('2006-08-21 00:00', '1999-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: radiusAccServMIB.setRevisionsDescriptions(('Revised version as published in RFC 4671. This version obsoletes that of RFC 2621 by deprecating the MIB table containing IPv4-only address formats and defining a new table to add support for version- neutral IP address formats. The remaining MIB objects from RFC 2621 are carried forward into this version.', 'Initial version as published in RFC 2621.',))
if mibBuilder.loadTexts: radiusAccServMIB.setLastUpdated('200608210000Z')
if mibBuilder.loadTexts: radiusAccServMIB.setOrganization('IETF RADIUS Extensions Working Group.')
if mibBuilder.loadTexts: radiusAccServMIB.setContactInfo(' Bernard Aboba Microsoft One Microsoft Way Redmond, WA 98052 US Phone: +1 425 936 6605 EMail: bernarda@microsoft.com')
if mibBuilder.loadTexts: radiusAccServMIB.setDescription('The MIB module for entities implementing the server side of the Remote Authentication Dial-In User Service (RADIUS) accounting protocol. Copyright (C) The Internet Society (2006). This version of this MIB module is part of RFC 4671; see the RFC itself for full legal notices.')
radiusMIB = ObjectIdentity((1, 3, 6, 1, 2, 1, 67))
if mibBuilder.loadTexts: radiusMIB.setStatus('current')
if mibBuilder.loadTexts: radiusMIB.setDescription('The OID assigned to RADIUS MIB work by the IANA.')
radiusAccounting = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2))
radiusAccServMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 1))
radiusAccServ = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1))
radiusAccServIdent = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServIdent.setStatus('current')
if mibBuilder.loadTexts: radiusAccServIdent.setDescription("The implementation identification string for the RADIUS accounting server software in use on the system, for example, 'FNS-2.1'.")
radiusAccServUpTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServUpTime.setStatus('current')
if mibBuilder.loadTexts: radiusAccServUpTime.setDescription('If the server has a persistent state (e.g., a process), this value will be the time elapsed (in hundredths of a second) since the server process was started. For software without persistent state, this value will be zero.')
radiusAccServResetTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServResetTime.setStatus('current')
if mibBuilder.loadTexts: radiusAccServResetTime.setDescription("If the server has a persistent state (e.g., a process) and supports a 'reset' operation (e.g., can be told to re-read configuration files), this value will be the time elapsed (in hundredths of a second) since the server was 'reset.' For software that does not have persistence or does not support a 'reset' operation, this value will be zero.")
radiusAccServConfigReset = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusAccServConfigReset.setStatus('current')
if mibBuilder.loadTexts: radiusAccServConfigReset.setDescription('Status/action object to reinitialize any persistent server state. When set to reset(2), any persistent server state (such as a process) is reinitialized as if the server had just been started. This value will never be returned by a read operation. When read, one of the following values will be returned: other(1) - server in some unknown state; initializing(3) - server (re)initializing; running(4) - server currently running.')
radiusAccServTotalRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServTotalRequests.setReference('RFC 2866 section 4.1')
if mibBuilder.loadTexts: radiusAccServTotalRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAccServTotalRequests.setDescription('The number of packets received on the accounting port.')
radiusAccServTotalInvalidRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServTotalInvalidRequests.setReference('RFC 2866 sections 2, 4.1')
if mibBuilder.loadTexts: radiusAccServTotalInvalidRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAccServTotalInvalidRequests.setDescription('The number of RADIUS Accounting-Request packets received from unknown addresses.')
radiusAccServTotalDupRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServTotalDupRequests.setReference('RFC 2866 section 4.1')
if mibBuilder.loadTexts: radiusAccServTotalDupRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAccServTotalDupRequests.setDescription('The number of duplicate RADIUS Accounting-Request packets received.')
radiusAccServTotalResponses = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServTotalResponses.setReference('RFC 2866 section 4.2')
if mibBuilder.loadTexts: radiusAccServTotalResponses.setStatus('current')
if mibBuilder.loadTexts: radiusAccServTotalResponses.setDescription('The number of RADIUS Accounting-Response packets sent.')
radiusAccServTotalMalformedRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServTotalMalformedRequests.setReference('RFC 2866 section 3')
if mibBuilder.loadTexts: radiusAccServTotalMalformedRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAccServTotalMalformedRequests.setDescription('The number of malformed RADIUS Accounting-Request packets received. Bad authenticators or unknown types are not included as malformed Access-Requests.')
radiusAccServTotalBadAuthenticators = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServTotalBadAuthenticators.setReference('RFC 2866 section 3')
if mibBuilder.loadTexts: radiusAccServTotalBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: radiusAccServTotalBadAuthenticators.setDescription('The number of RADIUS Accounting-Request packets that contained an invalid authenticator.')
radiusAccServTotalPacketsDropped = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 11), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServTotalPacketsDropped.setReference('RFC 2866 section 3')
if mibBuilder.loadTexts: radiusAccServTotalPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: radiusAccServTotalPacketsDropped.setDescription('The number of incoming packets silently discarded for a reason other than malformed, bad authenticators, or unknown types.')
radiusAccServTotalNoRecords = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 12), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServTotalNoRecords.setStatus('current')
if mibBuilder.loadTexts: radiusAccServTotalNoRecords.setDescription('The number of RADIUS Accounting-Request packets that were received and responded to but not recorded.')
radiusAccServTotalUnknownTypes = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 13), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServTotalUnknownTypes.setReference('RFC 2866 section 4')
if mibBuilder.loadTexts: radiusAccServTotalUnknownTypes.setStatus('current')
if mibBuilder.loadTexts: radiusAccServTotalUnknownTypes.setDescription('The number of RADIUS packets of unknown type that were received.')
radiusAccClientTable = MibTable((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14), )
if mibBuilder.loadTexts: radiusAccClientTable.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccClientTable.setDescription('The (conceptual) table listing the RADIUS accounting clients with which the server shares a secret.')
radiusAccClientEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1), ).setIndexNames((0, "RADIUS-ACC-SERVER-MIB", "radiusAccClientIndex"))
if mibBuilder.loadTexts: radiusAccClientEntry.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccClientEntry.setDescription('An entry (conceptual row) representing a RADIUS accounting client with which the server shares a secret.')
radiusAccClientIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: radiusAccClientIndex.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccClientIndex.setDescription('A number uniquely identifying each RADIUS accounting client with which this server communicates.')
radiusAccClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientAddress.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccClientAddress.setDescription('The NAS-IP-Address of the RADIUS accounting client referred to in this table entry.')
radiusAccClientID = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientID.setReference('RFC 2865 section 5.32')
if mibBuilder.loadTexts: radiusAccClientID.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccClientID.setDescription('The NAS-Identifier of the RADIUS accounting client referred to in this table entry. This is not necessarily the same as sysName in MIB II.')
radiusAccServPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServPacketsDropped.setReference('RFC 2866 section 3')
if mibBuilder.loadTexts: radiusAccServPacketsDropped.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServPacketsDropped.setDescription('The number of incoming packets received from this client and silently discarded for a reason other than malformed, bad authenticators, or unknown types.')
radiusAccServRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServRequests.setReference('RFC 2866 section 4.1')
if mibBuilder.loadTexts: radiusAccServRequests.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServRequests.setDescription('The number of packets received from this client on the accounting port.')
radiusAccServDupRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServDupRequests.setReference('RFC 2866 section 4.1')
if mibBuilder.loadTexts: radiusAccServDupRequests.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServDupRequests.setDescription('The number of duplicate RADIUS Accounting-Request packets received from this client.')
radiusAccServResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServResponses.setReference('RFC 2866 section 4.2')
if mibBuilder.loadTexts: radiusAccServResponses.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServResponses.setDescription('The number of RADIUS Accounting-Response packets sent to this client.')
radiusAccServBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServBadAuthenticators.setReference('RFC 2866 section 3')
if mibBuilder.loadTexts: radiusAccServBadAuthenticators.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServBadAuthenticators.setDescription('The number of RADIUS Accounting-Request packets that contained invalid authenticators received from this client.')
radiusAccServMalformedRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServMalformedRequests.setReference('RFC 2866 section 3')
if mibBuilder.loadTexts: radiusAccServMalformedRequests.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServMalformedRequests.setDescription('The number of malformed RADIUS Accounting-Request packets that were received from this client. Bad authenticators and unknown types are not included as malformed Accounting-Requests.')
radiusAccServNoRecords = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServNoRecords.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServNoRecords.setDescription('The number of RADIUS Accounting-Request packets that were received and responded to but not recorded.')
radiusAccServUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 11), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServUnknownTypes.setReference('RFC 2866 section 4')
if mibBuilder.loadTexts: radiusAccServUnknownTypes.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServUnknownTypes.setDescription('The number of RADIUS packets of unknown type that were received from this client.')
radiusAccClientExtTable = MibTable((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15), )
if mibBuilder.loadTexts: radiusAccClientExtTable.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientExtTable.setDescription('The (conceptual) table listing the RADIUS accounting clients with which the server shares a secret.')
radiusAccClientExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1), ).setIndexNames((0, "RADIUS-ACC-SERVER-MIB", "radiusAccClientExtIndex"))
if mibBuilder.loadTexts: radiusAccClientExtEntry.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientExtEntry.setDescription('An entry (conceptual row) representing a RADIUS accounting client with which the server shares a secret.')
radiusAccClientExtIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: radiusAccClientExtIndex.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientExtIndex.setDescription('A number uniquely identifying each RADIUS accounting client with which this server communicates.')
radiusAccClientInetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientInetAddressType.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientInetAddressType.setDescription('The type of address format used for the radiusAccClientInetAddress object.')
radiusAccClientInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientInetAddress.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientInetAddress.setDescription('The IP address of the RADIUS accounting client referred to in this table entry, using the IPv6 address format.')
radiusAccClientExtID = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientExtID.setReference('RFC 2865 section 5.32')
if mibBuilder.loadTexts: radiusAccClientExtID.setStatus('current')
if mibBuilder.loadTexts: radiusAccClientExtID.setDescription('The NAS-Identifier of the RADIUS accounting client referred to in this table entry. This is not necessarily the same as sysName in MIB II.')
radiusAccServExtPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtPacketsDropped.setReference('RFC 2866 section 3')
if mibBuilder.loadTexts: radiusAccServExtPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtPacketsDropped.setDescription('The number of incoming packets received from this client and silently discarded for a reason other than malformed, bad authenticators, or unknown types. This counter may experience a discontinuity when the RADIUS Accounting Server module within the managed entity is reinitialized, as indicated by the current value of radiusAccServerCounterDiscontinuity.')
radiusAccServExtRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtRequests.setReference('RFC 2866 section 4.1')
if mibBuilder.loadTexts: radiusAccServExtRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtRequests.setDescription('The number of packets received from this client on the accounting port. This counter may experience a discontinuity when the RADIUS Accounting Server module within the managed entity is reinitialized, as indicated by the current value of radiusAccServerCounterDiscontinuity.')
radiusAccServExtDupRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtDupRequests.setReference('RFC 2866 section 4.1')
if mibBuilder.loadTexts: radiusAccServExtDupRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtDupRequests.setDescription('The number of duplicate RADIUS Accounting-Request packets received from this client. This counter may experience a discontinuity when the RADIUS Accounting Server module within the managed entity is reinitialized, as indicated by the current value of radiusAccServerCounterDiscontinuity.')
radiusAccServExtResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtResponses.setReference('RFC 2866 section 4.2')
if mibBuilder.loadTexts: radiusAccServExtResponses.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtResponses.setDescription('The number of RADIUS Accounting-Response packets sent to this client. This counter may experience a discontinuity when the RADIUS Accounting Server module within the managed entity is reinitialized, as indicated by the current value of radiusAccServerCounterDiscontinuity.')
radiusAccServExtBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtBadAuthenticators.setReference('RFC 2866 section 3')
if mibBuilder.loadTexts: radiusAccServExtBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtBadAuthenticators.setDescription('The number of RADIUS Accounting-Request packets that contained invalid authenticators received from this client. This counter may experience a discontinuity when the RADIUS Accounting Server module within the managed entity is reinitialized, as indicated by the current value of radiusAccServerCounterDiscontinuity.')
radiusAccServExtMalformedRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtMalformedRequests.setReference('RFC 2866 section 3')
if mibBuilder.loadTexts: radiusAccServExtMalformedRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtMalformedRequests.setDescription('The number of malformed RADIUS Accounting-Request packets that were received from this client. Bad authenticators and unknown types are not included as malformed Accounting-Requests. This counter may experience a discontinuity when the RADIUS Accounting Server module within the managed entity is reinitialized, as indicated by the current value of radiusAccServerCounterDiscontinuity.')
radiusAccServExtNoRecords = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 11), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtNoRecords.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtNoRecords.setDescription('The number of RADIUS Accounting-Request packets that were received and responded to but not recorded. This counter may experience a discontinuity when the RADIUS Accounting Server module within the managed entity is reinitialized, as indicated by the current value of radiusAccServerCounterDiscontinuity.')
radiusAccServExtUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 12), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtUnknownTypes.setReference('RFC 2866 section 4')
if mibBuilder.loadTexts: radiusAccServExtUnknownTypes.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtUnknownTypes.setDescription('The number of RADIUS packets of unknown type that were received from this client. This counter may experience a discontinuity when the RADIUS Accounting Server module within the managed entity is reinitialized, as indicated by the current value of radiusAccServerCounterDiscontinuity.')
radiusAccServerCounterDiscontinuity = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 13), TimeTicks()).setUnits('centiseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServerCounterDiscontinuity.setStatus('current')
if mibBuilder.loadTexts: radiusAccServerCounterDiscontinuity.setDescription('The number of centiseconds since the last discontinuity in the RADIUS Accounting Server counters. A discontinuity may be the result of a reinitialization of the RADIUS Accounting Server module within the managed entity.')
radiusAccServMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 2))
radiusAccServMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1))
radiusAccServMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2))
radiusAccServMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1, 1)).setObjects(("RADIUS-ACC-SERVER-MIB", "radiusAccServMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAccServMIBCompliance = radiusAccServMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServMIBCompliance.setDescription('The compliance statement for accounting servers implementing the RADIUS Accounting Server MIB. Implementation of this module is for IPv4-only entities, or for backwards compatibility use with entities that support both IPv4 and IPv6.')
radiusAccServExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1, 2)).setObjects(("RADIUS-ACC-SERVER-MIB", "radiusAccServExtMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAccServExtMIBCompliance = radiusAccServExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtMIBCompliance.setDescription('The compliance statement for accounting servers implementing the RADIUS Accounting Server IPv6 Extensions MIB. Implementation of this module is for entities that support IPv6, or support IPv4 and IPv6.')
radiusAccServMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 1)).setObjects(("RADIUS-ACC-SERVER-MIB", "radiusAccServIdent"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServUpTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServResetTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServConfigReset"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalInvalidRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalNoRecords"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalUnknownTypes"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientAddress"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientID"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServNoRecords"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServUnknownTypes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAccServMIBGroup = radiusAccServMIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: radiusAccServMIBGroup.setDescription('The collection of objects providing management of a RADIUS Accounting Server.')
radiusAccServExtMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 2)).setObjects(("RADIUS-ACC-SERVER-MIB", "radiusAccServIdent"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServUpTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServResetTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServConfigReset"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalInvalidRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalNoRecords"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalUnknownTypes"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientInetAddressType"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientInetAddress"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientExtID"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtNoRecords"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtUnknownTypes"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServerCounterDiscontinuity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAccServExtMIBGroup = radiusAccServExtMIBGroup.setStatus('current')
if mibBuilder.loadTexts: radiusAccServExtMIBGroup.setDescription('The collection of objects providing management of a RADIUS Accounting Server.')
mibBuilder.exportSymbols("RADIUS-ACC-SERVER-MIB", radiusAccServMalformedRequests=radiusAccServMalformedRequests, radiusAccServerCounterDiscontinuity=radiusAccServerCounterDiscontinuity, radiusAccServExtDupRequests=radiusAccServExtDupRequests, radiusAccServTotalMalformedRequests=radiusAccServTotalMalformedRequests, radiusAccClientTable=radiusAccClientTable, radiusAccServMIBCompliances=radiusAccServMIBCompliances, radiusAccServResponses=radiusAccServResponses, radiusAccServExtMIBCompliance=radiusAccServExtMIBCompliance, radiusAccServUpTime=radiusAccServUpTime, radiusAccServExtResponses=radiusAccServExtResponses, radiusAccServMIBGroup=radiusAccServMIBGroup, radiusAccServTotalRequests=radiusAccServTotalRequests, radiusAccClientIndex=radiusAccClientIndex, radiusAccServMIB=radiusAccServMIB, radiusAccServExtMIBGroup=radiusAccServExtMIBGroup, radiusAccClientExtIndex=radiusAccClientExtIndex, radiusAccClientInetAddressType=radiusAccClientInetAddressType, radiusAccServConfigReset=radiusAccServConfigReset, radiusAccServMIBGroups=radiusAccServMIBGroups, PYSNMP_MODULE_ID=radiusAccServMIB, radiusAccServExtRequests=radiusAccServExtRequests, radiusAccServExtMalformedRequests=radiusAccServExtMalformedRequests, radiusAccServTotalDupRequests=radiusAccServTotalDupRequests, radiusAccServExtBadAuthenticators=radiusAccServExtBadAuthenticators, radiusAccServPacketsDropped=radiusAccServPacketsDropped, radiusAccServBadAuthenticators=radiusAccServBadAuthenticators, radiusAccounting=radiusAccounting, radiusAccServNoRecords=radiusAccServNoRecords, radiusAccServResetTime=radiusAccServResetTime, radiusAccClientExtID=radiusAccClientExtID, radiusAccServMIBConformance=radiusAccServMIBConformance, radiusAccServTotalNoRecords=radiusAccServTotalNoRecords, radiusAccServExtUnknownTypes=radiusAccServExtUnknownTypes, radiusAccServTotalUnknownTypes=radiusAccServTotalUnknownTypes, radiusAccServExtNoRecords=radiusAccServExtNoRecords, radiusAccServTotalBadAuthenticators=radiusAccServTotalBadAuthenticators, radiusAccServTotalInvalidRequests=radiusAccServTotalInvalidRequests, radiusAccClientInetAddress=radiusAccClientInetAddress, radiusAccServTotalResponses=radiusAccServTotalResponses, radiusAccServMIBObjects=radiusAccServMIBObjects, radiusAccServTotalPacketsDropped=radiusAccServTotalPacketsDropped, radiusAccClientID=radiusAccClientID, radiusAccServExtPacketsDropped=radiusAccServExtPacketsDropped, radiusMIB=radiusMIB, radiusAccServ=radiusAccServ, radiusAccServMIBCompliance=radiusAccServMIBCompliance, radiusAccServRequests=radiusAccServRequests, radiusAccServUnknownTypes=radiusAccServUnknownTypes, radiusAccServDupRequests=radiusAccServDupRequests, radiusAccClientExtEntry=radiusAccClientExtEntry, radiusAccClientExtTable=radiusAccClientExtTable, radiusAccServIdent=radiusAccServIdent, radiusAccClientAddress=radiusAccClientAddress, radiusAccClientEntry=radiusAccClientEntry)
