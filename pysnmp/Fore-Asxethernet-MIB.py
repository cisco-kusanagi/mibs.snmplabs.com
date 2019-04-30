#
# PySNMP MIB module Fore-Asxethernet-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Asxethernet-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
software, = mibBuilder.importSymbols("Fore-Common-MIB", "software")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, ObjectIdentity, NotificationType, TimeTicks, IpAddress, Bits, Integer32, Counter64, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "ObjectIdentity", "NotificationType", "TimeTicks", "IpAddress", "Bits", "Integer32", "Counter64", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
asxEthernetAutoNegotiate = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5))
if mibBuilder.loadTexts: asxEthernetAutoNegotiate.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: asxEthernetAutoNegotiate.setOrganization('FORE')
class AsxEthernetModes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("tenHalfDuplex", 1), ("tenFullDuplex", 2), ("hundredHalfDuplex", 3), ("hundredFullDuplex", 4), ("auto", 5))

asxEthernetAutoNegotiationTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1), )
if mibBuilder.loadTexts: asxEthernetAutoNegotiationTable.setStatus('current')
asxEthernetAutoNegotiationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: asxEthernetAutoNegotiationEntry.setStatus('current')
asxEthernetConfigModes = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 1), AsxEthernetModes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asxEthernetConfigModes.setStatus('current')
asxEthernetOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 2), AsxEthernetModes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asxEthernetOperStatus.setStatus('current')
asxEthernetLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link-up", 1), ("link-down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asxEthernetLinkState.setStatus('current')
asxEthernetRemoteAutoNeg = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("not-detected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asxEthernetRemoteAutoNeg.setStatus('current')
asxEthernetRemoteOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 0), ("tenHalfDuplex", 1), ("tenFullDuplex", 2), ("hundredHalfDuplex", 3), ("hundredFullDuplex", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asxEthernetRemoteOperStatus.setStatus('current')
mibBuilder.exportSymbols("Fore-Asxethernet-MIB", asxEthernetLinkState=asxEthernetLinkState, asxEthernetAutoNegotiationTable=asxEthernetAutoNegotiationTable, asxEthernetRemoteOperStatus=asxEthernetRemoteOperStatus, AsxEthernetModes=AsxEthernetModes, PYSNMP_MODULE_ID=asxEthernetAutoNegotiate, asxEthernetAutoNegotiationEntry=asxEthernetAutoNegotiationEntry, asxEthernetConfigModes=asxEthernetConfigModes, asxEthernetOperStatus=asxEthernetOperStatus, asxEthernetRemoteAutoNeg=asxEthernetRemoteAutoNeg, asxEthernetAutoNegotiate=asxEthernetAutoNegotiate)
