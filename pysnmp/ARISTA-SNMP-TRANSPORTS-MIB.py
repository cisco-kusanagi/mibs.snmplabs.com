#
# PySNMP MIB module ARISTA-SNMP-TRANSPORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-SNMP-TRANSPORTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, ObjectIdentity, Integer32, IpAddress, Bits, TimeTicks, Counter32, Gauge32, Unsigned32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "Integer32", "IpAddress", "Bits", "TimeTicks", "Counter32", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier")
TDomain, DisplayString, TextualConvention, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "DisplayString", "TextualConvention", "TAddress")
aristaSnmpTransportMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10))
aristaSnmpTransportMIB.setRevisions(('2014-08-15 00:00', '2012-01-09 13:00', '2012-01-05 18:30',))
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setOrganization('Arista Networks, Inc.')
class TransportAddressIPv4NS(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d:2d@*1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 255)

class TransportAddressIPv6NS(TextualConvention, OctetString):
    status = 'current'
    displayHint = '0a[2x:2x:2x:2x:2x:2x:2x:2x]0a:2d@*1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(19, 255)

aristaUDPNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 1))
if mibBuilder.loadTexts: aristaUDPNSDomain.setStatus('current')
aristaTCPNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 2))
if mibBuilder.loadTexts: aristaTCPNSDomain.setStatus('current')
aristaUDPNS6Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 3))
if mibBuilder.loadTexts: aristaUDPNS6Domain.setStatus('current')
aristaTCPNS6Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 4))
if mibBuilder.loadTexts: aristaTCPNS6Domain.setStatus('current')
aristaAuthFailTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5))
aristaTransportConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6))
aristaAuthFailTrapTDomain = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 1), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaAuthFailTrapTDomain.setStatus('current')
aristaAuthFailTrapSrcTAddress = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 2), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaAuthFailTrapSrcTAddress.setStatus('current')
aristaAuthFailTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1))
aristaAuthFailCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2))
aristaAuthFailCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2, 1)).setObjects(("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaAuthFailCompliance = aristaAuthFailCompliance.setStatus('current')
aristaAuthFailTrapObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1, 1)).setObjects(("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapTDomain"), ("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapSrcTAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaAuthFailTrapObjectsGroup = aristaAuthFailTrapObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-SNMP-TRANSPORTS-MIB", TransportAddressIPv4NS=TransportAddressIPv4NS, aristaAuthFailTrapObjects=aristaAuthFailTrapObjects, aristaAuthFailCompliances=aristaAuthFailCompliances, PYSNMP_MODULE_ID=aristaSnmpTransportMIB, aristaTCPNSDomain=aristaTCPNSDomain, aristaUDPNSDomain=aristaUDPNSDomain, aristaAuthFailCompliance=aristaAuthFailCompliance, aristaUDPNS6Domain=aristaUDPNS6Domain, aristaAuthFailTrapSrcTAddress=aristaAuthFailTrapSrcTAddress, TransportAddressIPv6NS=TransportAddressIPv6NS, aristaSnmpTransportMIB=aristaSnmpTransportMIB, aristaAuthFailTrapTDomain=aristaAuthFailTrapTDomain, aristaTCPNS6Domain=aristaTCPNS6Domain, aristaAuthFailTrapObjectsGroup=aristaAuthFailTrapObjectsGroup, aristaTransportConformance=aristaTransportConformance, aristaAuthFailTrapGroups=aristaAuthFailTrapGroups)
