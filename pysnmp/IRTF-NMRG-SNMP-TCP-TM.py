#
# PySNMP MIB module IRTF-NMRG-SNMP-TCP-TM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IRTF-NMRG-SNMP-TCP-TM
# Produced by pysmi-0.3.4 at Mon Apr 29 19:46:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, experimental, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, iso, ObjectIdentity, Counter32, Unsigned32, Counter64, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "experimental", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "iso", "ObjectIdentity", "Counter32", "Unsigned32", "Counter64", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nmrgSnmpDomains = ModuleIdentity((1, 3, 6, 1, 3, 91, 1))
nmrgSnmpDomains.setRevisions(('2002-02-25 00:00',))
if mibBuilder.loadTexts: nmrgSnmpDomains.setLastUpdated('200202250000Z')
if mibBuilder.loadTexts: nmrgSnmpDomains.setOrganization('IRTF Network Management Research Group')
snmpTCPDomain = ObjectIdentity((1, 3, 6, 1, 3, 91, 1, 1))
if mibBuilder.loadTexts: snmpTCPDomain.setStatus('current')
class SnmpTCPAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

mibBuilder.exportSymbols("IRTF-NMRG-SNMP-TCP-TM", snmpTCPDomain=snmpTCPDomain, PYSNMP_MODULE_ID=nmrgSnmpDomains, SnmpTCPAddress=SnmpTCPAddress, nmrgSnmpDomains=nmrgSnmpDomains)
