#
# PySNMP MIB module IRTF-NMRG-SNMP-TCP-TM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IRTF-NMRG-SNMP-TCP-TM
# Produced by pysmi-0.3.4 at Wed May  1 13:57:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Gauge32, IpAddress, iso, Counter64, experimental, ObjectIdentity, Counter32, Bits, Integer32, ModuleIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Gauge32", "IpAddress", "iso", "Counter64", "experimental", "ObjectIdentity", "Counter32", "Bits", "Integer32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nmrgSnmpDomains = ModuleIdentity((1, 3, 6, 1, 3, 91, 1))
nmrgSnmpDomains.setRevisions(('2002-02-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nmrgSnmpDomains.setRevisionsDescriptions(('Initial version, published as RFC XXXX.',))
if mibBuilder.loadTexts: nmrgSnmpDomains.setLastUpdated('200202250000Z')
if mibBuilder.loadTexts: nmrgSnmpDomains.setOrganization('IRTF Network Management Research Group')
if mibBuilder.loadTexts: nmrgSnmpDomains.setContactInfo('Juergen Schoenwaelder TU Braunschweig Bueltenweg 74/75 38106 Braunschweig Germany Phone: +49 531 391-3283 Email: schoenw@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: nmrgSnmpDomains.setDescription('This MIB module defines the SNMP over TCP transport mapping.')
snmpTCPDomain = ObjectIdentity((1, 3, 6, 1, 3, 91, 1, 1))
if mibBuilder.loadTexts: snmpTCPDomain.setStatus('current')
if mibBuilder.loadTexts: snmpTCPDomain.setDescription('The SNMP over TCP over IPv4 transport domain. The corresponding transport address is of type SnmpTCPAddress.')
class SnmpTCPAddress(TextualConvention, OctetString):
    description = 'Represents a TCP/IPv4 address: octets contents encoding 1-4 IP-address network-byte order 5-6 TCP-port network-byte order '
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

mibBuilder.exportSymbols("IRTF-NMRG-SNMP-TCP-TM", SnmpTCPAddress=SnmpTCPAddress, PYSNMP_MODULE_ID=nmrgSnmpDomains, snmpTCPDomain=snmpTCPDomain, nmrgSnmpDomains=nmrgSnmpDomains)
