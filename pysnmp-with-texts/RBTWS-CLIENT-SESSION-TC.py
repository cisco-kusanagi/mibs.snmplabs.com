#
# PySNMP MIB module RBTWS-CLIENT-SESSION-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-CLIENT-SESSION-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:53:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Counter32, MibIdentifier, TimeTicks, Unsigned32, iso, Integer32, Bits, ModuleIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter32", "MibIdentifier", "TimeTicks", "Unsigned32", "iso", "Integer32", "Bits", "ModuleIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsClientSessionTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 10))
rbtwsClientSessionTc.setRevisions(('2007-10-08 00:10', '2006-09-26 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsClientSessionTc.setRevisionsDescriptions(('v1.1.0: Introduced RbtwsClientAccessMode to be used instead of RbtwsAccessType from rbtwsApTc module. (In 6.0, direct- and network-attached APs were unified.)', 'v1.0.1: initial version',))
if mibBuilder.loadTexts: rbtwsClientSessionTc.setLastUpdated('200710091719Z')
if mibBuilder.loadTexts: rbtwsClientSessionTc.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsClientSessionTc.setContactInfo('www.enterasys.com')
if mibBuilder.loadTexts: rbtwsClientSessionTc.setDescription("Textual Conventions used by Enterasys Networks wireless switches. Copyright 2007 Enterasys Networks, Inc. All rights reserved. This SNMP Management Information Base Specification (Specification) embodies confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class RbtwsUserAccessType(TextualConvention, Integer32):
    description = 'Describes the access type by the user'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mac", 1), ("web", 2), ("dot1x", 3), ("last-resort", 4))

class RbtwsClientSessionState(TextualConvention, Integer32):
    description = "Enumeration of the client session states. Value 'associated(1)' applies only to wireless sessions. Value 'wired(8)' applies only to wired sessions."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("associated", 1), ("authorizing", 2), ("authorized", 3), ("active", 4), ("de-associated", 5), ("roaming-away", 6), ("updated-to-roam", 7), ("wired", 8), ("clearing", 9), ("invalid", 10), ("web-authing", 11))

class RbtwsClientDot1xState(TextualConvention, Integer32):
    description = 'Enumeration of the dot1x states for a client.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("wired", 6), ("aborting", 7), ("held", 8))

class RbtwsClientAuthenProtocolType(TextualConvention, Integer32):
    description = 'Enumeration of the dot1x client authentication protocol types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("eap-tls", 2), ("eap-ttls", 3), ("md5", 4), ("peap", 5), ("leap", 6), ("pass-through", 7))

class RbtwsClientAccessMode(TextualConvention, Integer32):
    description = "Describes the access mode (type) used by client. Value 'ap(2)' indicates a client that is attached to the switch via an access point. Value 'wired(3)' indicates a client that is attached to the switch via the wired network (no access point is involved)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("ap", 2), ("wired", 3))

mibBuilder.exportSymbols("RBTWS-CLIENT-SESSION-TC", RbtwsClientAuthenProtocolType=RbtwsClientAuthenProtocolType, rbtwsClientSessionTc=rbtwsClientSessionTc, RbtwsClientDot1xState=RbtwsClientDot1xState, PYSNMP_MODULE_ID=rbtwsClientSessionTc, RbtwsClientSessionState=RbtwsClientSessionState, RbtwsClientAccessMode=RbtwsClientAccessMode, RbtwsUserAccessType=RbtwsUserAccessType)
