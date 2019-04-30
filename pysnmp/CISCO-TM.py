#
# PySNMP MIB module CISCO-TM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TM
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoDomains, = mibBuilder.importSymbols("CISCO-SMI", "ciscoDomains")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, Gauge32, Counter64, ObjectIdentity, Bits, MibIdentifier, NotificationType, iso, ModuleIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "Gauge32", "Counter64", "ObjectIdentity", "Bits", "MibIdentifier", "NotificationType", "iso", "ModuleIdentity", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTransportMappings = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1))
ciscoTransportMappings.setRevisions(('2001-08-23 16:00', '2000-06-21 16:00',))
if mibBuilder.loadTexts: ciscoTransportMappings.setLastUpdated('200108231600Z')
if mibBuilder.loadTexts: ciscoTransportMappings.setOrganization('Cisco Systems, Inc.')
snmpUDPVPNDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 1))
if mibBuilder.loadTexts: snmpUDPVPNDomain.setStatus('current')
class SnmpUDPVPNAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d/32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 38)

snmpAAL5Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 2))
if mibBuilder.loadTexts: snmpAAL5Domain.setStatus('current')
class SnmpAAL5VCIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d/4d/4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

snmpCNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 3))
if mibBuilder.loadTexts: snmpCNSDomain.setStatus('current')
class SnmpCNSIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '19a.255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(19, 274)

mibBuilder.exportSymbols("CISCO-TM", snmpAAL5Domain=snmpAAL5Domain, PYSNMP_MODULE_ID=ciscoTransportMappings, SnmpUDPVPNAddress=SnmpUDPVPNAddress, snmpUDPVPNDomain=snmpUDPVPNDomain, SnmpAAL5VCIdentifier=SnmpAAL5VCIdentifier, snmpCNSDomain=snmpCNSDomain, SnmpCNSIdentifier=SnmpCNSIdentifier, ciscoTransportMappings=ciscoTransportMappings)
