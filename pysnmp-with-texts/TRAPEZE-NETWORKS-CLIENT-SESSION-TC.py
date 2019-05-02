#
# PySNMP MIB module TRAPEZE-NETWORKS-CLIENT-SESSION-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-CLIENT-SESSION-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:27:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, Bits, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, ModuleIdentity, Counter64, Integer32, TimeTicks, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Bits", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter64", "Integer32", "TimeTicks", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzClientSessionTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 10))
trpzClientSessionTc.setRevisions(('2012-04-19 00:40', '2011-01-27 00:33', '2009-11-30 00:21', '2007-10-08 00:10', '2006-09-26 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzClientSessionTc.setRevisionsDescriptions(('v1.4.0: Introduced TCs: TrpzClientDeviceType, TrpzClientDeviceGroupName, TrpzClientDeviceProfileName. (for 8.0 release)', "v1.3.3: Added User Access Type value 'profile' (5). Reserved User Access Type value 6. (for 7.5 release)", 'v1.2.1: Improved description.', 'v1.1.0: Introduced TrpzClientAccessMode to be used instead of TrpzAccessType from trpzApTc module. (In 6.0, direct- and network-attached APs were unified.)', 'v1.0.1: initial version',))
if mibBuilder.loadTexts: trpzClientSessionTc.setLastUpdated('201204190040Z')
if mibBuilder.loadTexts: trpzClientSessionTc.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzClientSessionTc.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzClientSessionTc.setDescription("Textual Conventions used by Trapeze Networks wireless switches. Copyright 2006-2012 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzUserAccessType(TextualConvention, Integer32):
    description = "Enumeration of user access types (also referred to as ''login types'')."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("mac", 1), ("web", 2), ("dot1x", 3), ("last-resort", 4), ("profile", 5))

class TrpzClientSessionState(TextualConvention, Integer32):
    description = "Enumeration of the client session states. Value 'associated(1)' applies only to wireless sessions. Value 'wired(8)' applies only to wired sessions."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("associated", 1), ("authorizing", 2), ("authorized", 3), ("active", 4), ("de-associated", 5), ("roaming-away", 6), ("updated-to-roam", 7), ("wired", 8), ("clearing", 9), ("invalid", 10), ("web-authing", 11))

class TrpzClientDot1xState(TextualConvention, Integer32):
    description = 'Enumeration of the dot1x states for a client.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("wired", 6), ("aborting", 7), ("held", 8))

class TrpzClientAuthenProtocolType(TextualConvention, Integer32):
    description = 'Enumeration of the dot1x client authentication protocol types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("eap-tls", 2), ("eap-ttls", 3), ("md5", 4), ("peap", 5), ("leap", 6), ("pass-through", 7))

class TrpzClientAccessMode(TextualConvention, Integer32):
    description = "Describes the access mode (type) used by client. Value 'ap(2)' indicates a client that is attached to the switch via an access point. Value 'wired(3)' indicates a client that is attached to the switch via the wired network (no access point is involved)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("ap", 2), ("wired", 3))

class TrpzClientDeviceType(TextualConvention, OctetString):
    description = 'The type of a client device. Consists of printable ASCII characters between 0x21 (!), and 0x7e (~), with no leading, embedded, or trailing space. Is a zero length string if unknown.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TrpzClientDeviceGroupName(TextualConvention, OctetString):
    description = 'The name of a group of device types. Consists of printable ASCII characters between 0x21 (!), and 0x7e (~), with no leading, embedded, or trailing space. Is a zero length string if unknown.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TrpzClientDeviceProfileName(TextualConvention, OctetString):
    description = 'The name of a device profile. A device profile is a collection of policies that apply to one or more types of client devices. Consists of printable ASCII characters between 0x21 (!) and 0x7e (~), with no leading, embedded, or trailing space. Is a zero length string if unknown.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-CLIENT-SESSION-TC", TrpzClientDeviceType=TrpzClientDeviceType, TrpzUserAccessType=TrpzUserAccessType, trpzClientSessionTc=trpzClientSessionTc, TrpzClientDeviceProfileName=TrpzClientDeviceProfileName, TrpzClientAuthenProtocolType=TrpzClientAuthenProtocolType, TrpzClientDeviceGroupName=TrpzClientDeviceGroupName, TrpzClientSessionState=TrpzClientSessionState, TrpzClientDot1xState=TrpzClientDot1xState, TrpzClientAccessMode=TrpzClientAccessMode, PYSNMP_MODULE_ID=trpzClientSessionTc)
