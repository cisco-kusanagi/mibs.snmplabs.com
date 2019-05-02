#
# PySNMP MIB module NTWS-CLIENT-SESSION-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-CLIENT-SESSION-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:25:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Integer32, ObjectIdentity, MibIdentifier, Gauge32, TimeTicks, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Integer32", "ObjectIdentity", "MibIdentifier", "Gauge32", "TimeTicks", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Counter32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntwsClientSessionTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 10))
ntwsClientSessionTc.setRevisions(('2007-10-08 00:10', '2007-08-16 00:02', '2006-09-26 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsClientSessionTc.setRevisionsDescriptions(('v1.1.0: Introduced NtwsClientAccessMode to be used instead of NtwsAccessType from ntwsApTc module. (In 6.0, direct- and network-attached APs were unified.)', 'v1.0.2, MRT v1: Made changes in order to make MIB comply with corporate MIB conventions.', 'v1.0.1: initial version',))
if mibBuilder.loadTexts: ntwsClientSessionTc.setLastUpdated('200710080010Z')
if mibBuilder.loadTexts: ntwsClientSessionTc.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsClientSessionTc.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsClientSessionTc.setDescription("Textual Conventions used by Nortel Networks wireless switches. Copyright 2007 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class NtwsUserAccessType(TextualConvention, Integer32):
    description = 'Describes the access type by the user'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mac", 1), ("web", 2), ("dot1x", 3), ("last-resort", 4))

class NtwsClientSessionState(TextualConvention, Integer32):
    description = "Enumeration of the client session states. Value 'associated(1)' applies only to wireless sessions. Value 'wired(8)' applies only to wired sessions."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("associated", 1), ("authorizing", 2), ("authorized", 3), ("active", 4), ("de-associated", 5), ("roaming-away", 6), ("updated-to-roam", 7), ("wired", 8), ("clearing", 9), ("invalid", 10), ("web-authing", 11))

class NtwsClientDot1xState(TextualConvention, Integer32):
    description = 'Enumeration of the dot1x states for a client.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("wired", 6), ("aborting", 7), ("held", 8))

class NtwsClientAuthenProtocolType(TextualConvention, Integer32):
    description = 'Enumeration of the dot1x client authentication protocol types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("eap-tls", 2), ("eap-ttls", 3), ("md5", 4), ("peap", 5), ("leap", 6), ("pass-through", 7))

class NtwsClientAccessMode(TextualConvention, Integer32):
    description = "Describes the access mode (type) used by client. Value 'ap(2)' indicates a client that is attached to the switch via an access point. Value 'wired(3)' indicates a client that is attached to the switch via the wired network (no access point is involved)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("ap", 2), ("wired", 3))

mibBuilder.exportSymbols("NTWS-CLIENT-SESSION-TC", ntwsClientSessionTc=ntwsClientSessionTc, NtwsClientAuthenProtocolType=NtwsClientAuthenProtocolType, PYSNMP_MODULE_ID=ntwsClientSessionTc, NtwsClientDot1xState=NtwsClientDot1xState, NtwsClientAccessMode=NtwsClientAccessMode, NtwsClientSessionState=NtwsClientSessionState, NtwsUserAccessType=NtwsUserAccessType)
