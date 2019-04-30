#
# PySNMP MIB module Dot1xMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dot1xMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:43:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, iso, Counter32, IpAddress, ModuleIdentity, TimeTicks, MibIdentifier, Counter64, Integer32, Gauge32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "iso", "Counter32", "IpAddress", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Counter64", "Integer32", "Gauge32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swdot1xMGMTMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 30))
if mibBuilder.loadTexts: swdot1xMGMTMIB.setLastUpdated('0007150000Z')
if mibBuilder.loadTexts: swdot1xMGMTMIB.setOrganization(' ')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

dot1xGuestVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 30, 1))
dot1xGuestVlanName = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 30, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xGuestVlanName.setStatus('current')
dot1xGuestVlanPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 30, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xGuestVlanPort.setStatus('current')
dot1xGuestVlanDelState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 30, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xGuestVlanDelState.setStatus('current')
mibBuilder.exportSymbols("Dot1xMGMT-MIB", PYSNMP_MODULE_ID=swdot1xMGMTMIB, swdot1xMGMTMIB=swdot1xMGMTMIB, dot1xGuestVlanDelState=dot1xGuestVlanDelState, dot1xGuestVlanName=dot1xGuestVlanName, PortList=PortList, dot1xGuestVlanPort=dot1xGuestVlanPort, dot1xGuestVlan=dot1xGuestVlan)
